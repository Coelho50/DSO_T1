from Personagem import Personagem

class Mago(Personagem):
	def __init__(self, nome: str, hp: float, item: str, dps: float, mana: float):
		self.__dps = dps
		self.__mana = mana
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