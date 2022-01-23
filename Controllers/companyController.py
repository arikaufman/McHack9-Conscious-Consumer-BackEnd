from flask import Blueprint, jsonify,Response
from Domain.company import Company
from Domain.companyDomain import companyDomain
import json
from flask_cors import CORS

bp = Blueprint('companyController', __name__, url_prefix='/companyController')

@bp.route('/getlist/<sector>')
def getList(sector):
   companies = companyDomain.getList(sector)
   companies2DArray = []
   for company in companies:
      print(company.id)
      companies2DArray.append([company.id, company.sector, company.name, company.location, company.address, company.websiteurl, company.esgrating])
   return json.dumps(companies2DArray)


