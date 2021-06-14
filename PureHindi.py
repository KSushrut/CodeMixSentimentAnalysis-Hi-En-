#!/usr/bin/env python
# coding: utf-8

# 
# <h1>Pure Hindi Text</h1>

# In[1]:


import nltk
#nltk.download('all')
from nltk.tokenize import word_tokenize
import nltk.data
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import sys
sys.path.append('D:/CodeMix/')
import stanza
import pandas as pd


# <h1>Tokenization

# In[ ]:


hitxt="हिंदी सिनेमा की सबसे खूबसूरत एक्ट्रेसेज में मधुबाला नाम सबसे ऊपर आता है | ❤️"
hi_token = word_tokenize(hitxt)
for i in hi_token:
  if "|" in i and len(i)>1:
    hi_token.insert(hi_token.index(i)+1,"|")
    hi_token[hi_token.index(i)]=i[:-1]
print("Tokenization:",hi_token)


# # Substituting Emojis

# In[7]:


import emoji
sep_tokens = emoji.separate_emoji(hi_token)
print(sep_tokens)
emoji_sub=emoji.convert_emoji(sep_tokens)
print("Emojis:",emoji_sub)


# <h1>Script Validation

# In[8]:


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
for words in hi_token:
  if(detectLang(words,wordFlag=True,lang="HI")=='HI'):
    scr_val.append(words)
print("Script Val:",scr_val)


# <h1>Stop word removal

# In[25]:


stopwords = ['मैं', 'मुझको', 'मेरा', 'अपने आप को', 'हमने', 'हमारा', 'अपना', 'हम', 'आप', 'आपका', 'तुम्हारा', 'अपने आप', 'स्वयं',
             'वह', 'इसे, उसके', 'खुद को', 'कि वह', 'उसकी', 'उसका', 'खुद ही', 'यह', 'इसके', 'उन्होने', 'अपने', 'क्या', 'जो', 'किसे',
             'किसको', 'कि', 'ये', 'हूँ', 'होता है', 'रहे', 'थी', 'थे', 'होना', 'गया', 'किया जा रहा है', 'किया है', 'है', 'पडा', 'होने', 'करना',
             'करता है', 'किया', 'रही', 'एक', 'लेकिन', 'अगर', 'या', 'क्यूंकि', 'जैसा', 'जब तक', 'जबकि', 'की', 'पर', 'द्वारा', 'के लिए', 'साथ',
             'के बारे में', 'खिलाफ', 'बीच', 'में', 'के माध्यम से', 'दौरान', 'से पहले', 'के बाद', 'ऊपर', 'नीचे', 'को', 'से', 'तक', 'से नीचे', 'करने में', 'निकल', 'बंद', 'से अधिक',
             'तहत', 'दुबारा', 'आगे', 'फिर', 'एक बार', 'यहाँ', 'वहाँ', 'कब', 'कहाँ', 'क्यों', 'कैसे', 'सारे', 'किसी', 'दोनो', 'प्रत्येक', 'ज्यादा', 'अधिकांश', 'अन्य', 'में कुछ', 'ऐसा', 
             'में कोई', 'मात्र', 'खुद', 'समान', 'इसलिए', 'बहुत', 'सकता', 'जायेंगे', 'जरा', 'चाहिए', 'अभी', 'और', 'कर दिया', 'रखें', 'का', 'हैं', 'इस', 'होता', 'करने', 'ने', 'बनी', 'तो',
             'ही', 'हो','इसका', 'था', 'हुआ', 'वाले', 'बाद', 'लिए', 'सकते', 'इसमें', 'दो', 'वे', 'करते', 'कहा', 'वर्ग', 'कई', 'करें', 'होती', 'अपनी', 'उनके', 'यदि', 'हुई', 'जा', 'कहते',
             'जब', 'होते', 'कोई', 'हुए', 'व', 'जैसे', 'सभी', 'करता', 'उनकी', 'तरह', 'उस', 'आदि', 'इसकी', 'उनका', 'इसी', 'पे', 'तथा', 'भी', 'परंतु', 'इन', 'कम', 'दूर', 'पूरे', 'गये', 
             'तुम', 'मै', 'यहां', 'हुये', 'कभी', 'अथवा', 'गयी', 'प्रति', 'जाता', 'इन्हें', 'गई', 'अब', 'जिसमें', 'लिया', 'बड़ा', 'जाती', 'तब', 'उसे', 'जाते', 'लेकर', 'बड़े', 'दूसरे', 'जाने',
             'बाहर', 'स्थान', 'उन्हें', 'गए', 'ऐसे', 'जिससे', 'समय', 'दोनों', 'किए', 'रहती', 'इनके', 'इनका', 'इनकी', 'सकती', 'आज', 'कल', 'जिन्हें', 'जिन्हों', 'तिन्हें', 'तिन्हों', 'किन्हों', 
             'किन्हें', 'इत्यादि', 'इन्हों', 'उन्हों', 'बिलकुल', 'निहायत', 'इन्हीं', 'उन्हीं', 'जितना', 'दूसरा', 'कितना', 'साबुत', 'वग़ैरह', 'कौनसा', 'लिये', 'दिया', 'जिसे', 'तिसे', 'काफ़ी', 'पहले',
             'बाला', 'मानो', 'अंदर', 'भीतर', 'पूरा', 'सारा', 'उनको', 'वहीं', 'जहाँ', 'जीधर', 'के', 'एवं', 'कुछ', 'कुल', 'रहा', 'जिस', 'जिन', 'तिस', 'तिन', 'कौन', 'किस', 'संग', 'यही',
             'बही', 'उसी', 'मगर', 'कर', 'मे', 'एस', 'उन', 'सो', 'अत' ]


