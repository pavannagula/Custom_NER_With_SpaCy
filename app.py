from flask import Flask, render_template, request, jsonify
import spacy


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_entities', methods=['POST'])
def extract_entities():
    # Get user input from the form
    user_input = request.form['user_input']

    # Replace this with your NER model logic to extract entities
    custom_ner = spacy.load("model-best") 
    extracted_entities = custom_ner(user_input)

    # Return the extracted entities as JSON
    return ({'entities': extracted_entities})

if __name__ == '__main__':
    app.run(debug=True)
