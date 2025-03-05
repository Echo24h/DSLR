# DataScience x Logistic Regression Project

## Objective
This project focuses on exploring basic concepts in Data Science with an emphasis on Logistic Regression for classification problems. It will guide you through key steps in data exploration, cleaning, visualization, and model training. The goal is to implement a logistic regression model to solve a classification problem and develop a toolkit for Machine Learning tasks.

## Key Steps

### 1. Data Exploration and Cleaning
- **Data Inspection**: You will start by analyzing the provided dataset, identifying the types of data, their ranges, and potential inconsistencies.
- **Data Cleaning**: This phase involves cleaning the dataset by handling missing values, removing unnecessary information, and ensuring the data is ready for analysis.

### 2. Data Visualization
Visualization plays a crucial role in understanding the structure of your data and detecting anomalies. You will create various visualizations to gain insights into the dataset:
- **Histogram**: To determine which Hogwarts course has a homogeneous score distribution between the four houses.
- **Scatter Plot**: To identify features that are similar to each other.
- **Pair Plot**: To visualize relationships between different features and select which ones are relevant for logistic regression.

### 3. Logistic Regression
The core of the project is implementing a **Logistic Regression** model using the one-vs-all approach for multi-class classification:
- **Training the Model**: Using gradient descent to minimize the error, you will train the logistic regression model and save the weights.
- **Making Predictions**: Once the model is trained, you will use it to predict the Hogwarts House for test data.

### Mandatory Requirements
- **Data Analysis**: You will create a program to display basic statistics of the numerical features, avoiding the use of built-in functions like `describe()`, `count()`, or others that do the work for you.
  
- **Data Visualization Scripts**:
  - `histogram.extension`: Displays a histogram to identify the most homogeneous course in terms of score distribution.
  - `scatter_plot.extension`: Shows a scatter plot to find similar features.
  - `pair_plot.extension`: Displays a pair plot to help choose the most relevant features for logistic regression.

- **Logistic Regression Scripts**:
  - `logreg_train.extension`: Trains the logistic regression model using gradient descent and generates a file with the model's weights.
  - `logreg_predict.extension`: Uses the trained model to make predictions and creates a formatted output file with the predicted Hogwarts Houses.

## Final Deliverables
- **Trained Model**: A file containing the learned weights of the logistic regression model.
- **Prediction File**: A file with predicted Hogwarts Houses for the test dataset.

This project provides a hands-on experience in data cleaning, exploration, visualization, and machine learning model implementation with logistic regression, all essential skills for a data scientist.
