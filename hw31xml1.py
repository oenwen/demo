import xml.etree.ElementTree as ET

tree = ET.parse('newsafr.xml')

root = tree.getroot()

xml_items = root.findall("channel/item/description")

words_lists = list()

for xmli in xml_items:
  words_lists.append(xmli.text.split())
 
words = []
for word_list in words_lists:
  words.extend(word_list)

long_words = []
for word in words:
  if len(word) > 6:
    long_words.append(word)

print(*sorted(set(long_words), key = long_words.count, reverse=True)
[:10], sep = '\n')
