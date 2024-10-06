# import pandas as pd
import re

# Let's first take a look at the content of the uploaded file to determine its structure
file_path = '/home/s2644572/anlp/assignment1/assignment1-data/model-br.en'

# with open(file_path, 'r') as file:
#     content_preview = file.readlines()[:10]  # Read the first 10 lines to understand the structure
    
# print(content_preview)

data_dict = {}

# Read the file and populate the dictionary
with open(file_path, 'r') as file:
    for line in file:
        # Extract the first three characters as key and the value after the tab as value
        key = line[:3]
        value = line.split('\t')[1]
        data_dict[key] = float(value)

# Read if there is zero probabilities
if 0. in data_dict.values():
    print("There is probability of zero")
else:
    print("Only non-zero probabilites existing")
# list(data_dict.items())[:10]


# # Return the vocabulary_size
# unique_trigrams = set()

# with open(file_path, 'r') as file:
#     for line in file:
#         # Extract the trigram part using regular expression
#         match = re.search(r'^\s*(\S+)\t', line)
#         if match:
#             trigram = match.group(1)
#             unique_trigrams.add(trigram)

# # Calculate the vocabulary size
# vocabulary_size = len(unique_trigrams)

# # Display the result
# print(vocabulary_size)