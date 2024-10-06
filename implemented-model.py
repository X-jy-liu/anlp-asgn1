from collections import Counter
import re

trained_model_path = '/home/s2644572/anlp/assignment1/assignment1-data/model-br.en'
en_training_data_path = '/home/s2644572/anlp/assignment1/assignment1-data/training.en'

def read_file(file_path):
    with open(file_path,"r") as file:
        content = file.read()
    return content

# preprocessing rule to be changed
def preprocess_line(input_string):
    # leave alphabetic, integers, space and period only
    cleaned_string = re.sub(r'[^A-Za-z0-9 .]', '', input_string)
    cleaned_string = re.sub(r'[0-9]', '0', cleaned_string)
    
    return cleaned_string.lower()


def generate_trigram(content):
    cleaned_content = preprocess_line(content)
    trigrams = []
    for i in range(len(cleaned_content) - 2):
        trigrams.append(cleaned_content[i:i+3])
    return trigrams 

def calculate_probabiliries(trigrams):
    trigrams_counts = Counter(trigrams)
    total_counts = sum(trigrams_counts.values())
    trigrams_probs = {}
    for trigram, count in trigrams_counts.items():
        #currently is MLE but needs to change later
        trigrams_probs[trigram] = count / total_counts
    
    return trigrams_probs