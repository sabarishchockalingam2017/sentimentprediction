import pandas as pd
import json
from nltk.tokenize import word_tokenize
import string
from config.main_config import PROJECT_HOME
from os import path
import os
import csv
import logging
import logging.config

logger = logging.getLogger('helper.data_processing')

'''Functions to assist with processing files and bring their content into python.'''

def jsontodf(file_path,n_lines=5000):
    json_content = []
    with open(file_path, mode='r', encoding='utf8') as tempfile:
        for i in range(n_lines):
            json_content.append(json.loads(tempfile.readline()))
    logger.info("Data loaded from json to dataframe.")
    return pd.DataFrame(json_content)


def normalize_corpus(original_corpus):
    """ Function to normalize corpus to be input into NLP model.
    Parameters:
        original_corpus (list): contains original text that will be normalized.

    Returns:
        normalized_corpus (Pandas Series): original corpus normalized.
    """
    # lowercasing
    original_corpus = pd.Series(original_corpus)
    normalized_corpus = original_corpus.apply(lambda x: x.lower())

    # tokenizing
    normalized_corpus = normalized_corpus.apply(word_tokenize)

    # removing stopwords
    #from nltk.corpus import stopwords
    #set(stopwords.words('english'))
    sw_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
               'you', "you're", "you've", "you'll", "you'd", 'your', 'yours',
               'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
               "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
               'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
               'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
               'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
               'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
               'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with',
               'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
               'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
               'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
               'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
               'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
               's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now',
               'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
               'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
               "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn',
               "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
               'won', "won't", 'wouldn', "wouldn't"]

    # punctuation translation table to remove punctuation
    transtable = str.maketrans('', '', string.punctuation)
    normalized_corpus = normalized_corpus.apply(lambda x: [w.translate(transtable)
                                                                     for w in x if w not in sw_list])
    # removing empty strings
    normalized_corpus = normalized_corpus.apply(lambda x: [w for w in x if (w != '' and w.isalpha())])

    return normalized_corpus

def ft_preproc(labelsdf, textser):
    """ Processes given dataframe to be inputted into fasttext. Creates temporary text file.
    Parameters:
        labelsdf (DataFrame): Dataframe containing labels for accompanying textdf.
        textdf (Series): DataFrame or Series containing text to be classified.
     Returns:
        temppath (str): String for path to temporary preprocessed file."""

    labsep1 = '__label__'
    formatteddf = pd.DataFrame()
    formatteddf['labels'] = labelsdf.apply(lambda x: labsep1 + str(x))
    formatteddf['text'] = textser.apply(lambda x: str(x).replace('\n', '').replace('\t', ''))
    formatteddf['formatted'] = formatteddf.apply(lambda x: x['labels'] + ' ' + x['text'], axis=1)
    temppath = path.join(PROJECT_HOME,'data', 'ftformatted.txt')

    with open(temppath, mode='w', encoding='utf8') as file:
        for item in formatteddf['formatted']:
            file.write(item)
            file.write('\n')

    return temppath

def ft_predict(ft_model, ft_input):
    """ Function to predict multiple sentences/corpus using fasttext model.
    Parameters:
        ft_model (FastText Model): trained FastText model that will predict label for input.
        ft_input (List): list of strings to be labelled.
    Returns:
         ft_results (List): label output from fasttext model for inputted text. """

    temppath = path.join(PROJECT_HOME, 'data', 'ft_temp_input.txt')
    ft_input_df = pd.DataFrame()
    ft_input_df['text'] = pd.Series(ft_input)
    ft_input_df['text'].to_csv(temppath,
                               index=False,
                               sep=' ',
                               header=False,
                               quoting=csv.QUOTE_NONE, quotechar="",
                               escapechar=" ")

    # with open(tempfilepath, mode='w') as file:
    #     file.writelines(ft_input)

    ft_results = ft_model.test(temppath, k=1)

    return ft_results