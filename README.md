# Diamond_pricing
IronHack week 7 project / Kaggle_competition
# Pricing Diamonds with Machine Learning

![](https://c.tenor.com/z_VjWCffIRAAAAAC/spirited-away-coal.gif)


In this kaggle competition, we have to launch a diamond pricing tool that uses ML and statistical models to predict the price based on some features such as shape, color, clarity or carats. Once we train our algorithm, we must make a prediction on a test set and submit it to the kaggle competition.

## Workflow

First of all, we will propose an array of candidate locations across the US, based on clusterization of similar tech-companies based on the ZIP-code of their location. We shortlist them to 10 final candidates located in San Francisco, Silicon Valley, New York and Seattle.

Second, for each location, we create a database with the interesting venues for our client in a radius of 800m. Then we query to this database wich venues are located closer than 500m and build a total score according to a previous weight distribution. The final output is a total score and a map where the proposed location and near venues are displayed.

## What is in this repo

In this repository you will find:

 - A readmi.md file with information about the project (this document).

 - A slide with the bulletpoints of this project
 
 - 3 Jupyter Notebooks, for cleaning the data and training the model with Train, and launching a prediction with Test.
 
 - A "DATA" folder with Train and Test datasets from kaggle.
 
  - A "src" folder with source code for cleaning dataframes, etc.
 
## Libraries

In this project we have used the following libraries:

 - [pandas](https://pandas.pydata.org/docs/)
 
 - [numpy](https://numpy.org/doc/)
 
 - [seaborn](https://seaborn.pydata.org/)

 - [scikit-learn](https://scikit-learn.org/stable/)
 
 - [pickle](https://docs.python.org/3/library/pickle.html/)

