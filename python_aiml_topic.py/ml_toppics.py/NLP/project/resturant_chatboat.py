from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import datetime

lemmatizer = WordNetLemmatizer()


food_database = [

    "tea",
    "coffee",
    "pizza",
    "burger",
    "icecream",
    "cold drink",
    "maggie",
    "samosha",
    "kachori",
    "lassi",
    "cake",
    "sandwich",
    "pasta",
    "momo",
    "biryani",
    "stream",
    "ice cream"

]
time_based_special = {

    "morning": {

        "greeting": "Good Morning ☀️",

        "special": [
            "special tea",
            "poha"
        ],

        "message": "Would You Like Breakfast ?"
    },



    "afternoon": {

        "greeting": "Good Afternoon 🌤️",

        "special": [
            "kadhi chawal",
            "lassi"
        ],

        "message": "Would You Like Lunch ?"
    },



    "evening": {

        "greeting": "Good Evening 🌙",

        "special": [
            "coffee",
            "samosha"
        ],

        "message": "Would You Like Some Snacks ?"
    }
}

current_hour = datetime.datetime.now().hour


if current_hour < 12:

    current_time = "morning"

elif current_hour < 16:

    current_time = "afternoon"

else:

    current_time = "evening"


current_data = time_based_special[current_time]


menu = {

    "tea": 10,
    "special tea": 20,
    "coffee": 50,
    "maggie": 100,
    'gulabjamun': 15,
    'dahi bada': 18,
    'samosha': 15,
    'kachori': 25,
    'allu pakode': 90,
    'pannir pakode': 100,
    'lassi':  50,
    'chach':  40,
    'pepsi': 25,
    'cola': 25,

     'dall chawal full plate': 150,
    'dall chawal half plate': 100,
    'kadi chawal full plate': 180,
    'kadi chawal half plate': 120
}

sweet = {

    'gulabjamun': 15,
    'dahi bada': 18
}


snacks = {

    'samosha': 15,
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

lunchs = {
    'dall chawal full plate': 150,
    'dall chawal half plate': 100,
    'kadi chawal full plate': 180,
    'kadi chawal half plate': 120
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

lunchs_text = '\n'.join(
    [f"{item} - {price}rs" for item, price in lunchs.items()]
)

def normalize_word(word):

    return lemmatizer.lemmatize(word)

def clean_words(sentence):

    # lowercase
    sentence = sentence.lower()

    # tokenize
    words = re.findall(r"[a-z]+", sentence)

    # stopwords
    stop_words = set(stopwords.words("english"))

    # this word not remove
    stop_words.discard("no")
    stop_words.discard("not")

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
    "i want lunchs",
    "no",
    "yes",
    "hello"



]


# Answers
answers = [
    f"Our Menu:\n{menu_text}\n\nPlease Write Your Order Sir",
    f"Our Sweet dish:\n{sweets_text}\n\nPlease Write Your Order Sir",
    f"Our Drinks:\n{drinks_text}\n\nPlease Write Your Order Sir",
    f"Our Snacks dish:\n{snacks_text}\n\nPlease Write Your Order Sir",
    f"Our lunch dish:\n{lunchs_text}\n\nPlease Write Your Order Sir",
    "\nNo problem,\nHello sir i am ai assistent\nwhich type food you want ??\n\nTypes:\nSnacks\nSweets\nDrinks\nlunch\n\nIf you say yes i suggest you somthing special dish for you ??",
    "\nHello sir i am ai assistent\nwhich type food you want ??\n\nTypes:\nSnacks\nSweets\nDrinks\nlunch",


    "Hello I am your AI assistant.\nWhich dish you want ??"


]

# Chat loop
user_input = 'hello'.lower().strip()
print("\nWelcome to our resturent")
print("\n" + current_data["greeting"])

print("\nToday's Special:\n")

for item in current_data["special"]:

    print(item.title())

print("\n" + current_data["message"])
all_orders = []

grand_total = 0

while True:

    user_input = input("\nYou: ").lower().strip()
    print(synonyms_of(user_input))

    # EXIT
    if user_input == "exit":

        print("\nBot: Thank You Visit Again")
        break


    food_detected = False

    for food in food_database:
        normalize_comp_word = normalize_word(food)

        if normalize_comp_word in normalize_word(user_input):

            food_detected = True
            break

 
 

    # ================= ORDER CHECK =================

    current_order = []

    current_bill = 0

    for item, price in menu.items():

        if item in user_input:

            current_order.append(item)
            all_orders.append(item)

            current_bill += price
            grand_total += price

            # total_bill += price

    # ================= BILL =================

    if len(current_order) > 0:

        print("\nBot: Your Order Bill")

        print("----------------------")

        for item in current_order:

            print(item, "=", menu[item], "rs")

        print("----------------------")

        print("Total Bill =", current_bill, "rs")

         # ================= ALL ORDER HISTORY =================

        print("\n📦 All Orders")
        print("----------------------")

        for item in all_orders:

            print(item, "=", menu[item], "rs")

        print("----------------------")

        print("Grand Total =", grand_total, "rs")

    # ================= NOT AVAILABLE =================


    # elif any(word in user_input for word in clean_words(menu_text)):
       
    #     print(
    #         "\nBot: Not Available This Order\nPlease Write Again Your Order"
    #     )
    elif food_detected:

        print(
            "\nBot: Sorry 😔"
            "\nThis Food Is Not Available"
            "\nPlese order in minue"
        )
        continue

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

        print("\nBot:\n", answers[best_index])
