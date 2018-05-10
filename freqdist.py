from nltk.probability import  FreqDist
from pprint import pprint

import json
import nltk

nltk.download('punkt')


with open('jobs.json') as jobsfile:
    jobs = json.loads(jobsfile.read())

words = FreqDist([])
for job in jobs:
    words += FreqDist(nltk.tokenize.word_tokenize(job['text'].lower()))

pprint(words.most_common(100))
