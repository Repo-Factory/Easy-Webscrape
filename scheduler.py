import schedule
from webscrape import scrape


schedule.every().day.at("15:14").do(lambda: scrape  (
                                                    ['td', 'aria-label', 'Symbol', False, 'Symbol'], 
                                                    ['td', 'aria-label', 'Name', False, 'Name'],
                                                    ['td', 'aria-label', 'Price', True, 'Price'], 
                                                    url='https://finance.yahoo.com/cryptocurrencies/',
                                                    requireSelenium=False,
                                                    scrapeName='crypto',
                                                    overRide=False,
                                                    fullScrape=True,
                                                    ))


while True:
    schedule.run_pending()
