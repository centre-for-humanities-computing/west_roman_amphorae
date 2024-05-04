"""""Functions for obtaining count and frequency values"""

import pandas as pd

from plot import create_series


def sum_freq_per_year(
    data: pd.DataFrame,
    sum_freq: str,
    lower_date: str,
    upper_date: str,
    freq_per_year: str = "Sum_freq_per_year",
) -> pd.DataFrame:
    """
    Calculates frequency per year per object.

    Args:
        data (pd.DataFrame): A pandas dataframe.
        sum_freq (str): A dataframe column containing summed frequency values per object type.
        lower_date (str): The name of the dataframe column containing start dates.
        upper_date (str): The name of the dataframe column containing end dates.
        freq_per_year (str): A dataframe column with resulting sum frequency values per year per object.
        The name of the column can be set up (by default = 'Sum_freq_per_year').

    Returns:
        pd.DataFrame: An input dataframe with a new column containg sum frequency values per year.
    """

    for row in range(len(data)):
        data[freq_per_year] = data[sum_freq] / (data[upper_date] - data[lower_date])
    return data


def year_freq_df(
    data: pd.DataFrame,
    lower_date: str,
    upper_date: str,
    sum_freq: str,
    name: str = "Frequency",
    index_name: str = "Year",
) -> pd.Series:
    """
    Creates a dataframe with years and the corresponding frequency values.

    Args:
        data (pd.DataFrame): A pandas dataframe.
        lower_date (str): A dataframe column containing start dates.
        upper_date (str): A dataframe column containing end dates.
        sum_freq (str): A dataframe column containing sum frequency values per year per object.
        name (str): The name of the output Series. Can be set up (by default = 'Frequency').
        index_name (str):  The name of the row of the output Series. Can be set up (by default = 'Year').

    Returns:
        pd.Series: A one-dimensional labeled array with sum frequncy values for each year in a given date range.
    """

    minimum = data[lower_date].min()
    maximum = data[upper_date].max()

    date_dict = dict.fromkeys(range(int(minimum), int(maximum)), 0)

    df = data.dropna(subset=[lower_date])
    df = df.dropna(subset=[upper_date])

    for row in range(len(df)):
        for year in range(
            df[lower_date].astype(int).iloc[row], df[upper_date].astype(int).iloc[row]
        ):
            date_dict[year] += df[sum_freq].iloc[row]

    return create_series(date_dict, name=name, index_name=index_name)


def year_object_count_df(
    data: pd.DataFrame,
    lower_date: str,
    upper_date: str,
    object_list: str,
    name: str = "Site count",
    index_name: str = "Year",
) -> pd.Series:
    """
    Creates a dataframe with years and the corresponding site count values.

     Args:
        data (pd.DataFrame): A pandas dataframe.
        lower_date (str): The name of the dataframe column containing start dates.
        upper_date (str): The name of the dataframe column containing end dates.
        object_list (str): the name of the dataframe column containing the list of f.ex., sites, provenances, etc
        name (str): The name of the output Series. Can be set up (by default = 'Site count').
        index_name (str): The name of the row of the output Series. Can be set up (by default = 'Year').

    Returns:
        pd.Series: A one-dimensional labeled array with years and site count values.
    """

    minimum = data[lower_date].min()
    maximum = data[upper_date].max()

    date_dict = dict.fromkeys(range(int(minimum), int(maximum)), 0)

    df = data.dropna(subset=[lower_date])
    df = df.dropna(subset=[upper_date])

    for year in date_dict:

        result_list = []

        for row in range(len(df)):
            if (
                df[lower_date].astype(int).iloc[row]
                <= year
                <= df[upper_date].astype(int).iloc[row]
            ):
                result_list.append(df[object_list].iloc[row])

        length = len(result_list)

        if length == 0:
            continue

        else:

            flat_list = [item for sublist in result_list for item in sublist]

            date_dict[year] = len(set(flat_list))

    return create_series(date_dict, name=name, index_name=index_name)
