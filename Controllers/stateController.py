from flask import Blueprint, jsonify
from flask_cors import CORS
from Domain.state import State
from Domain.stateDomain import stateDomain
import json

bp = Blueprint('stateController', __name__, url_prefix='/stateController')

@bp.route('/get/<name>/<item>/<longitude>/<latitude>')
def get(name, item, longitude, latitude):
   state = State(name, item, longitude, latitude)
   return jsonify(stateDomain.get(state).__dict__)

