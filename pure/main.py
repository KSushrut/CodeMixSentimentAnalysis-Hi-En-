#Imports
from preprocessing import *
import json
from sklearn.metrics import classification_report

#Get the comments


#Get list of all comments from JSON
comments = [
    "हिंदी सिनेमा की सबसे खूबसूरत एक्ट्रेसेज में मधुबाला नाम सबसे ऊपर आता है | ❤️",
    "वैक्सीन पूरी तरह से सुरक्षित और कारगर, टीकाकरण में तकनीक का इस्तेमाल किया जाएगा; नीति आयोग के सदस्य डॉ वी. के. पॉल से खास बातचीत",
    "हनुमंत ! दिव्य ! रुद्रा अवतार , सूरज को निगलने की शक्ति ! 'जय हनुमान ज्ञान गुण सागर , जय कपीश तिहूँ लोक उजागर' राम दूत अतुलित बल नामा , अंजनी-पुत्र पवन सुत नामा '",
    "निर्देशक रेणुका शहाणे ने 'त्रिभंग' में मुद्दों के साथ साथ भावनाओं को अहम जगह दी है और यही बात दिल को छूती है। फिल्मीबीट की ओर से फिल्म को 3.5 स्टार।",
    "हमारा अस्तित्व एक दयाहीन निर्मम जटिल उलझन है ; दो मात्राओं या संख्याओं का समीकरण जिसका समाधान या निराकरण अभी तक नहीं हुआ है",
    "दीवाली का त्यौहार भारत में एक प्रमुख खरीदारी की अवधि का प्रतीक है। उपभोक्ता खरीद और आर्थिक गतिविधियों के संदर्भ में दीवाली, पश्चिम में क्रिसमस के बराबर है। ",
    "जियो का छोटे कारोबारियों के लिए खास ऑफर !! 😊कनेक्टिविटी खर्च घटाने के साथ ही बिजनेस बढ़ाने में ऐसे करेगी मदद|",
    "अनेक बार हारा तो क्या,अनेक ठोकर खाई तो क्या,ठोकर के आगे का पथ,ले जाऐगा बुलंदि पर।😊👍🏻",
    "हमारे देश को आजादी दिलाने में अनेकों लोगों का हाथ था। इस गणतंत्र दिवस पर आईए हम सब उन्हें नमन करे। 🙏🏻",
    "इस लॉकडॉन सभी अध्यापक अध्यापिकाओं ने बहुत मेहनत की है ताकि हमारे देश के बच्चों की पढ़ाई में कोई कमी न आए। #सम्मान 🙌🏻❤️"
]

y_true = ["Positive","Neutral","Neutral","Neutral","Neutral","Neutral","Neutral","Positive","Neutral","Positive"]
y_pred = []

#Run preprocessing
for comment in comments:
    #Filter
    fitered_comment = filter(comment)
    #Tokenize
    tokens = tokenize(fitered_comment)
    #Any intermediate steps?
    
    #Converting tokens to dictionary
    tokDict = separate_into_dict(tokens)
    #Removing stopwords
    stopRemoved = hindiStopwordsRemover(tokDict)
    #Lemmatization
    lemmHin = lemmatize_hi(stopRemoved)
    #POS Tagging
    postag = postagger_hi(lemmHin)
    #Negation Handling
    negHin = negation_handling_hin(postag)
    #Sentiment Score
    senti = sentiment(negHin)
    if senti[1] > -0.2 and senti[1] < 0.2:
        y_pred.append("Neutral")
    else:
        y_pred.append(senti[0])
print(y_pred)

print(classification_report(y_true,y_pred))