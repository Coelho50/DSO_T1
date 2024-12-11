from DAO.DAO import DAO
from entidades.Guerreiro import Guerreiro

class GuerreiroDAO(DAO):
    def __init__(self):
        super().__init__('guerreiro.pkl')
    
    def add(self, guerreiro: Guerreiro):
        if((guerreiro is not None) and isinstance(guerreiro, Guerreiro) and isinstance(guerreiro.nome, str)):
            super().add(guerreiro.nome, Guerreiro)
    
    def update(self, guerreiro: Guerreiro):
        if((guerreiro is not None) and isinstance(guerreiro, Guerreiro) and isinstance(guerreiro.nome, int)):
            super().update(guerreiro.nome, guerreiro)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)