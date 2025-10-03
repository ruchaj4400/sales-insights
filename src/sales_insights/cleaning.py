import pandas as pd

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Apply generic cleaning steps."""
    df = df.drop_duplicates()

    # Parse date columns (if column name looks like date)
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].str.strip()

    return df
