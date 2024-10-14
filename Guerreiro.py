from Personagem import Personagem

class Guerreiro(Personagem):
	def __init__(self, nome: str, hp: float, item: str, dps: float):
		self.__dps = dps
		super.__init__(self, nome, hp, item):
			self.__nome = nome
			self.__hp = hp
			self.__item = item

	@property
	def dps(self): -> float
		return self.__dps

	@dps.setter
	def dps(self, dps: float):
		self.__dps = dps