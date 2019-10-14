import nltk
from nltk import trigrams  
#A. To read the content of the nlp_input.text file and encode the content to UTF8 
with open('nlp_input.txt', encoding='utf8', errors='ignore') as f:
    nlp_q7_text = f.read()

#B. To Tokenize the text into words and apply lemmatization technique on each word



#First, To perform Tokenization on the nlp_input_text, we will use words Tokenization:
q7wordToken = nltk.word_tokenize(nlp_q7_text)
for word in q7wordToken:
    print(word)


#To apply lemmatization technique on each word

from nltk.stem import WordNetLemmatizer


q7_lemmatization = WordNetLemmatizer()
q7_lemmatization_result = q7_lemmatization.lemmatize(str(q7wordToken))
print(q7_lemmatization_result)


#c. To Find all the trigrams for the words.
from nltk import trigrams
Q7_trigrams = list(trigrams(q7wordToken))

print(Q7_trigrams)

#d. To Extract the top 10 of the most repeated trigrams based on their count
from collections import Counter, OrderedDict
import operator

q7_repeated_trigrams = Counter(Q7_trigrams).most_common(10)

repeated_trigrams = OrderedDict(q7_repeated_trigrams)

print(repeated_trigrams)

#F. To Find all the sentences with the most repeated tri-grams and show the result
q7sentenceToken = nltk.sent_tokenize(nlp_q7_text)
mystring = ''
myList = []
result = []
for w in repeated_trigrams:
    for word in w:
        
        mystring += word
        mystring += ' '
    myList.append(mystring)
    mystring = ''


for sentence in q7sentenceToken:
    for l in myList:
        if l in sentence:
            stringResult=''
            stringResult += sentence +'->repeated tri-gram:('+l+')'
            result.append(stringResult)
for r in result:
    print(r)