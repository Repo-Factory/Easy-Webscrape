import pandas as pd

def JSONtoExcel(origin, destination):
    df_json = pd.read_json('dataFile.json')
    df_json.to_csv('dataFile.csv', index=False)
    df_json.to_json('newJSON.json')
    df_json.to_excel('dataFile.xlsx', index=False)

JSONtoExcel('','')