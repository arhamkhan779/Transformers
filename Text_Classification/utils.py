from transformers import AutoModelForSequenceClassification,BertTokenizer
import spacy
import pickle
from pathlib import Path
import joblib

def Load_Model(path:Path) ->any:
    try:
        model=AutoModelForSequenceClassification.from_pretrained(path)
        return model
    except Exception as e:
        raise e
    
def Load_Tokenizer(path:Path) ->any:
    try:
        tokenizer=BertTokenizer.from_pretrained(path)
        return tokenizer
    except Exception as e:
        raise e

def Load_Preprocessing_Pipeline(Link:str) ->any:
    try:
        Pipeline=spacy.load(Link)
        return Pipeline

    except Exception as e:
        raise e
    
def Preprocess_Text(sent:str,pipeline:any) -> str:
    try:
       doc=pipeline(sent)
       sent=[word.lemma_.lower() for word in doc if not word.is_punct and not word.is_stop]
       return ' '.join(sent)
    except Exception as e:
        raise e
    
def Load_Encoder(path: Path) -> any:
    try:
        Encoder=joblib.load(path)
        return Encoder
    except Exception as e:
        raise e
        
