from Domain.itemToSectorRelation import ItemToSectorRelation
from Common.sqlconnector import sqlconnector

class itemToSectorRelationDataAccess:
   def getList():
      itemToSectorRelations = []
      rows = sqlconnector.connect("SELECT * FROM itemToSectorRelation;")
      for row in rows:
          itemToSectorRelations.append(ItemToSectorRelation(row[0], row[1]))
      return itemToSectorRelations