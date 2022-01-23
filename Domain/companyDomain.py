from DataAccess.companyDataAccess import companyDataAccess

class companyDomain:
   def getList(sector=""):
      return companyDataAccess.getList(sector)