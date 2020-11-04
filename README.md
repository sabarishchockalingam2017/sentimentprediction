# Sentiment Prediction App Repository

- [Project Description](#project-description)
- [Repo structure](#repo-structure)
- [Running the application](#running-the-application)
  * [1. Set up environment](#1-set-up-environment)
    + [With `virtualenv` and `pip`](#with-virtualenv-and-pip)
    + [With `conda`](#with-conda)
  * [2. Configure Flask app](#2-configure-flask-app)
  * [3. Initialize the database](#3-initialize-the-database)
  * [4. Download and upload data ](#4-download-and-upload-data)
  * [5. Run the application](#5-run-the-application)

## Project Description
This sentiment prediction app was created to predict the general emotional tone of a given text.

## Repo structure 

```
├── README.md                         <- You are here
│
├── app
│   ├── helpers/                      <- Helper files used by app
│       ├── prediction_handler.py     <- Functions used to load model and output prediction rating
│   ├── static/                       <- CSS, JS files that remain static
│       ├── main.css                  <- CSS formatting parameters for app
│   ├── templates/                    <- HTML (or other code) that is templated and changes based on a set of inputs
│       ├── about.html                <- About page of web app giving brief description
│       ├── dataset.html              <- Dataset description page
│       ├── home.html                 <- Main page with app
│       ├── layout.html               <- Base layout followed by all other pages
│       ├── model.html                <- Page explaining model
│   ├── app.py                        <- Flask app's main .py file
│   ├── forms.py                      <- Form objects for wtforms and Flaskforms packages
│   ├── Proc                          <- File to be used for cloud deployment to use gunicorn server 
│
├── config                            <- Directory for configurations files (yaml, py, conf, etc.) to control app and set parameters
│   ├── logging/                      <- Configuration files for python loggers
│   ├── flask_config.py               <- Settings for flask app
│   ├── main_config.py                <- Settings for other items such as model storage directory and data directory
│
├── data                              <- Folder that contains data used or generated. Only the external/ and sample/ subdirectories are tracked by git. 
│   ├── archive/                      <- Place to put archive data is no longer usabled. Not synced with git. 
│   ├── external/                     <- External data sources, will be synced with git
│   ├── sample/                       <- Sample data used for code development and testing, will be synced with git
│
├── docs                              <- A default Sphinx project; see sphinx-doc.org for details.
│
├── figures                           <- Generated graphics and figures to be used in reporting.
│
├── models                            <- Trained model objects (TMOs), model predictions, and/or model summaries
│   ├── archive                       <- No longer current models. This directory is included in the .gitignore and is not tracked by git
│
├── notebooks
│   ├── develop                       <- Current notebooks being used in development.
│   ├── deliver                       <- Notebooks shared with others. 
│   ├── archive                       <- Develop notebooks no longer being used.
│   ├── template.ipynb                <- Template notebook for analysis with useful imports and helper functions. 
│
├── src                               <- Source data for the project 
│   ├── archive/                      <- No longer current scripts.
│   ├── helpers/                      <- Helper scripts used in main src files 
│   ├── sql/                          <- SQL source code
│   ├── add_songs.py                  <- Script for creating a (temporary) MySQL database and adding songs to it 
│   ├── ingest_data.py                <- Script for ingesting data from different sources 
│   ├── generate_features.py          <- Script for cleaning and transforming data and generating features used for use in training and scoring.
│   ├── train_model.py                <- Script for training machine learning model(s)
│   ├── score_model.py                <- Script for scoring new predictions using a trained model.
│   ├── postprocess.py                <- Script for postprocessing predictions and model results
│   ├── evaluate_model.py             <- Script for evaluating model performance 
│
├── test                              <- Files necessary for running model tests (see documentation below) 

├── run.py                            <- Simplifies the execution of one or more of the src scripts 
├── app.py                            <- Flask wrapper for running the model 
├── config.py                         <- Configuration file for Flask app
├── requirements.txt                  <- Python package dependencies 
```
This project structure was partially influenced by the [Cookiecutter Data Science project](https://drivendata.github.io/cookiecutter-data-science/).

## Running the application

