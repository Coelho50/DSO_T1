from entidades.Party import Party
from entidades.Batalha import Batalha

class Jogador:
    def __init__(self, nome: str):
        self.__nome=nome
        self.__batalhas=[]
        self.__vitorias=0
        self.__parties=[]

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome=nome
    
    def add_batalha(self, batalha: Batalha):
        self.__batalhas.append(batalha)
        if batalha.vencedor==self:
            self.__vitorias+=1
    def remove_batalha(self, batalha: Batalha):
        self.__batalhas.remove(batalha)
        if batalha.vencedor==self:
            self.__vitorias-=1
    @property
    def vitorias(self) -> int:
        return self.__vitorias
    
    def add_parties(self, parties: Party):
        self.__parties.append(parties)
    def remove_parties(self, parties: Party):
        self.__parties.remove(parties)
    
