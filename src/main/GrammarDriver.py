import re
import requests
from resources.ConfigEnum import ConfigEnum as CE

class GrammarWebDriver:
    
    web_address = 'https://www.merriam-webster.com/dictionary/'

    # Regular expressions for parsing source code
    pos_regex = r'\"important-blue-link\"[\s]*href=[\"\/<>a-zA-Z]*</a>'
    contradiction_regex = r'[^a-zA-Z\d\s]+'
    mult_same_pos_regex = r'[\(\d\)]'
    
    def get_parts_of_speech(self, words):
        word_to_pos={}
        for word in words:
            word = word[:-1].lower() if word[len(word)-1] == '\n' else word.lower()
            resp = requests.get(self.web_address + word) #Figured this out by going through different words and seeing how the web address would change
            response_text = resp.text
            parts_of_speech = []
            pos_tags = re.findall(self.pos_regex, response_text)
            for pos_tag in pos_tags:
                pos = pos_tag.split('>')[1].split('<')[0]
                if re.search(self.mult_same_pos_regex, pos):
                    parts_of_speech.append(pos.split(" ")[0])    
                else:
                    parts_of_speech.append(pos)
            if re.search(self.contradiction_regex, word):
                parts_of_speech.append("contraction")
            word_to_pos[word] = list(set(parts_of_speech))
            # print(f"Added list to dict for word: {word}")
        
        return word_to_pos

