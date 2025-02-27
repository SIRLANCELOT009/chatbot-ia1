from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Cargar el modelo de IA (puedes cambiar "facebook/blenderbot-400M-distill" por otro)
chatbot_pipeline = pipeline("conversational", model="facebook/blenderbot-400M-distill")

@app.route('/')
def home():
    return "🚀 ChatBot IA de Turismo Verde está en línea"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"response": "Por favor, envía un mensaje válido."})

    # Procesar la pregunta con IA
    response = chatbot_pipeline(user_input)
    return jsonify({"response": response[0]['generated_text']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

