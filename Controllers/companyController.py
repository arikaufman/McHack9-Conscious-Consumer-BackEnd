from flask import Blueprint, jsonify,Response
from Domain.company import Company
from Domain.companyDomain import companyDomain
import json
from flask_cors import CORS

bp = Blueprint('companyController', __name__, url_prefix='/companyController')

@bp.route('/getlist/<item>')
def getList(item):
   companies = companyDomain.getList(item)
   companies2DArray = []
   for company in companies:
      print(company.id)
      companies2DArray.append([company.id, company.sector, company.name, company.latitude, company.longitude, company.esgrating])
   return json.dumps(companies2DArray)


