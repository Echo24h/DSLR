import pandas as pd
import numpy as np
import math
import sys
from utils import load_csv


def ft_mean(values: list) -> float:
    """
    Calculate the mean of a list of values.

    Args:
        values (list): The list of values to calculate the mean of.

    Returns:
        float: The mean of the values.
    """
    return sum(values) / len(values)


def ft_std(values: list) -> float:
    """
    Calculate the standard deviation of a list of values.

    Args:
        values (list): The list of values to calculate the standard deviation of.

    Returns:
        float: The standard deviation of the values.
    """
    mean = ft_mean(values)
    n = len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / n)


def ft_percentile(values: list, percentile: float) -> float:
    """
    Calculate the percentile of a list of values.

    Args:
        values (list): The list of values to calculate the percentile of.
        percentile (float): The percentile to calculate (0-100).

    Returns:
        float: The percentile of the values.
    """
    values.sort()
    index = (len(values) - 1) * percentile / 100
    lower = values[int(index)]
    upper = values[int(index) + 1]
    return lower + (upper - lower) * (index - int(index))


def ft_min(values: list) -> float:
    """
    Calculate the minimum value of a list of values.

    Args:
        values (list): The list of values to calculate the minimum of.

    Returns:
        float: The minimum value of the values.
    """
    min_value = float("inf")
    for value in values:
        if value < min_value:
            min_value = value
    return min_value


def ft_max(values: list) -> float:
    """
    Calculate the maximum value of a list of values.

    Args:
        values (list): The list of values to calculate the maximum of.

    Returns:
        float: The maximum value of the values.
    """
    max_value = float("-inf")
    for value in values:
        if value > max_value:
            max_value = value
    return max_value


def ft_describe(data: pd.DataFrame) -> pd.DataFrame:
    """
    Create a DataFrame with the following statistics for each column:
    - Count
    - Mean
    - Std
    - Min
    - 25%
    - 50%
    - 75%
    - Max

    Args:
        data (pd.DataFrame): The dataset to describe

    Returns:
        pd.DataFrame: A DataFrame with the statistics for each column
    """
    statistics = {}
    for column in data.columns:
        values = [x for x in data[column].values if not pd.isnull(x)]
        if all(isinstance(x, (int, float, np.int64, np.float64)) for x in values):
            statistics[column] = {
                "Count": len(values),
                "Mean": ft_mean(values),
                "Std": ft_std(values),
                "Min": ft_min(values),
                "25%": ft_percentile(values, 25),
                "50%": ft_percentile(values, 50),
                "75%": ft_percentile(values, 75),
                "Max": ft_max(values),
            }
    return pd.DataFrame(statistics)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python describe.py <file_path>")
        exit(1)
    data = load_csv(sys.argv[1])
    print(ft_describe(data))

    # For comparison
    # print(data.describe())
