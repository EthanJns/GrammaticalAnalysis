from WordAnalyzer import WordAnalyzer as WA

class SentenceAnalyzer:
    
    def __init__(self, wa, pos_file):
        self.wa = wa
        self.pos_dict = {}
        pos_text = pos_file.readlines()
        for text in pos_text:
            #print(text)
            pos_split = text.split(":")
            self.pos_dict[pos_split[0]] = pos_split[1][:-1]
            
        print(self.pos_dict)

    def analyze_sentence(self, sentence):
        return 0
    
    def analyze_sentences(self, sentences):
        return 0

    def analyze_text(self, sentences_file):
        sentences_pos = open('./resources/sentences_list','w+')
        sentences = sentences_file.readlines()
        for sentence in sentences:
            print(sentence)
            new_sentence = sentence.strip() + ' : '
            for word in sentence.strip().split(" "):
                new_sentence = new_sentence + self.pos_dict[word.lower().strip()]+" "
            sentences_pos.write(new_sentence+"\n")
        sentences_pos.close()

        return 0