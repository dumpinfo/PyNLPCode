#!/usr/bin/env python
# coding: utf-8

# __Exercise 1__

# In[1]:


# MACHINE TRANSLATION:
# see e.g. http://www.aclweb.org/anthology/R11-1077, https://nlp.stanford.edu/courses/cs224n/2010/reports/bipins.pdf
# data: parallel corpora, aligned at sentence level (automatically or manually)
# size: usually assumed the larger the better, 2nd paper: 100,00 documents
# reasons for large amount: probability that a word or combination of words has been seen during training increases


# __Exercise 2__

# In[2]:


import nltk
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
test, devtest, training = names[:500], names[500:1000], names[1000:]

def gender_features1(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    features["suffix2"] = name[-2:].lower()
    return features

train_set = [(gender_features1(n), g) for (n,g) in training]
devtest_set = [(gender_features1(n), g) for (n,g) in devtest]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)


# In[3]:


def error_analysis(gender_features):
    errors = []
    for (name, tag) in devtest:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag, guess, name))
    print 'no. of errors: ', len(errors)        
        
    for (tag, guess, name) in sorted(errors): # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)        
        
error_analysis(gender_features1)        


# In[4]:


def gender_features2(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    features["suffix2"] = name[-2:].lower()
    features["suffix3"] = name[-3:].lower()
    return features

train_set = [(gender_features2(n), g) for (n,g) in training]
devtest_set = [(gender_features2(n), g) for (n,g) in devtest]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)


# In[5]:


error_analysis(gender_features2)


# In[6]:


def gender_features3(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    features["suffix2"] = name[-2:].lower()
    features["suffix3"] = name[-3:].lower()
    features["prefix3"] = name[:3].lower()
    return features

train_set = [(gender_features3(n), g) for (n,g) in training]
devtest_set = [(gender_features3(n), g) for (n,g) in devtest]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)


# In[7]:


error_analysis(gender_features3)


# In[8]:


def gender_features4(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    features["suffix2"] = name[-2:].lower()
    features["suffix3"] = name[-3:].lower()
    features["prefix3"] = name[:3].lower()
    features["num_vowels"] = len([letter for letter in name if letter in 'aeiouy'])
    return features

train_set = [(gender_features4(n), g) for (n,g) in training]
devtest_set = [(gender_features4(n), g) for (n,g) in devtest]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)


# In[9]:


# final performance test:
test_set = [(gender_features4(n), g) for (n,g) in test]
print nltk.classify.accuracy(classifier, test_set)


# In[10]:


# performance slightly worse than in dev-test -> features reflect some idiosyncracies of dev-test


# __Exercise 3)__

# In[11]:


from nltk.corpus import senseval
instances = senseval.instances('serve.pos')
size = int(len(instances) * 0.1)
training, test = instances[size:], instances[:size]


# In[12]:


training[0]


# In[13]:


def sense_features(instance):
    features = {}
    features["word-type"] = instance.word
    features["word-tag"] = instance.context[instance.position][1] 
    features["prev-word"] = instance.context[instance.position-1][0]
    features["prev-word-tag"] = instance.context[instance.position-1][1]
    features["next-word"] = instance.context[instance.position+1][0]
    features["next-word-tag"] = instance.context[instance.position+1][1]
    return features

train_set = [(sense_features(instance), instance.senses) for instance in training]
test_set = [(sense_features(instance), instance.senses) for instance in test]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)


# __Exercise 4)__

# In[14]:


from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
classifier.show_most_informative_features(30)


# In[15]:


# most of them already indicate some judgment in themselves ('ugh', 'mediocrity') or belong to typical phrases that
# indicate one direction of judgement ('understands' -> '... understands how to create atmosphere' or something like that)
# some seem to be names of actors etc. which tend to be judged one direction or the other
# surprising -> '33', 'wires'


# __Exercise 5)__

# In[ ]:




