from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = '/usr/bin/google-chrome'
# options.headless = True
# executable = "/mnt/c/Users/User/Documents/programming/Resources/chromedriver.exe"
driver = webdriver.Chrome(options=options, service=Service("/usr/bin/chromedriver"))

driver.get("https://www.google.com")
print(driver.find_elements(By.TAG_NAME,'head'))