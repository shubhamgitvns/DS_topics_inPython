from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import re

menu = {

    "tea": 10,
    "special tea": 20,
    "coffee": 50,
    "maggie": 100,
    'gulabjamun': 15,
    'dahi bada': 18,
    'samosh': 15,
    'kachori': 25,
    'allu pakode': 90,
    'pannir pakode': 100,
    'lassi':  50,
    'chach':  40,
    'pepsi': 25,
    'cola': 25,
}

sweet = {

    'gulabjamun': 15,
    'dahi bada': 18
}


snacks = {

    'samosh': 15,
    'kachori': 25,
    'allu pakode': 90,
    'pannir pakode': 100
}

drinks = {
    'lassi':  50,
    'chach':  40,
    'pepsi': 25,
    'cola': 25
}
# Create menu text automatically
menu_text = "\n".join(
    [f"{item} - {price}rs" for item, price in menu.items()]
)
sweets_text = '\n'.join(
    [f"{item} - {price}rs" for item, price in sweet.items()]
)

drinks_text = '\n'.join(
    [f"{item} - {price}rs" for item, price in drinks.items()]
)
snacks_text = '\n'.join(
    [f"{item} - {price}rs" for item, price in snacks.items()]
)


def clean_words(sentence):

    # lowercase
    sentence = sentence.lower()

    # tokenize
    words = re.findall(r"[a-z]+", sentence)

    # stopwords
    stop_words = set(stopwords.words("english"))

    filtered = []
    for word in words:

        if word not in stop_words:

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
    "menue please",
    "i want sweets dish",
    " i want drinks",
    "i want snacks",

    "hello"

  

]


# Answers
answers = [
    f"Our Menu:\n{menu_text}\n\nPlease Write Your Order Sir",
    f"Our Sweet dish:\n{sweets_text}\n\nPlease Write Your Order Sir",
    f"Our Sweet dish:\n{drinks_text}\n\nPlease Write Your Order Sir",
    f"Our Sweet dish:\n{snacks_text}\n\nPlease Write Your Order Sir",

    "Hello I am your AI assistant.\nWhich dish you want ??"

  
]

# Chat loop
user_input = 'hello'.lower().strip()
print("\nWelcome to our resturent\nHello sir i am ai assistent\nwhich type food you want ??")
print("Types:")
print("Menue\nSnacks\nSweets\nDrinks")
while True:

    user_input = input("\nYou: ").lower().strip()

    # EXIT
    if user_input == "exit":

        print("\nBot: Thank You Visit Again")
        break

    # ================= ORDER CHECK =================

    order_found = []

    total_bill = 0

    for item, price in menu.items():

        if item in user_input:

            order_found.append(item)

            total_bill += price

    # ================= BILL =================

    if len(order_found) > 0:

        print("\nBot: Your Order Bill")

        print("----------------------")

        for item in order_found:

            print(item, "=", menu[item], "rs")

        print("----------------------")

        print("Total Bill =", total_bill, "rs")

    # ================= NOT AVAILABLE =================

    elif any(word in user_input for word in clean_words(menu_text)):

        print(
            "\nBot: Not Available This Order\nPlease Write Again Your Order"
        )

    # ================= CHATBOT =================

    else:

        scores = []

    # Compare all questions
    for sentence in questions:

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

        print("\nBot:", answers[best_index])
