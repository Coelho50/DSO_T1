from Personagem import Personagem

class Healer(Personagem):
    def __init__(self, nome: str, hp: float, item: str, dps: float, mana: float, hps: float):
        super().__init__(nome, hp, item)
        self.__dps = None
        self.__mana = None
        self.__hps = None
        if isinstance(dps, float):
            self.__dps = dps
        else:
            raise ValueError("DPS")
        if isinstance(mana, float):
            self.__mana = mana
        else:
            raise ValueError("mana")
        if isinstance(hps, float):
            self.__hps = hps
        else:
            raise ValueError("HPS")

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

    @property
    def hps(self) -> float:
        return self.__hps

    @hps.setter
    def hps(self, hps: float):
        if isinstance(hps, float):
            self.__hps = hps
        else:
            raise ValueError("HPS")
