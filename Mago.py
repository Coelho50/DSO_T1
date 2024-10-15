from Personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome: str, hp: float, item: str, dps: float, mana: float):
        super().__init__(nome, hp, item)
        self.__dps = None
        self.__mana = None
        if isinstance(dps, float):
            self.__dps = dps
        else:
            raise ValueError("DPS")
        if isinstance(mana, float):
            self.__mana = mana
        else:
            raise ValueError("mana")

    @property
    def dps(self) -> float:
        return self.__dps

    @dps.setter
    def dps(self, dps: float):
        if isinstance(dps, float):
            self.__dps = dps
        else:
            raise ValueError("DPS")

    @property
    def mana(self) -> float:
        return self.__mana

    @mana.setter
    def mana(self, mana: float):
        if isinstance(mana, float):
            self.__mana = mana
        else:
            raise ValueError("mana")
