from WordAnalyzer import WordAnalyzer as WA
import re

class SentenceAnalyzer:
    
    def __init__(self, wa, pos_file):
        print(pos_file.closed)
        self.wa = wa
        self.pos_dict = {}
        pos_text = pos_file.readlines()
        for text in pos_text:
            pos_split = text.split(":")
            word = pos_split[0]
            pos = pos_split[1].strip().split(",")
            self.pos_dict[word] = pos
        print(self.pos_dict)

    def analyze_sentence(self, sentence):
        return 0
    
    def analyze_sentences(self, sentences):
        return 0

    def decide_pos_manual(self, pos_list, word, sentence):
            print("Decide part of speech for [{0}] in the sentence: [{1}]".format(word, sentence))
            print(pos_list)
            print("Please enter the index number of the correct POS: ")
            index_number = input()
            return pos_list[int(index_number)]

    def analyze_text(self, sentences_file):
        sentences_pos = open('./resources/sentences_list','w+')
        sentences = sentences_file.readlines()
        for sentence in sentences:
            sentence = re.sub('[^a-zA-Z\d\s]', '', sentence.strip()) # Removing all punctuation
            new_sentence = sentence + ':'
            words = sentence.strip().split(" ")
            for word in words:
                pos_list = self.pos_dict[word.lower().strip()]
                new_sentence = new_sentence + (pos_list[0] + " " if  len(pos_list) == 1 else self.decide_pos_manual(pos_list, word, sentence) + " ")
            print("New sentence is: {0}".format(new_sentence))
            sentences_pos.write(new_sentence+"\n")
        sentences_pos.close()
        