from flask import Flask, render_template, request
from utils import Load_Model, Load_Tokenizer, Translate

try:
    print("Loading Artifacts ---> Start")
    PATH = "translator"
    tokenizer = Load_Tokenizer(tokenizer_path=PATH)
    model = Load_Model(Model_Path=PATH)
    print("Loading Artifacts ---> Done")

except Exception as e:
    raise e

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    translated_text = ""
    if request.method == "POST":
        sentence = request.form["sentence"]
        translated_text = Translate(model=model, tokenizer=tokenizer, sentence=sentence)
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
