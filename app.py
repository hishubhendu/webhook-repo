from flask import Flask, request, Blueprint, jsonify 
from webhook import save_to_db

webhook = Blueprint('webhook', __name__, url_prefix='/webhook') 

@webhook.route('/receiver', methods=["POST"])
def receiver():
    json_data = request.get_json()
    save_to_db(json_data)
    return jsonify({"message": "Data saved successfully"}), 200

@webhook.route('/health', methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200

def create_app():                        
    app = Flask(__name__)
    app.register_blueprint(webhook)  # Registering all the blueprints
    return app



if __name__ == '__main__':
    app = create_app()  # Creating our Flask app
    app.run(debug=True, port=5000)
