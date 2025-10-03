import pandas as pd
from pathlib import Path

def load_csv(path):
    # load a CSV file as a pandas DF
    return pd.read_csv(Path(path))

def save_csv(df, path):
    #save DF to CSV
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)