#!/usr/bin/env python
# coding: utf-8

# **Exercise 1)**

# In[1]:


help(str)


# In[2]:


help(list)


# In[3]:


help(tuple)


# **Exercise 2)**

# In[4]:


# tuples + lists: slicing, concatination, indexing
# only lists: reverse, sort, pop
# only tuple: hash
hash((1,2))


# **Exercise 3)**

# In[5]:


myTuple = tuple([1])
print myTuple
type(myTuple)


# In[6]:


myTuple = (1,)
print myTuple
type(myTuple)


# **Exercise 4)**

# In[7]:


words = ['is', 'NLP', 'fun', '?']
tmp = words[0]
words[0] = words[1]
words[1] = tmp
words[3] = '!'
words


# In[8]:


words = ['is', 'NLP', 'fun', '?']
words[0], words[1], words[3] = words[1], words[0], '!'
words


# **Exercise 5)**

# In[9]:


help(cmp)


# In[10]:


cmp(3,9)


# In[11]:


cmp(9,3)


# In[12]:


# can differentiate 3 cases


# **Exercise 6)**

# In[13]:


sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
n = 3
[sent[i:i+n] for i in range(len(sent)-n+1)]


# In[14]:


sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
n = 1
[sent[i:i+n] for i in range(len(sent)-n+1)]


# In[15]:


sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
n = len(sent)
[sent[i:i+n] for i in range(len(sent)-n+1)]


# **Exercise 7)**

# In[16]:


if (0):
    print 'true!'


# In[17]:


if (1):
    print 'true!'


# In[18]:


if ('foo'):
    print 'true!'


# In[19]:


if (()):
    print 'true!'


# In[20]:


if ((1,2)):
    print 'true!'


# In[21]:


if (-1):
    print 'true!'


# **Exercise 8)**

# In[22]:


'Monty' < 'Python'


# In[23]:


'Z' < 'a'


# In[24]:


'z' < 'a'


# In[25]:


'Monty' < 'Montague'


# In[27]:


('Monty', 1) < ('Monty', 2)


# In[28]:


('Monty', 1) < ('Montague', 2)


# In[29]:


(1, 'Monty') < (2, 'Montague')


# **Exercise 9)**

# In[30]:


# a
myStr = '  some    whitespaced string  '
' '.join(myStr.split())


# In[31]:


# b
import re
re.sub(r'\s+', ' ', re.sub(r'^\s+|\s+$', '', myStr))


# **Exercise 10)**

# In[32]:


def sortWords(words):
    def cmp_len(word1, word2):
        return cmp(len(word1), len(word2))
    return sorted(words, cmp=cmp_len)

sortWords(['The', 'dog', 'gave', 'John', 'the', 'newspaper'])


# **Exercise 11)**

# In[33]:


sent1 = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
sent2 = sent1
sent1[1] = 'cat'
sent2


# In[34]:


# a
sent1 = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
sent2 = sent1[:]
sent1[1] = 'cat'
sent2
# [:] -> copy list items, instead of creating reference to same list


# In[35]:


# b
text1 = [['The', 'dog', 'gave', 'John', 'the', 'newspaper'], ['The', 'cat', 'miowed']]
text2 = text1[:]
text1[0][1] = 'monkey'
text2
# did not copy inner lists, but references to them


# In[36]:


# c
from copy import deepcopy
help(deepcopy)


# In[37]:


text1 = [['The', 'dog', 'gave', 'John', 'the', 'newspaper'], ['The', 'cat', 'miowed']]
text3 = deepcopy(text1)
text1[0][1] = 'monkey'
text3


# **Exercise 12)**

# In[38]:


word_table = [[''] * 3] * 4
word_table[1][2] = "hello"
word_table
# multiplication adds references to the same list, not copies of it


# In[39]:


word_table = [['' for count1 in range(3)] for count2 in range(4)]
word_table[1][2] = "hello"
word_table


# **Exercise 13)**

# In[40]:


word_vowels = [[]]
words = ['The', 'dog', 'gave', 'John', 'the', 'newspaper', 'The', 'cat', 'miowed']
for word in words:
    if (len(word) > len(word_vowels)-1):
        for index in range(len(word_vowels), len(word)+1):
            word_vowels.append([])
    num_vowels = len(re.findall(r'[aeiouAEIOU]', word))
    if (num_vowels > len(word_vowels[len(word)])-1):
        for index in range(len(word_vowels[len(word)]), num_vowels+1):
            word_vowels[len(word)].append(set())
    word_vowels[len(word)][num_vowels].add(word)
print word_vowels[3][1]
print word_vowels[9][3]


# **Exercise 14)**

# In[2]:


def novel10(text):
    splitIndex = len(text) / 10
    print [w for w in text[-splitIndex:] if w not in text[:-splitIndex]]
from nltk.book import *
novel10(text3)
    


# **Exercise 15)**

# In[42]:


import nltk
def countWords(sent):
    sent = sent.split()
    fdist = nltk.FreqDist(w.lower() for w in sent)
    for key in sorted(fdist.keys()):
        print '%s: %d' % (key, fdist[key])
countWords(' '.join(sent9))        


# **Exercise 16)**

# In[43]:


# a
def gematria(word):
    letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8, 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100, 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
    return sum(letter_vals[l] for l in word if len(re.findall(r'[a-z]', l)) > 0)
gematria('gematria')


# In[44]:


# b
for fileid in nltk.corpus.state_union.fileids():
    words666 = [w.lower() for w in nltk.corpus.state_union.words(fileid) if w.isalpha() and gematria(w.lower()) == 666]
    print '\n%s: %d' % (fileid, len(words666))
    print set(words666)


# In[45]:


# c
import random
def decode(text):
    num = random.randint(1, 1000)
    return num, set([w.lower() for w in text if w.isalpha() and gematria(w.lower()) == num])

result = decode(text4)
print result[0]
print result[1]


# **Exercise 17)**

# In[46]:


def shorten(text, n=20):
    most_freq = nltk.FreqDist(text).most_common(n)
    most_freq = [w for (w, num) in most_freq]
    print most_freq
    return [w for w in text if w not in most_freq]

print ' '.join(shorten(text3, 50)[:100])


# **Exercise 18)**

# In[47]:


def getWords(prop, value):
    lexicon = [('fish', 'water animal', 'fish'), ('house', 'building', 'haus'), ('whale', 'water animal', 'wejl')]
    if prop == 'meaning':
        return [w for (w, m, p) in lexicon if m == value]
    if prop == 'pronunciation':
        return [w for (w, m, p) in lexicon if p == value]
    
getWords('meaning', 'water animal')    


# In[48]:


getWords('pronunciation', 'haus')


# **Exercise 19)**

# In[49]:


from nltk.corpus import wordnet as wn
list_syns = [wn.synset('minke_whale.n.01'), wn.synset('orca.n.01'), wn.synset('novel.n.01'), wn.synset('tortoise.n.01')]
comp = wn.synset('right_whale.n.01')
sorted(list_syns, lambda x,y: cmp(comp.shortest_path_distance(x), comp.shortest_path_distance(y)))


# **Exercise 20)**

# In[55]:


def sortWords(wordList):
    fdist = nltk.FreqDist(wordList)
    return fdist.keys()
sortWords(['one', 'two', 'two', 'four', 'four', 'four', 'four', 'three', 'three', 'three'])


# **Exercise 21)**

# In[59]:


def unknownWords(text, vocab):
    return set(text).difference(set(vocab))
unknownWords(text3, nltk.corpus.words.words())


# **Exercise 22)**

# In[62]:


from operator import itemgetter
print sent3[:-1]
print sorted(sent3[:-1], key=itemgetter(1))
print sorted(sent3[:-1], key=itemgetter(-1))


# In[63]:


help(itemgetter)


# In[64]:


i = itemgetter(0)
print i('hallo')
print i(['hallo', 'welt'])


# **Exercise 23)**

# In[3]:


import nltk
def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value
        
trie = nltk.defaultdict(dict)
insert(trie, 'chat', 'cat')
insert(trie, 'chien', 'dog')
insert(trie, 'chair', 'flesh')
trie['c']['h']['a']['t']['value']


# In[4]:


import pprint
def lookup(trie, key):
    if len(key) == 0:
        if 'value' in trie:
            result = trie['value']
            return result
        elif (len(trie) == 1):
            keys = trie.keys()
            return lookup(trie[keys[0]], '')
        else:
            return 'no value found'
    else:
        if (key[0] in trie):
            return lookup(trie[key[0]], key[1:])
        else:
            return 'no value found'

print lookup(trie, 'ch')      


# **Exercise 24)**

# In[1]:


# TODO


# **Exercise 25)**

# In[2]:


help(nltk.edit_distance)


# In[7]:


nltk.edit_distance('kitten', 'sitting', True)


# **Exercise 26)**

# In[18]:


# a
def catalan_recursive(n):
    if (n == 0):
        return 1
    i = 0
    result = 0
    original_n = n
    while i < original_n:
        result += catalan_recursive(i) * catalan_recursive(n-1)
        n -= 1
        i += 1
    return result

catalan_recursive(6)


# In[15]:


# b
def catalan_dynamic(n, lookup={0:1}):
    result = 0
    if n == 0:
        return 1
    for i in range(n):
        if i not in lookup:
            lookup[i] = catalan_dynamic(i, lookup)
        if n-1 not in lookup:
            lookup[n-1] = catalan_dynamic(n-1, lookup)
        result += lookup[i] * lookup[n-1]    
        n -= 1
    return result

catalan_dynamic(6)


# In[35]:


# c
from timeit import Timer
t = Timer(lambda: catalan_recursive(10))
print t.timeit(number=10)
t = Timer(lambda: catalan_dynamic(10))
print t.timeit(number=10)


# **Exercise 27)**

# In[2]:


# TODO


# **Exercise 28)**

# In[3]:


# TODO


# **Exercise 29)**

# In[5]:


