import os
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Cargar el modelo de IA (puedes cambiar a otro compatible)
chatbot_pipeline = pipeline("conversational", model="facebook/blenderbot-400M-distill")

@app.route('/')
def home():
    return "🚀 ChatBot IA de Turismo Verde está en línea"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.json
        user_input = data.get("message", "").strip()

        if not user_input:
            return jsonify({"response": "Por favor, envía un mensaje válido."})

        # Crear conversación y obtener respuesta
        conversation = Conversation(user_input)
        response = chatbot_pipeline(conversation)

        return jsonify({"response": str(response.generated_responses[0])})

    except Exception as e:
        return jsonify({"error": "Ocurrió un error", "details": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Puerto dinámico para Render
    app.run(host='0.0.0.0', port=port)
