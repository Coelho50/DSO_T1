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
		self._personagens_cadastrados = controlador_principal.lista_personagens_cadastrados()
	
	def cria_party(self):
		self.__tela_party.mostra_mensagem("--------- CRIAÇÃO DE PARTY ---------")
		self.__tela_party.mostra_mensagem("Como se chamará a sua party?")
		nome_party = input(": ")
		self.__tela_party.mostra_mensagem("--------- PERSONAGENS DISPONÍVEIS ---------")
		for p in self._personagens_cadastrados:
			self.__tela_party.mostra_mensagem(f"{p.nome}")
		n_char = 0
		personagens = []
		while n_char != 4:
				try:
					print(f"Digite o nome do {n_char+1}° personagem da sua Party(Digite 0 para cancelar):")
					nome = self.__tela_party.pegar_dados("Nome: ", str)
					if nome == "0":
						return None
					elif self.verificador(nome, self._personagens_cadastrados) == None:
						raise PersonagemNotFoundException
					else:
						personagens.append(self.verificador(nome, self._personagens_cadastrados))
						n_char += 1
				except PersonagemNotFoundException as e:
					self.__tela_party.mostra_mensagem(e)
		self.__jogador.add_party(Party(nome_party, personagens[0], personagens[1], personagens[2], personagens[3]))
		self.__tela_party.mostra_mensagem("Party criada!")

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