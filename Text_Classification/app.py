from utils import Load_Encoder, Load_Model, Load_Preprocessing_Pipeline, Load_Tokenizer, Preprocess_Text
from flask import Flask, render_template, request, jsonify
import torch

MODEL_PATH = "Text_Classification\\save_model"
TOKENIZER_PATH = "Text_Classification\\save_model"
Encoder_Path = "Text_Classification\\LabelEncoder.pkl"
Preprocessor_link = "en_core_web_sm"

try:
    Model = Load_Model(MODEL_PATH)
    Tokenizer = Load_Tokenizer(TOKENIZER_PATH)
    Encoder = Load_Encoder(Encoder_Path)
    Preprocessor_pipeline = Load_Preprocessing_Pipeline(Preprocessor_link)

except Exception as e:
    raise e

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/main", methods=["GET", "POST"])
def Main():
    if request.method == "POST":
        input_text = request.form.get("text")
        if input_text.strip():
            try:
                prediction = predict_label(
                    input_text, Model, Tokenizer, Encoder, Preprocessor_pipeline
                )
                return jsonify({"prediction": prediction[0]})
            except Exception as e:
                return jsonify({"error": str(e)})
        return jsonify({"error": "Input text cannot be empty"})
    return render_template("index.html")

def predict_label(sent: str, model: any, tokenizer: any, encoder: any, preprocessor: any):
    sent = Preprocess_Text(sent, preprocessor)
    inputs = tokenizer(sent, return_tensors="pt", padding=True, truncation=True, max_length=200)
    outputs = model(**inputs)
    logits = outputs.logits
    prediction_label = torch.argmax(logits, dim=1).item()
    return encoder.inverse_transform([prediction_label])

if __name__ == "__main__":
    app.run(debug=True)
