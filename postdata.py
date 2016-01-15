import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
import  csv
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


#nltk.download()

#f = open('cong2.csv')
#reader = csv.reader(f)
#for row in reader:
#    print row

#patterns= ['this','that']
#text = 'Does this text match the pattern?'

#for pattern in patterns:

#	if re.search(pattern,text):
#		print 'match found'

#	else:
#		print 'not found'

def removePunctuation(input_list):
    punctuation=re.compile(r'[,./?!":;|-]')
    
    punct_remove = [punctuation.sub(" ", word) for word in input_list]
    
    return punct_remove

# Remove Stop Words
def removeStopWords(input_list):
    stop=stopwords.words('english')
    #Need to preserve not,nor and no as these contain information
    stop.remove('not')
    stop.remove('nor')
    stop.remove('no')
    stop.append('')
    
    for s in stop:
        while s in input_list:
            input_list.remove(s)
    return input_list
ofile  = open('kkk.txt', "wb")
writer = csv.writer(ofile)

with open ('bajaj2.csv','rb') as testing_file:
	testing_data=csv.reader(testing_file)
	for row in testing_data:
		word_list_split=re.split('\s+',row[0].lower())
		word_list_minus_punct=removePunctuation(word_list_split)
		word_list_minus_stop=removeStopWords(word_list_minus_punct)
		for word in word_list_minus_stop:
			writer.writerow([word])
			
    
