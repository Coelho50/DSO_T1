from entidades.Batalha import Batalha
from entidades.Jogador import Jogador
from excecoes.BatalhaNotFoundException import BatalhaNotFoundException
from excecoes.JogadorNotFoundException import JogadorNotFoundException
from excecoes.PartyNotFoundException import PartyNotFoundException
from telas.TelaBatalha import TelaBatalha


class ControladorBatalha():
	def __init__(self, controlador_principal):
		self.__tela_batalha = TelaBatalha(self)
		self.__controlador_principal = controlador_principal
		self.__jogador1 = Jogador
		

	def cria_batalha(self):
		atributos = self.__tela_batalha.menu_criacao_batalha(self.__jogador1, self.__controlador_principal.jogadores_cadastrados)
		if atributos == None:
			return 0
		else:
			self.__jogador1.add_batalha(Batalha(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]))
			self.__controlador_principal.jogador_DAO.update(self.__jogador1)
			atributos[1].add_batalha(Batalha(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]))
			self.__controlador_principal.jogador_DAO.update(atributos[1])
		self.__tela_batalha.mostra_mensagem('Criação bem sucedida','Batalha adicionada com sucesso.')

	def remove_batalha(self):
		while True:
			try:
				self.__tela_batalha.mostra_mensagem("Qual batalha deseja remover?(digite '0' para cancelar)")
				self.lista_batalhas()
				n = self.__tela_batalha.pegar_dados("N° da batalha: ", int)
				if n == "0":
						return None
				elif n > 0 and n <= len(self.__jogador1.batalhas):
					b = self.__jogador1.batalhas[n-1]
					j1 = self.__jogador1.batalhas[n-1].jogador_1 # O jogador logado pode estar na primeira ou segunda posição
					j2 = self.__jogador1.batalhas[n-1].jogador_2 # Se remover o jogador logado primeiro não será possível remover o segundo
					j1.remove_batalha(b)
					j2.remove_batalha(b)
					self.__tela_batalha.mostra_mensagem("Batalha removida!")
					return None
				else:
					raise BatalhaNotFoundException
			except BatalhaNotFoundException as e:
				self.__tela_batalha.mostra_mensagem(e)
		
	def lista_batalhas(self):
		batalhas = []
		for p in self.__jogador1.batalhas:
			batalhas.append(p.nome)
		print(batalhas)
		self.__tela_batalha.menu_lista_batalhas(batalhas)

	def abrir_menu(self):
		self.__jogador1 = self.__controlador_principal.jogador_logado
		lista_opcoes = {1: self.cria_batalha, 2: self.remove_batalha, 3: self.lista_batalhas}
		while True:
			opcao_selecionada = self.__tela_batalha.mostra_menu(lista_opcoes)
			if opcao_selecionada == 4:
				return 0
			else:
				lista_opcoes[opcao_selecionada]()

	def verificador(self, lista, mensagem, exception):
		while True:
			try:
				self.__tela_batalha.mostra_mensagem(mensagem)
				inp = self.__tela_batalha.pegar_dados("Nome: ", str)
				if inp == "0":
					return None
				for i in lista:
					if i.nome == inp:
						return i
				raise exception
			except exception as e:
				self.__tela_batalha.mostra_mensagem(e)