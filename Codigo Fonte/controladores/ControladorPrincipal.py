from telas.TelaInicial import TelaInicial
from entidades.Jogador import Jogador
from controladores.ControladorPersonagem import ControladorPersonagem
from controladores.ControladorParty import ControladorParty
from controladores.ControladorBatalha import ControladorBatalha
from excecoes.JogadorNotFoundException import JogadorNotFoundException
from excecoes.PersonagemNotFoundException import PersonagemNotFoundException
from excecoes.RemoverJogadorLogadoException import RemoverJogadorLogadoException
from DAO.JogadorDAO import JogadorDAO

class ControladorPrincipal:
	def __init__(self):
		#self.__jogadores_cadastrados = []
		self.__jogador_logado = None
		self.__jogador_DAO = JogadorDAO()
		self.__controlador_personagem = ControladorPersonagem(self)
		self.__controlador_party = ControladorParty(self)
		self.__controlador_batalhas = ControladorBatalha(self)
		self.__tela_inicial = TelaInicial(self)

	@property
	def jogador_logado(self):
		return self.__jogador_logado

	@property
	def jogadores_cadastrados(self):
		return self.__jogador_DAO.get_all()

	def editar_batalhas(self):
		self.__controlador_batalhas.abrir_menu()

	def editar_parties(self):
		self.__controlador_party.abrir_menu()

	def editar_personagens(self):
		self.__controlador_personagem.abrir_menu()

	def remover_jogador(self):
		while True:
			try:
				nome_jogador = self.__tela_inicial.tela_remocao_jogador(self.lista_nomes_jogadores())
				if nome_jogador == None:
					return None
				elif nome_jogador == self.__jogador_logado.nome:
					raise RemoverJogadorLogadoException
				elif nome_jogador == 'Chave inexistente':
					raise JogadorNotFoundException
				jogador_excluir = self.seleciona_jogador_por_nome(nome_jogador)
			except JogadorNotFoundException as e:
				self.__tela_inicial.mostra_mensagem(e, e)
			except RemoverJogadorLogadoException as e:
				self.__tela_inicial.mostra_mensagem("Encerrando sessão", e)
				self.__jogador_DAO.remove(self.__jogador_logado.nome)
				self.encerrar_sessao()
			else:
				self.__jogador_DAO.remove(jogador_excluir.nome)
				self.__tela_inicial.mostra_mensagem('Remover Jogador', f'Jogador "{nome_jogador}" excluido')

	def encerrar_sessao(self):
		exit()

	def add_jogador(self, nome: str):
		while True:
			try:
				self.seleciona_jogador_por_nome(nome)
			except JogadorNotFoundException:
				self.__jogador_DAO.add(Jogador(nome))
				return None
			else:
				self.__tela_inicial.mostra_mensagem('Erro', "Jogador já cadastrado")
				return None

	def lista_nomes_jogadores(self):
		lista_nomes = []
		for i in self.__jogador_DAO.get_all():
			lista_nomes.append(i.nome)
		return lista_nomes

#	def lista_jogadores_por_vitoria(self):
#		self.__tela_inicial.mostra_mensagem("Jogadores cadastrados:")
#		jogadores_ordenados = self.ordena_jogadores_vitoria(self.__jogadores_cadastrados.copy())
#		for i in jogadores_ordenados:
#			self.__tela_inicial.mostra_mensagem(f'[{i.nome}: {len(i.batalhas)} batalhas, {i.vitorias} vitórias]')

	def lista_personagens_cadastrados(self):
		personagem = self.__controlador_personagem.lista_nomes_personagens
		if personagem == 'Chave inexistente':
			raise PersonagemNotFoundException

	def seleciona_jogador_por_nome(self, nome):
		jogador = self.__jogador_DAO.get(nome)
		if jogador == 'Chave inexistente':
			raise JogadorNotFoundException
		else:
			return jogador

	def ordena_jogadores_vitoria(self, lista_ordenar):
		for i in range(len(lista_ordenar)):
		    for j in range(i+1, len(lista_ordenar)):
		        if lista_ordenar[i].vitorias <= lista_ordenar[j].vitorias:
		            temp = lista_ordenar[i]
		            lista_ordenar[i] = lista_ordenar[j]
		            lista_ordenar[j] = temp
		return lista_ordenar

	def login(self):
		while True:
			nome_usuario = self.__tela_inicial.pegar_dados_jogador("Login", "Informe seu login (digite 0 para fazer um novo cadastro):")
			if nome_usuario == "0":
				self.add_jogador(self.__tela_inicial.pegar_dados_jogador("Novo login", "Digite o nome do novo jogador: "))
			elif nome_usuario  == None or not nome_usuario:
				self.encerrar_sessao()
			else:
				try:
					jogador = self.seleciona_jogador_por_nome(nome_usuario)
				except JogadorNotFoundException as e:
					self.__tela_inicial.mostra_mensagem('Erro', e)
				else:
					self.__jogador_logado = jogador
					return jogador

	def abrir_sistema(self):
		while True:
			self.__jogador_logado = self.login()
			lista_opcoes = {1: self.editar_batalhas, 2: self.editar_parties, 3: self.editar_personagens, 
							4: self.remover_jogador, 5: self.encerrar_sessao}
			while self.__jogador_logado != None:
				opcao_selecionada = self.__tela_inicial.mostra_menu(lista_opcoes)
				if opcao_selecionada == 6:
					self.__jogador_logado = None
				elif opcao_selecionada == 'invalida':
					continue
				else:
					lista_opcoes[opcao_selecionada]()