from GrammarDriver import GrammarWebDriver as GWDriver
from selenium.webdriver.common.by import By
import threading
from resources.ConfigEnum import ConfigEnum as CE
import time

class WordAnalyzer:

    def __init__(self):
        self.gd = GWDriver()
        self.thread_locked = False


    def analyze_file_batch(self, word_list_file, pos_file):
        # word_list_file = open("./resources/10_common_english_sentences.txt","r",encoding='latin1')
        word_list = word_list_file.readlines()
        # Getting the parts of speech for words in batches in case of failure, can splice word list from last word
        batch_size = 30
        batch_number = 1
        thread_number = 3
        for i in range(0, len(word_list), batch_size*thread_number):
            pos_file = open("./resources/pos.txt","a+") if pos_file.closed else pos_file
            print(f"working on batch #{batch_number}")
            # In case of working with splices not divisible by 50, make sure no index out of bounds error is thrown
            splice_end_t_1 = batch_size if (len(word_list) - i) > batch_size else len(word_list) - i
            splice_end_t_2 = (i+(2*batch_size)) if (len(word_list) - (i+batch_size)) > batch_size else len(word_list) - (i+batch_size)
            
            # print("spliced ending 1 = {0}".format(splice_end_t_1))
            # print("spliced ending 2 = {0}".format(splice_end_t_2))
            threads = []
            start = time.time()
            word_to_pos = {}
            for t in range(thread_number):
                batch_begin = i + (t*batch_size)
                end_of_batch = i + ((1+t) * batch_size)
                print("batch_begin {0}\nbatch_end {1}".format(batch_begin, end_of_batch))
                splice_end = end_of_batch if (len(word_list) - end_of_batch) > batch_size else len(word_list) - i
                words = word_list[batch_begin : end_of_batch]
                print(words)
                threads.append(threading.Thread(target=self.gd.get_parts_of_speech, args=(words, word_to_pos, t)))
                threads[t].start()
            for t in threads:
                t.join()
            
            # words_t_1 = word_list[i:(i+splice_end_t_1)]
            # words_t_2 = word_list[i+batch_size:((i+batch_size)+splice_end_t_2)]
            # t1 = threading.Thread(target=self.gd.get_parts_of_speech, args=(words_t_1, word_to_pos))
            # t2 = threading.Thread(target=self.gd.get_parts_of_speech, args=(words_t_2, word_to_pos))
            #  = self.gd.get_parts_of_speech(words)
            # start = time.time()
            # t1.start()
            # t2.start()
            # t1.join()
            # t2.join()
            end = time.time()
            total_time = end - start
            print(f"total time to finish 100 words was {total_time} seconds")
            print(f"meaning to process only 1000 words it would take us {(total_time*10)/60.00} minutes")
            print(f"So for 47000 words thats {((total_time*470)/60.00)} minutes")
            # print("length of dict is {0}".format(len(word_to_pos)))
            # Iterate through the retrieved dictionary and store it in the file
            for word in word_to_pos:
                # print("Word: {0}".format(word))
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


