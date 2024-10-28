from telas.TelaInicial import TelaInicial
from controladores.ControladorPersonagem import ControladorPersonagem
from controladores.ControladorParty import ControladorParty
#from controladores.ControladorBatalhas import Controlador 				-> ainda nao implementado

class ControladorPrincipal:

	def __init__(self):
		self.__controlador_personagem = ControladorPersonagem(self)
		self.__controlador_party = ControladorParty(self)
		#self__controlador_batalhas = controlador_batalha 				-> ainda nao implementado
		self.__tela_inicial = TelaInicial(self)

#	def editar_batalhas(self): 											-> ainda nao implementado
#		self.__controlador_batalhas

	def editar_parties(self):
		self.__controlador_party

	def editar_personagens(self):
		self.__controlador_personagem

	
	def abrir_sistema(self):
		lista_opcoes = {1: self.editar_batalhas, 2: self.editar_parties, 3: self.editar_personagens, 
						4: self.editar_jogadores, 5: self.encerrar_sessao}

		while True:
			opcao_selecionada = self.__tela_inicial.mostra_menu()
			controlador_chamado = lista_opcoes[opcao_selecionada]
			controlador_chamado()