from nltk.tokenize import word_tokenize
import sys
import stanza
import new_emoji as emoji
import abbr
import langCheck
import HindiSWN
import EngSWN
sys.path.append('D:/CodeMix/')

##########          GLOBAL VARIABLES DECLARED HERE            ##########

normal_list=[]
scr_val=[]
engDict = {}
hinDict = {}
nlp_en = stanza.Pipeline('en') # This sets up a default neural pipeline in English
nlp_hi = stanza.Pipeline('hi')
"""
pos_dict = {
'CC': 'coordinating conjunction','CD': 'cardinal digit','DET': 'determiner',
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
"""
#########################################################################

def englishStopwordsRemover(engDict):
    #stopwords_en = list(set(stopwords.words('english')))
    stopwords_en = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]
    newEngDict = {}
    if "won" in stopwords_en:
        print("won is there")
    for index,enToken in engDict.items():
        if enToken not in stopwords_en:
            newEngDict.update({index:enToken})
    return newEngDict

def hindiStopwordsRemover(hinDict):
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
    newHinDict = {}
    for index,hiToken in hinDict.items():
        if hiToken not in stopwords:
            newHinDict.update({index:hiToken})
    return newHinDict
     
def preprocessing(text):      
    #function to tokenize, substitute emojis, replace abbreviations
    text = text.lower()
    tokenized_list = word_tokenize(text)
    
    emoji_sub = emoji.convert_emoji(emoji.separate_emoji(tokenized_list)) #substituting emojis
        
    #replacing abbreviations
    normal_list = [x for x in abbr.abbr_sub(emoji_sub) if x != '']                    
    
    #Separate Hindi and English
    engDict,hinDict = langCheck.separate_into_dict(normal_list)
    
    #Identify if there are some Hindi words in Latin Script in English Dict
    if engDict != {}:
        langIden = langCheck.identifyLang(' '.join(langCheck.convert_dict_to_list(engDict)))
        #Check for ambiguity
        langEval = langCheck.evalLangTag(langIden)
        #Transliterate
        engstring = langCheck.mytransliterate(langEval)
    
        #Add the transliterated words from EngDict to HinDict
        for i,eng in enumerate(engstring):
            if i in engDict and engDict[i] != eng:
                #This is the transliterated word
                hinDict.update({i : eng})
                del engDict[i]
        
    
    #Sort the dictionaries according to key
    engDict = {key: value for key, value in sorted(engDict.items(), key=lambda item: item[0])}
    hinDict = {key: value for key, value in sorted(hinDict.items(), key=lambda item: item[0])}

    print("Language",engDict,hinDict)

    #Hindi Stopwords
    hinDict = hindiStopwordsRemover(hinDict)
    #print("Removed Hindi StopWords:",hinDict)
    
    #English Stopwords
    engDict = englishStopwordsRemover(engDict)
    #print("Removed English StopWords:",engDict)

    #Check if pure eng, pure hi or codemix
    if hinDict and engDict:
        clang = "CM"
    elif hinDict and not engDict:
        clang = "PH"
    elif engDict and not hinDict:
        clang = "PE"


    #Merge the dictionaries
    stop_list = langCheck.mergeDict(engDict,hinDict)

    #Return both the dictionaries after preprocessing
    return normal_list,stop_list,hinDict,engDict, clang

#Add the ! to the words till we hit a noun, verb or an adjective
def negation_handling_eng(pos_dict):
    newDict = {}
    exclamation = False
    skip = False
    for index,word in pos_dict.items():
        actualWord = word.split("/")[0]
        #Check if the word is NOT
        if actualWord == "not":
            #Make the exclamation alive
            exclamation = not exclamation
            skip = True
        elif exclamation == True:
            skip = False
            #Check if the word is adjective, noun or a verb
            pos = word.split("/")[1]
            #Add the exclamation
            word = '!' + word
            if pos == 'ADJ' or pos == 'NOUN' or pos == 'VERB':
                #Set exclamation to False
                exclamation = False
            #If any other tag, negate them
        #Update in new dict
        if skip == False:
            newDict.update({index : word})
        else:
            skip = False
    return(newDict)

