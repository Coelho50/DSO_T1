from telas.AbstractTela import AbstractTela
from excecoes.OpcaoInvalidaException import OpcaoInvalidaException

class TelaPersonagem(AbstractTela):
	def __init__(self, controlador_personagem):
		self.__controlador_personagem = controlador_personagem

	def mostra_menu(self, lista_opcoes):
		print("------- PERSONAGENS -------")
		print("1 - Criar novo personagem")
		print("2 - Excluir personagem")
		print("3 - Listar personagens")
		print("4 - Retornar ao menu principal")
		opcao = self.le_opcao(lista_opcoes)
		return opcao

	#deve ser passado para a funcao a lista de opcoes a serem escolhidas
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

	#passar o tipo do dado que deve ser devolvido e uma mensagem para pedir mostrar ao usuario
	def pegar_dados(self, msg, tipo):
		while True:
			try:
				dado = tipo(input(msg))
			except ValueError:
				print(f'Dado passado deve ser do tipo {tipo}')
			else:
				return dado