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
word_list_splice = word_list[0:50]
word_to_pos = gd.get_parts_of_speech(word_list_splice)
pos_file = open("./resources/pos.txt","w+")
for word in word_to_pos:
    # word:pos1,pos2,pos3
    word_pos = word + ":"
    for pos in word_to_pos[word]:
        word_pos += pos +","
    word_pos = word_pos[:-1] + "\n"
    pos_file.write(word_pos)
pos_file.close()
word_list_file.close() 


