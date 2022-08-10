from robot.robot import instantiateDriver
from robot.robotFunctions import *
from parser.parser import getHTMLRequest, getHTMLSelenium
from parser.parserFunctions import *
from dataHandling.dataFileHelper import writeToFiles
from configurations.formatConfigurations import *


class ScraperSession:

    """
    ScraperSession is a Singleton Class that Facilitates the Actual Scraping of Information From the Site
    Passes Collected Info/HTML to the parsing functions
    """

    def __new__(cls, requireSelenium):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ScraperSession, cls).__new__(cls)
        return cls.instance
    def __init__(self, requireSelenium):
        self.driver = None
        self.driverSession = False
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
    
    """
    Web scrape function takes in tags and certain configuration parameters to aid in webscraping and produce an excel 
    sheet with the desired information, each tag type will be its own column
    

    *args_list - any number of tags to scrape from the front end formatted as:
             ['tag', 'attr_key', "attr_value", contains, 'columnName']
    tag - type of tag to scrape (span, div, href)
    attr_key - can be any attribute like 'class' or 'aria_label'
    attr_value - will be corresponding value for example class='product': attr_value = 'product'
    contains - Mark true if you want any tag that continas the attr_value, false if the tag must be the exact attr_value
    columnName - Indicate how you want the column to show up in excel

    url - url of website to be scraped
    requireSelenium - if site doesn't freely allow scraping you'll have to start selenium session and come up with a method
    to get past measures put in place, sometimes going through a browser in and of itself is sufficient
    overRide - the scrape will output information to a json, csv, and txt file. If you want to do continued scrapes and 
    preserve all information, set this parameter to False. If True, will create a fresh document
    fullScrape - It's a good idea to scrape the HTML and see how the tags come out before creating a potentially useless file
    set fullScrape to False to do a test run which prints how the tags will be output

    Examples of args can be seen in configurations/argConfigurations output can be seen in dataFiles folder
    """

    scraperSession = ScraperSession(requireSelenium)
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
        ['td', 'aria-label', 'Symbol', False, 'Symbol'], 
        ['td', 'aria-label', 'Name', False, 'Name'],
        ['td', 'aria-label', 'Price', True, 'Price'], 
        url='https://finance.yahoo.com/cryptocurrencies/',
        requireSelenium=False,
        scrapeName='crypto',
        overRide=True,
        fullScrape=True,
     )


