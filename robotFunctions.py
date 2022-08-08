from time import sleep
import pyclick
from selenium.webdriver.common.by import By


def injectScript(driver, injectString):
    response = driver.execute_script(injectString)
    return response


def getElementById(driver, ElementId):
    element = driver.find_element(By.ID, ElementId)
    return element


def getElementLocation(element):
    point = element.location
    return point


def getCoordinatesOfPoint(point):
    x = point[0]
    y = point[1]
    return [int(x), int(y)]


def fitCoordinatesToDisplay(x, y, width, height):
    xRatio = 2736/width 
    yRatio = 1824/height
    x *= xRatio
    y *= yRatio
    return [int(x), int(y)]


def pyClick(location):
    clicker = pyclick.HumanClicker()    
    clicker.move(location, 2)
    clicker.click()
