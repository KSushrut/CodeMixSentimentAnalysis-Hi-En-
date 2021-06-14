import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def loading_and_training():
    n = ['Count','Tweet','Sentiment']
    data=pd.read_csv('D:\\CodeMix\\ml_models\\CSV3.csv', sep=',',error_bad_lines=False, names=n)
    tweet = data.Tweet.fillna(' ')
    sentiment = data.Sentiment.fillna(' ')

    count_vectorizer = CountVectorizer(ngram_range=(1,2))    # Unigram and Bigram
    final_vectorized_data = count_vectorizer.fit_transform(tweet)  
    final_vectorized_data

    X_train, X_test, y_train, y_test = train_test_split(final_vectorized_data, sentiment, test_size=0.2, random_state=69)

    y_train=np.array(y_train).reshape(13558,1)
    y_test=np.array(y_test).reshape(3390,1)

    model_naive = MultinomialNB().fit(X_train, y_train.ravel()) 
    #predicted_naive = model_naive.predict(X_test)
    print("training done")
    return count_vectorizer,model_naive

def naive_bayes_prediction(tweet,count_vectorizer,model_naive):
    print(tweet)
    finalVector = count_vectorizer.transform([tweet]).toarray()
    return(model_naive.predict(finalVector))