from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import re

# Custom same meaning words
custom_words = {

    "varanasi": [
        "kashi",
        "banaras",
        "benares",
        "varansi",
        "varanasi"
    ],
    "temples": [
        "mandir",
        "temples",

    ]

}

# Clean words


def clean_words(sentence):

    # lowercase
    sentence = sentence.lower()

    # tokenize
    words = re.findall(r"[a-z]+", sentence)

    # stopwords
    stop_words = set(stopwords.words("english"))

    filtered = []

    for word in words:

        # remove common words
        if word not in stop_words:

            # custom synonym replace
            for main_word, synonyms in custom_words.items():

                if word in synonyms:

                    word = main_word

            filtered.append(word)

    return filtered


# Find synonyms
def synonyms_of(word):

    words = {word}

    for synset in wn.synsets(word):

        for lemma in synset.lemmas():

            words.add(
                lemma.name().lower().replace("_", " ")
            )

    return words


# Expand sentence words
def expanded_sentence_words(sentence):

    result = set()

    for word in clean_words(sentence):

        result.update(synonyms_of(word))

    return result


# Sentence similarity
def sentence_meaning_score(sentence1, sentence2):

    words1 = expanded_sentence_words(sentence1)

    words2 = expanded_sentence_words(sentence2)

    common = words1.intersection(words2)

    total = words1.union(words2)

    if not total:

        return 0, common

    score = len(common) / len(total)

    return score, common

data = [

    {
        "question": "about the history of varanasi",
        "answer": "Varanasi is one of the oldest cities in India."
    },

    {
        "question": "explain about the varanasi",
        "answer": "Varanasi, also known as Kashi and Banaras, is one of the oldest living cities in the world."
    },

    {
        "question": "famous temples in varanasi",
        "answer": "Varanasi is the city of temples there are many famous temples."
    },

    {
        "question": "varanasi temples list",
        "answer": "Varanasi is the city of temples there are many famous temples."
    },

    {
        "question": "top temples in banaras",
        "answer": "Varanasi is the city of temples there are many famous temples."
    },

    {
        "question": "main temples of kashi",
        "answer": "Varanasi is the city of temples there are many famous temples."
    },

    {
        "question": "varanasi ganga ghat",
        "answer": "There are around 84 ghats in Varanasi."
    },

    {
        "question": "varansi famous ghats",
        "answer": "This are the famous ganga ghats in varanasi."
    },

    {
        "question": "varanasi holly rivers",
        "answer": "These rivers in varanasi: Ganga, Varuna, Assi"
    },

    {
        "question": "local food",
        "answer": "Kashi is famous for its traditional street food culture."
    },

    {
        "question": "varanasi famous snacks",
        "answer": "Famous snacks in Varanasi: Kachori, Samosha."
    },

    {
        "question": "kashi famous sweets",
        "answer": "Famous sweets in kashi: Jalebi, Rabdi."
    },

    {
        "question": "kashi famous drinks",
        "answer": "Famous drinks in kashi: Lassi, Thandai."
    },

    {
        "question": "hello",
        "answer": "Hello I am your AI Guide."
    },

    {
        "question": "i am happy",
        "answer": "I think you are happy."
    },

    {
        "question": "i feel boring",
        "answer": "Ere guru banaras aial our bor ho jaiba."
    }

]


# Chat loop
user_input = 'hello'.lower().strip()
while True:

    user_input = input("\nYou: ").lower().strip()

    scores = []

    # Compare all questions
    for item in data:
        sentence = item['question']

        score, common = sentence_meaning_score(
            sentence,
            user_input
        )

        scores.append(score)
    # print(expanded_sentence_words(user_input))

    # print("\nScores =", scores)

    # Highest score
    max_score = max(scores)

    # Best matching index
    best_index = scores.index(max_score)

    # Final result
    if max_score == 0 or max_score < 0.2:

        print("\nBot: Not Understand ??")

    else:

        print("\nBot:", data[best_index]['answer'])
