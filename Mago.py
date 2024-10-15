from Personagem import Personagem

class Mago(Personagem):
	def __init__(self, nome: str, hp: float, item: str, dps: float, mana: float):
		super.__init__(self, nome, hp, item)
		self.__dps = None
		self.__mana = None
		if isinstance(dps, float):
			self.__dps = dps
		else:
			raise ValueError("DPS") #padrozinar na tela
		if isinstance(dps, float):
			self.__dps = dps


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