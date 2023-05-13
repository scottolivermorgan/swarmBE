"""app main"""
from flask import Flask
from flask_cors import CORS
from Domains.Client.api import clients_bp

app = Flask(__name__)
app.register_blueprint(clients_bp)
cors = CORS(app)
