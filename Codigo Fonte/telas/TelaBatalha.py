from excecoes.OpcaoInvalidaException import OpcaoInvalidaException
from telas.AbstractTela import AbstractTela


class TelaBatalha(AbstractTela):
	def __init__(self, controlador_batalha):
		self.__controlador_batalha = controlador_batalha


	def mostra_menu(self, lista_opcoes):
		print("------- BATALHAS -------")
		print("1 - Criar nova batalha")
		print("2 - Excluir batalha")
		print("3 - Listar batalhas")
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