from transformers import MarianTokenizer
from transformers import MarianMTModel
from pathlib import Path

def Load_Model(Model_Path:Path) -> MarianMTModel:
    try:
        model=MarianMTModel.from_pretrained(Model_Path)
        return model
    except Exception as e:
        print(f"Error Encountoured : {e}")

def Load_Tokenizer(tokenizer_path:Path) -> MarianTokenizer:
    try:
        tokenizer=MarianTokenizer.from_pretrained(tokenizer_path)
        return tokenizer
    except Exception as e:
        print(f"Error Encountoured : {e}")

def Translate(model:MarianMTModel,tokenizer:MarianTokenizer,sentence:str) -> str:
    try:
        inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        translated = model.generate(**inputs)
        return tokenizer.decode(translated[0], skip_special_tokens=True)
    except Exception as e:
        return e