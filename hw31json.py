import json
# from pprint import pprint
# import collections
# c = collections.Counter()

with open('newsafr.json', encoding = 'utf8') as newsafr_json:
  news = json.load(newsafr_json)
  
items = news['rss']['channel']['items']
words_lists = list()
for item in items:
  description = item['description']  
  words_lists.append(description.split())
  
words = []
for word_list in words_lists:
  words.extend(word_list)

long_words = []
for word in words:
  if len(word) > 6:
    long_words.append(word)

print(*sorted(set(long_words), key = long_words.count, reverse=True)
[:10], sep = '\n')
