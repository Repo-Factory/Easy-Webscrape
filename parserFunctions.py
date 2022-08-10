import bs4


def getSoup(responseText):
    soup = bs4.BeautifulSoup(responseText, 'lxml')
    return soup


def selectTags(soup, tag, attr, name, contains):
    if contains == True:
        tags = soup.select(f"{tag}[{attr}*='{name}']")
    if contains == False:
        tags = soup.select(f"{tag}[{attr}='{name}']")
    return tags


def getAllInnerText(listOfObjects):
    for object in listOfObjects:
        dirtyText = object.text
        cleanText = cleanWhiteSpace(dirtyText)
        yield cleanText


def cleanWhiteSpace(text):
    text = text.replace('\n', '')
    text = ' '.join(text.split())
    return text


def addCategoryNameToText(textObjects, columnName):
    for object in textObjects:
        dict = {}
        dict[columnName] = object
        yield dict


def getItemsTextByTags(soup, tag, attr, name, contains, columnName):
    tags = selectTags(soup=soup, tag=tag, attr=attr, name=name, contains=contains)
    text = getAllInnerText(tags)
    items = addCategoryNameToText(text, columnName)
    return items


def formatItems(items):
    for item in items:
        if items.index(item) % 2 == 0:
            items.pop(item)
    return items


def listGeneratorsText(soup, *args_list):
    generators = getAllTagTextGenerators(soup, *args_list)
    for generator in generators:
        i = 0
        for item in generator:
            print(f'{i}: {item}') 
            i += 1


# helper
def getAllTagTextGenerators(soup, *tagArrayArguments):
    for tagArrayArgument in tagArrayArguments:
        args_list = tagArrayArgument
        yield getItemsTextByTags(soup, *args_list)


def createZippedDataFrameFromTags(soup, *args_list):
    generators = getAllTagTextGenerators(soup, *args_list)
    generatorList = []
    for generator in generators:
        generatorList.append(generator)
    dataFrame = getZippedList(*generatorList)
    return dataFrame


# combines generators into zipped object
def getZippedList(*generators):
    zipped = zip(*generators)
    listZipped = list(zipped)
    for item in listZipped:
        yield(item)


# zip creates tuples of objects that don't translate well to JSON
def mergeZippedObjectDicts(zippedObject):
    listOfDictionaries = createListFromWrapperObject(zippedObject) # unwraps zipped generators 
    mergedDictionaries = mergeDictionariesInList(listOfDictionaries) # merges lists of zipped objects and returns generator
    listOfMergedDictionaries = createListFromWrapperObject(mergedDictionaries) # unwraps
    return listOfMergedDictionaries


# helper to unwrap generators
def createListFromWrapperObject(wrapperObject):
    JSONlist = []
    for item in wrapperObject:
        JSONlist.append(item)
    return JSONlist


def mergeDictionariesInList(listOfDictionaries): #listOfListOfDictionaries all rows in generator
    for dictionary in listOfDictionaries: # one row of dictionaries {}{}{}
        mergedDict = dict(merge_dicts(*dictionary))
        yield mergedDict


def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result





