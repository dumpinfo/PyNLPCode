#!/usr/bin/env python
# coding: utf-8

# __Exercise 1)__

# In[1]:


# if two chunks follow each other, it would not be possible to make clear 
# that they are two chunks instead of one chunk consisting of two words
# and also not where the first ends and the second begins


# __Exercise 2)__

# In[2]:


# singular noun phrases: <DT>?<JJ.*>*<NN.*>+
# plural noun phrases: <DT>?<JJ.*>*<NN.*>*<NNS>+


# __Exercise 3)__

# In[3]:


import nltk, re, pprint, random
from nltk.corpus import conll2000


# In[4]:


numSents = len(conll2000.chunked_sents('train.txt'))
for i in xrange(10):
    randomIndex = random.randint(0, numSents - 1)
    print conll2000.chunked_sents('train.txt', chunk_types=['PP'])[randomIndex]


# In[5]:


# possible tags: TO, IN, RB IN, VBG, JJ IN


# In[6]:


grammar = r"""
    PP: {<RB|JJ\$>?<IN>} # e.g. such as
        {<TO|VBG>} # e.g. to, regarding
"""
cp = nltk.RegexpParser(grammar)
brown = nltk.corpus.brown
for sent in brown.tagged_sents()[:10]:
    tree = cp.parse(sent)
    print tree


# In[7]:


# VBG is problematic of course, might have been a false hit / tag in the first place


# __Exercise 4__

# In[8]:


# for some input: get VP chunks from corpus
for i in xrange(10):
    print conll2000.chunked_sents('train.txt', chunk_types=['VP'])[i]


# In[9]:


# get the chinks of given example sentences (unfinished):
tag_sequences_to_chink = set()
for i in xrange(10):
    randomIndex = random.randint(0, numSents - 1)
    tree = conll2000.chunked_sents('train.txt', chunk_types=['NP', 'PP'])[randomIndex]
    for subtree in tree.subtrees():
        if subtree.label() != 'S':
            tag_sequences_to_chink.add(tuple([tag for (word, tag) in subtree.leaves()]))
print tag_sequences_to_chink            


# In[22]:


rule_string = r"""
    VP:
     {<.*>+}        # Chunk everything
"""
for tag_seq in tag_sequences_to_chink: # include a chink rule for each sequence determined in the stap before
    rule_string += '\n}'
    for tag in tag_seq:
        rule_string += '<' + tag + '>'
    rule_string += '{'       
chink_parser = nltk.RegexpParser(rule_string)

for i in xrange(10):
    print chink_parser.parse(conll2000.tagged_sents('train.txt')[i])  


# In[20]:


# quite a number of false hits, but maybe quite good given the naive approach / little data used here


# __Exercise 7__

# In[24]:


# a)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['VP'])[:100]
chunkscore = chink_parser.evaluate(test_sents)
print chunkscore


# In[28]:


# b)
pprint.pprint(chunkscore.missed())


# In[29]:


pprint.pprint(chunkscore.incorrect())


# In[30]:


# misses a lot of single-word VP
# incorrectly adds a lot of adjectives, POS and punctuation


# In[31]:


# c)
# does slightly better than the baseline chunker (but probably not good enough to be used productively as it is)


# In[ ]:




