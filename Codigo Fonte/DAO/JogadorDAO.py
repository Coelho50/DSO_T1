from DAO.DAO import DAO
from entidades.Jogador import Jogador

class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogadores.pkl')
    
    def add(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.nome, str)):
            super().add(jogador.nome, jogador)
    
    def update(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.nome, int)):
            super().update(jogador.nome, jogador)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)