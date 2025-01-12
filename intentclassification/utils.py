from transformers import DistilBertForSequenceClassification,DistilBertTokenizer
import spacy
from pathlib import Path

MAXLENGTH=22
TRUNCATION=True
PADDING='max_length'
LINK="en_core_web_sm"
CLASSES=['AddToPlaylist', 'BookRestaurant', 'GetWeather', 'PlayMusic',
       'RateBook', 'SearchCreativeWork', 'SearchScreeningEvent']

def Load_Model(path:Path) -> any:
    try:
        model=DistilBertForSequenceClassification.from_pretrained(path)
        return model
    except Exception as e:
        raise e

def Load_tokenizer(path:Path) ->any:
    try:
        tokenizer=DistilBertTokenizer.from_pretrained(path)
        return tokenizer
    except Exception as e:
        raise e

def Preprocess_Text(text:str,pipeline) ->str:
    try:
        doc=pipeline(text)
        text=[word.lemma_ for word in doc if not word.is_punct and not word.is_stop]
        return ' '.join(text)
    except Exception as e:
        raise e
    
def Load_Preprocessor_Pipeline(link:str) -> any:
    try:
        pipeline=spacy.load(link)
        return pipeline
    except Exception as e:
        raise e


