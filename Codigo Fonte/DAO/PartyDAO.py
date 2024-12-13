from DAO.DAO import DAO
from entidades.Party import Party

class PartyDAO(DAO):
    def __init__(self):
        super().__init__('Parties.pkl')
    
    def add(self, party: Party):
        if((party is not None) and isinstance(party, Party) and isinstance(party.nome, str)):
            super().add(party.nome, Party)
    
    def update(self, party: Party):
        if((party is not None) and isinstance(party, Party) and isinstance(party.nome, int)):
            super().update(party.nome, Party)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)