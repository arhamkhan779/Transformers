from flask import Flask, render_template, request
from utils import utils

# Initialize the model and tokenizer
obj = utils(model_path="codesnippetgenerator\\my_model", tokenizer_path="codesnippetgenerator\\my_model")
model = obj.Load_Model()
tokenizer = obj.Load_Tokenizer()

app = Flask(__name__)

# Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    code_snippet = None
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            code_snippet = obj.Generate(query, tokenizer=tokenizer, model=model)
    return render_template("main.html", code=code_snippet)

if __name__ == "__main__":
    app.run(debug=True)
