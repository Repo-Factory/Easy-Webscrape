class Settings():
    scrapeSiteURL = 'https://finance.yahoo.com/most-active/'
    requiresSelenium = False
    requiresParse = True
    

class parserSettings():
    parseTags = {'tag_type': 'a',
                 'tag_attr': 'class',
                 'tag_name': 'Fw(600) C($linkColor)'}
    
    
class robotSettings():
    requiresCaptcha = 'true'
    injectScripts = ['''
    
    ''']
    requiresLocateElement = 'false'