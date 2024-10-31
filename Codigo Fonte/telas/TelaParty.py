from excecoes.OpcaoInvalidaException import OpcaoInvalidaException
from telas.AbstractTela import AbstractTela

class TelaParty(AbstractTela):
	def __init__(self, controlador_party):
		self.__controlador_party = controlador_party


	def mostra_menu(self, lista_opcoes):
		print("------- PARTIES -------")
		print("1 - Criar nova party")
		print("2 - Excluir party")
		print("3 - Listar parties")
		print("4 - Retornar ao menu principal")
		print()
		opcao = self.le_opcao(lista_opcoes)
		return opcao

	def le_opcao(self, lista_opcoes):
		while True:
			print("O que você deseja fazer?")
			try:
				opcao = int(input(':'))
				if opcao not in lista_opcoes and opcao != 4:
					raise OpcaoInvalidaException
			except ValueError:
				print("Opção inválida")
				print()
			except OpcaoInvalidaException as e:
				print(e)
				print()
			else:
				return opcao
			
	def pegar_dados(self, msg, tipo):
		while True:
			try:
				dado = tipo(input(msg))
			except ValueError:
				print(f'Dado passado deve ser do tipo {tipo}')
			else:
				return dado