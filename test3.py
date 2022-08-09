from collections import ChainMap

symbol = {"Symbol": "BTC-USD"}                      
name =  {"Name": "Bitcoin USD"}
prices = {"Price": "100"}
symbol1 = {"Name": "ETH"}
name2 = {"Name": "Ethereum"}
prices2 = {"Price": "200"}
list1 = [name,prices,symbol]
list2 = [name2,prices2,symbol1] 
outerList = [list1,list2]


def mergeDictionariesInList(listOfDictionaries): #listOfListOfDictionaries all rows in generator
    for dictionary in listOfDictionaries: # one row of dictionaries {}{}{}
        mergedDict = dict(ChainMap(*dictionary))
        yield mergedDict


generator = mergeDictionariesInList(outerList)
for item in generator:
    print(item)