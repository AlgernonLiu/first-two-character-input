import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown
import re
import random

##################--------------------------------Train data
nltk.download('gutenberg')

def prepare_train_data(proportion):
    sentences = list(gutenberg.sents())  # Convert sentence objects to a list
    random.shuffle(sentences)

    num_sentences = len(sentences)
    num_selected_sentences = int(proportion * num_sentences)
    
    original_sentences = []
    for sentence in sentences[:num_selected_sentences]:
        # Remove all characters except letters and spaces
        original_sentence_str = re.sub(r'[^a-zA-Z\s]', '', " ".join(sentence))
        original_sentences.append(original_sentence_str)
    return original_sentences

# Define proportions for the training datasets


proportions = [0.01, 0.05, 0.10, 0.20, 0.40]

for proportion in proportions:
    train_data = prepare_train_data(proportion)
    filename = f'./corpus/train_data_{int(proportion * 100)}_percent.txt'
    
    # Write the selected sentences to a file
    with open(filename, 'w', encoding='utf-8') as f:
        for item in train_data:
            f.write("%s\n" % item)

    print(f"Done for train_data_{int(proportion * 100)}_percent.txt")


##################--------------------------------Test data
def generate_test_set():
    nltk.download("brown")
    sentences = list(brown.sents())  # Convert sentence objects to a list
    random.shuffle(sentences)

    original_sentences = []
    prefixed_sentences = []
    for sentence in sentences:
        # Remove all characters except letters and spaces
        sentence_str = re.sub(r'[^a-zA-Z\s,\.\']', '', "".join(word[:2] if len(word) > 1 else word + " " for word in sentence))
        original_sentence_str = re.sub(r'[^a-zA-Z\s]', '', " ".join(sentence))
        original_sentences.append(original_sentence_str)
        prefixed_sentences.append(sentence_str)

    return original_sentences, prefixed_sentences

def save_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write("%s\n" % item)

if __name__ == '__main__':
    original_sentences, prefixed_sentences = generate_test_set()
    save_to_file('./corpus/test_sen.txt', original_sentences)
    save_to_file('./corpus/test_prefix.txt', prefixed_sentences)
    print("Done for test_data!")
