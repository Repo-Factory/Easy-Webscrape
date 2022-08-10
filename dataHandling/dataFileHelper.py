import json
from .data import JSONtoCSV


def openFile(fileName, overRide):
    if overRide == True:
        dataFile = open(fileName, 'w', encoding='utf-8')
    else:
        dataFile = open(fileName, 'a', encoding='utf-8')
    return dataFile


def writeToJSONFile(data, fileName, overRide):
    dataFile = open(fileName, 'w', encoding='utf-8')
    dataFile.write(data)
    dataFile.close
    return print(f'Wrote to File {fileName}')


def writeToFileFormatted(data, fileName, overRide):
    dataFile = openFile(fileName, overRide)
    dataFile.write('\n')
    for line in data:
        dataFile.write(str(line))
        dataFile.write('\n')
    dataFile.close()
    return print(f'Wrote Formatted Text to File {fileName}')


def writeToFiles(data, scrapeName, overRide):
    JSON = json.dumps(data)
    writeToJSONFile(JSON, f'.\\dataFiles\\{scrapeName}.json', overRide)
    writeToFileFormatted(data, f'.\\dataFiles\\{scrapeName}.txt', overRide)
    JSONtoCSV(f'.\\dataFiles\\{scrapeName}.json', f'.\\dataFiles\\{scrapeName}.csv')

