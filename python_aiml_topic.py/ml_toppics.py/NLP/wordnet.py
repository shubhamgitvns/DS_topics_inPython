from nltk.corpus import wordnet as wn
import re


def clean_words(sentence):
    sentence = sentence.lower()
    return re.findall(r"[a-z]+", sentence)


def synonyms_of(word):
    words = {word}

    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            words.add(lemma.name().lower().replace("_", " "))

    return words


def expanded_sentence_words(sentence):
    result = set()

    for word in clean_words(sentence):
        result.update(synonyms_of(word))

    return result


def sentence_meaning_score(sentence1, sentence2):
    words1 = expanded_sentence_words(sentence1)
    words2 = expanded_sentence_words(sentence2)

    common = words1.intersection(words2) # add the filterd sentence sunonyms
    total = words1.union(words2) # get the unique words between two sets
   
    if not total:
        return 0, common

    score = len(common) / len(total)
    return score, common


s1 = "about the Varasnasi"
s2 = "I want films"
s3 = "I want sleep"
s4 = "I want drink"
s5 = 'i want drink wisky'
s6 = 'what is loop'
s7 = 'what is for'
s8 = 'hello'
s9 = 'what is while'
s10 = 'i am happy i feal happy'


for i in range(5):
    inputsentence = input("\nHello:\n").lower().strip()
    input_words = inputsentence.split()
    score1, c1 = sentence_meaning_score(s1, inputsentence)
    score2, c2 = sentence_meaning_score(s2, inputsentence)
    score3, c3 = sentence_meaning_score(s3, inputsentence)
    score4, c4 = sentence_meaning_score(s4,inputsentence)
    score5, c5 = sentence_meaning_score(s5,inputsentence)
    score6, c6 = sentence_meaning_score(s6,inputsentence)
    for_loop, c7 = sentence_meaning_score(s7,inputsentence)
    while_loop, c9 = sentence_meaning_score(s9,inputsentence)
    happy, c10 = sentence_meaning_score(s10,inputsentence)
    intro, c8 = sentence_meaning_score(s8,inputsentence)
    
    if "for" in input_words:
        for_loop = 1.0
    else:
        for_loop = 0 

    if "while" in input_words:
        while_loop = 1.0
    else:
        while_loop = 0    
    if 'loop' in input_words and 'for' not in input_words and 'while' not in input_words:
        s6 = 1.0
    else:
        s6=0
        



    max_ch = max(score1,score2,score3,score4,score5,score6,for_loop, while_loop, intro,happy)
    print(score1,score2,score3,score4,score5,score6,for_loop,intro,happy)
    if max_ch ==0.0:
        print("Not Understand ??")
    elif max_ch == score1:
        print("Varanasi, also known as Kashi or Banaras, is one of the oldest living cities in the world. It is located on the banks of the sacred Ganges River in the Indian state of Uttar Pradesh.The city is considered the spiritual capital of India and is deeply connected with Hindu culture, history, and traditions.")
        
    elif max_ch == score2:
        print("Movie Dekg lo")
    elif max_ch == score3:
        print("Aram Ker lo")
    elif max_ch == score4:
        print("Bilkol pe lo")
    elif max_ch == score5:
        print("Pe le pe le more raja")

    elif max_ch ==  score6:
            print("\nA loop in Python is used to repeat a task multiple times.\nThere are three types of loops\n while loop\n for loop\n do while loop")  
    
    elif max_ch == for_loop:
         print('\nA for loop in Python is used to repeat a task multiple times.\nSyntex: \nfor variable in sequence:\nCode: \nfor i in range(5):\nprint(i)\nOutpuut: \n1\n2\n3\n4\n5 ')
         
    
    elif max_ch == while_loop:
         print('\nA while loop is used to repeat code while a condition is True.\nSyntex: \nwhile condition:\nCode: \ni=0\n :\nprint(i)while i<=5:\nprint(i)\nOutpuut: \n1\n2\n3\n4\n5 ')
    
    elif max_ch == intro:

        print("\nHello..\nI am Shubham Your Torrist Guider\nWhere you wisit today??")
    elif max_ch == happy:
        print('I Think you are happy')





