from Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome: str, hp: float, item: str, dps: float):
        super().__init__(nome, hp, item)
        self.__dps = None
        if isinstance(dps, float):
            self.__dps = dps
        else:
            raise ValueError("DPS")

    @property
    def dps(self) -> float:
        return self.__dps

    @dps.setter
    def dps(self, dps: float):
        if isinstance(dps, float):
            self.__dps = dps
        else:
            raise ValueError("DPS")
