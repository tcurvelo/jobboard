from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize, wordpunct_tokenize
from nltk.corpus import stopwords

from pprint import pprint

import json
import nltk

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

with open('jobs.json') as jobsfile:
    jobs = json.loads(jobsfile.read())

words = FreqDist([])
for job in jobs:
    new_words = [
        w for w in wordpunct_tokenize('{} {}'.format(job['title'], job['text']).lower()) if w not in stop_words
    ]
    words += FreqDist(new_words)

pprint(words.most_common(100))
