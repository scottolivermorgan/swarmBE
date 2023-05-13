from flask import Blueprint, request,jsonify,abort
from flask_api import status
from sqlalchemy import func, select

clients_bp = Blueprint("clients_blueprint", __name__)

@clients_bp.route('/',methods = ['GET'])
def home():
    return "hello worlds"