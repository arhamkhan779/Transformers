from transformers import T5ForConditionalGeneration,T5Tokenizer
from pathlib import Path

MAXLENGTH=81
NUMBEAMS=5
NUMRETURNSEQUENCE=4
TOPk=100
TOPP=0.9
TEMPRATURE=1.0

def Load_Model(path:Path) -> any:
    try:
        model=T5ForConditionalGeneration.from_pretrained(path)
        return model
    except Exception as e:
        raise e
    
def Load_Tokenizer(path:Path) -> any:
    try:
        tokenizer=T5Tokenizer.from_pretrained(path)
        return tokenizer
    except Exception as e:
        raise e

def preprocess_input(text:str) -> str:
    try:
        preprocesed_text="paraphrase"+text
        return preprocesed_text
    except Exception as e:
        raise e
    
def Generator(model:any,tokenizer:any,text:str,max_length:int,num_return_sequence:int,num_beam:int,top_k:int,top_p:float,temprature:float,device) ->dict:
    try:
        text=preprocess_input(text=text)
        inputs=tokenizer(text,return_tensors="pt",truncation=True,max_length=max_length,padding="max_length")
        inputs={key:value.to(device) for key,value in inputs.items()}
        outputs=model.generate(
            input_ids=inputs['input_ids'],
            attention_mask=inputs['attention_mask'],
            max_length=max_length+20,
            num_beams=num_beam,
            num_return_sequences=num_return_sequence,
            top_k=top_k,
            top_p=top_p,
            temperature=temprature,
            do_sample=True,
            early_stopping=True

        )
        paraphrased_texts = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
        return paraphrased_texts
    except Exception as e:
        raise e