from Personagem import Personagem

class Healer(Personagem):
	def __init__(self, nome: str, hp: float, item: str, dps: float, mana: float, hps: float):
		self.__dps = dps
		self.__mana = mana
		self.__hps = hps
		super.__init__(self, nome, hp, item):
			self.__nome = nome
			self.__hp = hp
			self.__item = item

	@property
	def dps(self): -> str
		return self.__dps

	@dps.setter
	def dps(self, dps: float):
		self.__dps = dps

	@property
	def mana(self): -> float
		return self.__mana

	@mana.setter
	def mana(self, mana: float):
		self.__mana = mana

	@property
	def hps(self): -> float
		return self.__hps

	@hps.setter
	def hps(self, hps: float):
		self.__hps = hps