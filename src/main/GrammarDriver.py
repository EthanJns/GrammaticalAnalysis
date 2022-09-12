import re
import requests
from resources.ConfigEnum import ConfigEnum as CE

class GrammarWebDriver:
    
    web_address = 'https://www.merriam-webster.com/dictionary/'
    # Regular expressions for parsing source code
    pos_regex = r'\"important-blue-link\"[\s]*href=[\"\/<>a-zA-Z\s]*</a>'
    contradiction_regex = r'[^a-zA-Z\d\s]+'
    mult_same_pos_regex = r'[\(\d\)]'
    is_of_form = r'\"cxt text-uppercase\">[\sa-zA-Z]*</a>*'
    useable_pos = set(['noun', 'adjective', 'adverb', 'verb', 'pronoun', 'preposition', 'article', 'conjunction'])
    

    def get_pos_tags_andor_form(self, word):
        resp = requests.get(self.web_address + word) #Figured this out by going through different words and seeing how the web address would change
        other_form = None
        response_text = resp.text
        has_other_form = re.search(self.is_of_form, response_text)
        if has_other_form:
            other_form = re.findall(self.is_of_form, response_text)[0].split('>')[1].split('<')[0]
        pos_tags = re.findall(self.pos_regex, response_text)
        return pos_tags, other_form

    def get_parts_of_speech(self, words, word_to_pos, t):
        if len(words) == 0:
            return
        for word in words:
            parts_of_speech = []
            word = word[:-1].lower() if word[len(word)-1] == '\n' else word.lower()
            pos_tags, other_form = self.get_pos_tags_andor_form(word)

            for pos_tag in pos_tags:
                pos = pos_tag.split('>')[1].split('<')[0]
                if len(pos.split(' ')) > 1:
                    for part in pos.split(' '):
                        if part.lower() in self.useable_pos:
                            pos = part.lower()
                if re.search(self.mult_same_pos_regex, pos):
                    parts_of_speech.append(pos.split(" ")[0])    
                else:
                    if pos in self.useable_pos:
                        parts_of_speech.append(pos)
                    else:
                        print(pos +" is not in the set")

            if re.search(self.contradiction_regex, word):
                parts_of_speech.append("contraction")

            other_forms_set = self.get_other_form_pos(other_form, word_to_pos) if other_form is not None else set()
            word_to_pos[word] = list(set(parts_of_speech).union(other_forms_set))

    def get_other_form_pos(self, other_form, word_to_pos):
        if other_form in word_to_pos:
            return set(word_to_pos[other_form])
        else:
            pos_tags, other_form = self.get_pos_tags_andor_form(other_form)
            if other_form is not None:
                return self.get_other_form_pos(other_form, word_to_pos)
            else:
                parts_of_speech = []
                for pos_tag in pos_tags:
                    pos = pos_tag.split('>')[1].split('<')[0]
                    if re.search(self.mult_same_pos_regex, pos):
                        parts_of_speech.append(pos.split(" ")[0])    
                    else:
                        parts_of_speech.append(pos)

                if other_form is not None and re.search(self.contradiction_regex, other_form):
                    parts_of_speech.append("contraction")
                if other_form is not None:
                    word_to_pos[other_form] = list(set(parts_of_speech))
                return set(parts_of_speech)


