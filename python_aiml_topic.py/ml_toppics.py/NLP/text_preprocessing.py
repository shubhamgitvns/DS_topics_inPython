import re
data ="random 100 words peragaraph which include punchuation symbolsThe old," \
" dusty bookstore—located on 5th Avenue—was a hidden treasure trove; it smelled of aged paper," \
" leather, and vanilla. Look at this! exclaimed Sarah, pointing eagerly toward a leather-bound " \
"journal. The cover was worn, yet beautiful; it had a strange, golden crest engraved in the center." \
" She asked the clerk, How much for this item? He smiled, stroked his gray beard, and whispered," \
" For you? It's free. Sarah gasped. Was this a trick? She opened the first page, finding a handwritten note: Adventure awaits"
# covert data in lowercase
data = data.lower()
print(len(data))
# remove puncuation
clean_data = re.sub(r'[^\w\s]', '',data)

# remove numbers
clean_data = re.sub(r'\d+','',clean_data)

# remove extra space

clean_data = " ".join(clean_data.split())

 # tokkenization
clean_data = clean_data.split()

print(clean_data)

print(len(clean_data))