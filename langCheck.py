from getLanguage import langIdentify
from google.transliteration import transliterate_word

#Prepare the hindi dict
f = open("D:\CodeMix\hindi_words\HinWords.txt","r",encoding="utf-8",errors='ignore')
allHindiWords = [x.replace("\n","") for x in f.readlines()]
f.close()

#Script Validate
def detectLang(word,lang="EN"):
    if len(word)>=1 and lang == "EN":
        for x in word:
            if ord(x) not in list(range(65,123)):                
                return False
            return True
    if len(word)>=1 and lang == "HI":
        for x in word:
            if ord(x) not in list(range(2304,2432)):
                return False
            return True
    return False

#Identify language first
def identifyLang(string):
    return(langIdentify(string,"classifiers/HiEn.classifier")[0])

#Transliterate the hindi words, else keep it as it is
def mytransliterate(newList):
    final_list = []
    for x in newList:
        #If language tagged is English
        if x[1] == "EN":
            final_list.append(x[0])
        #If language tagged is Hindi
        elif x[1] == "HI":
            #Transliterate
            out = getGoodTransliteration(x[0])
            final_list.append(out)
    return(final_list)

#Separate into dictionaries
def separate_into_dict(tokens):
    hindiDict = {}
    englishDict = {}
    for i,token in enumerate(tokens):
        if detectLang(token,lang="EN"):
            englishDict.update({i : token})
        elif detectLang(token,lang="HI"):
            hindiDict.update({i : token})
    return englishDict,hindiDict

#Convert list to dictionary
def convert_dict_to_list(dicti):
    return [x for x in dicti.values()]

#Get key from value
def getKey(val,dicti):
    for x,y in dicti.items():
        if y == val:
            return x

#Merge dictionary
def mergeDict(eng,hin):
    eng.update(hin)
    return [x for x in {key: value for key, value in sorted(eng.items(), key=lambda item: item[0])}.values()]

#Looks for language ambiguity
def evalLangTag(langTokens):
    #List of ambiguous words
    ambiguous = ["so","me","main","to","hum"]
    for i in range(len(langTokens)-2):
        #If left word and right word have same lang tag and middle word has different lang tag
        if langTokens[i][1] == langTokens[i+2][1] and langTokens[i+1][1] != langTokens[i][1]:
            #Check if the word is in ambiguous
            if langTokens[i+1][0] in ambiguous:
                #Update the language
                langTokens[i+1][1] = langTokens[i][1]
    return(langTokens)

#Check transliteration which is best
def getGoodTransliteration(word):
    #Get the Hindi Dict
    out = transliterate_word(word, lang_code='hi')
    global allHindiWords
    if len(out) == 0:
        return None
    for o in out:
        if o in allHindiWords:
            return o
    return out[0]