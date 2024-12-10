from DAOs.dao import DAO
from entidades.Healer import Healer

class HealerDAO(DAO):
    def __init__(self):
        super().__init__('healer.pkl')
    
    def add(self, healer: Healer):
        if((healer is not None) and isinstance(healer, Healer) and isinstance(healer.nome, str)):
            super().add(healer.nome, Healer)
    
    def update(self, healer: Healer):
        if((healer is not None) and isinstance(healer, Healer) and isinstance(healer.nome, int)):
            super().update(healer.nome, healer)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)