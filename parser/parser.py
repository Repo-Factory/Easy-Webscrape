import requests


def getHTMLSelenium(driver):
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    return html


def getHTMLRequest(url):
    headers =   {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
                 'Content-Type:text/html; charset=utf-8'
                }    
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text

