#!/usr/bin/env python
# coding: utf-8

# <h1>Tweets sentiment classification</h1>

# In[45]:


import random
import nltk
from nltk.corpus import twitter_samples
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# In[46]:


pos_tweets = [(string, 1) for string in twitter_samples.strings('positive_tweets.json')]
neg_tweets = [(string,0) for string in twitter_samples.strings('negative_tweets.json')]
pos_tweets.extend(neg_tweets)
comb_tweets = pos_tweets
random.shuffle(comb_tweets)
tweets,labels = (zip(*comb_tweets))


# In[47]:


count_vectorizer = CountVectorizer(ngram_range=(1,2),max_features=10000)
X = count_vectorizer.fit_transform(tweets)


# In[48]:


X_train,X_test,y_train,y_test = train_test_split(X,labels,test_size=0.2,random_state=10)


# In[49]:


rf = RandomForestClassifier(n_estimators=100,n_jobs=4,random_state=10)
rf.fit(X_train,y_train)


# In[50]:


preds = rf.predict(X_test)
print(accuracy_score(y_test,preds))
print(confusion_matrix(y_test,preds))


# In[58]:


from nltk.corpus import stopwords
tfidf = TfidfVectorizer(ngram_range=(1,2),max_features=10000, stop_words=stopwords.words('english'))
X = tfidf.fit_transform(tweets)


# In[59]:


X_train,X_test,y_train,y_test = train_test_split(X,labels,test_size=0.2,random_state=10)


# In[60]:


rf = RandomForestClassifier(n_estimators=100,n_jobs=4,random_state=10)
rf.fit(X_train,y_train)


# In[61]:


preds = rf.predict(X_test)
print(accuracy_score(y_test,preds))
print(confusion_matrix(y_test,preds))


# In[ ]:




