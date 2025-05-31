import pandas as pd

def loadMovies(path="data/CleanMovies.csv"):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print("Error loading the dataset from file!")
        return pd.DataFrame()