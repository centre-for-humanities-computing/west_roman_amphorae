"""Fucntions for creating series and ploting lines graphs"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
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


def plot_graph(
    dicts_of_df: Dict[str, pd.Series],
    ax,
    palette: List[str],
    linewidth: int = 3,
    linestyle: str = "solid",
):
    """
    Plot line graphs with information in different dataframes.

    Args:
        dicts_of_df (Dict[str, pd.Series]): A dictionary containing series.
        ax: Axes or array of Axes.
        palette (List[str]): A list with colours names for lines.
        linewidth (int): The width of a line.
        linestyle (str): The line style f.ex., 'solid' or 'dashed'.
    """

    for key, colour in zip(dicts_of_df.keys(), palette):
        data = dicts_of_df.get(key)
        sns.lineplot(
            data=data,
            ax=ax,
            label=key,
            color=colour,
            linewidth=linewidth,
            linestyle=linestyle,
        )
