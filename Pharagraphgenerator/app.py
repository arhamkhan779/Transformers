from flask import Flask, render_template, request, jsonify
from utils import Load_Model, Load_Tokenizer, Generator
from pathlib import Path
import torch

MAXLENGTH = 81
NUMBEAMS = 5
NUMRETURNSEQUENCE = 4
TOPk = 100
TOPP = 0.9
TEMPRATURE = 1.0

try:
    model = Load_Model(Path("Pharagraphgenerator/saved_t5_model"))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    tokenizer = Load_Tokenizer(Path("Pharagraphgenerator/saved_t5_model"))
except Exception as e:
    raise e

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/main", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/generate", methods=['POST'])
def generate():
    try:
        data = request.get_json()
        text = data['text']
        paraphrases = Generator(
            model=model,
            tokenizer=tokenizer,
            text=text,
            max_length=MAXLENGTH,
            num_return_sequence=NUMRETURNSEQUENCE,
            num_beam=NUMBEAMS,
            top_k=TOPk,
            top_p=TOPP,
            temprature=TEMPRATURE,
            device=device
        )
        return jsonify({'paraphrases': paraphrases})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
