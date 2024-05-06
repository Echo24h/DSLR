import pandas as pd
import matplotlib.pyplot as plt
from utils import load_csv
import numpy as np


def ft_pair_plot(data: pd.DataFrame) -> None:
    """
    Generate a pair plot of the data.
    
    Args:
        data (pd.DataFrame): The DataFrame containing the data.
    """
    # Création d'un pair plot (scatter plot matrix)
    fig, axs = plt.subplots(8, 8, figsize=(10, 10))
    for i, column1 in enumerate(data.columns):
        for j, column2 in enumerate(data.columns):
            if i != j:
                values1 = [x for x in data[column1].values if not pd.isnull(x)]
                values2 = [x for x in data[column2].values if not pd.isnull(x)]
                if all(isinstance(x, (int, float)) for x in values1) and all(isinstance(x, (int, float)) for x in values2):
                    axs[i, j].scatter(values1, values2, alpha=0.5)
                    axs[i, j].set_title(f"{column1} vs {column2}")
                    axs[i, j].set_xlabel(column1)
                    axs[i, j].set_ylabel(column2)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data = load_csv("datasets/dataset_train.csv")
    ft_pair_plot(data)