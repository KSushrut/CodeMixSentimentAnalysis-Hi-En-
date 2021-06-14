tagsDict = {
    "ADJ" : "a",
    "NOUN" : "n",
    "ADV" : "r",
    "VERB" : "v"
}
def split_line(line):
    cols = line.split("\t")
    return cols

def get_pos_tag(cols):
    return cols[0]

def get_words(cols):
    words_ids = cols[4].split(" ")
    words = [w.split("#")[0] for w in words_ids]
    return words

def get_positive(cols):
    return cols[2]

def get_negative(cols):
    return cols[3]

def get_objective(cols):
    return 1 - (float(cols[2]) + float(cols[3]))

def get_scores(sentiword):
    f = open("D:\CodeMix\SentiWordNet_3.0.0_20130122.txt","r")
    res = 0
    wordList = {}
    count = 0
    score = 0.0
    for line in f:
        if not line.startswith("#"):
            cols = split_line(line)
            words = get_words(cols)
            pos = get_pos_tag(cols)
            for word in sentiword:
                negate = False
                if word.startswith("!"):
                    negate = True
                    actualWord = word[1:]
                else:
                    actualWord = word
                actualWord,tagWord = actualWord.split("/")[0], actualWord.split("/")[1]
                if tagWord == "ADJ" or tagWord == "ADV" or tagWord == "VERB" or tagWord == "NOUN":
                    tag = tagsDict[tagWord]
                    if actualWord in words and pos == tag:                    
                        if not negate:
                            res += float(get_positive(cols)) - float(get_negative(cols))
                        else:
                            res += (float(get_positive(cols)) - float(get_negative(cols))) * -1
                        count = count + 1
                        if actualWord in wordList.keys():
                            wordList.update({actualWord : wordList[actualWord] + float(get_positive(cols)) - float(get_negative(cols))})
                        else:
                            wordList.update({actualWord : float(get_positive(cols)) - float(get_negative(cols))})
    if len(wordList.keys()) > 0:
        score = res / len(wordList.keys())
    if score > 0:
        return ("Positive",score)
    elif res < 0:
        return ("Negative",score)
    return ("Neutral",score)