from telas.AbstractTela import AbstractTela
from excecoes.OpcaoInvalidaException import OpcaoInvalidaException

class TelaInicial(AbstractTela):
	def __init__(self, controlador_principal):
		self.__controlador_principal = controlador_principal

	def get_login(self):
		return = input("Login (digite 0 para cadastrar um novo jogador): ")

	def mostra_menu(self, lista_opcoes):
		print("------- MENU PRINCIPAL -------")
		print("1 - Batalhas")
		print("2 - Parties")
		print("3 - Personagens")
		print("4 - Remover jogador cadastrado")
		print("5 - Encerrar sessão")
		opcao = self.le_opcao(lista_opcoes)
		return opcao

	def le_opcao(self, lista_opcoes):
		while True:
			print("O que você deseja consultar?")
			try:
				opcao = int(input(':'))
				if opcao not in lista_opcoes:
					raise OpcaoInvalidaException
			except ValueError:
				print("Opção inválida")
				print()
			except OpcaoInvalidaException as e:
				print(e)
				print()
			else:
				return opcao

	def seleciona_jogador(self):
		nome = input("Nome do jogador a ser modificado:")
		return nome