import nltk
trie = nltk.defaultdict(dict)
insert(trie, 'chat', 'cat')
insert(trie, 'chien', 'dog')
insert(trie, 'chair', 'flesh')
insert(trie, 'chic', 'stylish')
trie['c']['h']['a']['t']['value']


# In[6]:


def pprint_trie(trie, line=''):
    if 'value' in trie:
        print line + ': \'' + trie['value'] + '\''
        return
    for index, key in enumerate(sorted(trie.keys())):
        if (index == 0):
            pprint_trie(trie[key], line + key)
        else:
            pprint_trie(trie[key], ('-' * len(line)) + key)

pprint_trie(trie)


# **Exercise 30)**

# In[15]:


def lookup_unique(key, trie, unique='', buffer_unique=''):
    if len(key) == 0:
        if len(buffer_unique) > 0:
            return buffer_unique
        else:  
            return unique
    if len(trie[key[0]]) == 1:
        if len(buffer_unique) > 0:
            new_buffer_unique = buffer_unique
        else:
            new_buffer_unique = unique + key[0]
        return lookup_unique(key[1:], trie[key[0]], unique + key[0], new_buffer_unique)
    return lookup_unique(key[1:], trie[key[0]], unique + key[0])
        

def compress(text):          
    trie = nltk.defaultdict(dict)
    for word in text:
        insert(trie, word, word)
    return [lookup_unique(w, trie) for w in text]

compressed = compress(text1)
from __future__ import division
print (100.0/len(''.join(text1))) * len(''.join(compressed))
print ' '.join(compressed[:200])


# In[16]:


compressed = compress(sent3)
print (100.0/len(''.join(sent3))) * len(''.join(compressed))
print ' '.join(compressed)


# **Exercise 31)**

# In[1]:


def load(fileName):
    f = open(fileName + '.txt')
    return f.read()
raw = load('corpus')
import textwrap
wrapped = textwrap.wrap(raw)
print wrapped[:10]


# In[23]:


def justify(wrapped_text):
    line_length = max(len(line) for line in wrapped_text)
    for line in wrapped_text:
        words = line.split()
        num_chars = sum(len(word) for word in words)
        num_spaces = line_length - num_chars
        num_slots = len(words) - 1
        fixed_spaces = int(num_spaces / num_slots)
        spaces = 0
        for index, word in enumerate(words[:-1]):
            word += ' ' * fixed_spaces
            spaces += fixed_spaces
            words[index] = word
            
        while num_spaces - spaces > 0:
            remainder = (num_spaces - spaces) % num_slots
            chunk_size = int(len(words) / (remainder + 1))
            chunk = 0
            for index, word in enumerate(words[:-1]):
                if remainder and chunk == chunk_size:
                    word += ' '
                    spaces += 1
                    chunk = 0
                else:    
                    chunk += 1
                words[index] = word
            
        print ''.join(words)
        
justify(wrapped[:30])


# **Exercise 32)**

# In[7]:


import nltk
def summarize(text_sents, n):
    from operator import itemgetter
    freqDist = nltk.FreqDist([w.lower() for sent in text_sents for w in sent])
    scoresSents = [(sum(freqDist[word] for word in sent), index, sent) for (index, sent) in enumerate(text_sents)]
    sortByFreq = sorted(scoresSents, key=itemgetter(0), reverse=True)[:n]
    sortByIndex = sorted(sortByFreq, key=itemgetter(1))
    for (freq, index, sent) in sortByIndex:
        print index, ': ', sent, '\n'
    
from nltk.corpus import brown
summarize(brown.sents(categories='religion'), 10)


# **Exercise 33)**

# In[8]:


# TODO


# **Exercise 34)**

# In[9]:


# TODO


# **Exercise 35)**

# In[10]:


# TODO


# **Exercise 36)**

# In[30]:


def word_square(n):
    # works only if n < 5, with 5 exceeds maximum recursion callstack
    # TODO: Do this iteratively to avoid the callstack issue?
    from nltk.corpus import words
    myWords = [word.upper() for word in filter(lambda w: len(w) == n, words.words())] # get all words of length n
    
    square = []
    skipWords = [[] for i in range(n)] # cache for words that have already been tested at position i
    
    def check_against_square(word): # checks if current state of square would allow to add word to it
        if word in square:
            return False
        for (index, square_word) in enumerate(square):
            if (word[index] != square_word[len(square)]):
                return False
        return True
    
    def add_word(): # recursively adds / removes words from square until solution is found
        if len(square) == n:
            return True
        for word in myWords:
            if len(square) == n:
                return True
            if (word not in skipWords[len(square)]) and check_against_square(word): # add the word to square if it hasn't been tested unsuccessfully already and if it fits 
                square.append(word)
                add_word()
        if len(square) != n and len(square) != 0:   
            skipWords[len(square) - 1].append(square.pop()) # add word to cache
            for i in range(len(square) + 1, n): # reset the following parts of the cache
                skipWords[i] = []
            add_word()
        return False
            
        
    if add_word():
        for word in square:
            print word
    else:
        print 'No square found :/'
            
word_square(4)    


# In[31]:


word_square(3)

