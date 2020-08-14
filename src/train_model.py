from config import PROJECT_HOME
from os import path
from src.helpers.data_processing import jsontodf, normalize_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import cross_val_score
import pandas as pd
import fasttext
# from gensim.models import Word2Vec
# import string
# import nltk

'This script loads and processes data, and then trains and saves the model'


# data_folder = 'twitter_dataset'
# data_file = 'twitter_sentiment.csv'

# file paths
data_path = path.join(PROJECT_HOME, 'data', 'yelp_dataset')
corpus_path = path.join(data_path, 'yelp_academic_dataset_review.json')

# loading data
corpus_df = jsontodf(corpus_path, n_lines=50000)
corpus_df = corpus_df[['text', 'stars']]

# normalizing text
#corpus_df['normalized'] = normalize_corpus(corpus_df['text'])

# # w2vmodel = Word2Vec(reviewdf['normalized'],
# #                     size=50,
# #                     min_count=10)
#
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=500, max_df=7000,
                        norm='l2', encoding='utf8',
                        ngram_range=(1, 2),
                        stop_words='english')

features = tfidf.fit_transform(corpus_df['text']).toarray()
traindf = pd.get_dummies(corpus_df, columns=['stars'])

# logreg = LogisticRegression(solver='lbfgs',
#                            multi_class='multinomial',
#                            max_iter=1000)
# logreg.fit(features, corpus_df['stars'])

fast

# CV_n = 5
# accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV_n)
#







