# Sentiment Prediction App Repository

- [Project Description](#project-description)
- [Repo structure](#repo-structure)
- [Running the application](#running-the-application)
  * [1. Set up environment](#1-set-up-environment)
    + [With `virtualenv` and `pip`](#with-virtualenv-and-pip)
    + [With `conda`](#with-conda)
  * [2. Download and upload data ](#2-download-and-upload-data)
  * [3. Train model ](#3-train-model)
  * [4. Run the application](#4-run-the-application)

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
├── data                              <- Folder that contains data used or generated. Place yelp_dataset folder here.
│
├── logs                              <- Directory holds logs created by logger files.
│
├── models                            <- Directory to save trained models and load afterwards
│
├── src                               <- Source data for the project 
│   ├── archive/                      <- No longer current scripts.
│   ├── helpers/                      <- Helper scripts used in main src files 
│   ├── train_model.py                <- Run script to train and save fasttext model.
│
├── run.py                            <- Run to start up flask app
├── requirements.txt                  <- Python package dependencies 
```
This project structure was partially influenced by the [Cookiecutter Data Science project](https://drivendata.github.io/cookiecutter-data-science/).

## Running the application
### 1. Setup Environment
Make sure to have virtualenv or conda installed.

Add a FLASK_KEY environmental variable with a password.
```bash
echo $FLASK_KEY='your_password'
```

#### With `virtualenv`
```bash
pip install virtualenv

virtualenv sentimentprediction

source sentimentprediction/bin/activate

pip install -r requirements.txt

```
#### With `conda`

```bash
conda create -n sentimentprediction python=3.7
conda activate sentimentprediction
pip install -r requirements.txt

```

### 2. Download and upload data

Download the yelp data set from: https://www.yelp.com/dataset/download.

Place the dataset in a folder called 'yelp_dataset' in the data folder.

### 3. Train model
Run the following command from the projects home directory.
```bash
python src/train_model.py
```

### 4. Run the application
Run the following command from the projects home directory.
```bash
python run.py
```