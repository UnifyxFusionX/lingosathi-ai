from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    language = data.get('lang', 'hi')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    response = f"Ye chatbot ka jawaab hai: {user_message}"
    
    translated = GoogleTranslator(source='auto', target=language).translate(response)
    
    return jsonify({'reply': translated})

@app.route('/', methods=['GET'])
def home():
    return 'LingoSathi chatbot backend running!'

if __name__ == '__main__':
    app.run(debug=True)
