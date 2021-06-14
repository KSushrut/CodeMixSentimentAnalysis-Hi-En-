#!/usr/bin/env python
# coding: utf-8

# # **Implement Data Preprocessing part in the architecture for Pure Enlgish**
# 
# 

# In[3]:


import nltk
from nltk.tokenize import word_tokenize
import nltk.data
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import sys
sys.path.append('D:/CMTSA/CodeMix/')


# <h2>Pure English Text</h2>

# In[8]:


#test for atleast 10 pure English code
text='Kya bhai.. 🤗 kya chal rha hai 🤭 no comments 🙇🏻‍♀️🙌🏻🙏🏾'
text=text.lower()       #to lowercase


# <h2>Tokenization: Split sentences into individual tokens</h2>

# In[9]:


tokenized_list = word_tokenize(text)
print("Words Tokenize List:", tokenized_list)


# <h2>Substituting Emoticons</h2>

# In[10]:


import new_emoji as emoji
sep_tokens = emoji.separate_emoji(tokenized_list)
emoji_sub=emoji.convert_emoji(sep_tokens)
print(emoji_sub)


# # **Text Normalization: Substituting Abbreviations**

# In[11]:


import abbr
normal_list=abbr.abbr_sub(emoji_sub)
print(normal_list)


# # Script Valdiation

# In[12]:


def detectLang(inText,charFlag=False,wordFlag=False,sentenceFlag=False,lang="EN"):
  if charFlag:
    if len(inText)==1 and lang == "EN":
      if ord(inText) in list(range(65,123)):
        return "EN"
    if len(inText)==1 and lang == "HI":
      if ord(inText) in list(range(2304,2432)):
        return "HI"
  if wordFlag:
    if len(inText)>1 and lang == "EN":
      for x in inText:
        if ord(x) not in list(range(65,123)):
          return "Not Found"
      return "EN"
    if len(inText)>1 and lang == "HI":
      for x in inText:
        if ord(x) not in list(range(2304,2432)):
          return "Not Found"
      return "HI"

    if sentenceFlag:
      pass

  return "Not Found"

  #https://en.wikipedia.org/wiki/List_of_Unicode_characters
  #https://jrgraphix.net/r/Unicode/0020-007F
scr_val=[]
for words in normal_list:
  if(detectLang(words,wordFlag=True,lang="EN")=='EN' or detectLang(words,wordFlag=True,lang="HI")=='HI'):
    scr_val.append(words)
print(scr_val)


# <h2>Removing Stop Words</h2>

# In[13]:


stop_words_en = set(stopwords.words('english')) 

filtered_text_nltk = [] #without stopwords
# tokenized_text = word_tokenize(text)

for token in scr_val:
  if token not in stop_words_en:
    filtered_text_nltk.append(token)

print(filtered_text_nltk)


# <h2>Lemmetization</h2>

# In[14]:


lemmatizer = WordNetLemmatizer() 
lemmatized_list = []
for w in filtered_text_nltk:
  lemmatized_list.append(lemmatizer.lemmatize(w)) 
print(filtered_text_nltk)
print(lemmatized_list)


# In[ ]:




