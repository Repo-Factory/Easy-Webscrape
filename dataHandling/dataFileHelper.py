import json
from .data import JSONtoCSV


def openFile(fileName, overRide):
    if overRide == True:
        dataFile = open(fileName, 'w', encoding='utf-8')
    else:
        dataFile = open(fileName, 'a', encoding='utf-8')
    return dataFile


def writeToFile(data, fileName, overRide):
    dataFile = openFile(fileName, overRide)
    dataFile.write('\n' + data)
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
    writeToFileFormatted(data, f'.\\dataFiles\\{scrapeName}.txt', overRide)
    JSON = json.dumps(data)
    writeToFile(JSON, f'.\\dataFiles\\{scrapeName}.json', overRide)
    JSONtoCSV(f'.\\dataFiles\\{scrapeName}.json', f'.\\dataFiles\\{scrapeName}.csv')

