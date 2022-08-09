import json
from data import JSONtoCSV

def writeToFile(data, fileName):
    dataFile = open(fileName, 'w', encoding='utf-8')
    dataFile.write('\n' + data)
    dataFile.close
    return print('Wrote to File')


def writeDictToFile(data, fileName):
    dataFile = open(fileName, "a", encoding='utf-8')
    dataFile.write("{\n")
    for k in data.keys():        
        dataFile.write(F"'{k}': '{data[k]}',\n")  # add comma at end of line
    dataFile.write("}\n\n")
    dataFile.close()
    return print('Wrote Dict to File')


def writeListToFile(data, fileName):
    dataFile = open(fileName, "a", encoding='utf-8')
    for line in data:
        dataFile.write(str(line))
        dataFile.write('\n')
    dataFile.close()
    return print('Wrote List to File')


def writeJSONstringByLine(data, fileName):
    dataFile = open(fileName, "a", encoding='utf-8')
    string_list = data.split(',')
    for string in string_list:
        dataFile.write(string + '\n')
        dataFile.close
    return print('Wrote JSON to File')


def writeToFiles(data):
    writeListToFile(data, 'dataFile.txt')
    JSON = json.dumps(data)
    writeToFile(JSON, 'dataFile.json')
    JSONtoCSV('dataFile.json', 'dataFile.csv')