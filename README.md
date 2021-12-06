# Diamond_pricing
IronHack week 7 project / Kaggle_competition
# Pricing Diamonds with Machine Learning

![](https://c.tenor.com/z_VjWCffIRAAAAAC/spirited-away-coal.gif)


In this kaggle competition, we have to launch a diamond pricing tool that uses ML and statistical models to predict the price based on some features such as shape, color, clarity or carats. Once we train our algorithm, we must make a prediction on a test set and submit it to the kaggle competition.

## Workflow

In the Cleaning JN, we make some feature engineering, dropping features with high co-linearity and handling the categorical features (in this case, we assign numerical values).

In the Training JN, we make a train/test split of the Train dataset and try some different regression models. We choose a RandomForestRegressor, and optimize the hyperparameters with GridSearchCV. We fit this model with the whole Train dataset.

In the Predicting JN, we make a prediction for the prices of Test dataset, using the model of the previous JN.

## What is in this repo

In this repository you will find:

 - A readmi.md file with information about the project (this document).

 - A slide with the bulletpoints of this project
 
 - 3 Jupyter Notebooks, for cleaning the data and training the model with Train, and launching a prediction with Test.

 - A "Bonus" dataset with lateral thinking for trying different approaches.

 - A "DATA" folder with Train and Test datasets from kaggle.
 
  - A "src" folder with source code for cleaning dataframes, etc.
 
## Libraries

In this project we have used the following libraries:

 - [pandas](https://pandas.pydata.org/docs/)
 
 - [numpy](https://numpy.org/doc/)
 
 - [seaborn](https://seaborn.pydata.org/)

 - [scikit-learn](https://scikit-learn.org/stable/)
 
 - [pickle](https://docs.python.org/3/library/pickle.html/)

