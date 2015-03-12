import numpy as np
import random
import pickle

dataset = [[1,20,1], [2,21,0], [3,22,1]]

# it zips column by column
print zip(*dataset)
# [(1, 2, 3), (20, 21, 22), (1, 0, 1)]

'''
pickle
with open('./data/sentences.pickle', 'wb') as handle:
	pickle.dump(X, handle)
with open('./data/sentences.pickle', 'rb') as handle:
	X = pickle.load(handle)
'''


#uniform
print random.uniform(-1,1)
mu = 0
sigma = 2
print np.random.normal(mu, sigma)


np.genfromtxt('myfile.csv',delimiter=',')

# shuffle lines of a file
# cat yourfile.txt | while IFS= read -r f; do printf "%05d %s\n" "$RANDOM" "$f"; done | sort -n | cut -c7- >> new_file
# wc -l < file_name for # of lines
# head -n K file_name > out, tail -n K file_name > out for splitting files with K number of lines top to bottom
# codecs.open(trainfile,'r','utf8')

def rms_error(predictions, targets):
    return math.sqrt(ms_error(predictions, targets))

def ms_error(predictions, targets):
    return mean([(p - t)**2 for p, t in zip(predictions, targets)])

def mean_error(predictions, targets):
    return mean([abs(p - t) for p, t in zip(predictions, targets)])

def mean_boolean_error(predictions, targets):
    return mean([(p != t)   for p, t in zip(predictions, targets)])