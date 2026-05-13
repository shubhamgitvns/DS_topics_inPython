
# Wordset is a english word database which using in NLP 
# and storing the words meaning, synonyms, antonyms, relations

import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet

word = wordnet.synsets("bad")
for syn in word:
    for lemma in syn.lemmas():
        if lemma.antonyms():
            print(lemma.antonyms()[0].name()) # print antonyms()
        # print(lemma.name()) # print synonyms of the words
 
 



# print(synonyms)
