from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


'''Creates Selenium Webdriver and passes HTML to parser'''

def instantiateDriver():
    options = Options()
    agent = UserAgent()
    userAgent = agent.random
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\Conner\\chromedriver.exe")
    return driver



