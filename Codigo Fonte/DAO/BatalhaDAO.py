from DAO.DAO import DAO
from entidades.Batalha import Batalha

class BatalhaDAO(DAO):
    def __init__(self):
        super().__init__('Batalhas.pkl')
    
    def add(self, batalha: Batalha):
        if((batalha is not None) and isinstance(batalha, Batalha) and isinstance(batalha.nome, str)):
            super().add(batalha.nome, batalha)
    
    def update(self, batalha: Batalha):
        if((batalha is not None) and isinstance(batalha, Batalha) and isinstance(batalha.nome, int)):
            super().update(batalha.nome, batalha)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)