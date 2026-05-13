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

from nltk.corpus import wordnet as wn

def word_similarity(word1, word2):
    synsets1 = wn.synsets(word1)
    synsets2 = wn.synsets(word2)

    if not synsets1 or not synsets2:
        return None

    # Beginner version:
    # take the first meaning of each word
    s1 = synsets1[0]
    s2 = synsets2[0]

    return s1.path_similarity(s2)

pairs = [
    ("car", "automobile"),
    ("dog", "cat"),
    ("happy", "sad"),
    ("big", "large"),
    ("book", "table"),
    ("buy", "purchase"),
    ("fast","faster")
]

for w1, w2 in pairs:
    score = word_similarity(w1, w2)
    print(w1, "-", w2, "=", score)