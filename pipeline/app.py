from transformers import pipeline
from flask import Flask,render_template,url_for,request

translation_pipeline=pipeline("translation",model="helsinki-NLP/opus-mt-fr-en")
sentiment_pipeline =pipeline("sentiment-analysis")
summarization_pipeline=pipeline("summarization")
generation_pipeline=pipeline("text-generation")
NER_pipeline=pipeline("ner",grouped_entities=True)
app=Flask(__name__)

@app.route("/")
def home_Page():
    return render_template("home.html")

@app.route("/Main",methods=['POST','GET'])
def Main():
    sent = None
    gen = None
    trans = None
    ner = None
    summ = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        task = request.form.get('task')

        if task == 'sentiment':
            sent = sentiment_pipeline(user_input)
            return render_template('main.html', sent=sent)
        elif task == 'generation':
            gen = generation_pipeline(user_input)
            return render_template('main.html', gen=gen)
        elif task == 'translation':
            trans = translation_pipeline(user_input)
            return render_template('main.html', trans=trans)
        elif task == 'summarization':
            summ = summarization_pipeline(user_input)
            return render_template('main.html', summ=summ)
        elif task == 'named_entity_recognition':
            ner = NER_pipeline(user_input)
            return render_template('main.html', ner=ner)



    return render_template('main.html')



if __name__ == "__main__":
    app.run(debug=True)