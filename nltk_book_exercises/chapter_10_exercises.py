#!/usr/bin/env python
# coding: utf-8

# __Exercise 1__

# In[1]:


import nltk, re, pprint


# In[2]:


read_expr = nltk.sem.Expression.fromstring
read_expr('Asi -> -Bsu') # Asi: "Agnus sings", Bsu: "Bertie sulks"


# In[3]:


read_expr('Cr & Cb') # Cr: "Cyril runs", Cb: "Cyril barks"


# In[4]:


read_expr('-r -> s') # r: "rain", s: "snow"


# In[5]:


read_expr('-((Oc | Tc) -> Ih)') # Oc: "Olive comes", Tc: "Tofu comes", Ih: "Irene is happy"


# In[6]:


read_expr('-(Pc | Ps)') # Pc: "Pat coughed", Ps: "Pat sneezed"


# In[7]:


read_expr('(Ica -> -Yco) -> (Yca -> -Ico)') # Ico: "I come", Yco: "you come", Ica: "I call", Yca: "You call"


# __Exercise 2__

# In[8]:


read_expr('like(angus,cyril) & hate(irene,cyril)')


# In[9]:


read_expr('taller(tofu,bertie)')


# In[10]:


read_expr('love(bruce,bruce) & love(pat,pat)')
# or
read_expr('love(bruce,bruce) & love(pat,bruce)')


# In[11]:


read_expr('see(cyril,bertie) & -see(angus,bertie)')


# In[12]:


read_expr('fourleggedfriend(cyril)')


# In[13]:


read_expr('near(tofu,olive) & near(olive,tofu)')


# __Exercise 3__

# In[14]:


read_expr('exists x.like(angus,x) & exists y.like(y,julia)')


# In[15]:


read_expr('exists x.(dog(x) & love(angus,x) & love(x,angus))')


# In[16]:


read_expr('-exists x.smile(x,pat)')


# In[17]:


read_expr('exists x.(cough(x) & sneeze(x))')


# In[18]:


read_expr('-exists x.(cough(x) | sneeze(x))')


# In[19]:


read_expr('exists x.(love(bruce,x) & -equal(x,bruce))')


# In[20]:


read_expr('-exists x.(love(x,pat) & -equal(x,matthew))')


# In[21]:


read_expr('all x.(like(cyril,x) & -equal(x,irene))')


# In[22]:


read_expr('exists x.asleep(x) & all y.(-equal(x,y) & -asleep(y))')


# __Exercise 4__

# In[23]:


read_expr(r'\x.(feed(x,cyril) & give(x,cappuccino,angus))')


# In[24]:


read_expr(r'\x.give(pat,warandpeace,x)')


# In[25]:


read_expr(r'all y.(\x.love(y,x))')


# In[26]:


read_expr(r'all y.(\x.(love(y,x) | detest(y,x)))')


# In[27]:


read_expr(r'all y.(\x.(love(y,x) & -detest(y,x)))')


# __Exercise 5__

# In[28]:


read_expr = nltk.sem.Expression.fromstring
e1 = read_expr(r'\x.(exists y.love(x,y))')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify())


# In[29]:


# Translation: Pat loves someone.


# In[30]:


e1 = read_expr(r'\x.(exists y.(love(x,y) | love(y,x)))')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify())


# In[31]:


# Translation: Pat loves someone or someone loves Pat.


# In[32]:


e1 = read_expr(r'\x.(walk(fido))')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify())


# __Exercise 6__

# In[33]:


e1 = read_expr(r'\P.\x.all y.(dog(y) -> P(x,pat))')
e2 = read_expr('chase')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify()) # \x.all y.(dog(y) -> chase(x,pat))


# In[34]:


e1 = read_expr(r'\P.\x.exists y.(dog(y) & P(pat,x))')
e2 = read_expr('chase')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify()) # \x.exists y.(dog(y) & chase(pat,x))


# In[35]:


e1 = read_expr(r'\P x0 x1.exists y.(present(y) & P(x1,y,x0))')
e2 = read_expr('give')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify()) # \x0 x1.exists y.(present(y) & give(x1,y,x0))


# __Exercise 7__

# In[36]:


e1 = read_expr(r'\P.exists y.(dog(x) & P(x))')
e2 = read_expr('bark')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify()) # exists y.(dog(x) & bark(x))


# In[37]:


e1 = read_expr(r'\P.P(fido)')
e2 = read_expr('bark')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify()) # bark(fido)


# In[38]:


e1 = read_expr(r'\P. all x.(dog(x) -> bark(x))')
e2 = read_expr('\\P. all x.(dog(x) -> P(x))')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify()) # all x.(dog(x) -> bark(x))


# __Exercise 11__ (unfinished)

# In[39]:


# Sentences:
# 1) Once upon a time there was a little boy, and he wanted to be a cock-a-doo-dle-doo.
# 2) So he was a cock-a-doo-dle-doo.
# 3) And he wanted to fly up into the sky.
# 4) So he did fly up into the sky.

# Should translate to:
# 1) be(boy) & want(boy, be(boy,cock-a-doo-dle-doo))
# 2) be(boy,cock-a-doo-dle-doo)
# 3) want(boy, fly(boy))
# 4) fly(boy)
from nltk import load_parser
cp = load_parser('file:chapter_10_ex11.fcfg')
# 2)
query = 'So he was a cock-a-doo-dle-doo'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)


# In[40]:


# 3)
query = 'And he wanted to fly up into the sky'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)


# In[41]:


# 1a)
query = 'Once upon a time there was a little boy'
cp = load_parser('file:chapter_10_ex11.fcfg')
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)


# In[42]:


# 1b)
query = 'he wanted to be a cock-a-doo-dle-doo'
cp = load_parser('file:chapter_10_ex11.fcfg')
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)


# In[43]:


# 1)
query = 'Once upon a time there was a little boy and he wanted to be a cock-a-doo-dle-doo'
cp = load_parser('file:chapter_10_ex11.fcfg')
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)


# In[44]:


# 4)
query = 'So he did fly up into the sky'
cp = load_parser('file:chapter_10_ex11.fcfg')
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)


# In[59]:


dom = {'b', 'c'}
v = """
boy => b
cockadoodledoo => c
fly => {b}
be => {(b)}, (b, c)}
"""
# don't know how to add the want with the nested phrase :/
val = nltk.Valuation.fromstring(v)
print(val)


# In[60]:


m = nltk.Model(dom, val)
g = nltk.Assignment(dom)
m.evaluate('fly ( boy )', g)


# In[61]:


m.evaluate('fly ( cockadoodledoo )', g)


# In[62]:


m.evaluate('-fly ( boy )', g)


# In[63]:


m.evaluate('be ( boy , cockadoodledoo )', g)


# In[64]:


m.evaluate('be ( boy )', g)


# In[65]:


m.evaluate('be ( cockadoodledoo , boy )', g)


# In[ ]:




