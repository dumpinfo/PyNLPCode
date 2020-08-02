#!/usr/bin/env python
# coding: utf-8

# **Exercise 1)**

# In[1]:


s = 'colorless'
s = s[:4] + 'u' + s[4:]
s


# **Exercise 2)**

# In[2]:


'dishes'[:-2]


# In[3]:


'running'[:-4]


# In[4]:


'nationality'[:-5]


# In[5]:


'undo'[2:]


# In[6]:


'preheat'[3:]


# **Exercise 3)**

# In[1]:


'in'[-5]


# **Exercise 4)**

# In[8]:


monty = 'Monty Python'
monty[6:11:2]


# In[9]:


monty[10:5:-2]


# In[10]:


monty[1:10:-2]


# In[2]:


monty[1:6:1.5]


# **Exercise 5)**

# In[12]:


monty[::-1]


# **Exercise 6)**

# In[13]:


from __future__ import division
import nltk, re, pprint


# In[14]:


# a - one or more letters
nltk.re_show(r'[a-zA-Z]+', monty)


# In[15]:


# b - one capital letter and zero or more lowercase letters
nltk.re_show(r'[A-Z][a-z]*', monty)
nltk.re_show(r'[A-Z][a-z]*', 'A very Intersting3 example')


# In[16]:


# c - a word starting with p, followed by 0 up to 2 vowels and ending with p
nltk.re_show(r'p[aeiou]{,2}t', 'two pouting party pets - pt')


# In[17]:


# d - integer or decimal number
nltk.re_show(r'\d+(\.\d+)?', 'This should match 23 as well as 1.093 and 999.9')


# In[18]:


# e - zero or more sequences of not-a-vowel - vowel - not-a-vowel
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', 'This should match pet as well as cut and lol')


# In[19]:


# f - one or more alphanumeric characters or one or more charcters that are neither alpahnumeric nor whitespace
nltk.re_show(r'\w+|[^\w\s]+', 'should match me but not \n')


# **Exercise 7)**

# In[20]:


a = r'^(the|a|an)$'
nltk.re_show(a, 'the something')
nltk.re_show(a, 'the')
nltk.re_show(a, 'an')
nltk.re_show(a, 'anything')


# In[21]:


b = r'\d+([\+\*]\d+)+'
nltk.re_show(b, 'something+2')
nltk.re_show(b, '2*3+8')
nltk.re_show(b, '200+5000')
nltk.re_show(b, '2*3+8-5/6')


# **Exercise 8)**

# In[22]:


from bs4 import BeautifulSoup
import urllib

def getContentFromURL(url):
    raw = urllib.urlopen(url).read()
    soup = BeautifulSoup(raw)
    return soup.get_text()

getContentFromURL('http://www.nltk.org/')


# **Exercise 9)**

# In[23]:


def load(fileName):
    f = open(fileName + '.txt')
    return f.read()
corpusText = load('corpus')


# In[24]:


# a
pattern = r'''(?x)
    [\.,;"'?\(\):\-_`\[\]\{\}]+ # one or more punctuation symbols, brackets etc.
'''
print nltk.regexp_tokenize(corpusText, pattern)


# In[25]:


# b
pattern = r'''(?x)
    (?:\d+\.)?\d+\s?\$                  # Monetary amount like 2.40$
    | \$\s?(?:\d+\.)?\d+                # Monetary amount like $2.40
    | \d{4}\-\d{2}\-\d{2}               # Date like 2016-22-01
    | \d{1,2}\s[A-Z][a-z]{2,8}\s\d{4}   # Date like 2 March 1998
    | [A-Z][a-z]+(?:\s[A-Z][a-z]+)?     # Proper Names - TODO: don't match beginning of sentence
'''
testString = 'should match 3.50$ or 8 $ or 9$ or $2.40 or 2016-11-01 or 2 March 1998 or 19 January 2001 or Sam or United Nations'
print nltk.regexp_tokenize(testString, pattern)


# In[26]:


print nltk.regexp_tokenize(corpusText, pattern)


# **Exercise 10)**

# In[27]:


sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
print [(w, len(w)) for w in sent]


# **Exercise 11)**

# In[28]:


raw = 'Tres tristes tigres comen trigo en un trigal.'
raw.split('t')


# **Exercise 12)**

# In[29]:


for char in raw[:10]:
    print char


# **Exercise 13)**

# In[30]:


raw.split()


# In[31]:


raw.split(' ')


# In[32]:


sent = 'Tres\ttristes\ttigres\tcomen\ttrigo\ten\tun\ttrigal.'
sent.split()


# In[33]:


sent.split(' ')


# In[34]:


sent = 'Tres   tristes   tigres   comen   trigo   en   un   trigal.'
sent.split()


# In[35]:


sent.split(' ')


# In[36]:


sent = 'Tres \ttristes\t\t\ttigres\t\t comen\t \t trigo en un trigal.'
sent.split()


# In[37]:


sent.split(' ')


# **Exercise 14)**

# In[38]:


words = raw.split()
print words
words.sort()
print words


# In[39]:


words = raw.split()
sorted(words)


# In[40]:


words


# In[4]:


# .sort() changes original list, sorted() returns new list


# **Exercise 15)**

# In[42]:


'3' * 7


# In[43]:


3 * 7


# In[44]:


int('3') * 7


# In[45]:


str(3) * 7


# **Exercise 16)**

# In[5]:


montyTest


# In[47]:


from test import montyTest
montyTest


# In[48]:


import test
test.montyTest


# **Exercise 17)**

# In[49]:


words = ['some', 'superexcitingly', 'long', 'example', 'words']
for w in words:
    print '%6s' % w,


# In[50]:


for w in words:
    print '%-6s' % w,


# In[51]:


for w in words:
    print '%6s' % w


# **Exercise 18)**

# In[52]:


myCorpus = load('corpus')
tokens = nltk.wordpunct_tokenize(myCorpus)


# In[53]:


whWords = [w for w in tokens if w.startswith('wh') or w.startswith('Wh')]
print whWords[:50]


# In[54]:


print sorted(set(whWords))


# **Exercise 19)**

# In[55]:


freqs = open('freqs.txt').readlines()
freqs


# In[56]:


splitted = [[line.split()[0], int(line.split()[1])] for line in freqs]
splitted


# **Exercise 20)**

# In[57]:


# extracts the topic of the article of the day of given Wikipedia Homepage
def find_topic(url, trigger):
    text = urllib.urlopen(url).read()
    index = text.rfind(trigger)
    text = text[index:]
    title_with_markup = re.findall(r'\<b\>.+?\<\/b\>', text)[0]
    soup = BeautifulSoup(title_with_markup)
    return soup.get_text()

# German Wikipedia:
print find_topic('https://de.wikipedia.org/wiki/Wikipedia:Hauptseite', '<span class="mw-headline" id="Artikel_des_Tages">Artikel des Tages</span>')

# English Wikipedia:
print find_topic('https://en.wikipedia.org/wiki/Main_Page', '<span class="mw-headline" id="From_today.27s_featured_article">From today\'s featured article</span>')

# Danish Wikipedia:
print find_topic('https://da.wikipedia.org/wiki/Forside', '<div style="padding-left: 38px; color:#333;">Ugens artikel</div>')


# **Exercise 21)**

# In[76]:


def unknown(url):
    content = getContentFromURL(url)
    lowercased = re.findall(r'[\s\(\[\{]([a-z]+)', content)
    words = nltk.corpus.words.words()
    return [w for w in lowercased if w not in words]
print unknown('https://en.wikipedia.org/wiki/Main_Page')


# In[59]:


# derived forms, abbreviations, foreign words


# **Exercise 22)**

# In[75]:


print unknown('http://news.bbc.co.uk/')


# In[74]:


def unknown(url):
    text = urllib.urlopen(url).read()
    text = re.sub(r'\<script(?:.|\n)*?\<\/script\>', '', text)
    text = re.sub(r'\<style(?:.|\n)*?\<\/style\>', '', text)
    soup = BeautifulSoup(text)
    content = soup.get_text()
    lowercased = re.findall(r'[\s\(\[\{]([a-z]+)', content)
    words = nltk.corpus.words.words()
    return set([w for w in lowercased if w not in words])

print unknown('http://www.bbc.com/news')


# **Exercise 23)**

# In[62]:


sample_text = "I don't hate regular expressions."
nltk.regexp_tokenize(sample_text, r'n\'t|\w+')


# In[63]:


# doesn't work because of greediness of operators -> don matches \w+
print nltk.regexp_tokenize(sample_text, r'\w+(?=n\'t)|n\'t|\w+')
print nltk.regexp_tokenize('It doesn\'t split donald.', r'\w+(?=n\'t)|n\'t|\w+') # ?= lookahead assertion


# **Exercise 24)**

# In[64]:


def encode(text):
    text = text.lower();
    trans = [('ate', '8'), ('e', '3'), ('i', '1'), ('o', '0'), ('l', '|'), ('s', '5'), ('\.', '5w33t!')]
    for (key, value) in trans:
        text = re.sub(key, value, text)
    return text

print encode('Hello World!')
print encode('It is getting late.')


# In[65]:


def encode_enhanced(text):
    text = text.lower();
    trans = [('ate', '8'), ('e', '3'), ('i', '1'), ('o', '0'), ('l', '|'), ('^s|(?<=\s)s', '$'), ('s', '5'), ('\.', '5w33t!')]
    #?<= lookbehind assertion
    for (key, value) in trans:
        text = re.sub(key, value, text)
    return text
encode_enhanced('Should treat sea different from ass.')


# **Exercise 25)**

# In[66]:


# a
def piginizeWord(word):
    cons = re.findall(r'^[^aeiouAEIOU]*', word)
    return word[len(cons[0]):] + cons[0] + 'ay'
    
piginizeWord('string')    


# In[67]:


# b
def piginizeText(text):
    def helper(matchObj):
        return piginizeWord(matchObj.group(0))
    return re.sub(r'[A-Za-z]+', helper, text)
piginizeText('Some quiet string here that should be converted to Pig Latin at once.')


# In[68]:


# c
def piginizeWordImproved(word):
    cons = re.findall(r'^[^aeiouAEIOU]+(?=y)|^[^aeiouqAEIOUQ]*(?:qu)?(?:Qu)?[^aeiouqAEIOUQ]*', word)[0]
    remainder = word[len(cons):]
    if (word.istitle()):
        return remainder.title() + cons.lower() + 'ay'
    return remainder + cons + 'ay'

def piginizeText(text):
    def helper(matchObj):
        return piginizeWordImproved(matchObj.group(0))
    return re.sub(r'[A-Za-z]+', helper, text)
piginizeText('My quiet yellow stylish string that should be converted to Pig Latin at once.')


# **Exercise 26)**

# In[69]:


text = urllib.urlopen('https://tr.wikipedia.org/wiki/%C4%B0stanbul').read()
text = re.sub(r'\<script(?:.|\n)*?\<\/script\>', '', text)
text = re.sub(r'\<style(?:.|\n)*?\<\/style\>', '', text)
soup = BeautifulSoup(text)
content = soup.get_text()
tokens = nltk.wordpunct_tokenize(content)
text = nltk.Text(tokens)
words = [w.lower() for w in text]


# In[70]:


vowel_sequences = []
for word in words:
    vowels = ''.join(re.findall(r'[aeiou]', word))
    if (len(vowels) > 0):
        vowel_sequences.append(vowels)
print vowel_sequences[:50]    


# In[71]:


bigrams = []
for vowel_seq in vowel_sequences:
    count = 0
    while (count + 1 < len(vowel_seq)):
        bigrams.append((vowel_seq[count], vowel_seq[count + 1]))
        count += 1
print bigrams[:50]                       


# In[72]:


vowels = ['a', 'e', 'i', 'o', 'u']
cfd = nltk.ConditionalFreqDist(bigrams)
cfd.conditions()


# In[73]:


cfd.tabulate(conditions=vowels,samples=vowels)


# **Exercise 27)**

# In[81]:


import random
def laugh():
    raw = ''.join(random.choice('aehh ') for x in range(500))
    return ' '.join(raw.split())
laugh()


# **Exercise 28)**

# In[82]:


# three words -> woulld be compatible with splitting on whitespace
# one compound word -> would make sense semantically, may be relevant for natural language understanding applications
# nine words -> would make sense phonetically, relevant for speech processing applications


# **Exercise 29)**

# In[83]:


def ari(category):
    words = nltk.corpus.brown.words(categories=category)
    sents = nltk.corpus.brown.sents(categories=category)
    av_wordlength = sum(len(w) for w in words) / len(words)
    av_sentlength = sum(len(s) for s in sents) / len(sents)
    return (4.71 * av_wordlength) + (0.5 * av_sentlength) - 21.43
print ari('lore')
print ari('learned')
print ari('government')
print ari('romance')


# **Exercise 30)**

# In[85]:


porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
text = 'New rules allowing Sikh police officers to wear turbans instead of traditional police hats have been introduced in New York, officials say. The New York Police Department said the turbans must be navy blue and have the NYPD insignia attached. Under the new rules, religious members of the force are also permitted to grow beards up to half-an-inch long. Sikh officers have until now worn turbans under their caps. Beards have not been permitted.'
tokens = nltk.wordpunct_tokenize(text)
print [porter.stem(t) for t in tokens]
print '\n\n'
print [lancaster.stem(t) for t in tokens]


# In[86]:


# Porter preserves upper case, uses unicode, seems to tend to longer stems


# **Exercise 31)**

# In[88]:


saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
lengths = []
for w in saying:
    lengths.append(len(w))
lengths    


# **Exercise 32)**

# In[89]:


silly = 'newly formed bland ideas are inexpressible in an infuriating way'
# a
bland = silly.split()
print bland


# In[91]:


# b
''.join(w[1] for w in bland)


# In[92]:


# c
' '.join(bland)


# In[96]:


# d
for w in sorted(bland):
    print w


# **Exercise 33)**

# In[97]:


# a
'inexpressible'.index('re')


# In[98]:


# b
words = ['this', 'is', 'a', 'dull', 'list', 'of', 'words']
words.index('dull')


# In[99]:


# c
bland[:bland.index('in')]


# **Exercise 34)**

# In[106]:


def convertNationality(adjective):
    if (adjective.endswith('dian') or adjective.endswith('ese')):
        return adjective[:-3] + 'a'
    elif (adjective.endswith('ian')):
        return adjective[:-1]
        
print convertNationality('Canadian')   
print convertNationality('Australian')
print convertNationality('Chinese')


# **Exercise 35)**

# In[123]:


pronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'they']
corpus = ' '.join(nltk.corpus.webtext.words())
sample1 = re.findall(r'[aA]s best as (?:I|you|he|she|it|we|they) can', corpus)
print sample1[:10]
print len(sample1)
sample2 = re.findall(r'[aA]s best (?:I|you|he|she|it|we|they) can', corpus)
print sample2[:10]
print len(sample2)


# **Exercise 36)**

# In[126]:


print ' '.join(nltk.corpus.genesis.words('lolcat.txt')[:500])


# In[137]:


def lolcat(word):
    word = re.sub(r'ight', 'iet', word)
    word = re.sub(r'^I$', 'ai', word)
    word = re.sub(r'(?<=[^aeiouAEIOU])i$', 'ai', word)
    word = re.sub(r'le$', 'el', word)
    def helper(matchObj):
        return 'e' + matchObj.group(1)
    word = re.sub(r'([^aeiouAEIOU])e$', helper, word)
    word = re.sub(r'(?<=[^aeiouAEIOU])er$', 'ah', word)
    word = re.sub(r'ou', 'ow', word)
    word = re.sub(r'Ou', 'Ow', word)
    word = re.sub(r'(?<=[^aeiouAEIOU])y$', 'eh', word)
    word = re.sub(r'th', 'f', word)
    word = re.sub(r'Th', 'F', word)
    word = re.sub(r'ing$', 'in', word)
    return word    
print lolcat('I')
print lolcat('hi')
print lolcat('right')
print lolcat('kite')
print lolcat('like')
print lolcat('over')
print lolcat('loud')
print lolcat('kitty')
print lolcat('three')
print lolcat('nothing')
print lolcat('little')


# **Exercise 37)**

# In[138]:


help(re.sub)


# In[140]:


def clean(html):
    # remove html tags:
    text = re.sub(r'\<.*?\>', '', html)
    # normalize whitespace:
    text = re.sub(r'\s+', ' ', text)
    return text
clean('<span class="some class">A span    which  should<br> be cleaned</span>')


# **Exercise 38)**

# In[142]:


# a
text = 'some text with long-\nterm and encyclo-\npedia'
words = re.findall(r'\w+\-\n\w+', text)
words


# In[143]:


# b
for w in words:
    print re.sub('\n', '', w)


# In[145]:


# c
for w in words:
    word = re.sub('\n', '', w)
    parts = word.lower().split('-')
    if (parts[0] not in nltk.corpus.words.words() and parts[1] not in nltk.corpus.words.words()):
        print re.sub('\-', '', word)
    else:
        print word


# **Exercise 39)**

# In[148]:


def soundex(name):
    first = name[0]
    # remove w & h
    encoded = first.lower() + re.sub('[wh]', '', name[1:].lower())
    # replace consonants with numbers
    encoded = re.sub(r'[bfpv]', '1', encoded)
    encoded = re.sub(r'[cgjkqsxz]', '2', encoded)
    encoded = re.sub(r'[dt]', '3', encoded)
    encoded = re.sub(r'l', '4', encoded)
    encoded = re.sub(r'[mn]', '5', encoded)
    encoded = re.sub(r'r', '6', encoded)
    # merge adjacent same digits into one
    count = 1
    while count < 7:
        encoded = re.sub(str(count) + '{2,}', str(count), encoded)
        count += 1
    # remove vowels
    encoded = encoded[0].upper() + re.sub('[aeiouy]', '', encoded[1:])
    # if first character is digit, replace it with the saved letter
    if (encoded[0].isdigit()):
        encoded = first.upper() + encoded[1:]
    # encoded must contain 3 digits -> fill it up with zeros if too short    
    if (len(encoded) < 4):
        encoded += '000'
    return encoded[:4]    
    
print soundex('Robert') #R163
print soundex('Rupert') #R163
print soundex('Rubin') #R150
print soundex('Ashcraft') #A261
print soundex('Ashcroft') #A261
print soundex('Tymczak') #T522 
print soundex('Pfister') #P236   


# **Exercise 40)**

# In[150]:


def ari(raw):
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(raw)
    words = nltk.word_tokenize(raw)
    av_wordlength = sum(len(w) for w in words) / len(words)
    av_sentlength = sum(len(s) for s in sents) / len(sents)
    return (4.71 * av_wordlength) + (0.5 * av_sentlength) - 21.43
print ari(nltk.corpus.abc.raw("rural.txt"))
print ari(nltk.corpus.abc.raw("science.txt"))


# **Exercise 41)**

# In[152]:


words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
# more elegant with regular expression instead of nested list comprehension:
vsequences = set([''.join(re.findall(r'[aeiou]', word)) for word in words])
sorted(vsequences)


# In[153]:


# nested list comprehension:
vsequences = set([''.join([char for char in word if char in 'aeiou']) for word in words])
sorted(vsequences)


# **Exercise 42)**

# In[163]:


from nltk.corpus import wordnet as wn
class IndexedText(object):
    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
            for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/4) # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            offset = '(WordNet Offset: ' + str(wn.synsets(self._text[i])[0].offset()) + ')'
            ldisplay = '%*s' % (width, lcontext[-width:])
            rdisplay = '%-*s' % (width, rcontext[:width])
            print ldisplay, rdisplay, offset
                
    def _stem(self, word):
        return self._stemmer.stem(word).lower()

porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('grail.txt')
text = IndexedText(porter, grail)
text.concordance('lie')


# **Exercise 43)**

# In[181]:


def guessLanguage(text):
    tokens = nltk.wordpunct_tokenize(text)
    text = nltk.Text(tokens)
    fdist_text = nltk.FreqDist(text)
    best_guess = ('', 0)
    best_intersection = []
    for lang in nltk.corpus.udhr.fileids():
        if (lang.endswith('-Latin1')):
            fdist_lang = nltk.FreqDist(nltk.corpus.udhr.words(lang))
            intersection = list(set(fdist_text.keys()) & set(fdist_lang.keys()))
            dict_text = []
            dict_lang = []
            for word in intersection:
                dict_text.append((word, fdist_text[word]))
                dict_lang.append((word, fdist_lang[word]))
            spearman = nltk.spearman_correlation(dict_text, dict_lang)
            if ((best_guess[1] == 0 and spearman != 0.0) or (spearman != 0.0 and spearman > best_guess[1])):
                best_guess = (lang[:-7], spearman)
    return best_guess[0];

help(nltk.spearman_correlation)
print guessLanguage('This is clearly an example of English text which should not be hard to recognize.')
print guessLanguage(u'Carapax (von gr. charax „Befestigungsanlage“, „Palisade“ und pagios „fest“; Plural: Carapaces) ist eine Bezeichnung für eine bei verschiedenen Tiergruppen (Taxa) unabhängig voneinander entstandene harte Bedeckung der Körperoberseite. Bei Schildkröten heißt der Carapax gemeinsprachlich Rückenschild oder Rückenpanzer, bei Krustentieren (Krebstieren in der Küche) ist er ein Teil der „Schale“. Viele Krebstiere (Crustacea) besitzen eine Hautfalte, die vom Kopfhinterrand (Segment der 2. Maxille) ausgeht; diese kann auch primär (z. B. Cephalocarida) oder sekundär (z. B. Asseln und Flohkrebse) fehlen, gehört also nicht zum Grundbauplan der Krebstiere. Vielfach ist die chitinöse Kopffalte durch eingelagerten Kalk panzerartig versteift, vor allem bei vielen Zehnfußkrebsen. Bedeckt diese Struktur als Rückenschild einige oder ggf. alle Rumpfsegmente, wird sie Carapax genannt. Der Carapax schließt also an den Kopf an, setzt sich über dessen Hinterrand hinaus fort und erstreckt sich mehr oder weniger weit über den Rumpf des Krebses. Je nach Ausbildung kann er auch den Kopf selbst umhüllen (z. B. bei den Muschelkrebsen) und mehr oder weniger weit auch seitlich herabgezogen sein.  – Zum Artikel …')


# In[182]:


print guessLanguage(u'Dødsstraf eller livsstraf er henrettelse som straf for en forbrydelse. I de jurisdiktioner, der praktiserer dødsstraf, er den som regel forbeholdt et lille antal alvorlige forbrydelser, ofte overlagt mord og landsforræderi. I Kina praktiseres tillige dødsstraf for økonomisk kriminalitet og narkokriminalitet, og i Iran for homoseksualitet, ligesom der i visse områder kontrolleret af islamiske oprørsbevægelser gennemføres henrettelser baseret på en streng fortolkning af sharia. Mange lande har dødsstraf i den militære straffelov eller for forbrydelser begået i krigstid. I Danmark blev dødsstraf første gang afskaffet i den borgerlige straffelov den 15. april 1930. Loven trådte i kraft 15. april 1933. Dødsstraf blev på dette tidspunkt beholdt i den militære straffelov. I forbindelse med retsopgøret efter 2. verdenskrig genindførtes dødsstraffen (som kaldtes livsstraf) i 1945 for forbrydelser begået under besættelsen. Loven var en særlov og kendes som Landsforræderloven eller retteligen Straffelovstillægget og havde tilbagevirkende kraft for handlinger begået efter 9. april 1940. 46 personer blev på den baggrund henrettet af frivillige politifolk. Den 20. juli 1950 kl. 01:00 blev Ib Birkedal Hansen henrettet som den sidste i Danmark. (Læs mere..)')


# **Exercise 44)**

# In[189]:


def novel_sense(word, text):
    content_words = []
    stopwords = nltk.corpus.stopwords.words('english')
    count = 0
    for w in text:
        if (w.isalpha() and w not in stopwords):
            content_words.append((w, count))
        count += 1    
    count = 0
    oddest = False
    for w in content_words:
        if (w[0] == word):
            count_comparisons = 0
            overall_sim = 0
            for synset in wn.synsets(w[0]):
                # compare to words in context on left side:
                for index in range(1, min(21, count+1)):
                    context_word = content_words[count - index][0]
                    for context_synset in wn.synsets(context_word):
                        path_sim = synset.path_similarity(context_synset)
                        if (path_sim != None):
                            overall_sim += path_sim 
                            count_comparisons += 1
                # compare to words in context on right side:            
                for index in range(1, min(21, len(content_words)-count-1)):
                        context_word = content_words[count + index][0]
                        for context_synset in wn.synsets(context_word):
                            path_sim = synset.path_similarity(context_synset)
                            if (path_sim != None):
                                overall_sim += path_sim 
                                count_comparisons += 1            
            av_sim = overall_sim / count_comparisons
            if (oddest == False or oddest[1] > av_sim):
                oddest = (w[1], av_sim) # w[1] = original index of the word in the text
        count += 1
    if (oddest != False):    
        print text[max(0, oddest[0] - 50):min(oddest[0] + 50, len(text))]
        print 'Average Similarity: ', str(oddest[1])

novel_sense('love', nltk.corpus.gutenberg.words('austen-emma.txt'))

