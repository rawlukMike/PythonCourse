import json
import sys
import requests
import re

shakespear = {
  "hamlet"      :  "https://raw.githubusercontent.com/cs109/2015/master/Lectures/Lecture15b/sparklect/shakes/hamlet.txt",
  "romeojuliet" : "https://raw.githubusercontent.com/cs109/2015/master/Lectures/Lecture15b/sparklect/shakes/romeojuliet.txt",
  "othello"     : "https://raw.githubusercontent.com/cs109/2015/master/Lectures/Lecture15b/sparklect/shakes/othello.txt"
}

def word_count(str):
  counts = dict()
  words = str.split()
  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  return counts

params = sys.argv[1:]
data = requests.get(shakespear[params[0]])
wordsCounted=word_count(re.sub("[!,*)@#%(&$_?.^]", " ", data.text.upper()))
#print(wordsCounted[params[1]])
print(json.dumps(wordsCounted, sort_keys=True))
