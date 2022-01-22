from flask import Blueprint, jsonify
from Domain.company import Company

bp = Blueprint('companyController', __name__, url_prefix='/companyController')

@bp.route('/get')
def hello_world():
   company = Company(1, "electronics", "apple", "latitude longitude", "https://www.apple.com/ca/", 27)
   return jsonify(company.__dict__)


