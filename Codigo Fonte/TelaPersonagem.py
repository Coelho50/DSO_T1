from AbstractTela import AbstractTela
from OpcaoInvalidaException import OpcaoInvalidaException

class TelaPersonagem(AbstractTela):
	def __init__(self, controlador_personagem):
		self.__controlador_personagem = controlador_personagem

	def mostra_menu(self):
		print("------- PERSONAGENS -------")
		print("1 - Criar novo personagem")
		print("2 - Excluir personagem")
		print("3 - Listar personagens")
		print("4 - Retornar ao menu principal")
		print()

	#deve ser passado para a funcao o tamanho da lista de numero_opcoes a serem escolhidas
	def le_opcao(self, numero_opcoes:int = 0):
		if numero_opcoes == 0:
			raise OpcoesException
		else:
			return self.ler_ate_opcao_valida(numero_opcoes)

	def ler_ate_opcao_valida(self, numero_opcoes):
		while True:
			try:
				opcao = int(input("Escolha uma opção: "))
				self.asseguro_opcao_valida(opcao, numero_opcoes)
				return opcao
			except ValueError:
				print("Ocorreu um erro, selecione a opção com um número inteiro")
			except OpcaoInvalidaException:
				print("Opcao fora do intervalo")

	def asseguro_opcao_valida(self, opcao, numero_opcoes):
		if not (opcao >= 1 and opcao <= numero_opcoes):
			raise OpcaoInvalidaException