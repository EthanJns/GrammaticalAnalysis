from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from resources.ConfigEnum import ConfigEnum as CE

class GrammarWebDriver:
    
    def __init__(self, config_dict):
        
        options = Options()
        options.binary_location = config_dict[CE.CHROME_LOCATION].strip()
        # options.headless = True
        service_location = config_dict[CE.CHROME_DRIVER_LOCATION].strip()

        self.driver = webdriver.Chrome(options=options, service=Service(service_location))

    def get_driver(self):
        return self.driver