
# Wordset is a english word database which using in NLP 
# and storing the words meaning, synonyms, antonyms, relations

from nltk.corpus import wordnet as wn

word = "happy"

synsets = wn.synsets(word)

print("Word:", word)
print("Number of meanings found:", len(synsets))

for s in synsets:
    print("\nSynset:", s.name())
    print("Definition:", s.definition())
    print("Examples:", s.examples())
    print("Lemma names:", s.lemma_names())