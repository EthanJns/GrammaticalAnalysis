from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from resources.ConfigEnum import ConfigEnum as CE
import time
import requests


#Below is code uses to build our config which will be used to take user system specific information to use as needed
def build_config():
    config_dict = {}
    config_file = open('./resources/config.txt', 'r')
    for line in config_file.readlines():
        key_value = line.split('=')
        if len(key_value) == 2:
            config_dict[key_value[0]] = key_value[1]
    return config_dict


config_dict = build_config()

#Instanciating web driver, the tool we will use to scrape the internet ----------------
options = Options()
options.binary_location = config_dict[CE.CHROME_LOCATION].strip()
options.headless = True
service_location = config_dict[CE.CHROME_DRIVER_LOCATION].strip()
driver = webdriver.Chrome(options=options, service=Service(service_location))
#--------------------------------------------------------------------------------------

#For the following demonstration, we will be attempting to get the parts of speech for the words in the list
web_address = 'https://www.merriam-webster.com/dictionary/'
class_name = 'important-blue-link' #Retrieved this by going through websites source code

word_list = ['the', 'contract', 'is', 'long', 'and', 'boring', 'but', 'we', 'must', 'read']

start = time.time()
for word in word_list:
    driver.get(web_address + word) #Figured this out by going through different words and seeing how the web address would change
    parts_of_speech = []
    parts_of_speech_elements = driver.find_elements(By.CLASS_NAME, class_name) #Words can have more than one part of speech, so we want to make sure we get all of them
    for element in parts_of_speech_elements:
        parts_of_speech.append(element.text)

    print("---------WORD--------")
    print(word)
    print("---------POS---------")
    print(parts_of_speech)
    print("----------------------\n")
end = time.time()
total_time = end - start
print(f"total time to finish 10 words was {total_time} seconds")
print(f"meaning to process only 1000 words it would take us {(total_time*100)/60.00} minutes")
print(f"Or thats {((total_time*100)/60.00)/60.00} hours")
print(f"therefore to process the whole list of 47000 words, it would take approximately {((total_time*4700.00)/60)/1440.00} days")

print('\n-------------------------------------------------\n Now how about only using GET requests rather than using the webdriver get method\n')

start = time.time()
for word in word_list:
    resp = requests.get(web_address + word) #Figured this out by going through different words and seeing how the web address would change
    response_text = resp.text
    parts_of_speech = []
    all_instances = response_text.split("important-blue-link")
    for i in range(len(all_instances)-1):
        a_tag = all_instances[i+1].split("</a>")
        i = i+1
        pos_split = a_tag[0]
        parts_of_speech.append(a_tag[0].split("</span")[0][1:].split(">")[1])

    print("---------WORD--------")
    print(word)
    print("---------POS---------")
    print(parts_of_speech)
    print("----------------------\n")
end = time.time()
total_time = end - start
print(f"total time to finish 10 words was {total_time} seconds")
print(f"meaning to process only 1000 words it would take us {(total_time*100)/60.00} minutes")
print(f"So for 47000 words thats {((total_time*4700)/60.00)/60.00} hours")


