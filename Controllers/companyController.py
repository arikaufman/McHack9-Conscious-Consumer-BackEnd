from flask import Blueprint, jsonify
from Domain.company import Company
from flask_cors import CORS
from Domain.state import State
from Domain.stateDomain import stateDomain

bp = Blueprint('companyController', __name__, url_prefix='/companyController')

@bp.route('/get')
def hello_world():
   company = Company(1, "electronics", "apple", "latitude longitude", "https://www.apple.com/ca/", 27)
   return jsonify(company.__dict__)

@bp.route('/get/<name>/<item>/<longitude>/<latitude>')
def get(name, item, longitude, latitude):
   state = State(name, item, longitude, latitude)
   return jsonify(stateDomain.get(state))


