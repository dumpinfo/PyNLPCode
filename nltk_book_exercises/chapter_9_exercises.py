#!/usr/bin/env python
# coding: utf-8

# __Exercise 1__

# In[1]:


import nltk, re, pprint
from nltk import load_parser
grammar8 = load_parser('file:chapter_9_ex1_a.fcfg')
sent = "I am happy".split()
trees = grammar8.parse(sent)
for tree in trees:
    print tree


# In[2]:


sent = "she is happy".split()
trees = grammar8.parse(sent)
for tree in trees:
    print tree


# In[3]:


sent = "you is happy".split()
trees = grammar8.parse(sent)
for tree in trees:
    print tree


# In[4]:


sent = "they am happy".split()
trees = grammar8.parse(sent)
for tree in trees:
    print tree


# In[5]:


grammar20 = load_parser('file:chapter_9_ex1_b.fcfg')
sent = "I am happy".split()
trees = grammar20.parse(sent)
for tree in trees:
    print tree


# In[6]:


sent = "she is happy".split()
trees = grammar20.parse(sent)
for tree in trees:
    print tree


# In[7]:


sent = "you is happy".split()
trees = grammar20.parse(sent)
for tree in trees:
    print tree


# In[8]:


sent = "they am happy".split()
trees = grammar20.parse(sent)
for tree in trees:
    print tree


# __Exercise 2__

# In[9]:


grammar = load_parser('file:chapter_9_ex2.fcfg')
sent = "the boy sings".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# In[10]:


sent = "boy sings".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# In[11]:


sent = "the boys sing".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# In[12]:


sent = "boys sing".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# In[13]:


sent = "the water is precious".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# In[14]:


sent = "water is precious".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# __Exercise 3__

# In[15]:


def subsumes(f1, f2):
    if len(f2.keys()) > len(f1.keys()):
        return False;
    for key in f2.keys():
        if (key not in f1.keys()) or (f1[key] != f2[key]):
            return False;
    return True

fs1 = nltk.FeatStruct(A='a')
fs2 = nltk.FeatStruct(A='a', B='b')
print subsumes(fs1, fs2)
print subsumes(fs2, fs1)


# __Exercise 4__

# In[16]:


# don't know what is expected here :/ see chapter_9_ex4.fcfg


# __Exercise 5__

# In[17]:


grammar = load_parser('file:chapter_9_ex5.fcfg')
sent = "ich sehe die Hunde".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# In[18]:


sent = "wir kommen".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# In[19]:


sent = "ich komme die Hunde".split()
trees = grammar.parse(sent)
for tree in trees:
    print tree


# __Exercise 6__

# In[20]:


grammar = load_parser('file:chapter_9_ex6.fcfg')

def parse(sent, grammer):
    sent = sent.split()
    trees = grammar.parse(sent)
    for tree in trees:
        print tree

parse("un cuadro hermoso", grammar)


# In[21]:


parse("unos cuadros hermosos", grammar)


# In[23]:


parse("una cortina hermosa", grammar)


# In[24]:


parse("unas cortinas hermosas", grammar)


# In[25]:


parse("un cuadro hermosas", grammar)


# In[27]:


parse("unos cortinas hermosas", grammar)


# In[ ]:




