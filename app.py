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

    # Load your custom NER model
    custom_ner = spacy.load("model-best")
    
    # Apply your NER model to the user's input
    text_doc = custom_ner(user_input)

    # Extract entities
    extracted_entities = []
    for ent in text_doc.ents:
        extracted_entities.append({
            'text': ent.text,
            'label': ent.label_
        })

    # Return the extracted entities as JSON
    return jsonify({'entities': extracted_entities})

if __name__ == '__main__':
    app.run(debug=True)
