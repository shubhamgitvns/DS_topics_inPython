
# Wordset is a english word database which using in NLP 
# and storing the words meaning, synonyms, antonyms, relations

import nltk
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.corpus import wordnet

# Sentences
sentence1 = "I buy an laptop"
sentence2 = "I purchased a car"

# Lowercase
sentence1 = sentence1.lower()
sentence2 = sentence2.lower()

# Tokennize
tokens1 = sentence1.split()
tokens2 = sentence2.split()

# Stopwords

stop_words = set(stopwords.words('english'))
filterd1 = []
filterd2 = []
for ch in tokens1:
    if ch not in stop_words:
        filterd1.append(ch) 

for ch in tokens2:
    if ch not in stop_words:
        filterd2.append(ch) 
print(filterd1)
print(filterd2)

# match synonyms
match_count =0
synonyms1 = []
synonyms2 = []
# match synonyms for filerd1 data
for ch1 in filterd1:
    
    for syn in wordnet.synsets(ch1):
            for lemma in syn.lemmas():
                 
                 synonyms1.append(lemma.name())
    print(synonyms1) 


for ch2 in filterd2:
    
    for syn in wordnet.synsets(ch2):
            for lemma in syn.lemmas():
                 
                 synonyms2.append(lemma.name())

                 if  ch1 in synonyms2 or  ch2 in synonyms2:
                      print(ch1, "=", ch2)
                      match_count+=1
                      break
                      
                 
    # Final Result
print("\nSimilarity Score =", match_count)

if match_count > 0:

    print("Sentences are SIMILAR")

else:

    print("Sentences are NOT similar")








