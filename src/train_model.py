from config.main_config import PROJECT_HOME
from os import path
from src.helpers.data_processing import jsontodf, ft_preproc, ft_predict
import fasttext
import logging.config

'This script loads and processes data, and then trains and saves the model'

logger = logging.getLogger('train_model')

# file paths
data_path = path.join(PROJECT_HOME, 'data', 'yelp_dataset')
corpus_path = path.join(data_path, 'yelp_academic_dataset_review.json')

# loading data
corpus_df = jsontodf(corpus_path, n_lines=50000)
corpus_df = corpus_df[['text', 'stars']]

# preprocessing to format for fasttext
ft_inputfile = ft_preproc(corpus_df['stars'], corpus_df['text'])
ft_model = fasttext.train_supervised(input=ft_inputfile, lr=1, dim=300, wordNgrams=3)
logger.warning("Model trained.")
model_save_path = path.join(PROJECT_HOME, 'models', 'ft_model.bin')
ft_model.save_model(model_save_path)
ft_results = ft_predict(ft_model, ['Good restaurant.', 'Bad restaurant.'])