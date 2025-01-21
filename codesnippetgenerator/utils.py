from transformers import T5Tokenizer,T5ForConditionalGeneration
from pathlib import Path


class utils:
       def __init__(self,model_path:Path,tokenizer_path:Path) ->any:
           self.model_path=model_path
           self.tokenizer_path=tokenizer_path
       
       def Load_Model(self) -> any:
           '''
           This Function will take model path
           return T5 Trained Model
           '''
           try:
               model=T5ForConditionalGeneration.from_pretrained(self.model_path)
               return model
           except Exception as e:
               print(f"Error Encontoured :{e}")

       def Load_Tokenizer(self) -> any:
           '''
           This Function will take tokenizer path
           return T5 Tokenizer
           '''
           try:
               tokenizer=T5Tokenizer.from_pretrained(self.tokenizer_path)
               return tokenizer
           except Exception as e:
               print(f"Error Encontoured :{e}")

       def Generate(self,Query:str,tokenizer:any,model:any) -> str:
           '''
           This Function is utilize to 
           Generate the code snippet of provided query
           Take , model , tokenizer and query as input
           return generated output 
           '''
           try:
               Query=Query.lower()
               input_ids=tokenizer.encode("generate code:"+Query,return_tensors="pt",max_length=256,padding="max_length",truncation=True)
               output=model.generate(input_ids,max_length=256,num_beams=4,early_stopping=True)
               generated_code=tokenizer.decode(output[0],skip_special_tokens=True)
               return generated_code
           except Exception as e:
               print(f"Error Encontered : {e}")