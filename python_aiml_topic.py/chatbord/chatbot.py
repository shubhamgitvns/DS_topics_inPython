from nltk.corpus import wordnet as wn
import re


# Clean words
def clean_words(sentence):

    sentence = sentence.lower()

    return re.findall(r"[a-z]+", sentence)


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

    "varanasi famous temples lits",

    "varanasi ganga ghat",

    "varansi famous ghats list",

    "varanasi holly river",

    "local food",
    "varanasi famous snacks",
    "hello",

    "i am happy"

]


# Answers
answers = [
    "Varanasi is one of the oldest cities in India.",
    
    "There are revers in varanasi:\nGanga, Varuna, Assi",

    "Varanasi is the city of temples there are many famous temples.\nKashi Vishwanath\nAnyapurna Temple\nMritunjay Mahadev Temple\nKal Bherva Temple\nSankat Mochan Temple",

    "There are around 84 ghats in Varanasi, and each ghat has its own history, rituals, and atmosphere.\nPeople come to the ghats for:\nHoly Bathing\nPrayer\nMeditation\nYoga\nBoat Riding",
    "This are the local food in varanasi:\nSnakes:\nKachori, Samosha, Puri Sabji, Tomato chat, Allu Tikki, Chola Papad\nSweets:\nJalabi, Rabdi,Longlatta, Gulab Jamun, Barfi\n Drinks:\nThandai, Aam Panna, Lassi, Sugarcan Juse, Badam Dudh, Malio",
    "List of Famous Snakes:\nKachori, Samosha, Puri Sabji, Tomato chat, Allu Tikki, Chola Papad",
    "This are the famous gnnga ghats in varanasi:\n Assi Ghat, Deshashwmag Ghat, Tulsi Ghat.",
   
    "Hello I am your AI Guide.",

    "I think you are happy."

]

# Main chatbot function
def get_bot_response(user_input):

    user_input = user_input.lower().strip()

    scores = []

    # Compare all questions
    for sentence in questions:

        score, common = sentence_meaning_score(
            sentence,
            user_input
        )

        scores.append(score)

    print(scores)

    # Highest score
    max_score = max(scores)

    # Best matching index
    best_index = scores.index(max_score)

    # Final result
    if max_score == 0 or max_score < 0.5:

        return "Not Understand ??"

    else:

        return answers[best_index]