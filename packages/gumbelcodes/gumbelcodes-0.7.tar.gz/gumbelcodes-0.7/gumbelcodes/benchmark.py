import json
import random
import time
from gumbelcodes.models.keyedvectors import KeyedVectors
words = list(json.load(open('glove_s600_dictionary.json','r')).keys())

embedding = KeyedVectors(
    codes="trimmed_glove_s300_.codes.npy", 
    codebook="trimmed_glove_s300_.codebook.npy", 
    trie="glove_s300_trie.marisa")

for i in range(10**3):
    try:
        w = random.choice(words)
        embedding[w]
    except Exception as e:
        print(e)
        pass
print(embedding[w])