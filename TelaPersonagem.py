from AbstractTela import AbstractTela

class TelaPersonagem(AbstractTela):
	def __init__(self, controlador_personagem):
		self.__controlador_personagem = controlador_personagem

	def mostra_menu():
		print("------- PERSONAGENS -------")
		print("1 - Criar novo personagem")
		print("2 - Excluir personagem")
		print("3 - Listar personagens")
		print("4 - Retornar ao menu principal")

	def le_opcao():
		pass