from GrammarDriver import GrammarWebDriver as GWDriver
from selenium.webdriver.common.by import By
import threading
from resources.ConfigEnum import ConfigEnum as CE

class WordAnalyzer:

# TODO:
    # For words that are in different forms, we need to grab the word inside this other class "cxt text-uppercase"
    # and then add or look that word up
    def __init__(self):
        self.gd = GWDriver()
        self.thread_locked = False


    def analyze_file_batch(self, word_list_file, pos_file):
        # word_list_file = open("./resources/10_common_english_sentences.txt","r",encoding='latin1')
        word_list = word_list_file.readlines()
        # Getting the parts of speech for words in batches in case of failure, can splice word list from last word
        batch_size = 100
        batch_number = 1
        thread_number = 5
        for i in range(0, len(word_list), batch_size*thread_number):
            pos_file = open("./resources/pos.txt","a+") if pos_file.closed else pos_file
            print(f"working on batches #{batch_number}-{batch_number+thread_number-1}")
            # In case of working with splices not divisible by 50, make sure no index out of bounds error is thrown
            threads = []
            word_to_pos = {}
            finished_threads = 0
            for t in range(thread_number):
                batch_begin = i + (t*batch_size)
                end_of_batch = i + ((1+t) * batch_size)
                splice_end = end_of_batch if (len(word_list) - end_of_batch) > batch_size else len(word_list) - i
                words = word_list[batch_begin : end_of_batch]
                threads.append(threading.Thread(target=self.gd.get_parts_of_speech, args=(words, word_to_pos)))
                threads[t].start()
            for t in threads:
                t.join()

            for word in word_to_pos:
                word_pos = word + ":"
                for pos in word_to_pos[word]:
                    word_pos += pos +","
                word_pos = word_pos[:-1] + "\n"
                if len(word_to_pos[word]) == 0:
                    continue
                pos_file.write(word_pos)
            
            pos_file.close()
            batch_number = batch_number + thread_number
        # pos_file.close()
        

    def analyze_single_word(self, word, pos_dict):
        self.gd.get_parts_of_speech([word],pos_dict)
        

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