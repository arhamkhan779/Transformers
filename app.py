from flask import Flask, render_template, request, jsonify
from transformers import pipeline, TFAutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)

# Load the model and tokenizer from the saved directory
PATH = "save_model"
model = TFAutoModelForSeq2SeqLM.from_pretrained(PATH)
tokenizer = AutoTokenizer.from_pretrained(PATH)

# Create the summarization pipeline
Text_Summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    max_length = int(request.form['max_length'])  # Get the max_length from the frontend input
    
    # Generate the summary
    summary = Text_Summarizer(text, max_length=max_length)
    summary_text = summary[0]['summary_text']
    
    return jsonify({'summary': summary_text})

if __name__ == "__main__":
    app.run(debug=True)
