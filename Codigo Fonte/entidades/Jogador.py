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

    @property
    def batalhas(self) -> list:
        return self.__batalhas

    @batalhas.setter
    def batalhas(self, batalhas: list):
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

    @property
    def parties(self) -> list:
        return self.__parties

    @parties.setter
    def parties(self, parties: list):
        self.__parties.append(party)

    def remove_party(self, party: Party):
        self.__parties.remove(party)
        if party.vencedor==self:
            self.__vitorias-=1