# First-Two-Character-Input Method for Sentence Generation

Welcome to the First-Two-Char Input Method for Sentence Generation project! This project aims to generate complete sentences based on the first two characters provided as input. I utilize the KyTea toolkit for word segmentation and sentence generation. The approach includes training a statistical model on a preprocessed corpus and evaluating its performance based on accuracy and sentence similarity.

## Usage

To run the project, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/first-two-char-input-method.git
   cd first-two-char-input-method

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt

3. **Generate Train and Test Set**:
   ```sh
   python3 data_generation.py

4. **Make corpus**:
   ```sh
   python3 make_corpus.py <data>.txt

5. **Train model**:
   ```sh
   train-kytea -full corpus/<data>.txt -model model.dat

6. **Model Evaluation**:
   ```sh
   python3 test.py -model model.dat

## Introduction
In this project, I propose a novel approach for sentence generation using a first-two-char input method. The method predicts complete sentences based on the first two characters of each word. This approach is particularly useful for applications where typing speed and efficiency are critical.

## Method
1. Data Collection and Preprocessing: I use text data from the Gutenberg and Brown corpora. The Gutenberg corpus includes works of classic literature, providing a rich and diverse language dataset. The Brown corpus consists of various genres of written American English from the 1960s, offering a broad spectrum of contemporary language use. The data is preprocessed to remove non-alphanumeric characters.
2. Corpus Creation: Using the KyTea toolkit, I segment the text into words and generate sentences based on the first two characters of each word.
3. Model Training: Train the statistical model on the generated corpus to predict complete sentences given the first two characters.
4. Evaluation: The model's performance is evaluated using accuracy and sentence similarity metrics.

## Dataset
Training Dataset: The dataset is collected from the Gutenberg corpus, which includes a variety of literary works.
Testing Dataset: The dataset is collected from the Brown corpus, representing a wide range of written American English.
Preprocessing: I remove illegal characters from the text data before using KyTea for segmentation.

## Acknowledgments
This project references code for training with KyTea from the repository [a-first-two-char-input-method](https://github.com/yaitaimo/a-first-two-char-input-method). I extend my sincere thanks to the original author for their contribution.
