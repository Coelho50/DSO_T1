class Personagem:
	def __init__(self, nome: str, hp: float, item: str):
		self.__nome = nome
		self.__hp = hp
		self.__item = item

	@property
	def nome(self):	-> str
		return self.__nome

	@nome.setter
	def nome(self, nome: str):
		self.__nome = nome

	@property
	def classe(self):
		return self.__classe

	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, hp: str):
		self.__hp = hp

	@property
	def item(self):
		return self.__item

	@item.setter
	def item(self, item: str):
		self.__item = item