# In[28]:


rem_sw=[]
for i in scr_val:
    if i not in stopwords:
        rem_sw.append(i)
print("Stop Words",rem_sw)


# In[15]:


stanza.download('hi')       # This downloads the English models for the neural pipeline
nlp = stanza.Pipeline('hi') # This sets up a default neural pipeline in English
doc = nlp("हिंदी सिनेमा की सबसे खूबसूरत एक्ट्रेसेज में मधुबाला नाम सबसे ऊपर आता है|❤️")
print(doc)

# # Lemmatization

# In[17]:

def extract_lemma(doc):
    parsed_text = {'word':[], 'lemma':[]}
    for sent in doc.sentences:
        for wrd in sent.words:
            #extract text and lemma
            parsed_text['word'].append(wrd.text)
            parsed_text['lemma'].append(wrd.lemma)
    #return a dataframe
    return pd.DataFrame(parsed_text)

#call the function on doc
print(extract_lemma(doc))


# # POS Tagging

# In[5]:

pos_dict = {
'CC': 'coordinating conjunction','CD': 'cardinal digit','DT': 'determiner',
'EX': 'existential there (like: \"there is\" ... think of it like \"there exists\")',
'FW': 'foreign word','IN':  'preposition/subordinating conjunction','JJ': 'adjective \'big\'',
'JJR': 'adjective, comparative \'bigger\'','JJS': 'adjective, superlative \'biggest\'',
'LS': 'list marker 1)','MD': 'modal could, will','NN': 'noun, singular \'desk\'',
'NNS': 'noun plural \'desks\'','NNP': 'proper noun, singular \'Harrison\'',
'NNPS': 'proper noun, plural \'Americans\'','PDT': 'predeterminer \'all the kids\'',
'POS': 'possessive ending parent\'s','PRP': 'personal pronoun I, he, she',
'PRP$': 'possessive pronoun my, his, hers','RB': 'adverb very, silently,',
'RBR': 'adverb, comparative better','RBS': 'adverb, superlative best',
'RP': 'particle give up','TO': 'to go \'to\' the store.','UH': 'interjection errrrrrrrm',
'VB': 'verb, base form take','VBD': 'verb, past tense took',
'VBG': 'verb, gerund/present participle taking','VBN': 'verb, past participle taken',
'VBP': 'verb, sing. present, non-3d take','VBZ': 'verb, 3rd person sing. present takes',
'WDT': 'wh-determiner which','WP': 'wh-pronoun who, what','WP$': 'possessive wh-pronoun whose',
'WRB': 'wh-abverb where, when','QF' : 'quantifier, bahut, thoda, kam (Hindi)','VM' : 'main verb',
'PSP' : 'postposition, common in indian langs','DEM' : 'demonstrative, common in indian langs'
}


# In[10]:


def extract_pos(doc):
    parsed_text = {'word':[], 'pos':[], 'exp':[]}
    for sent in doc.sentences:
        for wrd in sent.words:
            if wrd.pos in pos_dict.keys():
                pos_exp = pos_dict[wrd.pos]
            else:
                pos_exp = 'NA'
            parsed_text['word'].append(wrd.text)
            parsed_text['pos'].append(wrd.pos)
            parsed_text['exp'].append(pos_exp)
    #return a dataframe of pos and text
    return pd.DataFrame(parsed_text)
print(extract_pos(doc))


# In[ ]:




