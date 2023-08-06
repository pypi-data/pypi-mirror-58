from setuptools import setup, find_packages

setup(
    name='transformer_korean',
    version='0.0.3',
    description='Text-to-Text Transformer for Korean QA Task',
    author='yeontaek oh',
    author_email='oh31400@naver.com',
    url='https://github.com/yeontaek/Text-to-Text-Transformer',
    python_requires='>=3.5',
    packages= find_packages(),
    install_requires=[
        'tensorflow >=2.0',
        'tensorflow-datasets >= 1.3.2',
        'pandas >= 0.24.2',
        'numpy >= 1.16.3 ',
        'six>=1.12.0'
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)