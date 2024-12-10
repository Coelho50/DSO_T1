
from entidades.Personagem import Personagem
from entidades.Healer import Healer
from entidades.Mago import Mago
from entidades.Guerreiro import Guerreiro
from telas.TelaPersonagem import TelaPersonagem
from excecoes.PersonagemJaAddException import PersonagemJaAddException
#Controle responsavel pela lista de personagens. Instancia a tela de personagens a ser utilizada pelo usuario
class ControladorPersonagem:
	def __init__(self, controlador_principal):
		self.__tela_personagem = TelaPersonagem(self)
		self.__personagens_cadastrados = []

	@property
	def personagens_cadastrados(self):
		return self.__personagens_cadastrados

	def cria_personagem(self):
		atributos = self.__tela_personagem.menu_criacao_personagem()
		if atributos == None:
			return 0
		elif atributos[1] == "Healer":
			self.__personagens_cadastrados.append(Healer(atributos[0], atributos[3], atributos[4], atributos[5], atributos[6], atributos[7]))
		elif atributos[1] == "Mago":
			self.__personagens_cadastrados.append(Mago(atributos[0], atributos[3], atributos[4], atributos[5], atributos[6], atributos[7]))
		elif atributos[1] == "Guerreiro":
			self.__personagens_cadastrados.append(Guerreiro(atributos[0], atributos[3], atributos[4], atributos[5], atributos[6], atributos[7]))
		self.__tela_personagem.mostra_mensagem('Criação bem sucedida', f'{atributos[0]} adicionado a lista de personagens')

	def remove_personagem(self):
		nome = self.__tela_personagem.menu_remover_personagem(self.lista_nomes_personagens())
		if nome == None:
			return None
		try:
			self.verif_nome_repetido(nome)
		except PersonagemJaAddException:
			self.__personagens_cadastrados.remove(self.pegar_personagem_por_nome(nome))
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
				for i in self.__personagens_cadastrados:
					if i.classe == filtro:
						lista_completa.append([f'{i.nome}: {i.item} ITEM, {i.hp}HP, {i.dps}DPS, {i.mana}MANA, {i.hps}HPS'])
			else:
				for i in self.__personagens_cadastrados:
					lista_completa.append([f'{i.nome}: {i.item} ITEM, {i.hp}HP, {i.dps}DPS, {i.mana}MANA, {i.hps}HPS'])
			filtro = self.__tela_personagem.menu_lista_personagens(lista_completa)


	def lista_nomes_personagens(self):
		lista_nomes = []
		for i in self.__personagens_cadastrados:
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
		for char in self.__personagens_cadastrados:
			if char.nome == nome:
				return char
		return None

	def verif_nome_repetido(self, nome):
		if  self.pegar_personagem_por_nome(nome) != None:
			raise PersonagemJaAddException
 	
#	def pegar_classe(self):
#		while True:
#			classe = self.__tela_personagem.pegar_dados("Classe: ", str)
#			if (classe == "Mago" or classe == "Healer" or classe == "Guerreiro"):
#				return classe
#			self.__tela_personagem.mostra_mensagem("Classe inválida. Um personagem deve ser Mago, Guerreiro ou Healer")

	def pegar_nome(self):
		while True:
			nome = self.__tela_personagem.pegar_dados("Nome: ", str)
			try:
				self.verif_nome_repetido(nome)
			except PersonagemJaAddException as e:
				self.__tela_personagem.mostra_mensagem(e)
			else:
				return nome