from config.main_config import MODEL_PATH
import fasttext
import string
import logging.config
import boto3
''' This file contains functions to take in input and return predictions.'''

logger = logging.getLogger('prediction_handler')


# loading sentiment prediction model
spmodel = fasttext.load_model(MODEL_PATH)
logger.info("Sentiment prediction model loaded.")

def get_prediction(user_input):
    'This function extracts the sentiment prediction from the model output.'
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))
    model_out=spmodel.predict(user_input)
    return model_out[0][0][9]

def load_model():
    'Returns loaded model object from s3 object'
    cred = boto3.Session(profile_name='default2').get_credentials()
    ACCESS_KEY = cred.access_key
    SECRET_KEY = cred.secret_key

    s3client = boto3.client('s3',
                            aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY
                            )

    response = s3client.get_object(Bucket='sentpred', Key='ft_model.bin')

    body = response['Body'].read()
    loaded_model = fasttext.load_model(body)
    return loaded_model

