''' Kohls 
        ['span', 'class', "prod_price_amount red_color", False, 'Price']
        ['p' 'rel' "/product/", True, 'Name']
        url='https://www.kohls.com/search.jsp?submit-search=&search=clothes+for+men',
        requireSelenium=True,
        scrapeName='kohls',
        overRide=True,
        fullScrape=False

'''


''' Yahoo Finance    
        ['td', 'aria-label', 'Symbol', False, 'Symbol'], 
        ['td', 'aria-label', 'Name', False, 'Name'],
        ['td', 'aria-label', 'Price', True, 'Price'], 
        url='https://finance.yahoo.com/cryptocurrencies/',
        requireSelenium=False,
        scrapeName=crypto,
        overRide=True,
        fullScrape=True,
'''


''' Amazon
        ['span', 'class', 'a-size-base-plus a-color-base a-text-normal', True, 'Product'], 
        ['span', 'class', 'a-size-base-plus a-color-base', True, 'Brand'],
        ['span', 'class', 'a-offscreen', False, 'Price'],
        url = 'https://www.amazon.com/s?k=wallets+women&crid=3D5IPPH14Z552&sprefix=wallets+wome%2Caps%2C353&ref=nb_sb_noss_2',
        requireSelenium=True,
        scrapeName='amazon',
        overRide=True,
        fullScrape=True
 '''


''' HanziDb
        ['a', 'href', "/character/", True, 'Character'], 
        ['span', 'style', "color;", True, 'Pinyin'],
        ['span', 'class', "smmr", False, 'Definition'],
        url = 'http://hanzidb.org/character-list',
        requireSelenium=False,
        scrapeName='chinese',
        overRide=True,
        fullScrape=True
'''


''' Default
        [],
        [],
        [],
        url= 'https://scrape.com',
        requireSelenium=True,
        scrapeName='scrape',
        overRide=True,
        fullScrape=True
'''