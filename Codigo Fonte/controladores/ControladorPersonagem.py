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
		self.__controlador_principal = controlador_principal

	def cria_personagem(self):
		self.__tela_personagem.mostra_mensagem("--------- CRIAÇÃO DE PERSONAGEM ---------")
		self.__tela_personagem.mostra_mensagem("Insira abaixo os dados requisitados para criar um novo personagem")
		classe = self.pegar_classe()
		nome = self.pegar_nome()
		hp = self.__tela_personagem.pegar_dados("HP: ", float)
		item = self.__tela_personagem.pegar_dados("Item: ", str)
		dps = self.__tela_personagem.pegar_dados("DPS: ", float)
		mana = self.__tela_personagem.pegar_dados("Mana: ", float)
		hps = self.__tela_personagem.pegar_dados("HPS: ", float)
		if classe == "Healer":
			self.__personagens_cadastrados.append(Healer(nome, hp, item, dps, mana, hps))
		elif classe == "Mago":
			self.__personagens_cadastrados.append(Mago(nome, hp, item, dps, mana, hps))
		elif classe == "Guerreiro":
			self.__personagens_cadastrados.append(Guerreiro(nome, hp, item, dps, mana, hps))
		self.__tela_personagem.mostra_mensagem(f'{nome} adicionado a lista de personagens')

	def remove_personagem(self):
		self.__tela_personagem.mostra_mensagem("--------- REMOVER PERSONAGEM ---------")
		self.lista_nomes_personagens()
		self.__tela_personagem.mostra_mensagem("Quem você deseja remover?")
		nome = self.__tela_personagem.pegar_dados(":", str)
		try:
			self.verif_nome_repetido(nome)
		except PersonagemJaAddException:
			self.__personagens_cadastrados.remove(self.pegar_personagem_por_nome(nome))
			self.__tela_personagem.mostra_mensagem(f'{nome} removido')
		else:
			self.__tela_personagem.mostra_mensagem("Personagem ainda não adicionado a lista")

	def lista_personagens(self):
		vazio = True
		self.__tela_personagem.mostra_mensagem("Quais classes você deseja listar? (Todas, Mago, Guerreiro, Healer)")
		classe = self.__tela_personagem.pegar_dados(":", str)
		if len(self.__personagens_cadastrados) == 0:
			self.__tela_personagem.mostra_mensagem("Ainda não foram adicionados personagens")
		elif classe == 'Todas':
			for char in self.__personagens_cadastrados:
				self.__tela_personagem.mostra_mensagem(f'{char.nome}: {char.hp} HP, {char.dps} DPS, {char.mana} Mana, {char.hps} HPS, item: {char.item}')
		elif classe == 'Guerreiro' or classe == 'Mago' or classe == 'Healer':
			for char in self.__personagens_cadastrados:
				if char.classe == classe:
					self.__tela_personagem.mostra_mensagem(f'{char.nome}: {char.hp} HP, {char.dps} DPS, {char.mana} Mana, {char.hps} HPS, item: {char.item}')
					vazio = False
			if vazio:
				self.__tela_personagem.mostra_mensagem(f'Ainda não há personagens da classe {classe} na lista')
		else:
			self.__tela_personagem.mostra_mensagem("Classe inválida")

	def lista_nomes_personagens(self):
		for char in self.__personagens_cadastrados:
			self.__tela_personagem.mostra_mensagem(char.nome)

	def abrir_menu(self):
		lista_opcoes = {1: self.cria_personagem, 2: self.remove_personagem, 3: self.lista_personagens}
		while True:
			opcao_selecionada = self.__tela_personagem.mostra_menu(lista_opcoes)
			if opcao_selecionada == 4: #--------------> perguntar pro professor uma maneira melhor
				return 0
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
 	
	def pegar_classe(self):
		while True:
			classe = self.__tela_personagem.pegar_dados("Classe: ", str)
			if (classe == "Mago" or classe == "Healer" or classe == "Guerreiro"):
				return classe
			self.__tela_personagem.mostra_mensagem("Classe inválida. Um personagem deve ser Mago, Guerreiro ou Healer")

	def pegar_nome(self):
		while True:
			nome = self.__tela_personagem.pegar_dados("Nome: ", str)
			try:
				self.verif_nome_repetido(nome)
			except PersonagemJaAddException as e:
				self.__tela_personagem.mostra_mensagem(e)
			else:
				return nome