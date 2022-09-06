from GrammarDriver import GrammarWebDriver as GWDriver
from selenium.webdriver.common.by import By
from resources.ConfigEnum import ConfigEnum as CE


class WordAnalyzer:

    def __init__(self):
        print("Instanciating Driver")
        self.gd = GWDriver()


    def analyze_file_batch(self, word_list_file, pos_file):
        # word_list_file = open("./resources/10_common_english_sentences.txt","r",encoding='latin1')
        word_list = word_list_file.readlines()
        # Getting the parts of speech for words in batches in case of failure, can splice word list from last word
        batch_size = 100
        batch_number = 1
        for i in range(0, len(word_list), batch_size):
            pos_file = open("./resources/pos.txt","a+")
            print(f"working on batch #{batch_number}")
            # In case of working with splices not divisible by 50, make sure no index out of bounds error is thrown
            splice_end = batch_size if (len(word_list) - i) > batch_size else len(word_list) - i
            words = word_list_splice[i:(i+splice_end)]
            word_to_pos = gd.get_parts_of_speech(words)

            # Iterate through the retrieved dictionary and store it in the file
            for word in word_to_pos:
                word_pos = word + ":"
                for pos in word_to_pos[word]:
                    word_pos += pos +","
                word_pos = word_pos[:-1] + "\n"
                pos_file.write(word_pos)
            pos_file.close()
            batch_number += 1

    def analyze_single_word(self, word):
        return self.gd.get_parts_of_speech(list(word))

    def analyze_words(self, words):
        return self.gd.get_parts_of_speech(words)


    def build_config():
        config_dict = {}
        config_file = open('./resources/config.txt', 'r')
        for line in config_file.readlines():
            key_value = line.split('=')
            if len(key_value) == 2:
                config_dict[key_value[0]] = key_value[1]
        return config_dict


