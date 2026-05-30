import re
from nltk.corpus import stopwords
data ="random 100 words peragaraph which include punchuation symbolsThe old," \
" dusty bookstore—located on 5th Avenue—was a hidden treasure trove; it smelled of aged paper," \
" leather, and vanilla. Look at this! exclaimed Sarah, pointing eagerly toward a leather-bound " \
"journal. The cover was worn, yet beautiful; it had a strange, golden crest engraved in the center." \
" She asked the clerk, How much for this item? He smiled, stroked his gray beard, and whispered," \
" For you? It's free. Sarah gasped. Was this a trick? She opened the first page, finding a handwritten note: Adventure awaits"

# print len of data
print(len(data))

# covert data in lowercase
data = data.lower()

# remove puncuation
data = re.sub(r'[^\w\s]', '',data)

# remove numbers
data = re.sub(r'\d+','',data)

# remove extra space
data = " ".join(data.split())

# print len of data
print(len(data))

 # tokkenization
tokenize_data = data.split()


#  remove stop words
stop_word = stopwords.words('english')
filter_data = []

for word in tokenize_data:
    if word not in stop_word:
        filter_data.append(word)

# join words again        
clean_data = " ".join(filter_data) 

print(clean_data)

# print len of data
print(len(clean_data))