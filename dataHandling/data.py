import pandas as pd

def JSONtoCSV(origin, destination):
    df_json = pd.read_json(origin)
    df_json.to_csv(destination, index=False)

