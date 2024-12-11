from DAO.DAO import DAO
from entidades.Mago import Mago

class MagoDAO(DAO):
    def __init__(self):
        super().__init__('mago.pkl')
    
    def add(self, mago: Mago):
        if((mago is not None) and isinstance(mago, Mago) and isinstance(mago.nome, str)):
            super().add(mago.nome, Mago)
    
    def update(self, mago: Mago):
        if((mago is not None) and isinstance(mago, Mago) and isinstance(mago.nome, int)):
            super().update(mago.nome, mago)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)