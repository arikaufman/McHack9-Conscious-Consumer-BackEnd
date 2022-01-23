from Domain.company import Company
from Common.sqlconnector import sqlconnector

class companyDataAccess:
   def getList(sector):
      companies = []
      rows = sqlconnector.connect("SELECT * FROM companies WHERE sector='" + sector + "';")
      for row in rows:
          companies.append(Company(row[0], row[1], row[2], row[3], row[4], row[5]))
      return companies