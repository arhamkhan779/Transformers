from flask import Flask, render_template, request
from utils import Load_Model, Load_tokenizer, Load_Preprocessor_Pipeline, Preprocess_Text, MAXLENGTH, PADDING, TRUNCATION, LINK, CLASSES
from pathlib import Path
import torch

model_path = Path("intentclassification/model")
tokenizer_path = Path("intentclassification/model")

try:
    print("Loading Artifacts ----------> Start")
    model = Load_Model(model_path)
    tokenizer = Load_tokenizer(tokenizer_path)
    preprocess_pipeline = Load_Preprocessor_Pipeline(LINK)
    print("Loading Artifacts ----------> Done")
except Exception as e:
    raise e


def Predict(model: any, tokenizer: any, preprocess_pipeline: any, text: str, Classes: list) -> str:
    try:
        text = Preprocess_Text(text, preprocess_pipeline)
        input_dims = tokenizer(
            text,
            padding=PADDING,
            max_length=MAXLENGTH,
            truncation=TRUNCATION,
            return_tensors='pt'
        )
        with torch.no_grad():
            prediction = model(**input_dims)
            logits = prediction.logits
        prediction_label = torch.argmax(logits, dim=1).item()
        return Classes[prediction_label]
    except Exception as e:
        raise e


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/main", methods=["GET", "POST"])
def main():
    prediction = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            prediction = Predict(model, tokenizer, preprocess_pipeline, user_input, CLASSES)
    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
