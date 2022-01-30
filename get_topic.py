import re
import nltk
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup

url = 'http://techcrunch.com/2016/05/26/snapchat-series-f/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find('title').get_text()
document = ' '.join([p.get_text() for p in soup.find_all('p')])

stop = stopwords.words(‘english’)

document = re.sub(‘[^A-Za-z .-]+’, ‘ ‘, document)
document = ‘ ‘.join(document.split())
document = ‘ ‘.join([i for i in document.split() if i not in stop])

words = nltk.tokenize.word_tokenize(document)
words = [word.lower() for word in words if word not in stop]
fdist = nltk.FreqDist(words)
most_freq_nouns = [w for w, c in fdist.most_common(10) if nltk.pos_tag([w])[0][1] in NOUNS]
