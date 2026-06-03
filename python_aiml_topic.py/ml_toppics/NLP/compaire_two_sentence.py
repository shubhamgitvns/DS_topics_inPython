from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "This is Hell",
    "Heaven is this"
]

vectorizer = CountVectorizer()

vectors = vectorizer.fit_transform(sentences)

similarity = cosine_similarity(vectors)
print("Vectors")
print(vectorizer)
print(vectors)
print(similarity)