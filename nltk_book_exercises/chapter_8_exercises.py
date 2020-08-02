#!/usr/bin/env python
# coding: utf-8

# __Exercise 1__

# In[1]:


# Today is Saturday, the 5th of May 2018 and my name is Julia, living in [address],
# and I'm currently fullfilling an nltk book assignment.


# __Exercise 2__

# In[3]:


# used in sense of 'no matter how': 
#    “However beautiful the strategy, you should occasionally look at the results.”
#    “However bad you think you’re going to be in that room, not being there is worse.”
# used as connector:
#    "However, they kept on, with unabated perseverance."


# __Exercise 3__

# In[14]:


# (Kim arrived) or (Dana left and everyone cheered).
# (Kim arrived or Dana left) and everyone cheered.

import nltk, pprint, re
grammar = nltk.CFG.fromstring("""
S -> NP VP
S -> S Conj S
VP -> "arrived" | "left" | "cheered"
NP -> "Kim" | "Dana" | "everyone"
Conj -> "and" | "or"
""")

sr_parse = nltk.ShiftReduceParser(grammar, trace=2)
sent = 'Kim arrived or Dana left and everyone cheered'.split()
for tree in sr_parse.parse(sent):
    print tree


# In[16]:


grammar = nltk.PCFG.fromstring("""
S -> NP VP [0.6]
S -> S Conj S [0.4]
VP -> "arrived" | "left" | "cheered" [1.0]
NP -> "Kim" | "Dana" | "everyone" [1.0]
Conj -> "and" | "or" [1.0]
""")

viterbi_parse = nltk.ViterbiParser(grammar, trace=2)
sent = 'Kim arrived or Dana left and everyone cheered'.split()
for tree in viterbi_parse.parse(sent):
    print tree


# __Exercise 4__

# In[17]:


from nltk import Tree
help(Tree)


# __Exercise 5__

# In[24]:


# a
tree1 = Tree('NP', 
             [Tree('JJ', ['old']), 
              Tree('NP', 
                   [Tree('N', ['men']), Tree('Conj', ['and']), Tree('N', ['women'])])])
print(tree1)


# In[25]:


tree2 = Tree('NP', 
             [Tree('NP', 
                   [Tree('JJ', ['old']), Tree('N', ['men'])]), 
              Tree('Conj', ['and']), 
              Tree('NP', ['women'])])
print(tree2)


# In[22]:


# b
tree3 = Tree.fromstring("((S (NP I) (VP (VP (V shot) (NP (Det an) (N elephant))) (PP (P in) (NP (Det my) (N pajamas))))))")
tree3.draw()


# In[23]:


# c
tree4 = Tree('S', 
             [Tree('NP', 
                   [Tree('Det', ['The']), Tree('N', ['woman'])]), 
              Tree('VP', 
                   [Tree('V', ['saw']), 
                    Tree('NP', 
                         [Tree('Det', ['a']), Tree('N', ['man'])]),
                    Tree('NP',
                        [Tree('JJ', ['last']), Tree('N', ['Thursday'])])])])
print(tree4)
tree4.draw()


# In[ ]:




