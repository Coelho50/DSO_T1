from AbstractTela import AbstractTela

class TelaInicial(AbstractTela):
	def __init__(self, controlador_party):
		self.__controlador_party = controlador_party

	def mostra_menu(self):
		print("------- PARTIES -------")
		print("1 - Criar nova party")
		print("2 - Excluir personagem")
		print("3 - Listar personagens")
		print("4 - Retornar ao menu principal")
		print()