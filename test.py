import re
import sys
import Mykytea

##################--------------------------------Function
def get_mk(opt=''):
    mk = Mykytea.Mykytea(opt)
    return mk

def get_kytea_txt(mk, txt):
    n_txt = mk.getTagsToString(txt)
    p = re.compile('\s\s/UNK')
    n_txt = re.sub(p, '', n_txt)
    return n_txt

def remove_prefix(sentence):
    words = sentence.split()
    cleaned_words = [word.split('/')[1] if '/' in word else word for word in words]
    return ' '.join(cleaned_words)



def calculate_accuracy(predictions_file, groundtruth_file, num_examples=5):
    correct_words = 0
    total_words = 0
    examples = []
    best_example = None
    best_accuracy = 0
 
    with open(predictions_file, 'r', encoding='utf-8') as pred_file, open(groundtruth_file, 'r', encoding='utf-8') as truth_file:
        for pred_line, truth_line in zip(pred_file, truth_file):
            pred_sentence = remove_prefix(pred_line.strip())
            truth_sentence = truth_line.strip()
            
            # Skip if the generated sentence is empty
            if not pred_sentence:
                continue
            
            pred_words = pred_sentence.split()
            truth_words = truth_sentence.split()
            total_words += len(truth_words)
            example = {
                'prediction': pred_sentence,
                'ground_truth': truth_sentence,
                'correct_words': [],
                'incorrect_words': [],
                
            }
            for pred_word, truth_word in zip(pred_words, truth_words):
                if pred_word == truth_word:
                    correct_words += 1
                    example['correct_words'].append(pred_word)
                else:
                    example['incorrect_words'].append({'predicted': pred_word, 'actual': truth_word})

            examples.append(example)

            accuracy = correct_words / total_words if total_words > 0 else 0
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_example = example

    examples = [ex for ex in examples if len(ex['ground_truth']) > 0]  # 移除长度为零的句子

    examples.sort(key=lambda x: len(x['incorrect_words']) / len(x['ground_truth']))  # 按照错误单词比例排序

    accuracy = correct_words / total_words if total_words > 0 else 0
    
    top_25_example = examples[int(0.25 * len(examples))]  # Top 25%
    top_50_example = examples[int(0.50 * len(examples))]  # Top 50%
    top_75_example = examples[int(0.75 * len(examples))]  # Top 75%

    return accuracy, examples, top_25_example, top_50_example, top_75_example, best_accuracy, best_example

##################--------------------------------Main code

if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 run.py -model <model_filename>")
        sys.exit(1)
    
    # Get the model filename from the command-line arguments
    model_filename = sys.argv[2]
    
    # Call get_mk function with the specified model filename
    mk = get_mk(f'-model {model_filename}')
    
    input_file = './corpus/test_prefix.txt'
    output_file = './corpus/predictions.txt'
    
    with open(input_file, 'r', encoding='utf-8') as input_f, open(output_file, 'w', encoding='utf-8') as output_f:
        for line in input_f:
            txt = line.strip()
            n_txt = get_kytea_txt(mk, txt)
            output_f.write(n_txt + '\n')

    predictions_file = './corpus/predictions.txt'
    groundtruth_file = './corpus/test_sen.txt'
    accuracy, examples, top_25_example, top_50_example, top_75_example, best_accuracy, best_example= calculate_accuracy(predictions_file, groundtruth_file)
    
    print("Best Accuracy:", best_accuracy)
    print("Best Example:")
    print("Prediction:", best_example['prediction'])
    print("Ground Truth:", best_example['ground_truth'])
    print("Correct Words:", best_example['correct_words'])
    print("Incorrect Words:", best_example['incorrect_words'])
    
    print("Average Accuracy:", accuracy)
 
'''
    print("\nTop 25% Example:")
    print("Prediction:", top_25_example['prediction'])
    print("Ground Truth:", top_25_example['ground_truth'])
    print("Correct Words:", top_25_example['correct_words'])
    print("Incorrect Words:", top_25_example['incorrect_words'])


    print("\nTop 50% Example:")
    print("Prediction:", top_50_example['prediction'])
    print("Ground Truth:", top_50_example['ground_truth'])
    print("Correct Words:", top_50_example['correct_words'])
    print("Incorrect Words:", top_50_example['incorrect_words'])
 

    print("\nTop 75% Example:")
    print("Prediction:", top_75_example['prediction'])
    print("Ground Truth:", top_75_example['ground_truth'])
    print("Correct Words:", top_75_example['correct_words'])
    print("Incorrect Words:", top_75_example['incorrect_words'])
'''
    
