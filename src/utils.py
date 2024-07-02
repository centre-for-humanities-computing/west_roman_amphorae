""" Utility functions"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
from typing import List, Dict



def create_series(data: Dict[str, int], name: str, index_name: str) -> pd.Series:
    """
    Creates a one-dimensional labeled array.

    Args:
        date (Dict[str, int]): A dictionary with keys and values.
        name (str): The name of the Series.
        index_name (str): The name of the Series row.

    Returns:
        pd.Series: A one-dimensional labeled array.
    """

    data = pd.Series(data, name=name)
    data.index.name = index_name
    data.reset_index()

    return data



def dens_per_year(
    data: pd.DataFrame,
    type_dens: str,
    lower_date: str,
    upper_date: str,
    output_column: str = "density_per_year",
) -> pd.DataFrame:
    """
    Calculates density per year (density frequency) for each amphora type.

    Args:
        data (pd.DataFrame): A pandas dataframe.
        type_dens (str): A dataframe column containing density values for each amphora type (summed across sites).
        lower_date (str): The name of the dataframe column containing start dates.
        upper_date (str): The name of the dataframe column containing end dates.
        output_column (str): A dataframe column with resulting density values per year.
        The name of the column can be set up (default = 'density_per_year').

    Returns:
        pd.DataFrame: An input dataframe with a new column containg density per year (density frequency) for each amphora type.
    """

    data[output_column] = data[type_dens] / (data[upper_date] - data[lower_date])
    
    return data



def year_freq_series(
    data: pd.DataFrame,
    lower_date: str,
    upper_date: str,
    dens_per_year: str,
    name: str = "Frequency",
    index_name: str = "Year",
) -> pd.Series:
    """
    Creates a series with years as index and corresponding density frequency values summed across amphora types existing that year.

    Args:
        data (pd.DataFrame): A pandas dataframe.
        lower_date (str): A dataframe column containing start dates.
        upper_date (str): A dataframe column containing end dates.
        dens_per_year (str): A dataframe column containing density frequency values.
        name (str): The name of the output Series. Can be set up (by default = 'Frequency').
        index_name (str):  The name of the rows of the output Series. Can be set up (by default = 'Year').

    Returns:
        pd.Series: A one-dimensional labeled array with density frequency values summed across existing amphora types for each year.
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
            date_dict[year] += df[dens_per_year].iloc[row]

    return create_series(date_dict, name=name, index_name=index_name)



def year_site_count_series(
    data: pd.DataFrame,
    lower_date: str,
    upper_date: str,
    site_list: str,
    name: str = "Site count",
    index_name: str = "Year",
) -> pd.Series:
    """
    Creates a series with years as index and corresponding site count values.

     Args:
        data (pd.DataFrame): A pandas dataframe.
        lower_date (str): The name of the dataframe column containing start dates.
        upper_date (str): The name of the dataframe column containing end dates.
        site_list (str): the name of the dataframe column containing the list of sites
        name (str): The name of the output Series. Can be set up (by default = 'Site count').
        index_name (str): The name of the rows of the output Series. Can be set up (by default = 'Year').

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
                result_list.append(df[site_list].iloc[row])

        length = len(result_list)

        if length == 0:
            continue

        else:

            flat_list = [item for sublist in result_list for item in sublist]

            date_dict[year] = len(set(flat_list))

    return create_series(date_dict, name=name, index_name=index_name)



def year_type_count_series(
    data: pd.DataFrame,
    lower_date: str,
    upper_date: str,
    name: str = "Type count",
    index_name: str = "Year",
) -> pd.Series:
    """
    Creates a series with years as index and corresponding type count values.

     Args:
        data (pd.DataFrame): A pandas dataframe.
        lower_date (str): The name of the dataframe column containing start dates.
        upper_date (str): The name of the dataframe column containing end dates.
        name (str): The name of the output Series. Can be set up (by default = 'Type count').
        index_name (str): The name of the rows of the output Series. Can be set up (by default = 'Year').

    Returns:
        pd.Series: A one-dimensional labeled array with years and site count values.
    """

    minimum = data[lower_date].min()
    maximum = data[upper_date].max()

    date_dict = dict.fromkeys(range(int(minimum), int(maximum)), 0)

    df = data.dropna(subset=[lower_date])
    df = df.dropna(subset=[upper_date])

    for year in date_dict:

        counter = 0

        for row in range(len(df)):
            if (
                df[lower_date].astype(int).iloc[row]
                <= year
                <= df[upper_date].astype(int).iloc[row]
            ):
                counter += 1
        
        date_dict[year] = counter
    
    return create_series(date_dict, name=name, index_name=index_name)



def plot_graph(
    dict_w_series: Dict[str, pd.Series],
    ax,
    palette: List[str] = ["black", "green", "blue", "red", "orange", "purple", "pink", "lightblue", "limegreen", "grey", "orchid", "saddlebrown"],
    linewidth: int = 3,
    linestyle: str = "solid",
):
    """
    Plot line graphs.

    Args:
        dict_w_series (Dict[str, pd.Series]): A dictionary containing series.
        ax: Axes or array of Axes.
        palette (List[str]): A list with colour names for lines.
        linewidth (int): The width of a line.
        linestyle (str): The line style f.ex., 'solid' or 'dashed'.
    """

    for key, colour in zip(dict_w_series.keys(), palette):
        data = dict_w_series.get(key)
        sns.lineplot(
            data=data,
            ax=ax,
            label=key,
            color=colour,
            linewidth=linewidth,
            linestyle=linestyle,
        )



def plot_graph_w_jitter(
        dict_w_series: Dict[str, pd.Series],
        ax,
        palette: List[str] = ["black", "green", "blue", "red", "orange", "purple", "pink", "lightblue", "limegreen", "grey", "orchid", "saddlebrown"],
        jitter_bound: float = 0.05,
        linewidth: int = 3,
        linestyle: str = "solid",
):
    """
    Plot line graphs with a random tiny jitter to avoid overlapping.

    Args:
        dict_w_series (Dict[str, pd.Series]): A dictionary containing series.
        ax: Axes or array of Axes.
        palette (List[str]): A list with colour names for lines.
        jitter_bound (float): The bounds (-jitterbound, jitter_bound) of the uniform distribution from which the jitter is sampled.
        linewidth (int): The width of a line.
        linestyle (str): The line style f.ex., 'solid' or 'dashed'.
    """

    np.random.seed(0)

    for key, colour in zip(dict_w_series.keys(), palette):
        data = dict_w_series.get(key)
        jitter = np.random.uniform(-jitter_bound, jitter_bound, 1)
        data = data + jitter

        sns.lineplot(
            data=data,
            ax=ax,
            label=key,
            color=colour,
            linewidth=linewidth,
            linestyle=linestyle,
        )



def calculate_jitter_bound(dict_w_series: Dict[str, pd.Series]) -> float:
    """
    Calculate the jitter bound for the plot_graph_w_jitter function.

    Args:
        dict_w_series (Dict[str, pd.Series]): A dictionary containing series.

    Returns:
        float: The jitter bound.
    """

    max_value = max([max(dict_w_series[key]) for key in dict_w_series.keys()])

    return max_value * 0.03



def categorize_province(h1_province:str) -> str:
    """
    Function used for creating a column where provinces are categorized as West or East.
    """

    if h1_province in ["Italy", "Baetica", "Narbonense", "Lyonense", "Tarraconensis", "Africa"]:
        origin = "West"
    else:
        origin = "East"
    
    return origin



def categorize_region_east_west(h2_region:str) -> str:
    """
    Function used for creating a column where regions are categorized as West or East.
    """

    if h2_region in ["Campania", "Laietania", "Venetia", "Histra", "Coast Cadiz", "Guadalquivir", "Narbonense", "Lyonese", "Tarraconensis", "Africa"]:
        origin = "West"
    else:
        origin = "East"
    
    return origin



def categorize_region_lq_hq(h2_region:str) -> str:
    """
    Function used for creating a column where regions are categorized high or low quality.
    """

    if h2_region in ["Rhodes", "Campania", "Kos"]:
        quality = "High quality"
    else:
        quality = "Low quality"
    
    return quality

