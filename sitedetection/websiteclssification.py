import pandas as pd
import matplotlib.pyplot as plt
import nltk

from nltk.corpus import stopwords

# First time only
nltk.download('punkt')
nltk.download('stopwords')

data = {

    'food': ['dhosha', 'idley', 'daal makhni',
             'maggie', 'tea', 'lemon rise',
             'tandori kawab', 'lacha paratha',
             'machi bhat'],

    'movie': ['bhadmosh', 'lutery', 'sholey',
              'singham', 'angure',
              'ghar wali bhar wali',
              'sola sabnam', 'veeru','singham']

}

df = pd.DataFrame(data)

# Paragraph
peragraph = """
Yesterday I ate dhosha and maggie with tea.
After dinner I watched sholey and singham movie.
Tea was very good with machi bhat.
"""

# Step-1 Lowercase
lower_text = peragraph.lower()

# Step-2 Tokenization
tokens = lower_text.split()

# Step-3 Stopwords remove
stop_words = set(stopwords.words('english'))

filter_data = []

# step-4 filter the important word 
for word in tokens:

    # punctuation remove
    word = word.replace('.', '').replace(',', '')

    if word not in stop_words:
        filter_data.append(word)

print("Filtered words:")
print(filter_data)

# Total counts
total_food_count = 0
total_movie_count = 0

# step-5 Compaire the result
print("\nMatching Results:\n")

for item in filter_data:

    food_count = (df["food"] == item).sum()

    movie_count = (df["movie"] == item).sum()

    # add totals
    total_food_count += food_count
    total_movie_count += movie_count

    # print only matched words
    if food_count > 0:
        print(item, "=> Food Match =", food_count)

    if movie_count > 0:
        print(item, "=> Movie Match =", movie_count)

# step-6  Final totals
print("\nTotal Food Matches =", total_food_count)

print("Total Movie Matches =", total_movie_count)

# step-7 Final classification
if total_food_count > total_movie_count:
    print("\nParagraph is FOOD related")

elif total_movie_count > total_food_count:
    print("\nParagraph is MOVIE related")

else:
    print("\nParagraph is MIXED or UNKNOWN")

# step-8 Show the result in graph
category = ['food','moovie']
count = [total_food_count, total_movie_count]
plt.bar(category,count, color = ['green','orange'])
plt.title("Paragraph Classification")

plt.xlabel("Category")
plt.ylabel("Match Count")

plt.grid(axis='y')

plt.show()