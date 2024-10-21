from AbstractTela import AbstractTela

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

	#deve ser passado para a funcao o tamanho da lista de opcoes a serem escolhidas
	def le_opcao(self, opcoes:int = 0):
		if opcoes == 0:
			raise OpcoesException
		else:
			ler_ate_encontrar_opcao_valida(opcoes)

	def ler_ate_encontrar_opcao_valida(self, opcoes):
		while True:
			try:
				opcao = int(input("Escolha uma opção: "))
			except ValueError:
				print("Ocorreu um erro, selecione a opção com um número inteiro")
			else:
				return opcao  #------------>ainda aceitando opcao > opcoes

