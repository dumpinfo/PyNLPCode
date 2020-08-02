#!/usr/bin/env python
# coding: utf-8

# __Exercise 1)__

# In[1]:


#EYE DROPS OFF SHELF
# Correct: Eye(Noun) Drops(Noun Plural) off(Preposition) shelf(Noun)
# Misinterpretation: Eye(Noun) Drops(Verb) off(Preporsition) shelf(Noun)


# __Exercise 2)__

# In[2]:


import nltk
from nltk.corpus import brown
brown_tagged = brown.tagged_words(tagset='universal')
# word: contest, guess: noun
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_tagged if word == 'contest')
print tag_fd.keys()
print tag_fd['VERB']
print tag_fd['NOUN']


# In[3]:


# word: play, guess: verb
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_tagged if word == 'play')
print tag_fd.keys()
print tag_fd['VERB']
print tag_fd['NOUN']


# __Exercise 3)__

# In[4]:


# (They, PRON) (wind, VERB) (back, ADP) (the, DET) (clock, NOUN)
# (while, CONJ) (we, PRON) (chase, VERB) (after, ADP) (the, DET) (wind, NOUN)
# => (wind, VERB) vs. (wind, NOUN)


# __Exercise 4)__

# In[5]:


# Pronunciation dictionary, maps from written form to phonetic transcriptions of possible pronunciations
# Syntax tree analyzer, maps from surface form of sentence to analyzed tree structure


# __Exercise 5)__

# In[6]:


d = {}
d['foo'] = 'bar'
d['baz'] = 123
d


# In[7]:


# d['xyz']


# __Exercise 6)__

# In[8]:


del d['foo']
d


# __Exercise 7)__

# In[9]:


d1 = {'foo': 123, 'bar': 456}
d2 = {1: 'some entry', 'foo': 'something new'}
d1.update(d2)
print d1
print d2


# In[10]:


# added entries from d2 to d1, updated entries in d1 if existing in d2
# useful e.g. for cases like default tagger fallback -> can create a default dict that can be updated with more sophisticated tagger


# __Exercise 8)__

# In[11]:


e = {'headword': 'piano', 'part-of-speech': 'NOUN', 'sense': 'a musical instrument with keys', 'example': 'She like to play pieces by Mozart on her piano.'}


# __Exercise 9)__

# In[12]:


from nltk.text import Text
Text(brown.words()).concordance('go')


# In[13]:


Text(brown.words()).concordance('went')


# In[14]:


# 'go' appears after 'to', 'would', 'will', 'may' where 'went' cannot appear
# both can appear after pronouns/nouns


# __Exercise 10)__

# In[15]:


brown_tagged_sents = brown.tagged_sents()
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(nltk.word_tokenize('Villa Park is an association football stadium in Aston, Birmingham, England, with a seating capacity of 42,682. Formerly a sports ground in a Victorian amusement park, it has been the home of Aston Villa Football Club since 17 April 1897.'))


# In[16]:


# cannot tag words that it has not seen during training


# __Exercise 11)__

# In[17]:


help(nltk.AffixTagger)


# In[18]:


affix_tagger = nltk.AffixTagger(brown_tagged_sents, affix_length=3, min_stem_length=1)
affix_tagger.tag(nltk.word_tokenize('The Road to Emmaus appearance is one of the early resurrection appearances of Jesus after his crucifixion and the discovery of the empty tomb. Both the Meeting on the road to Emmaus and the subsequent Supper at Emmaus, depicting the meal that Jesus had with two disciples after the encounter on the road, have been popular subjects in art.'))


# In[19]:


# does well on nouns with typical endings
affix_tagger = nltk.AffixTagger(brown_tagged_sents, affix_length=2, min_stem_length=0)
affix_tagger.tag(nltk.word_tokenize('The Road to Emmaus appearance is one of the early resurrection appearances of Jesus after his crucifixion and the discovery of the empty tomb. Both the Meeting on the road to Emmaus and the subsequent Supper at Emmaus, depicting the meal that Jesus had with two disciples after the encounter on the road, have been popular subjects in art.'))


# __Exercise 12)__

# In[20]:


bigram_tagger = nltk.BigramTagger(brown_tagged_sents)


# In[21]:


bigram_tagger.tag(brown.sents()[0])


# In[22]:


bigram_tagger.tag(nltk.word_tokenize('The Road to Emmaus appearance is one of the early resurrection appearances of Jesus after his crucifixion and the discovery of the empty tomb. Both the Meeting on the road to Emmaus and the subsequent Supper at Emmaus, depicting the meal that Jesus had with two disciples after the encounter on the road, have been popular subjects in art.'))


# In[23]:


# performs very badly on unseen data -> once it sees 'None' tag, cannot tag the rest because in training it hasn't seen bigrams with 'None'


# __Exercise 13)__

# In[24]:


date_dict = {'day': '22', 'month': 'April', 'month_num': '04', 'year': '2017'}
print '{day} of {month}, {year}.'.format(**date_dict)
print '{month_num}/{day}/{year}'.format(**date_dict)


# __Exercise 14)__

# In[25]:


tags = []
for sent in brown_tagged_sents:
    for (word, tag) in sent:
        tags.append(tag)
        
sorted(set(tags))


# In[26]:


# shorter with list comprehension:
sorted(set(tag for sent in brown_tagged_sents for (word, tag) in sent))


# __Exercis 15)__

# In[27]:


# a)
# solution only considers common singular nouns in base form, using only one category for shorter run time
brown_tagged_words = brown.tagged_words(categories='news')
relevant_pairs = [pair for pair in brown_tagged_words if pair[1] in ['NN', 'NNS']]
fdist = nltk.FreqDist(relevant_pairs)
seen_words = []
for pair in relevant_pairs:
    plural_pair = (pair[0] + 's', 'NNS')
    if pair[0] not in seen_words and pair[1] == 'NN' and plural_pair in relevant_pairs and fdist[pair] < fdist[plural_pair]:
        print pair[0], ': singular ', fdist[pair], ', plural ', fdist[plural_pair]
        seen_words.append(pair[0])


# In[28]:


# b)
from collections import Counter
tagged_set = set(brown_tagged_words)
data = Counter(word for (word, tag) in tagged_set)
word_most_tags = data.most_common(1)[0][0]
for (word, tag) in tagged_set:
    if word == word_most_tags:
        print tag
        print nltk.help.brown_tagset(tag)
        print '\n'


# In[29]:


# c)
tags = [tag for (word, tag) in brown_tagged_words]
fdist = nltk.FreqDist(tags)
for (tag, count) in fdist.most_common(20):
    print tag, ': ', count
    print nltk.help.brown_tagset(tag)
    print '\n'
# mostly open-class words: nouns, verbs    


# In[34]:


# d)
all_bigrams = list(nltk.bigrams(brown_tagged_words))
tags_before_nouns = [tag1 for ((word1, tag1), (word2, tag2)) in all_bigrams if tag2.startswith('N')]
fdist = nltk.FreqDist(tags_before_nouns)
for (tag, count) in fdist.most_common(20):
    print tag, ': ', count
    print nltk.help.brown_tagset(tag)
    print '\n'


# __Exercise 16)__

# In[ ]:




