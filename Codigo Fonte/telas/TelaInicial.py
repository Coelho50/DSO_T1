from telas.AbstractTela import AbstractTela
from excecoes.OpcaoInvalidaException import OpcaoInvalidaException

class TelaInicial(AbstractTela):
	def __init__(self, controlador_principal):
		self.__controlador_principal = controlador_principal

	def mostra_menu(self, lista_opcoes):
		print("------- MENU PRINCIPAL -------")
		print("1 - Batalhas")
		print("2 - Parties")
		print("3 - Personagens")
		print("4 - Listar/remover jogadores cadastrados")
		print("5 - Fechar aplicação")
		print("6 - Logout")
		opcao = self.le_opcao(lista_opcoes)
		return opcao

	def le_opcao(self, lista_opcoes):
		while True:
			print("O que você deseja consultar?")
			try:
				opcao = int(input(':'))
				if opcao not in lista_opcoes and opcao != 6:
					raise OpcaoInvalidaException
			except ValueError:
				print("Opção inválida")
				print()
			except OpcaoInvalidaException as e:
				print(e)
				print()
			else:
				return opcao

	def pegar_dados_jogador(self, msg: str):
		nome = input(msg)
		return nome