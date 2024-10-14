from Personagem import Personagem
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
        self.__personagens=personagens

    def add_personagem(self,personagem: Personagem):
        if len(self.__personagens)<=4 and personagem not in self.__personagens:
            self.__personagens.append(personagem)
        else:
            pass 
        """raise exception"""

    def remove_personagem(self,personagem: Personagem):
        if personagem in self.__personagens:
            self.__personagens.remove(personagem)
        else:
            pass
            """raise exception"""

            


        
