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
	
	def cria_party(self):
		atributos = self.__tela_party.menu_criacao_party(self.__personagens)
		if atributos == None:
			return 0
		else:
			self.__jogador.add_party(Party(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]))
			print(self.__jogador.parties)
			self.__controlador_principal.jogador_DAO.update(self.__jogador)
		self.__tela_party.mostra_mensagem("Criação bem sucedida","Party criada!")

	def remove_party(self):
		while True:
			self.__tela_party.mostra_mensagem("Qual party deseja remover?(digite '0' para sair)")
			nome = input(": ")
			try:
				if nome == "0":
					break
				elif self.verificador(nome,self.__jogador.parties) != None:
					self.__jogador.remove_party(self.verificador(nome,self.__jogador.parties))
					self.__tela_party.mostra_mensagem(f"Party '{nome}' removida")
					break
				else:
					raise PartyNotFoundException
			except PartyNotFoundException as e:
				self.__tela_party.mostra_mensagem(e)
		
	def lista_parties(self):
		self.__tela_party.mostra_mensagem(f"Parties de {self.__jogador.nome}:")
		for i in self.__jogador.parties:
			self.__tela_party.mostra_mensagem(f'----------[{i.nome}]----------')
			self.__tela_party.mostra_mensagem(f'{i.personagens[0].nome}, {i.personagens[1].nome}, {i.personagens[2].nome}, {i.personagens[3].nome}\n')

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