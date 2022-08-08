from robot import instantiateDriver
from robotFunctions import *
from parser import getHTMLRequest, getHTMLSelenium
from parserFunctions import *
from dataFileHelper import writeToFile
from pprint import pprint

'''Creates Selenium Webdriver and passes HTML to parser'''


class ScraperSession:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ScraperSession, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.driver = None
        self.driverSession = None
    def startSeleniumWindow(self, url):
        self.driver = instantiateDriver()
        self.driverSession = self.driver.get(url)
    def getDriver(self):
        return self.driver
    def getHTML(self, url):
        if self.driverSession == None:
            html = getHTMLRequest(url)
        else:
            html = getHTMLSelenium(self.driver)
        soup = getSoup(html)
        return soup


scraperSession = ScraperSession()

# Yahoo Finance
# soup = scraperSession.getHTML('https://finance.yahoo.com/most-active')
# stocks = getObjectsByTag(soup, 'td')
# categories = filterInfoByAttribute(stocks, 'aria-label')
# info = getAllInnerText(stocks)
# data = zip(categories, info)
# data = list(data)
# json = createJsonWithDelimiter('Symbol', data)
# pprint(json)
# writeToFile(str(json), 'dataFile.txt')
# writeToFile(str(json), 'dataFile.json')

# Chinese
# soup = scraperSession.getHTML('http://hanzidb.org/character-list?page=2')
# characters = getItemsTextByTags(soup, 'tr')
# info = getAllInnerText(characters)
# for item in info:
#     print(item)


# Crypto

soup = scraperSession.getHTML('https://finance.yahoo.com/cryptocurrencies/')
# coins = getItemsTextByTags(soup, 'td', 'aria-label', 'Symbol', False)    
# names = getItemsTextByTags(soup, 'td', 'aria-label', 'Name', False)
# prices = getItemsTextByTags(soup, 'td', 'aria-label', 'Price', True)
# prices2 = getItemsTextByTags(soup, 'td', 'aria-label', 'Price', True)
# names2 = getItemsTextByTags(soup, 'td', 'aria-label', 'Name', False)
args_list = [   
                [soup, 'td', 'aria-label', 'Symbol', False], 
                [soup, 'td', 'aria-label', 'Price', True], 
                [soup, 'td', 'aria-label', 'Name', False]
            ]            

createDataFrameFromTags(soup, *args_list)

# whatWeKnowWeCanDo1 = getItemsTextByTags(*args_list[0])
# whatWeKnowWeCanDo2 = getItemsTextByTags(*args_list[1])
# whatWeKnowWeCanDo3 = getItemsTextByTags(*args_list[2])
# for arg in args_list:
#     whatWeKnowWeCanDo4 = getItemsTextByTags(*arg)
#     for item in whatWeKnowWeCanDo4:
#         print(item)

# dataFrameTest = getGeneratorsFromTags(*args_list)
# generator_args_list = []
# for generator in dataFrameTest:
#     generator_args_list.append(generator)

# # generatorList = [whatWeKnowWeCanDo1, whatWeKnowWeCanDo2, whatWeKnowWeCanDo3]

# # getZippedList(*generatorList)
# getZippedList(*generator_args_list)
