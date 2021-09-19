# Code-Mixed Sentiment Analysis for Multi-lingual [EN-HI] Social media text

# Table of Contents

- [Code Mixed Sentiment Analysis for Multi-lingual[EN-HI] Social media text](#code-mixed-sentiment-analysis-for-multi-lingual[en-hi]-social-media-text)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Development](#development)
- [License](#license)
- [Footer](#footer)


# Installation
[(Back to top)](#table-of-contents)<br>
1. Natural Language Toolkit (NLTK)

NLTK, a Python package for natural language processing. NLTK requires Python 3.5, 3.6, 3.7, or 3.8.M<br> 
- On Windows command prompt,<br>
  - Navigate to the location of the pip folder
  - Enter command to install NLTK <br>
```
  !pip install nltk
```  
- Or on Anaconda<br>
```
  conda install -c anaconda nltk
```
2. Stanza<br>
Stanza supports Python 3.6 or later. We recommend that you install Stanza via pip, the Python package manager. <br>
- On Windows command prompt, run:<br>
```
  !pip install stanza
```

This should also help resolve all of the dependencies of Stanza, for instance PyTorch 1.3.0 or above.
If you currently have a previous version of stanza installed, use:<br>
```
  !pip install stanza -U
```
- Or on Anaconda<br>
To install Stanza via Anaconda, use the following conda command:<br>
```
  conda install -c stanfordnlp stanza
```
Note that for now installing Stanza via Anaconda does not work for Python 3.8. For Python 3.8 please use pip installation. <br>
- From Source <br>
Alternatively, you can also install from source via Stanza’s git repository, which will give you more flexibility in developing on top of Stanza. For this option, run<br>
```
  git clone https://github.com/stanfordnlp/stanza.git
  cd stanza
  pip install -e 
```
 
 # Development
[(Back to top)](#table-of-contents)<br>
<h2>Architecture</h2>
Image here<br>
Initially, we have tried to implement the Data pre-processing section by considering Pure English and Pure Hindi text. Import the below packages<br>
```
import nltk
from nltk.tokenize import word_tokenize
import nltk.data
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import stanza
import pandas as pd
nltk.download('stopwords')
```

1. Input
Consider the below sample input throughout the process. 
```
en_text = 'King Kohli is gone for a duck! Caught by Ben Foakes. Ben Stokes gets the wicket. King y u play like that 😭#INDvENG'
hi_text = 'तुमने हमें पूज पूज कर पत्थर कर डाला ; वे जो हमपर जुमले कसते हैं हमें ज़िंदा तो समझते हैं हरिवंश राय  बच्चन'
```

2. Data Preprocessing

For Emojis, we have defined a `emoji.py` module in which, a set of emojis is consider as a dictionary where emoji is the key and description is the value.<br>
![image](https://user-images.githubusercontent.com/39995604/110206906-82428300-7ea6-11eb-8912-01d69a6b69dc.png)







 
