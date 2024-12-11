from DAO.DAO import DAO
from entidades.Personagem import Personagem

class PersonagemDAO(DAO):
    def __init__(self):
        super().__init__('personagens.pkl')
    
    def add(self, personagem: Personagem):
        if((personagem is not None) and isinstance(personagem, Personagem) and isinstance(personagem.nome, str)):
            super().add(personagem.nome, personagem)
    
    def update(self, personagem: Personagem):
        if((personagem is not None) and isinstance(personagem, Personagem) and isinstance(personagem.nome, int)):
            super().update(personagem.nome, personagem)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        return super().remove(key)