from flask import Flask, request, Blueprint, jsonify 
from webhook import save_to_db
import uuid

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')     #setting up mongoDB
db = client['mydatabase'] 
from datetime import datetime
webhook = Blueprint('webhook', __name__, url_prefix='/webhook') 



def save_to_db(data: dict, action: str):
    document = {
        "request_id": data.get('after') or str(uuid.uuid4()),  # Using commit hash or generating a UUID for non-push events
        "author": data['pusher']['name'] if action == 'push' else data['pull_request']['user']['login'],
        "action": action,
        "from_branch": data['ref'].split('/')[-1] if action == 'push' else data['pull_request']['head']['ref'],
        "to_branch": None if action == 'push' else data['pull_request']['base']['ref'],
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    }
    print("Document to insert:", document)
    db.webhook_logs.insert_one(document)
    print("Document inserted successfully")

    return "Logs created successfully"


@webhook.route('/receiver', methods=["POST"])
def receiver():
    json_data = request.get_json()
    save_to_db(json_data)
    return jsonify({"message": "Data saved successfully"}), 200


@webhook.route('/health', methods=["GET"])
def health():
    """this is health api to check flask's status"""
    return jsonify({"status": "OK"}), 200


def create_app():                        
    app = Flask(__name__)
    app.register_blueprint(webhook)  # Registering all the blueprints
    return app


if __name__ == '__main__':
    app = create_app()  # Creating our Flask app
    app.run(debug=True, port=5000)
