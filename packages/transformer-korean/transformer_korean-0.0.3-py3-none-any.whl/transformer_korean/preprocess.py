import tensorflow_datasets as tfds
import tensorflow as tf
import pandas as pd
import random



def truncate_seq_pair(tokens_a, max_num_tokens, rng):
  """Truncates a pair of sequences to a maximum sequence length."""
  while True:
    total_length = len(tokens_a)
    if total_length <= max_num_tokens:
      return tokens_a

    trunc_tokens = tokens_a
    assert len(trunc_tokens) >= 1

    # We want to sometimes truncate from the front and sometimes from the
    # back to add more randomness and avoid biases.
    if rng.random() < 0.5:
      tokens_a = trunc_tokens[1:]
    else:
      tokens_a = trunc_tokens[:-1]

def whitespace_tokenize(text):
  """Runs basic whitespace cleaning and splitting on a piece of text."""
  text = text.strip()
  if not text:
    return []
  tokens = text.split()
  return tokens

def create_masked_lm_predictions(tokens, masked_lm_prob=0.15):

    rng = random.Random(12345)
    cand_indexes = []
    for (i, token) in enumerate(tokens):
        cand_indexes.append([i])
    rng.shuffle(cand_indexes)

    output_tokens = list(tokens)

    num_to_predict = max(1, int(round(len(tokens) * masked_lm_prob)))

    masked_lms = []
    covered_indexes = set()
    for index_set in cand_indexes:
        if len(masked_lms) >= num_to_predict:
            break
        # If adding a whole-word mask would exceed the maximum number of
        # predictions, then just skip this candidate.
        if len(masked_lms) + len(index_set) > num_to_predict:
            continue
        is_any_index_covered = False
        for index in index_set:
            if index in covered_indexes:
                is_any_index_covered = True
                break
        if is_any_index_covered:
            continue
        for index in index_set:
            covered_indexes.add(index)

            masked_token = None
            # 80% of the time, replace with [MASK]
            if rng.random() < 0.8:
                masked_token = 1
            else:
                # 10% of the time, keep original
                if rng.random() < 0.5:
                    masked_token = tokens[index]
                # 10% of the time, replace with random word
                else:
                    masked_token = rng.randint(1, vocab.vocab_size - 1)

            output_tokens[index] = masked_token
            masked_lms.append(masked_token)
    return output_tokens


