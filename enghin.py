from preprocessing import *
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pandas as pd

df = pd.read_csv("D:\\CodeMix\\eng.csv",encoding="utf-8")

tweet = df.Tweet
sentiment = df.Sentiment

all_text = [(tweet[i],sentiment[i]) for i in range(10)]
print(all_text)
y_true = []
y_pred = []

for i,t in enumerate(all_text):
    print(i)
    text = t[0]
    y_true.append(t[1])
    _,_,hinDict,engDict = preprocessing(text)

    #Lemmatization
    lemmaeng=lemmatize_en(engDict)
    lemmahin=lemmatize_hi(hinDict)

    #print("Lemmatized Hindi:",lemmahin,"\nLemmatized English:",lemmaeng)

    #POS Tagging
    poseng=postagger_en(lemmaeng)
    poshin=postagger_hi(lemmahin)

    #print('POS English:',poseng)
    #print("POS Hindi:",poshin)

    #Negation handling
    negEng = negation_handling_eng(poseng)
    negHin = negation_handling_hin(poshin)
    #print("Negation Handling for English:",negEng)
    #print("Negation Handling for Hindi:",negHin)

    #Checking english senti and hindi senti
    engSent = EngSWN.get_scores(list(negEng.values()))
    hinSent = HindiSWN.get_scores(list(negHin.values()))
    print("English SentiWordNet Result:",engSent)
    print("Hindi SentiWordNet Result:",hinSent)
    combinedScore = engSent[1] + hinSent[1]
    print("Combined Score:",combinedScore)
    if combinedScore > 0.1:
        prediction = "Positive"
    elif combinedScore < -0.1:
        prediction = "Negative"
    else:
        prediction = "Neutral"
    print("Actual:",t[1])
    print("Pred:",prediction,"\n")
    y_pred.append(prediction)

print("True:",y_true)
print("Pred:",y_pred)
print(confusion_matrix(y_true, y_pred, labels=['Negative', 'Neutral', 'Positive']))
print(classification_report(y_true,y_pred))