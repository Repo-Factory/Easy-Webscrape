import bs4


def getSoup(responseText):
    soup = bs4.BeautifulSoup(responseText, 'lxml')
    return soup

# helper
def selectTags(soup, tag, attr, name, contains):
    if contains == True:
        tags = soup.select(f"{tag}[{attr}*='{name}']")
    if contains == False:
        tags = soup.select(f"{tag}[{attr}='{name}']")
    return tags

# helper
def getAllInnerText(listOfObjects, columnName):
    for object in listOfObjects:
        dict = {}
        dict[columnName] = object.text
        yield dict


def getItemsTextByTags(soup, tag, attr, name, contains):
    tags = selectTags(soup=soup, tag=tag, attr=attr, name=name, contains=contains)
    items = getAllInnerText(tags)
    return items


def getItemsTextByTagsInDict(soup, tag, attr, name, contains, columnName):
    tags = selectTags(soup=soup, tag=tag, attr=attr, name=name, contains=contains)
    items = getAllInnerText(tags, columnName)
    return items


# helper
def getGeneratorsFromTags(*tagArrayArguments):
    for tagArrayArgument in tagArrayArguments:
        args_list = tagArrayArgument
        yield getItemsTextByTagsInDict(*args_list)


def getZippedList(*generators):
    zipped = zip(*generators)
    listZipped = list(zipped)
    for item in listZipped:
        yield(item)


def createDataFrameFromTags(soup, *args_list):
    generators = getGeneratorsFromTags(*args_list)
    generatorList = []
    for generator in generators:
        generatorList.append(generator)
    dataFrame = getZippedList(*generatorList)
    return dataFrame


def createDictionaryFromDataFrame(dataFrame):
    i = 0
    dict = {}
    for item in dataFrame:
        dict[i] = item
        i+=1
    return dict


def createListFromDataFrame(dataFrame):
    JSONlist = []
    for item in dataFrame:
        JSONlist.append(item)
    return JSONlist
'''
args_list = {
                1: [soup, 'td', 'aria-label', 'Symbol', False], 
                2: [soup, 'td', 'aria-label', 'Price', True], 
                3: [soup, 'td', 'aria-label', 'Name', False]
            }
'''


'''
def getObjectsByClass(soup, tag, className):
    Objects = soup.findAll(lambda tag: tag.name == 'tag' and tag.get('class') == [className])
    return Objects 


def getObjectsByTag(soup, tag):
    Objects = soup.find_all(tag)
    return Objects


def filterInfoByAttribute(listOfObjects, attribute):
    for object in listOfObjects:
        yield object.attrs[attribute]


def getInnerTextForEachObject(listOfObjects):
    for object in listOfObjects:
        for segment in object.children:
            yield segment.text + '


def createJsonWithDelimiter(delimiter, list):
    i = 0
    dict = {}
    for item in list:
        if item[0] == delimiter:
            newList = []
            i+=1
        newList.append(item)
        dict[i] = newList
    return dict


def getAttributes(tags):
    for tag in tags:   
        for subTag in tag: 
            try: 
                yield subTag.attrs 
            except: 
                pass 


def produce_tags(parsed_html, tag_type, tag_attr, tag_name):
    needed_tags = parsed_html.findAll(lambda tag: tag.name == f'{tag_type}' and tag.get(f'{tag_attr}') == [f'{tag_name}'])
    for needed_tag in needed_tags:
        yield needed_tag.text
'''