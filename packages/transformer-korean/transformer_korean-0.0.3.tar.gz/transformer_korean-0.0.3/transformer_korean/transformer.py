import tensorflow as tf
from encoder import Encoder
from decoder import Decoder


class Transformer(tf.keras.Model):
    def __init__(self, num_layers,
                 d_model, num_heads, dff, vocab_size, enc_activation, dec_activation, rate=0.1):

        super(Transformer, self).__init__()

        self.encoder = Encoder(num_layers, d_model, num_heads, dff,
                               vocab_size+2, enc_activation, rate)

        self.decoder = Decoder(num_layers, d_model, num_heads, dff,
                               vocab_size+2, dec_activation, rate)

        self.final_layer = tf.keras.layers.Dense(vocab_size+2)

    def call(self, inp, tar, training, enc_padding_mask, look_ahead_mask, dec_padding_mask):

        # (batch_size, inp_seq_len, d_model)
        enc_output = self.encoder(inp, training, enc_padding_mask)

        # dec_output.shape == (batch_size, tar_seq_len, d_model)
        dec_output, attention_weights = self.decoder(tar, enc_output, training, look_ahead_mask, dec_padding_mask)

        # (batch_size, tar_seq_len, target_vocab_size)
        final_output = self.final_layer(dec_output)

        return final_output, attention_weights

    