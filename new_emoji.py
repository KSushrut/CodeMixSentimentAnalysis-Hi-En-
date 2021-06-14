emojis = {128514: ['laugh'], 128515 : ['smile'], 129315: ['laugh'], 128518: ['laugh'], 128517: ['hesitant'], 128522: ['smile'], 128578: ['smile'], 128513: ['cheerful'], 128519: ['blessed'], 128540: ['joking'], 128579: ['ironic', 'smile'], 128079: ['clap'], 128525: ['love'], 129392: ['loved'], 128536: ['flying', 'kiss'], 128535: ['kiss'], 128537: ['kiss', 'with', 'smile'], 128538: ['kiss', 'with', 'eyes', 'closed'], 128523: ['yummy'], 128539: ['joking'], 129320: ['suspicion'], 129488: ['skeptical'], 128526: ['i', 'am', 'cool'], 129321: ['amazing'], 129299: ['nerd'], 129395: ['party'], 128527: ['mischief'], 128530: ['unamused'], 128542: ['disappointed'], 128533: ['confused'], 128532: ['pensive'], 128543: ['worry'], 128577: ['slight', 'frown'], 9785: ['frown'], 128547: ['frustrated'], 128534: ['more', 'frustrated'], 128555: ['tired'], 128553: ['weary'], 129402: ['pleading'], 128546: ['slightly', 'cry'], 128557: ['cry'], 128548: ['fuming'], 128544: ['angry'], 128545: ['rage'], 129324: ['swearing'], 129327: ['mind', 'blown'], 128563: ['utter', 'shock'], 129397: ['too', 'hot'], 129398: ['freezing'], 128561: ['horror'], 128552: ['shock'], 128560: ['fear'], 128549: ['sadness'], 128531: ['frustration'], 129303: ['hug'], 129300: ['think'], 129325: ['blush'], 129323: ['quiet'], 128566: ['speechless'], 128529: ['disappointed'], 128556: ['nervous'], 128580: ['disdain'], 128559: ['mild', 'excitement'], 128550: ['mild', 'sadness'], 128558: ['awe'], 128562: ['astonished'], 129393: ['yawn'], 129316: ['mouthwatering'], 128564: ['asleep'], 128554: ['snoring'], 128565: ['dizzy'], 128516: ['grinning'], 129296: ['stop', 'talking'], 129396: ['inebriated'], 129314: ['disgust'], 129326: ['vomit'], 129319: ['sneezing'], 128567: ['wear', 'a', 'mask'], 129298: ['fever'], 129301: ['injury'], 129297: ['feeling', 'rich'], 129312: ['cowboy'], 128520: ['evil', 'smile'], 128127: ['devilish'], 128121: ['ogre'], 128122: ['evil'], 129313: ['clown'], 128169: ['poop'], 128123: ['playful', 'ghost'], 128128: ['skull'], 9760: ['danger'], 128125: ['alien'], 129302: ['robot'], 127875: ['halloween'], 128570: ['grinning', 'cat'], 128568: ['smiling', 'cat'], 128569: ['laughing', 'cat'], 128571: ['loving', 'cat'], 128572: ['smirking', 'cat'], 128573: ['kissing', 'cat'], 128576: ['shocked', 'cat'], 128575: ['sad', 'cat'], 128574: ['angry', 'cat'], 128293: ['lit'], 127770: ['irony'], 10084: ['love'], 128155: ['friend'], 128148: ['devastated'], 128154: ['environment'], 128156: ['korean', 'love'], 128420: ['ironic', 'love'], 10083: ['excitement'], 128149: ['best', 'friend'], 128152: ['new', 'love'], 128157: ['gifting', 'my', 'heart'], 128583: ['bow'], 128584: ['blush'], 128586: ['said', 'something', 'wrong'], 127758: ['earth'], 128175: ['accurate'], 9996: ['victory'], 129310: ['fingers', 'crossed'], 128077: ['yes'], 128078: ['no'], 129309: ['handshake'], 128591: ['folded', 'hands'], 128139: ['kiss', 'mark'],128588: ['pride']}
emoji_list = [x for x in emojis.keys()]

def separate_emoji(tokens):
    for token in tokens:
        #Find the token which has the emoji
        current_token = tokens.index(token)
        unified = [ord(t) for t in token]
        if any(u in unified for u in emoji_list):
            #Find which is the emoji token
            separate = []
            word = ''
            for t in unified:
                if t in emoji_list:
                    #Check if we have a word before it. If yes, add to separate list
                    if word != '':
                        separate.append(word)
                        word = ''
                    separate.append(chr(t))
                elif t in range(65,123) or t in range(2304,2432) or t in range(48,58):
                    word += chr(t)
            if word != '':
                separate.append(word)
            tokens = tokens[:current_token] + separate + tokens[current_token + 1:]
        else:
            #Check if there is some other token appended to it
            word = ''
            for t in unified:
                if t in range(65,123) or t in range(2304,2432):
                    word += chr(t)
            tokens = tokens[:current_token] + [word] + tokens[current_token + 1:]
    return(tokens)
                    
def convert_emoji(tokens):
    for token in tokens:
        current_token = tokens.index(token)
        if len(token) == 1:
                if ord(token) in emoji_list:
                    tokens = tokens[:current_token] + emojis[ord(token)] + tokens[current_token + 1:]
    return(tokens)