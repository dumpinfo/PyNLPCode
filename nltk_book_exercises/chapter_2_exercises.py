#!/usr/bin/env python
# coding: utf-8

# **Exercise 1)**

# In[1]:


phrase = ['My', 'very', 'unimaginative', 'phrase', '.']


# In[2]:


phrase + phrase


# In[3]:


phrase[-1:]


# In[4]:


phrase * 3


# In[5]:


phrase.sort()
phrase


# **Exercise 2)**

# In[6]:


import nltk
persuasion = nltk.corpus.gutenberg.words('austen-persuasion.txt')
len(persuasion)


# In[7]:


len(set(persuasion))


# **Exercise 3)**

# In[8]:


from nltk.corpus import brown
brown.words(categories=['religion', 'lore'])


# **Exercise 4)**

# In[9]:


from nltk.corpus import state_union
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ['men', 'women', 'people']
    if w.lower() == target)
cfd.plot()


# **Exercise 5)**

# In[10]:


from nltk.corpus import wordnet as wn
def relations(noun):
    noun_synset = wn.synset(noun)
    print 'Member Meronyms:\n '
    print noun_synset.member_meronyms()
    print '\nPart Meronyms:\n'
    print noun_synset.part_meronyms()
    print '\nSubstance Meronyms:\n'
    print noun_synset.substance_meronyms()
    print '\nMember Holonyms:\n'
    print noun_synset.member_holonyms()
    print '\nPart Holonyms:\n'
    print noun_synset.part_holonyms()
    print '\nSubstance Holonyms:\n'
    print noun_synset.substance_holonyms()
relations('tree.n.01')


# In[11]:


relations('honey.n.01')


# In[12]:


relations('wood.n.01')


# **Exercise 6)**

# Words could be spelled the same in two languages, but have different translations. With the means given so far: e.g. tag the words with the language ID.

# In[13]:


from nltk.corpus import swadesh
it2en = [(i + '-it', e) for (i, e) in swadesh.entries(['it', 'en'])]


# In[14]:


translate = dict(it2en)
translate['madre-it']


# In[15]:


de2en = [(d + '-de', e) for (d, e) in swadesh.entries(['de', 'en'])]
translate.update(dict(de2en))
translate['Hund-de']


# **Exercise 7)**

# In[16]:


emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance('however')


# In[17]:


from nltk.corpus import inaugural
last = inaugural.fileids()[-3]
print last
inaugural = nltk.Text(nltk.corpus.inaugural.words(last))
inaugural.concordance('however')


# **Exercise 8)**

# In[18]:


names = nltk.corpus.names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()


# In[19]:


len(names.words('female.txt'))


# In[20]:


len(names.words('male.txt'))


# **Exercise 9)**

# In[21]:


religion = brown.words(fileids='cd12')

## Vocabulary:
print len(set(religion))


# In[22]:


from nltk.corpus import webtext
movie = webtext.words(fileids='pirates.txt')
print len(set(movie))


# In[23]:


from __future__ import division

## Vocabulary richness:
print len(set(religion)) / len(religion)


# In[24]:


print len(set(movie)) / len(movie)


# In[25]:


movie_text = nltk.Text(movie)
religion_text = nltk.Text(religion)

## Word use:
movie_text.concordance('love')


# In[26]:


religion_text.concordance('love')


# In[27]:


movie_text.concordance('bear')


# In[28]:


religion_text.concordance('bear')


# **Exercise 10)**

# In[29]:


from __future__ import division

def third_of_tokens(text):
    words_in_text = [w for w in text if any(c.isalpha() for c in w)]

    fd = nltk.FreqDist(words_in_text)
    most = fd.most_common(1000)
    count = 0
    third_words = []

    for word, num in most:
        if ((count < (len(words_in_text) / 3)) & any(c.isalpha() for c in word)):
            count = count + num
            third_words.append(word)
    print third_words        
    print len(third_words)
    
third_of_tokens(movie)


# In[30]:


third_of_tokens(religion)


# In[31]:


third_of_tokens(emma)


# In[32]:


third_of_tokens(inaugural)


# **Exercise 11)**

# In[33]:


pronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'they']
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor', 'editorial', 'belles_lettres', 'government']
cfd.tabulate(conditions=genres, samples=pronouns)


# In[34]:


wh = ['what', 'when', 'who', 'why', 'where']
cfd.tabulate(conditions=genres, samples=wh)


# **Exercise 12)**

# In[35]:


count_distinct = 0
dublettes = []
prev = ''
for entry in nltk.corpus.cmudict.entries():
    if ((entry[0] == prev) and (entry[0] not in dublettes)):
        dublettes.append(entry[0])
    else: 
        count_distinct = count_distinct + 1
        prev = entry[0]
