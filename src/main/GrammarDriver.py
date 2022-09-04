
import requests
from resources.ConfigEnum import ConfigEnum as CE

class GrammarWebDriver:
    
    web_address = 'https://www.merriam-webster.com/dictionary/'
    class_name = 'important-blue-link' #Retrieved this by going through websites source code    

    def get_parts_of_speech(self, words):
        word_to_pos={}
        for word in words:
            resp = requests.get(self.web_address + word) #Figured this out by going through different words and seeing how the web address would change
            response_text = resp.text
            parts_of_speech = []
            all_instances = response_text.split(self.class_name)
            for i in range(len(all_instances)-1):
                a_tag = all_instances[i+1].split("</a>")
                i = i+1
                pos_split = a_tag[0]
                parts_of_speech.append(a_tag[0].split("</span")[0][1:].split(">")[1])
            word_to_pos[word] = parts_of_speech
        
        return word_to_pos

