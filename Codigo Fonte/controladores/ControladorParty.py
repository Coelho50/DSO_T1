from entidades.Jogador import Jogador
from entidades.Party import Party
from excecoes import GrupoCheioException, PersonagemNotFoundException
from telas.TelaParty import TelaParty

#Controle responsavel pelas parties do jogador. Instancia a tela de personagens a ser utilizada pelo usuario
class ControladorParty():
	def __init__(self, personagens: list):
		self.__tela_party = TelaParty(self)
		self.__jogador = Jogador
		self.__personagens = personagens
	
	def cria_party(self):
		self.__tela_party.mostra_mensagem("--------- CRIAÇÃO DE PARTY ---------")
		self.__tela_party.mostra_mensagem("Como se chamará a sua party?")
		nome = input(": ")
		n_char = 0
		personagens = []
		while n_char != 4:
				try:
					print(f"Digite o nome do {n_char}° personagem da sua Party(Digite 0 para cancelar):")
					nome = TelaParty.pegar_dados("Nome: ", str)
					if nome == "0":
						return None
					elif self.verificador(nome, personagens) == None:
						raise PersonagemNotFoundException
					else:
						personagens.append(self.verificador(nome, personagens))
						n_char += 1
				except PersonagemNotFoundException as e:
					self.__tela_party.mostra_mensagem(e)
		self.__jogador.add_party(Party(nome, personagens[0], personagens[1], personagens[2], personagens[3]))
		self.__tela_party.mostra_mensagem("Party criada!")
		
				
				
			

	def remover_party(self, nome:str):
		try:
			self.__jogador.remove_party(nome)
		except:
			pass
		
	def listar_parties(self):
		return self.__jogador.parties
	
	def abrir_menu(self):
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