from telas.TelaInicial import TelaInicial
from controladores.ControladorPersonagem import ControladorPersonagem
from controladores.ControladorParty import ControladorParty
#from controladores.ControladorBatalhas import Controlador 				-> ainda nao implementado
from excecoes.JogadorNotFoundException import JogadorNotFoundException

class ControladorPrincipal:

	def __init__(self):
		self.__jogadores_cadastrados = []
		self.__controlador_personagem = ControladorPersonagem(self)
		self.__controlador_party = ControladorParty(self)
		#self__controlador_batalhas = controlador_batalha 				-> ainda nao implementado
		self.__tela_inicial = TelaInicial(self)

	def editar_batalhas(self):
		pass
#		self.__controlador_batalhas 									-> ainda nao implementado

	def editar_parties(self):
		self.__controlador_party

	def editar_personagens(self):
		self.__controlador_personagem

	def remover_jogador(self):
		self.lista_jogadores_cadastrados()
		nome_jogador = self.__tela_inicial.seleciona_jogador
		try:
			jogador_excluir = seleciona_jogador
		except JogadorNotFoundException:
			print(f'Jogador "{nome_jogador}" não encontrado')
		else:
			self.__jogadores_cadastrados.remove(jogador_excluir)
			print(f'Jogador "{nome_jogador}" excluido')

	def encerrar_sessao(self):
		exit()

	def abrir_sistema(self):
		verify = False
		while not verify:
			usuario = self.__tela_inicial.get_login()
			verify = self.verificar_login(usuario)
		lista_opcoes = {1: self.editar_batalhas, 2: self.editar_parties, 3: self.editar_personagens, 
						4: self.remover_jogador, 5: self.encerrar_sessao}

		while True:
			opcao_selecionada = self.__tela_inicial.mostra_menu(lista_opcoes)
			controlador_chamado = lista_opcoes[opcao_selecionada]
			controlador_chamado()

	def lista_jogadores_cadastrados(self):
		print("Jogadores cadastrados:")
		for i in self.__jogadores_cadastrados:
			print(f'[{i.nome}]')

	def seleciona_jogador_por_nome(self, nome):
		for jogador in self.__jogadores_cadastrados:
			if jogador.nome == nome:
				return jogador
		raise JogadorNotFoundException

	def verificar_login(self, usuario):
		for jogador in self.__jogadores_cadastrados:
			if jogador.nome == 
