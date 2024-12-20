class Personagem:
	def __init__(self, nome: str, hp: float, item: str):
		self.__usos = 0
		self.__nome = None
		self.__hp = None
		self.__item = None

		if isinstance(nome, str):
			self.__nome = nome
		else:
			raise ValueError("nome") 
		if isinstance(hp, float):
			self.__hp = hp
		else:
			raise ValueError("HP")
		if isinstance(item, str):
			self.__item = item
		else:
			raise ValueError("item")

	@property
	def nome(self) -> str:
		return self.__nome

	@nome.setter
	def nome(self, nome: str):
		self.__nome = None
		if isinstance(nome, str):
			self.__nome = nome
		else:
			raise ValueError("nome")

	@property
	def usos(self) -> int:
		return self.__usos

	@usos.setter
	def usos(self, usos: int):
		self.__usos = None
		if isinstance(usos, int):
			self.__usos = usos
		else:
			raise ValueError("usos")

	@property
	def hp(self) -> float:
		return self.__hp

	@hp.setter
	def hp(self, hp: str):
		self.__hp = None
		if isinstance(hp, float):
			self.__hp = hp
		else:
			raise ValueError("HP")

	@property
	def item(self) -> str:
		return self.__item

	@item.setter
	def item(self, item: str):
		self.__item = None
		if isinstance(item, str):
			self.__item = item
		else:
			raise ValueError("item")

	@property
	def classe(self) -> str:
		return self.__class__.__name__ 