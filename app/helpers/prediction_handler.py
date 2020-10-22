from config.main_config import MODEL_PATH
import fasttext
import string
import logging.config

''' This file contains functions to take in input and return predictions.'''

logger = logging.getLogger('prediction_handler')

#loading sentiment prediction model
spmodel = fasttext.load_model(MODEL_PATH)
logger.info("Sentiment prediction model loaded.")

def get_prediction(user_input):
    'This function extracts the sentiment prediction from the model output.'
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))
    model_out=spmodel.predict(user_input)
    return model_out[0][0][9]