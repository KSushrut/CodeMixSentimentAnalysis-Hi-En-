from flask import Flask, render_template, request
from preprocessing import lexicon_sentiment, ml_preprocess
from ml_models.naive_bayes_model import *

app = Flask(__name__)

countVec, model_naive = loading_and_training()

@app.route('/',methods=['POST','GET'])
def main():
    sentiment = "Lexicon Sentiment Prediction: Not yet checked"
    ip = "The text you enter in the box."
    tl = "Transliteration of Hindi Latin to Devanagari."
    em = "Substituting emojis and abbreviations."
    neg = "Handling Negation."
    lexicon_accuracy = ""
    ml_accuracy = ""
    ml_prediction = "ML Sentiment Prediction: Not yet checked"
    if request.method == "POST":
        ip_text = request.form['ip_text']
        abb,stop,neg,prediction,clang = lexicon_sentiment(ip_text)
        fl_list = ' '.join(ml_preprocess(ip_text))
        ml_pred = naive_bayes_prediction(fl_list,countVec,model_naive)
        ml_prediction = "Naive Bayes Sentiment Prediction: "
        if ml_pred[0] == '-1':
            ml_prediction += 'Negative'
        elif ml_pred[0] == '0':
            ml_prediction += 'Neutral'
        else:
            ml_prediction += 'Positive'
        print(ml_pred)
        ip = ip_text
        tl = stop
        em = abb
        if clang == "PE":
            lexicon_accuracy = "70.00%"
            ml_accuracy = "88.40%"
        elif clang == "PH":
            lexicon_accuracy = "80.00%"
            ml_accuracy = "61.11%"
        else:
            lexicon_accuracy = "70.00%"
            ml_accuracy = "59.86%"
        sentiment = "Lexicon Sentiment Prediction: " + prediction[0].upper() + prediction[1:]
    return render_template('index.html',s=sentiment,i=ip,t=tl,n=neg,e=em,mls=ml_prediction,la=lexicon_accuracy,ma=ml_accuracy)

if __name__ == '__main__':
    app.run()