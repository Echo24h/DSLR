import pandas as pd
import matplotlib.pyplot as plt
from utils import load_csv


def ft_scatter_plot(data: pd.DataFrame) -> None:
    """
    Generate a scatter plot of the data.
    
    Args:
        data (pd.DataFrame): The DataFrame containing the data.
    """
    fig, axs = plt.subplots(4, 4, figsize=(20, 20))
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
    plt.subplots_adjust(hspace=0.7)
    plt.show()


if __name__ == "__main__":
    data = load_csv("datasets/dataset_train.csv")
    ft_scatter_plot(data)