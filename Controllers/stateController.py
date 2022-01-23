from flask import Blueprint, jsonify
from flask_cors import CORS
from Domain.state import State
from Domain.stateDomain import stateDomain
import json

bp = Blueprint('stateController', __name__, url_prefix='/stateController')

@bp.route('/get/<name>/<longitude>/<latitude>')
def get(name, longitude, latitude):
   state = State(name, str(longitude), str(latitude), str(0))
   return jsonify(stateDomain.get(state).__dict__)