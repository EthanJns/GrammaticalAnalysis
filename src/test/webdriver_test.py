from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from resources.ConfigEnum import ConfigEnum as CE


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

#For the following demonstration, we will be attempting to get the parts of speech for the words "the, contract, is, long"
web_address = 'https://www.merriam-webster.com/dictionary/'
class_name = 'important-blue-link' #Retrieved this by going through websites source code

word_list = ['the', 'contract', 'is', 'long']

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

