from telas.AbstractTela import AbstractTela

class TelaInicial(AbstractTela):
	def __init__(self, controlador_principal):
		self.__controlador_principal = controlador_principal

	def login(self):
		usuario = input("Login (digite 0 para cadastrar um novo jogador): ")

	def mostra_menu(self):
		print("------- MENU PRINCIPAL -------")
		print("1 - Batalhas")
		print("2 - Parties")
		print("3 - Personagens")
		print("4 - Remover jogador cadastrado")
		print("5 - Encerrar sessão")
		opcao = input("O que você deseja consultar?")
		return opcao

	def le_opcao(self):
		pass

	def seleciona_jogador_para_excluir(self):
		print("Quem você deseja remover?")
		nome = input(":")
		return nome