class DataProcessor(object):

    def __init__(self,
                 csv_path=None,
                 txt_path=None,
                 max_length=128,
                 buffer_size=20000,
                 batch_size=64,
                 pre_train=True):

        self.csv_path = csv_path
        self.txt_path = txt_path
        self.max_length = max_length
        self.buffer_size = buffer_size
        self.batch_size = batch_size
        self.pre_train = pre_train

    def load_data_csv(self):
        train = []
        train_input = []
        train_label = []
        question = self.csv_path[0]
        answer = self.csv_path[1]

        question_df = pd.read_csv(question, names='Q')
        question_df = list(question_df['Q'])
        count = 0
        for line in question_df:
            line = line.strip()
            if count == 0:
                count += 1
                continue
            if not line:
                continue
            else :
                train_input.append(line)
                count += 1



        answer_df = pd.read_csv(answer, names='A')
        answer_df = list(answer_df['A'])
        count = 0
        for line in answer_df:
            line = line.strip()
            if count == 0:
                count += 1
                continue
            if not line:
                continue
            else:
                train_label.append(line)
                count+=1

        train.append(train_input)
        train.append(train_label)

        return train



    def load_data_txt(self):
        document = []
        with open(self.txt_path, 'r', encoding='utf-8') as data:
            count = 0
            for line in data:
                line = line.strip()
                if not line:
                    continue
                document.append(line)
                count += 1
        return document

    def load_vocab_file(self, vocab_filename="vocab.subwords"):
        global vocab

        vocab = tfds.features.text.SubwordTextEncoder.load_from_file(vocab_filename)
        return vocab

    def tokenizer_train(self, train_data, vocab_size=2 ** 13, vocab_filename="vocab"):

        global tokenizer_train

        tokenizer_train = tfds.features.text.SubwordTextEncoder.build_from_corpus(
            (line for line in train_data[1]), target_vocab_size=vocab_size
        )
        tokenizer_train.save_to_file(vocab_filename)

        return tokenizer_train

    @staticmethod
    def encode(lang1, lang2, pre_train):
        """
        :param lang1: A Tensor containing the tokenized client text sentence
        :param lang2: A Tensor containing the tokenized QL TM text sentence
        :return: The originally passed tensors with a Start-of-Sequence (SOS) and
                 a End-of-Sequence (EOS) added.

        (SOS) = [vocab.vocab_size]
        (EOS) = [vocab.vocab_size + 1]
        """

        #train
        if pre_train:
            lang1 = [vocab.vocab_size] \
                    + create_masked_lm_predictions(vocab.encode(lang1.numpy())) \
                    + [vocab.vocab_size + 1]
        else :
            lang1 = [vocab.vocab_size] \
                    + vocab.encode(lang1.numpy()) \
                    + [vocab.vocab_size + 1]
        #target
        lang2 = [vocab.vocab_size] \
                + vocab.encode(lang2.numpy()) \
                + [vocab.vocab_size + 1]


        return lang1, lang2

    def filter_max_length(self, x, y):
        """
        :param x: The Feature tensor
        :param y: The Target tensor
        :return: The pair of Tensors whose lengths are less than or equal to self.max_length
        """

        return tf.logical_and(tf.size(x) <= self.max_length,
                              tf.size(y) <= self.max_length)

    def tf_encode(self, feature, target):
        """
        :param feature: The input feature text
        :param target:  The output target text
        :return: The encoded vector representations of the feature and target text.
        """

        return tf.py_function(self.encode, [feature, target, self.pre_train], [tf.int64, tf.int64])

    def to_tensor_dataset(self, data):
        """
        :param data: a DataFrame column that contains the feature_col and target_col
        :return: A TensorDataset made from the data DataFrame.
        """

        return tf.data.Dataset.from_tensor_slices(
            (
                tf.cast(data[0], tf.string),#train
                tf.cast(data[1], tf.string) #target
            )
        )

    def create_pretraining_data(self, document):
        # Account for <SOS>, <END>
        max_num_tokens = self.max_length - 2

        i = 0
        current_length = 0
        current_chunk = []

        train_input = []
        output_document =[]
        rng = random.Random(12345)

        while i < len(document):
            segment = document[i]
            current_chunk.append(segment)
            current_length += len(segment)
            if i == len(document) - 1 or current_length >= self.max_length:
                if current_chunk:
                    a_end = 1
                    if len(current_chunk) >= 2:
                        a_end = rng.randint(1, len(current_chunk) - 1)

                    tokens_a = []
                    for j in range(a_end):
                        tokens_a.append(current_chunk[j])

                    for j in range(a_end, len(current_chunk)):
                        tokens_a.append(current_chunk[j])

                    if len(tokens_a) == 0: continue

                    target = truncate_seq_pair(" ".join(tokens_a), max_num_tokens, rng)
                    train_input.append(target)
                current_chunk = []
                current_length = 0
            i += 1

        output_document.append(train_input)
        output_document.append(train_input)
        return output_document

    def preprocess(self, train):
        """

        :param train: Your training set.
        :param test: Your testing set.
        :return: filtered and batched TensorDatasets for train and test.
        """
        if self.pre_train:
            train_data = self.create_pretraining_data(train)
            train_data = self.to_tensor_dataset(train_data) #to tensor

        else:
            train_data = self.to_tensor_dataset(train)  # to tensor


        train_dataset = train_data.map(self.tf_encode) #encode
        train_dataset = train_dataset.filter(self.filter_max_length) #length filter
        train_dataset = train_dataset.cache()

        #shuffle data
        train_dataset = train_dataset.shuffle(self.buffer_size).padded_batch(self.batch_size,
                                                                             padded_shapes=([-1], [-1]))
        train_dataset = train_dataset.prefetch(tf.data.experimental.AUTOTUNE)

        return train_dataset