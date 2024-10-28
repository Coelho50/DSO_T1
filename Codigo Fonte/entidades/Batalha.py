from entidades.Personagem import Personagem
from entidades.Jogador import Jogador
class Batalha:
    def __init__(self,jogador_1: Jogador,jogador_2: Jogador,party_1: int,party_2: int,vencedor: Jogador):
        self.__jogador_1=jogador_1
        self.__jogador_2=jogador_2
        self.__party_1=party_1
        self.__party_2=party_2
        self.__vencedor=vencedor

    @property
    def jogador_1(self) -> Jogador:
        return self.__jogador_1
    @jogador_1.setter
    def jogador_1(self, jogador_1: Jogador):
        self.__jogador_1=jogador_1
    
    @property
    def jogador_2(self) -> Jogador:
        return self.__jogador_2
    @jogador_2.setter
    def jogador_2(self, jogador_2: Jogador):
        self.__jogador_2=jogador_2
    
    @property
    def party_1(self) -> int:
        return self.__party_1
    @party_1.setter
    def party_1(self, party_1: int):
        self.__party_1=party_1
    @property
    def party_2(self) -> int:
        return self.__party_2
    @party_2.setter
    def party_2(self, party_2: int):
        self.__party_2=party_2

    @property
    def vencedor(self) -> Jogador:
        return self.__vencedor
    @vencedor.setter
    def vencedor(self, vencedor: Jogador):
        self.__vencedor=vencedor

            


        
