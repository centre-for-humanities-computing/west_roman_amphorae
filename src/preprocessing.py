"""
Functions for preprocessing data.
"""

import pandas as pd

def make_years_to_float(data: pd.DataFrame, year_cols: list) -> pd.DataFrame:
    """
    Converts year values to float.

    Args:
        data (pd.DataFrame): A pandas dataframe.
        date_cols (list): A list of strings referring to columns with year data.

    Returns:
        pd.DataFrame: An input dataframe with year values converted to float.
    """

    for col in year_cols:
        # if the year string contains "BCE" the year should be negative, otherwise positive
        data[col] = data[col].apply(lambda x: -float(x[:-4]) if "BCE" in x else float(x[:-3]))

    return data