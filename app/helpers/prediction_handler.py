from config.main_config import MODEL_PATH
import fasttext
import string
import logging.config
import boto3


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

def glacier_load():
    'loads model from AWS S3 glacier'
    cred = boto3.Session(profile_name='default2').get_credentials()
    ACCESS_KEY = cred.access_key
    SECRET_KEY = cred.secret_key
    print(ACCESS_KEY)

    glacier = boto3.client('glacier',
                            aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY
                            )

    job_params = {'Type': 'inventory-retrieval',
                  'ArchiveId':'irx1pLNvoBxd0qlLN-eTGVF6zeLZ4ARXeZFo-gLbVCTmqXmz7COGqvO6qwdVLMUmT1bSogVEGQDca_Nd18g9o3LnusOfiw-n1m9k0GtrY6LHjJzSqESpDr0BMP8laxtgGd6WSNw_zg'}
    response = glacier.initiate_job(vaultName='arn:aws:glacier:us-east-2:351282577611:vaults/sentpred',
                                    jobParameters=job_params)
    #response = glacier.describe_vault(vaultName='arn:aws:glacier:us-east-2:351282577611:vaults/sentpred')
    body = response['Body'].read()

if __name__=='__main__':
    glacier_load()