import pandas as pd
import json
from nltk.tokenize import word_tokenize
import string

'''Functions to assist with processing files and bring their content into python.'''

def jsontodf(file_path,n_lines=5000):
    json_content = []
    with open(file_path, mode='r', encoding='utf8') as tempfile:
        for i in range(n_lines):
            json_content.append(json.loads(tempfile.readline()))

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
