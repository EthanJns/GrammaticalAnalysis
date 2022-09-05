from GrammarDriver import GrammarWebDriver as GWDriver
from selenium.webdriver.common.by import By
from resources.ConfigEnum import ConfigEnum as CE

def build_config():
    config_dict = {}
    config_file = open('./resources/config.txt', 'r')
    for line in config_file.readlines():
        key_value = line.split('=')
        if len(key_value) == 2:
            config_dict[key_value[0]] = key_value[1]
    return config_dict

gd = GWDriver()
word_list_file = open("./resources/wordlist.txt","r",encoding='latin1')
word_list = word_list_file.readlines()
# word_list_splice = word_list[0:600]

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

word_list_file.close() 
print("Finished")


