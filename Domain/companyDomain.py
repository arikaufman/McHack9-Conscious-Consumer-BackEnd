from DataAccess.companyDataAccess import companyDataAccess
from Domain.itemToSectorRelationDomain import itemToSectorRelationDomain

class companyDomain:
   def getList(item=""):
      itemToSectors = itemToSectorRelationDomain.getList()
      sector = ""
      for itemToSector in itemToSectors:
          if item == itemToSector.item:
              sector = itemToSector.sector
              break

      return companyDataAccess.getList(sector)