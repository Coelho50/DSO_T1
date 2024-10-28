from Personagem import Personagem
from excecoes.GrupoCheioException import GrupoCheioException
from excecoes.PersonagemNotFoundException import PersonagemNotFoundException
class Party:
    def __init__(self, nome: str, char1: Personagem, char2: Personagem, char3: Personagem, char4):
        self.__nome=nome
        self.__personagens=[char1,char2,char3,char4]
    
    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome=nome

    @property
    def personagens(self)-> list:
        return self.__personagens
    @personagens.setter
    def personagens(self, personagens: list):
        if len(personagens) <= 4:
            for i in range(4):
                if isinstance(personagens[i], Personagem):
                    self.__personagens = personagens
                else:
                    raise ValueError
        else:
            raise GrupoCheioException

    def add_personagem(self,personagem: Personagem):
        if len(self.__personagens) <=4 and personagem not in self.__personagens:
            self.__personagens.append(personagem)
        else:
            raise GrupoCheioException

    def remove_personagem(self, personagem: Personagem):
        if personagem in self.__personagens:
            self.__personagens.remove(personagem)
        else:
            raise PersonagemNotFoundException

            


        
