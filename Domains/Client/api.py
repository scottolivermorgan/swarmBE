from flask import Blueprint, request,jsonify,abort
from flask_api import status
from sqlalchemy import func, select,text
from database import engine


clients_bp = Blueprint("clients_blueprint", __name__)

@clients_bp.route('/',methods = ['GET'])
def home():
    return "hello worlds"

@clients_bp.route('/employee_list',methods = ['GET'])
def empoloyee_list():
    with engine.connect() as connection:
        var = connection.execute(text('select * from Employee'))
        return 'yay'