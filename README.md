# dsml-projects
Repository for Data Science / Machine Learning (DSML) projects I did for fun, exploring different ideas and challenges.

## Motivation 
I wanted to do have a more structured repo for my DSML projects and playgrounds, besides just randomly throwing the jupyter notebooks into a repo.
By "structered" I mean that I have a list of projects that I want to do and all of them will explore different aspects of handling data.

The topics for each project will be different and the work will be stored in a jupyter notebook and the equivalent in R.

## Structure
This will change if something else comes to mind, but for now it is as follows:
1. Data Cleaning
    * 2 Projects - one in Python, one in R
    * Messy dataset
2. Data Scraping/Mining
    * One project in Python
    * Gather the dataset myself.
3. Data Exploration Through Vizualizations
    * 2 Projects - one in Python and one in R.
    * More geared towards data visiualizations.
4. End-to-End Project
    * Make a prediction system with a dynamic dataset pulled from an api or scraped.
5. Different Machine Learning Algorithm usecases and Project that come to mind.
    * I'll store all my Kaggle competition submissions.

## Comments on the project
1. Data_Cleaning
    * [Doing Business Indicators in the Balkans and availability of skilled workers [P]](https://github.com/gsam1/dsml-projects/blob/master/1_Data_Cleaning/1_DC_Python_Project.ipynb) - I think I've made a lot of mistakes in assuming things, but for the sake of fooling around with *real* data I will go on. In addition changing the dimensionality reduction technique from PCA to t-SNE broke my whole logic. Have to revisit it.
    * [Mobile Subscribers Penetration [R]](https://github.com/gsam1/dsml-projects/blob/master/1_Data_Cleaning/1_DC_R_Project.ipynb) - Although not a *classic* sense a cleaning data project - as no linking with other data sets was done I managed to answer the questions I wanted initially.
2. Data Acquisition
    * [Differences between Rotten Tomatoes' Tomatometer and Audience score - filtered by genre. [P]](https://github.com/gsam1/dsml-projects/blob/master/2_Data_Acquisition/1_DA_Python_Project.ipynb) - Settled on scraping the 'DVD and Streaming' section of Rotten Tomatoes, while crosschecking it with the genres in IMDB. The goal is to see the difference between the critic score and the viewer score by genre. I found relatively interesting the differences between critics and viewer scores for the genres, as well as what happened during the years.
3. Data Exploration Through Vizualizations
    * [Exploring Telco Customer Churn[P]](https://github.com/gsam1/dsml-projects/blob/master/3_Data_Storytelling/1_DS_Python.ipynb) - Chose to explore the 'Telco Customer Churn' and I created a profile for the customer that is most likely will leave.
    * [Google Play Store Twitter Sentiment Analysis[R]](https://github.com/gsam1/dsml-projects/blob/master/3_Data_Storytelling/1_DS_R.ipynb) - Looked into the relation between Google Play App installs and twitter sentiment.
4. End-to-End Project
5. Playground
    * Python - Various undertakings and playground with data.
        * [Housing Prices Kaggle Competition](https://github.com/gsam1/dsml-projects/blob/master/5_Playground/House_Prices_Advanced_Regression_Techniques.ipynb) - Submitted prediction results. Evaluated various regression techniques.
        * [Titanic: Machine Learning from Disaster](https://github.com/gsam1/dsml-projects/blob/master/5_Playground/Titanic_Machine_Learning_from_Disaster.ipynb) - Another Kaggle competition. This time for classification.
        * [CIFAR 10 Example](https://github.com/gsam1/dsml-projects/blob/master/5_Playground/CIFAR10_Example.ipynb) - Using a ConvNet trying to get accurate class predicitions for the items, contained in the famous [CIFAR 10](https://www.cs.toronto.edu/~kriz/cifar.html).
        * [Movie Genre Prediction by Poster](https://github.com/gsam1/dsml-projects/blob/master/5_Playground/Movie_Genre_Prediction_by_Poster.ipynb) -  Trying to predict a movie's genre by just looking at the poster.
        * [Obligatory MNIST](https://github.com/gsam1/dsml-projects/blob/master/5_Playground/Obligatory_MNIST.ipynb) - Obligatory in our time to at least have the MNIST dataset.
        * [TMDB Box Office Prediction](https://github.com/gsam1/dsml-projects/blob/master/5_Playground/TMDB_Box_Office_Prediction.ipynb) - Participating in the (TMDB Box Office Prediction Kaggle Competition.)[https://www.kaggle.com/c/tmdb-box-office-prediction]. Upper 50% last submit.