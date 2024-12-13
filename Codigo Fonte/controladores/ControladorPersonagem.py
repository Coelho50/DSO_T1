from entidades.Personagem import Personagem
from telas.TelaPersonagem import TelaPersonagem
from excecoes.PersonagemJaAddException import PersonagemJaAddException
from excecoes.PersonagemNotFoundException import PersonagemNotFoundException
from DAO.PersonagemDAO import PersonagemDAO

#Controle responsavel pela lista de personagens. Instancia a tela de personagens a ser utilizada pelo usuario
class ControladorPersonagem:
	def __init__(self, controlador_principal):
		self.__tela_personagem = TelaPersonagem(self)
		#self.__personagens_cadastrados = []
		self.__personagem_DAO = PersonagemDAO()

	def cria_personagem(self):
		atributos = self.__tela_personagem.menu_criacao_personagem()
		if atributos == None:
			return 0
		else:
			self.__personagem_DAO.add(Personagem(atributos[0], atributos[1], atributos[3], atributos[4], atributos[5], atributos[6], atributos[7]))
		self.__tela_personagem.mostra_mensagem('Criação bem sucedida', f'{atributos[0]} adicionado a lista de personagens')

	def remove_personagem(self):
		nome = self.__tela_personagem.menu_remover_personagem(self.lista_nomes_personagens())
		if nome == None:
			return None
		try:
			self.verif_nome_repetido(nome)
		except PersonagemJaAddException:
			self.__personagem_DAO.remove(self.pegar_personagem_por_nome(nome))
			self.__tela_personagem.mostra_mensagem("Personagem removido", f'{nome} removido')
		else:
			self.__tela_personagem.mostra_mensagem("Erro", "Personagem ainda não adicionado a lista")

	def lista_personagens_completa(self):
		filtro = 'Todos'
		while True:
			lista_completa = []
			if filtro == None:
				return None
			elif filtro == "Mago" or filtro == "Healer" or filtro == "Guerreiro":
				for i in self.__personagem_DAO.get_all():
					if i.classe == filtro:
						lista_completa.append([f'{i.nome}: {i.classe}, {i.item} ITEM, {i.hp}HP, {i.dps}DPS, {i.mana}MANA, {i.hps}HPS'])
			else:
				for i in self.__personagem_DAO.get_all():
					lista_completa.append([f'{i.nome}: {i.classe}, {i.item} ITEM, {i.hp}HP, {i.dps}DPS, {i.mana}MANA, {i.hps}HPS'])
			filtro = self.__tela_personagem.menu_lista_personagens(lista_completa)


	def lista_nomes_personagens(self):	#-> Retorna o nome de todos os personagens como uma lista
		lista_nomes = []
		for i in self.__personagem_DAO.get_all():
			lista_nomes.append(i.nome)
		return lista_nomes

	def abrir_menu(self):
		lista_opcoes = {1: self.cria_personagem, 2: self.remove_personagem, 3: self.lista_personagens_completa}
		while True:
			opcao_selecionada = self.__tela_personagem.mostra_menu(lista_opcoes)
			if opcao_selecionada == 4:
				return None
			else:
				lista_opcoes[opcao_selecionada]()

	def pegar_personagem_por_nome(self, nome):
		personagem = self.__personagem_DAO.get(nome)
		if personagem == 'Chave inexistente':
			raise PersonagemNotFoundException
		return personagem

	def verif_nome_repetido(self, nome):
		try:
			self.pegar_personagem_por_nome(nome)
		except PersonagemNotFoundException:
			return 0
		else:
			raise PersonagemJaAddException
	@property
	def personagem_DAO(self):
		return self.__personagem_DAO.get_all()
#	def pegar_nome(self):
#		while True:
#			nome = self.__tela_personagem.pegar_dados("Nome: ", str)
#			try:
#				self.verif_nome_repetido(nome)
#			except PersonagemJaAddException as e:
#				self.__tela_personagem.mostra_mensagem(e)
#			else:
#				return nome