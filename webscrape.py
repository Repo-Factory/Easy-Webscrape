from robot.robot import instantiateDriver
from robot.robotFunctions import *
from parser.parser import getHTMLRequest, getHTMLSelenium
from parser.parserFunctions import *
from dataHandling.dataFileHelper import writeToFiles
from configurations.formatConfigurations import *


'''Creates Selenium Webdriver and passes HTML to parser'''


class ScraperSession:
    def __new__(cls, url, requireSelenium):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ScraperSession, cls).__new__(cls)
        return cls.instance
    def __init__(self, url, requireSelenium):
        self.driver = None
        self.driverSession = False
        self.url = url
        self.requiresSelenium = requireSelenium
    def startSeleniumWindow(self, url):
        self.url = url
        self.driver = instantiateDriver()
        self.driverSession = True
        self.driver.get(url)
    def getDriver(self):
        return self.driver
    def getHTML(self, url):
        if self.driverSession == False:
            html = getHTMLRequest(url)
        else:
            html = getHTMLSelenium(self.driver)
        soup = getSoup(html)
        return soup


def scrape(*args_list, url, requireSelenium, scrapeName, overRide, fullScrape):
    scraperSession = ScraperSession(url, requireSelenium)
    if scraperSession.requiresSelenium == True:
         scraperSession.startSeleniumWindow(url)
    soup = scraperSession.getHTML(url)
    if fullScrape == True:
        dataFrame = createZippedDataFrameFromTags(soup, *args_list) # returns zipped generators built from tags (has all text of tag type)
        formattedDataFrame = mergeZippedObjectDicts(dataFrame)
        writeToFiles(formattedDataFrame, scrapeName, overRide)
    else:
        listGeneratorsText(soup, *args_list)


scrape(        
        ['a', 'href', "/character/", True, 'Character'], 
        ['span', 'style', "color;", True, 'Pinyin'],
        ['span', 'class', "smmr", False, 'Definition'],
        url = 'http://hanzidb.org/character-list',
        requireSelenium=False,
        scrapeName='chinese',
        overRide=True,
        fullScrape=True
      )


