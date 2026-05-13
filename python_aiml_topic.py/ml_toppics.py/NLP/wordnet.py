from nltk.corpus import wordnet as wn

def get_synonyms(word):
    synonyms = set()

    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            name = lemma.name().replace("_", " ")
            if name.lower() != word.lower():
                synonyms.add(name)

    return sorted(synonyms)


def get_antonyms(word):
    antonyms = set()

    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            for antonym in lemma.antonyms():
                name = antonym.name().replace("_", " ")
                antonyms.add(name)

    return sorted(antonyms)


word = input("Enter a word: ")

# print("\nSynonyms:")
# for item in get_synonyms(word):
#     print("-", item)

print("\nAntonyms:")
for item in get_antonyms(word):
    print("-", item)