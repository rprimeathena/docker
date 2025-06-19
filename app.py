from flask import Flask, request, jsonify
import random

app = Flask(__name__)

SECRET_NUMBER = random.randint(1, 10)

@app.route('/')
def home():
    return "Bienvenue au jeu de devinette ! Envoyez un nombre (1-10) à /guess via POST."

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    if not data or 'number' not in data:
        return jsonify({'message': 'Veuillez envoyer un nombre dans le champ "number".'}), 400
    try:
        user_number = int(data['number'])
    except ValueError:
        return jsonify({'message': 'Le nombre doit être un entier.'}), 400
    if user_number == SECRET_NUMBER:
        return jsonify({'message': 'Bravo ! Vous avez deviné le bon nombre !'}), 200
    elif user_number < SECRET_NUMBER:
        return jsonify({'message': 'Trop petit !'}), 200
    else:
        return jsonify({'message': 'Trop grand !'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 