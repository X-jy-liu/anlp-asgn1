from collections import Counter
import re

trained_model_path = '/home/s2644572/anlp/assignment1/model-br.en'
en_training_data_path = '/home/s2644572/anlp/assignment1/training.en'

def read_file(file_path):
    with open(file_path,"r") as file:
        lines = file.readlines()
    return lines

# preprocessing rule to be changed
def preprocess_line(input_string):
    # leave alphabetic, integers, space and period only
    cleaned_string = re.sub(r'[^A-Za-z0-9 .]', '', input_string)
    cleaned_string = re.sub(r'[0-9]', '0', cleaned_string)
    
    return cleaned_string.lower()


def generate_trigrams(text):
    trigrams = []
    for line in text:
        cleaned_line = preprocess_line(line)
        for i in range(len(cleaned_line) - 2):
            trigram = cleaned_line[i:i + 3]
            trigrams.append(trigram)
    return trigrams

def count_trigrams(trigrams):
    return Counter(trigrams)

def calculate_probabilities(trigram_counts):
    total_count = sum(trigram_counts.values())
    trigram_probs= {}
    for trigram, count in trigram_counts.items():
        # currently MLE, can be adjusted later
        trigram_probs[trigram] = count / total_count
    return trigram_probs


# conbine all functions above and build the model
def build_trigram_language_model(file_path):
    text = read_file(file_path)
    trigrams = generate_trigrams(text)
    trigram_counts = count_trigrams(trigrams)
    trigram_probabilities = calculate_probabilities(trigram_counts)
    return trigram_probabilities

# Example usage

# file_path = '~/anlp/assignment 1-1/assignment1-data/training.en'
trigram_model = build_trigram_language_model(en_training_data_path)

# Display some trigrams and their probabilities
for trigram, prob in list(trigram_model.items())[:10]:
    print(f"Trigram: '{trigram}', Probability: {prob:.6f}")

output_file_path = '/home/s2644572/anlp/assignment 1-1/self_trigram_model.en'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for trigram, prob in sorted(trigram_model.items()):
        output_file.write(f"{trigram}\t{prob:.2e}\n")