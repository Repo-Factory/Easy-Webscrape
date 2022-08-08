def writeToFile(data, fileName):
    dataFile = open(fileName, 'a')
    dataFile.write(data)
    dataFile.close
    return print('Wrote to File')