print count_distinct
print (len(dublettes) / count_distinct) * 100


# **Exercise 13)**

# In[36]:


all_syns = list(wn.all_synsets('n'))
no_hyponyms = [s for s in all_syns if len(s.hyponyms()) == 0]
print (len(no_hyponyms) / len(all_syns)) * 100


# **Exercise 14)**

# In[37]:


def supergloss(s):
    gloss = 'definition: ' + s.definition() + '\n\n'
    gloss = gloss + 'Hypernyms:\n'
    for hypernym in s.hypernyms():
        gloss = gloss + hypernym.name() + ': ' + hypernym.definition() + '\n'
    gloss = gloss + '\nHyponyms:\n'
    for hyponym in s.hyponyms():
        gloss = gloss + hyponym.name() + ': ' + hyponym.definition() + '\n'
    return gloss


# In[38]:


print supergloss(wn.synset('bicycle.n.01'))


# In[39]:


print supergloss(wn.synset('believe.v.01'))


# **Exercise 15)**

# In[40]:


fd = nltk.FreqDist(brown.words())


# In[41]:


triple_words = [w for w in fd.keys() if fd[w] > 2]
print len(brown.words())
print len(triple_words)


# **Exercise 16)**

# In[42]:


def lexical_diversity(text):
    return len(text) / len(set(text))
for genre in nltk.corpus.brown.categories():
    print genre + ': ' + str(lexical_diversity(brown.words(categories=genre)))


# **Exercise 17)**

# In[43]:


def most_frequent_content_words(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content_words = [w.lower() for w in text if w.lower() not in stopwords and any(c.isalpha() for c in w)]
    fd = nltk.FreqDist(content_words)
    return [w for w, num in fd.most_common(50)]
print most_frequent_content_words(emma)


# In[44]:


print most_frequent_content_words(movie)


# **Exercise 18)**

# In[45]:


def most_frequent_bigrams(text):
    stopwords = nltk.corpus.stopwords.words('english')
    bigrams = [b for b in nltk.bigrams(text) if b[0] not in stopwords and b[1] not in stopwords and any(c.isalpha() for c in b[0]) and any(c.isalpha() for c in b[1])]
    fd = nltk.FreqDist(bigrams)
    return [b for b, num in fd.most_common(50)]

print most_frequent_bigrams(emma)


# In[46]:


print most_frequent_bigrams(movie)


# **Exercise 19)**

# In[47]:


def table(words, genres):
    cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
    cfd.tabulate(conditions=genres, samples=words)
    
table(['perhaps', 'maybe', 'possibly', 'surely', 'certainly', 'absolutely'], ['news', 'religion', 'government', 'learned', 'fiction', 'romance', 'humor'])    


# **Exercise 20)**

# In[48]:


def word_freq(word, genre):
    fd = nltk.FreqDist(brown.words(categories=genre))
    return fd[word]

word_freq('God', 'religion')


# In[49]:


word_freq('God', 'government')


# **Exercise 21)**

# In[50]:


prondict = nltk.corpus.cmudict.dict()
    
def guess_syllables(text):
    count_syllables = 0;
    for word in text:
        if any(c.isalpha() for c in word):
            try:
                pron = prondict[word.lower()][0]
            except KeyError:
                print '"' + word.lower() + '" does not exist in CMU!'
                continue
            else:    
                for syllable in pron:
                    if any(c.isnumeric() for c in syllable):
                        count_syllables = count_syllables + 1;
    return count_syllables

guess_syllables(['She', 'sells', 'seashells', 'by', 'the', 'seashore'])


# In[51]:


guess_syllables(['This', 'is', 'an', 'absolutely', 'fantastic', 'pythonic', 'program', '.'])


# In[52]:


guess_syllables(religion_text)


# **Exercise 22)**

# In[53]:


def hedge(text):
    text_hedged = []
    count = 0
    for word in text:
        text_hedged.append(word)
        count = count + 1
        if count == 3:
            text_hedged.append('like')
            count = 0
    return text_hedged

hedge(['She', 'sells', 'seashells', 'by', 'the', 'seashore', 'the', 'shells', 'she', 'sells', 'are', 'seashells'])            


# **Exercise 23)**

# In[1]:


# a
import pylab
get_ipython().run_line_magic('pylab', 'inline')
def zipf(text):
    fd = nltk.FreqDist(text)
    rank = 1
    freqs = []
    ranks = []
    for sample, count in fd.most_common(200):
        if any(c.isalpha() for c in sample):
            freqs.append(fd.freq(sample))
            ranks.append(rank)
            rank = rank + 1
    pylab.plot(ranks, freqs)            


# In[55]:


zipf(emma)


# In[56]:


zipf(religion_text)


# In[3]:


# b
import random
import nltk
random_text = ''
count = 0
while count < 100001:
    random_text = random_text + random.choice('abcdefg ')
    count = count + 1
text_split = random_text.split()
zipf(random_text.split())


# **Exercise 24)**

# In[4]:


# a
def generate_model(text, num=15, n=50):
    words = [w for w, count in nltk.FreqDist(text).most_common(n)]
    bigrams = nltk.bigrams(text)
    cfd = nltk.ConditionalFreqDist(bigrams)
    word = random.choice(words)
    for i in range(num):
        print word,
        word = cfd[word].max()

generate_model(nltk.corpus.genesis.words('english-kjv.txt'))


# In[59]:


generate_model(emma)


# In[60]:


generate_model(movie)


# In[61]:


def generate_model_random(text, num=15, n=50):
    words = [w for w, count in nltk.FreqDist(text).most_common(n)]
    word = random.choice(words)
    for i in range(num):
        print word,
        word = random.choice(words)
generate_model_random(emma)        


# In[62]:


generate_model_random(movie, 25, 200)


# In[6]:


# b
from nltk.corpus import brown
generate_model(brown.words(categories='news'))


# In[64]:


generate_model_random(brown.words(categories='news'))


# In[7]:


# c
generate_model(brown.words(categories=['news', 'romance']))


# In[66]:


generate_model_random(brown.words(categories=['news', 'romance']))


# In[67]:


generate_model(brown.words(categories=['belles_lettres', 'science_fiction']))


# In[68]:


generate_model(brown.words(categories=['news', 'romance']), 100, 100)


# **Exercise 25)**

# In[70]:


from nltk.corpus import udhr
def find_language(word):
    languages = []
    for fileid in udhr.fileids():
        if fileid.endswith('-Latin1') and word in udhr.words(fileid):
            languages.append(fileid[:-7])
    return languages        
            
print find_language('and')    


# In[73]:


print find_language('in')


# **Exercise 26)**

# In[74]:


num_hyponyms = 0
sum_hyponyms = 0
for synset in wn.all_synsets('n'):
    hyponyms = synset.hyponyms()
    if len(hyponyms) > 0:
        num_hyponyms = num_hyponyms + 1
        sum_hyponyms = sum_hyponyms + len(hyponyms)
        
print sum_hyponyms / num_hyponyms        


# **Exercise 27)**

# In[82]:


def average_polysemy(category):
    seen_words = []
    num_poly = 0
    sum_poly = 0
    for synset in wn.all_synsets(category):
        if num_poly > 20000:
            break;
        for lemma in synset.lemmas():
            lemma_name = lemma.name()
            if lemma_name not in seen_words:
                seen_words.append(lemma_name)
                num_poly = num_poly + 1
                sum_poly = sum_poly + len(wn.synsets(lemma_name, category))
    return sum_poly / num_poly

average_polysemy('n')                


# In[83]:


average_polysemy('v')


# In[84]:


average_polysemy('a')


# In[88]:


average_polysemy('r')


# **Exercise 28)**

# In[92]:


pairs = [('car', 'automobile'), ('gem', 'jewel'), ('journey', 'voyage'), ('boy', 'lad'), ('coast', 'shore'), 
         ('asylum', 'madhouse'), ('magician', 'wizard'), ('midday', 'noon'), ('furnace', 'stove'), ('food', 'fruit'), 
         ('bird', 'cock'), ('bird', 'crane'), ('tool', 'implement'), ('brother', 'monk'), ('lad', 'brother'), 
         ('crane', 'implement'), ('journey', 'car'), ('monk', 'oracle'), ('cemetery', 'woodland'), ('food', 'rooster'), 
         ('coast', 'hill'), ('forest', 'graveyard'), ('shore', 'woodland'), ('monk', 'slave'), ('coast', 'forest'), 
         ('lad', 'wizard'), ('chord', 'smile'), ('glass', 'magician'), ('rooster', 'voyage'), ('noon', 'string')]
lch = []
for word1, word2 in pairs:
    lch.append((word1, word2, wn.lch_similarity(wn.synsets(word1)[0], wn.synsets(word2)[0])))
from operator import itemgetter
sorted(lch,key=itemgetter(2),reverse=True)


# In[93]:


path = []
for word1, word2 in pairs:
    path.append((word1, word2, wn.path_similarity(wn.synsets(word1)[0], wn.synsets(word2)[0])))
sorted(path,key=itemgetter(2),reverse=True)

