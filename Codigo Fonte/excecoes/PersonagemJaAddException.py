class PersonagemJaAddException(Exception):
	def __init__(self):
		super().__init__("Personagem de mesmo nome já adicionado!")