def negation_handling_hin(pos_dict):
    newDict = {}
    exclamation = False
    skip = False
    for index,word in pos_dict.items():
        actualWord = word.split("/")[0]
        pos = word.split("/")[1]
        #Check if the word is नहीं
        if actualWord == "नहीं" or actualWord == "नही":
            #Do backward negation
            skip = True
            #Get the list of words backwards
            wordsChange = reversed([(x,y) for x,y in newDict.items()])
            for i,w in wordsChange:
                #Get POS Tag
                p = w.split("/")[1]
                #Exclamation is Alive
                newWord = "!" + w
                #Update in the dictionary
                newDict.update({i : newWord})
                if p == 'ADJ' or p == 'NOUN' or p == 'VERB':
                    break
        elif actualWord == "न" or actualWord == "ना":
            #Do forward negation
            exclamation = not exclamation
            skip = True
            #Add the exclamation
            word = '!' + word
            #Check if the word is adjective, noun or a verb
            if pos == 'ADJ' or pos == 'NOUN' or pos == 'VERB':
                #Set exclamation to False
                exclamation = False
        if skip == False:
            newDict.update({index : word})
        else:
            print(actualWord)
            skip = False
    return newDict

#function for english lemmatization
def lemmatize_en(filtered_eng):                      
    newDict = {}
    keys=list(filtered_eng.keys())
    values=filtered_eng.values()
    string=' '.join(values)
    doceng = nlp_en(string)
    lemmatized_list = []
    for sent in doceng.sentences:
        for word in sent.words:
            lemmatized_list.append(word.lemma)
    for i in range(len(values)) :
        newDict.update({keys[i]:lemmatized_list[i]})
    return (newDict)

#function for hindi lemmatization
def lemmatize_hi(filtered_hin):                      
    newDict = {}
    keys=list(filtered_hin.keys())
    values=filtered_hin.values()
    string=' '.join(values)
    dochi = nlp_hi(string)
    lemmatized_list = []
    for sent in dochi.sentences:
        for word in sent.words:
            lemmatized_list.append(word.lemma)
    for i in range(len(values)) :
        newDict.update({keys[i]:lemmatized_list[i]})
    return(newDict)
    
#function for pos tagging for english
def postagger_en(lemmaeng):                   
    newDict = {}
    keys=list(lemmaeng.keys())
    values=lemmaeng.values()
    string=' '.join(values)
    doceng = nlp_en(string)
    pos_list=[]
    for sent in doceng.sentences:
        for word in sent.words:
            pos_list.append(word.text+'/'+word.upos)
    for i in range(len(values)) :
        newDict.update({keys[i]:pos_list[i]})        
    return(newDict)

#function for pos tagging for hindi
def postagger_hi(lemmahin):                   
    newDict = {}
    keys=list(lemmahin.keys())
    values=lemmahin.values()
    string=' '.join(values)
    dochi = nlp_hi(string)
    pos_list=[]
    for sent in dochi.sentences:
        for word in sent.words:
            pos_list.append(word.text+'/'+word.upos)
    for i in range(len(values)) :
        newDict.update({keys[i]:pos_list[i]})        
    return(newDict)

def lexicon_sentiment(text):
    #Preprocessing
    abb,stop,hinDict,engDict, clang = preprocessing(text)

    #Lemmatization
    lemmaeng=lemmatize_en(engDict)
    lemmahin=lemmatize_hi(hinDict)

    #POS Tagging
    poseng=postagger_en(lemmaeng)
    poshin=postagger_hi(lemmahin)

    print('POS English:',poseng)
    print("POS Hindi:",poshin)

    #Negation handling
    negEng = negation_handling_eng(poseng)
    negHin = negation_handling_hin(poshin)
    print("Negation Handling for English:",negEng)
    print("Negation Handling for Hindi:",negHin)

    neg = langCheck.mergeDict(negEng,negHin)

    #Checking english senti and hindi senti
    engSent = EngSWN.get_scores(list(negEng.values()))
    hinSent = HindiSWN.get_scores(list(negHin.values()))
    print("English SentiWordNet Result:",engSent)
    print("Hindi SentiWordNet Result:",hinSent)
    combinedScore = engSent[1] + hinSent[1]
    print("Combined Score:",combinedScore)
    if combinedScore > 0:
        prediction = "positive"
    elif combinedScore < 0:
        prediction = "negative"
    else:
        prediction = "neutral"

    #Need to return abbr_sub, transliterated, negation and prediction
    return(abb,stop,neg,prediction,clang)

def ml_preprocess(text):
    textN = text.lower()
    tokenized_list = word_tokenize(textN)
    emoji_sub = emoji.convert_emoji(emoji.separate_emoji(tokenized_list)) #substituting emojis
    normal_list = [x for x in abbr.abbr_sub(emoji_sub) if x != '']
    engDict,hinDict = langCheck.separate_into_dict(normal_list)
    hinDict = hindiStopwordsRemover(hinDict)    
    engDict = englishStopwordsRemover(engDict)
    stop_list = langCheck.mergeDict(engDict,hinDict)
    return stop_list