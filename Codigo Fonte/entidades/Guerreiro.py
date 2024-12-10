from entidades.Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome: str, hp: float, item: str, dps: float, mana: float, hps: float):
        super().__init__(nome, hp, item, dps, mana, hps)