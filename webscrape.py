import json
from data import JSONtoExcel
from robot import instantiateDriver
from robotFunctions import *
from parser import getHTMLRequest, getHTMLSelenium
from parserFunctions import *
from dataFileHelper import writeListToFile, writeToFile


'''Creates Selenium Webdriver and passes HTML to parser'''


class ScraperSession:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ScraperSession, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.driver = None
        self.driverSession = False
        self.url = None
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


def main():
    scraperSession = ScraperSession()
    scraperSession.startSeleniumWindow('https://www.amazon.com/s?i=fashion&bbn=23946842011&rh=n%3A7141123011%2Cn%3A23946842011%2Cn%3A7147441011%2Cp_n_specials_match%3A21213697011&s=featured-rank&hidden-keywords=-heated%2C+-earring+-pack%2C+-set&pd_rd_r=f43c0e0a-13af-492f-85e2-99d37646e935&pd_rd_w=MRBWr&pd_rd_wg=VhycN&pf_rd_p=5beb1ac4-4079-411b-89b5-f6d76eb082ef&pf_rd_r=GCAMEA8ETYPG79SFJKZ5&ref=pd_gw_unk')
    soup = scraperSession.getHTML(scraperSession.url)
    args_list = [   
                    [soup, 'span', 'class', 'a-size-base-plus a-color-base a-text-normal', True, 'Product'], 
                    [soup, 'span', 'class', 'a-size-base-plus a-color-base', True, 'Brand'],
                    [soup, 'span', 'class', 'a-price', False, 'Price'], 
                    
                ]            
    dataFrame = createDataFrameFromTags(soup, *args_list)
    dictionary = createListFromDataFrame(dataFrame)
    writeListToFile(dictionary, 'amazon.txt')
    JSON = json.dumps(dictionary)
    writeToFile(JSON, 'amazon.json')
    

main()



''' Yahoo Finance Crypto
    [soup, 'td', 'aria-label', 'Symbol', False, 'Symbol'], 
    [soup, 'td', 'aria-label', 'Name', False, 'Name'],
    [soup, 'td', 'aria-label', 'Price', True, 'Price'], 
'''