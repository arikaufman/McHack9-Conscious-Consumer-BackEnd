from Domain.state import State
from Domain.companyDomain import companyDomain

class stateDomain:
   def get(state):
      state.esgRating = 30
      print(state.__dict__)
      return state