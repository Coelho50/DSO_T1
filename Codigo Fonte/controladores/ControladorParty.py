from entidades.Jogador import Jogador
from entidades.Party import Party
from excecoes.PartyNotFoundException import PartyNotFoundException
from excecoes.PersonagemNotFoundException import PersonagemNotFoundException
from telas.TelaParty import TelaParty
#Controle responsavel pelas parties do jogador. Instancia a tela de personagens a ser utilizada pelo usuario
class ControladorParty():
	def __init__(self, controlador_principal):
		self.__tela_party = TelaParty(self)
		self.__controlador_principal = controlador_principal
		self.__jogador = None
		self.__personagens = controlador_principal.personagens()

	@property
	def controlador_principal(self):
		return self.__controlador_principal

	def cria_party(self):
		atributos = self.__tela_party.menu_criacao_party(self.__personagens)
		if atributos == None:
			return 0
		else:
			self.__jogador.add_party(Party(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]))
			self.__controlador_principal.jogador_DAO.update(self.__jogador)
		self.__tela_party.mostra_mensagem("Criação bem sucedida","Party criada!")

	def remove_party(self):
		parties = []
		for p in self.jogador.parties:
			parties.append(p.nome)
		nome = self.__tela_party.menu_remover_party(parties)
		if nome == None:
			return None
		for p in self.jogador.parties:
			if p.nome == nome:
				self.__jogador.remove_party(p)
				self.__controlador_principal.jogador_DAO.update(self.__jogador)
				self.__tela_party.mostra_mensagem("party removido", f'{nome} removido')
				return None
		self.__tela_party.mostra_mensagem("Erro", "party ainda não adicionado a lista")
		
	def lista_parties(self):
		parties = []
		for p in self.jogador.parties:
			parties.append(p.nome)
		self.__tela_party.menu_lista_parties(parties)

	def abrir_menu(self):
		self.__jogador = self.__controlador_principal.jogador_logado
		lista_opcoes = {1: self.cria_party, 2: self.remove_party, 3: self.lista_parties}
		while True:
			opcao_selecionada = self.__tela_party.mostra_menu(lista_opcoes)
			if opcao_selecionada == 4: #--------------> perguntar pro professor uma maneira melhor
				return 0
			else:
				lista_opcoes[opcao_selecionada]()

	def verificador(self, nome, lista):
		for i in lista:
			if i.nome == nome:
				return i
		return None

	
	@property
	def jogador(self):
		return self.__jogador

	@jogador.setter
	def jogador(self, value):
	    self.__jogador = value