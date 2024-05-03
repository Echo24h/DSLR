import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import load_csv


def ft_histogram(data: pd.DataFrame) -> None:
    """
    Generate a histogram of the data.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
    """
    for column in data.columns:
        values = [x for x in data[column].values if not pd.isnull(x)]
        if all(isinstance(x, (int, float, np.int64, np.float64)) for x in values):
            plt.figure()
            plt.hist(values, bins=20)
            plt.title(column)
            plt.show()


if __name__ == "__main__":
    data = load_csv("datasets/dataset_train.csv")
    ft_histogram(data)
