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
    "temples":[
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


questions = [
    "about the history of varanasi",

    "explain about the varanasi",

    "famous temples in varanasi",

    "varanasi temples list",


    "top temples in banaras",

    "main temples of kashi",
##                          ##
    "varanasi ganga ghat",

    "varansi famous ghats",

    "varanasi holly river",

    "local food",

    "varanasi famous snacks",

    "hello",

    "i am happy"

]


# Answers
answers = [
    "Varanasi is one of the oldest cities in India.",

    "Varanasi, also known as Kashi and Banaras, is one of the oldest living cities in the world.\n It is located on the banks of the sacred Ganges River in the Indian state of Uttar Pradesh.\nThe name “Varanasi” comes from two rivers:\nVaruna\nAssi\nVaranasi has around 84 ghats, where people perform prayers, rituals, meditation, and holy bathing. The most famous ghats are:\nDashashwamedh Ghat\nAssi Ghat\nManikarnika Ghat\nTulsi Ghat\nThe city is deeply connected with Shiva and is considered the spiritual capital of India.\nIt is a city where ancient traditions and modern life exist together, making it one of the most unique cities in the world.\nVaranasi is also known for:\nclassical music\nSanskriti\nAdhyatm\nMeditation\nYoga\nTantra Mantra\nStreet food\nBanarasi paan\nSilk sarees\nKashik Cloths",

    "Varanasi is the city of temples there are many famous temples.\nBada Ganesh Temple\nKashi Vishwanath Temple\nAnyapurna Temple\nMritunjay Mahadev Temple\nKal Bherva Temple\nSankat Mochan Temple\nBHU",
    "Varanasi is the city of temples there are many famous temples.\nBada Ganesh Temple\nKashi Vishwanath Temple\nAnyapurna Temple\nMritunjay Mahadev Temple\nKal Bherva Temple\nSankat Mochan Temple\nBHU",
    "Varanasi is the city of temples there are many famous temples.\nBada Ganesh Temple\nKashi Vishwanath Temple\nAnyapurna Temple\nMritunjay Mahadev Temple\nKal Bherva Temple\nSankat Mochan Temple\nBHU",
    "Varanasi is the city of temples there are many famous temples.\nBada Ganesh Temple\nKashi Vishwanath Temple\nAnyapurna Temple\nMritunjay Mahadev Temple\nKal Bherva Temple\nSankat Mochan Temple\nBHU",

    "There are around 84 ghats in Varanasi, and each ghat has its own history, rituals, and atmosphere.\nPeople come to the ghats for:\nHoly Bathing\nPrayer\nMeditation\nYoga\nBoat Riding\nThis the famous ghatsin kashi where the torist mostly visit\nAssi Ghat, Deshashwmag Ghat, Tulsi Ghat, Ganga Mahal, Harishchandra Ghat, Namo Ghat, Lalita Ghat, Manikarnika Ghat.\nWhich ghat you visit??",
    "This are the famous gnnga ghats in varanasi:\n Assi Ghat, Deshashwmag Ghat, Tulsi Ghat.",

    
    "This are the local food in varanasi:\nSnakes:\nKachori, Samosha, Puri Sabji, Tomato chat, Allu Tikki, Chola Papad\nSweets:\nJalabi, Rabdi,Longlatta, Gulab Jamun, Barfi\n Drinks:\nThandai, Aam Panna, Lassi, Sugarcan Juse, Badam Dudh, Malio",

   "These revers in varanasi:\nGanga, Varuna, Assi",

    
     "List of Famous Snakes:\nKachori, Samosha, Puri Sabji, Tomato chat, Allu Tikki, Chola Papad",
   
    "Hello I am your AI Guide.\nWhich place you visit in varanasi",

    "I think you are happy."

]

# Chat loop
user_input = 'hello'.lower().strip()
for i in range(len(questions)):

    user_input = input("\nYou: ").lower().strip()

    scores = []

    # Compare all questions
    for sentence in questions:

        score, common = sentence_meaning_score(
            sentence,
            user_input
        )

        scores.append(score)
    print(expanded_sentence_words(user_input))    

    print("\nScores =", scores)

    # Highest score
    max_score = max(scores)

    # Best matching index
    best_index = scores.index(max_score)

    # Final result
    if max_score == 0 or max_score < 0.2:

        print("\nBot: Not Understand ??")

    else:

        print("\nBot:", answers[best_index])