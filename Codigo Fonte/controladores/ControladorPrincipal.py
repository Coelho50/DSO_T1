from telas.TelaInicial import TelaInicial
from entidades.Jogador import Jogador
from controladores.ControladorPersonagem import ControladorPersonagem
from controladores.ControladorParty import ControladorParty
from controladores.ControladorBatalha import ControladorBatalha
from excecoes.JogadorNotFoundException import JogadorNotFoundException

class ControladorPrincipal:

	def __init__(self):
		self.__jogadores_cadastrados = []
		self.__jogador_logado = None
		self.__controlador_personagem = ControladorPersonagem(self)
		self.__controlador_party = ControladorParty(self)
		self.__controlador_batalhas = ControladorBatalha(self)
		self.__tela_inicial = TelaInicial(self)

	@property
	def jogador_logado(self):
		return self.__jogador_logado

	@property
	def jogadores_cadastrados(self):
		return self.__jogadores_cadastrados

	def editar_batalhas(self):
		self.__controlador_batalhas.abrir_menu()

	def editar_parties(self):
		self.__controlador_party.abrir_menu()

	def editar_personagens(self):
		self.__controlador_personagem.abrir_menu()

	def remover_jogador(self):
		self.lista_jogadores_por_vitoria()
		while True:
			try:
				nome_jogador = self.__tela_inicial.pegar_dados_jogador("Digite o nome caso queira remover um jogador (0 para retornar ao menu principal): ")
				if nome_jogador == '0':
					return None
				if nome_jogador == self.__jogador_logado.nome:
					raise Exception
				jogador_excluir = self.seleciona_jogador_por_nome(nome_jogador)
			except JogadorNotFoundException as e:
				self.__tela_inicial.mostra_mensagem(e)
			except Exception:
				self.__tela_inicial.mostra_mensagem("Excluindo o cadastro e encerrando sessão...")
				self.__jogadores_cadastrados.remove(self.__jogador_logado)
				self.encerrar_sessao()
			else:
				self.__jogadores_cadastrados.remove(jogador_excluir)
				self.__tela_inicial.mostra_mensagem(f'Jogador "{nome_jogador}" excluido')

	def encerrar_sessao(self):
		self.__tela_inicial.mostra_mensagem("Sessão encerrada.")
		exit()

	def add_jogador(self, nome: str):
		while True:
			try:
				self.seleciona_jogador_por_nome(nome)
			except JogadorNotFoundException:
				self.__jogadores_cadastrados.append(Jogador(nome))
				self.__tela_inicial.mostra_mensagem(f'{nome} cadastrado')
				return None
			else:
				self.__tela_inicial.mostra_mensagem("Jogador já cadastrado")
				return None

	def lista_jogadores_por_vitoria(self):
		self.__tela_inicial.mostra_mensagem("Jogadores cadastrados:")
		jogadores_ordenados = self.ordena_jogadores_vitoria(self.__jogadores_cadastrados.copy())
		for i in jogadores_ordenados:
			self.__tela_inicial.mostra_mensagem(f'[{i.nome}: {len(i.batalhas)} batalhas, {i.vitorias} vitórias]')

	def lista_personagens_cadastrados(self):
		return self.__controlador_personagem.personagens_cadastrados

	def seleciona_jogador_por_nome(self, nome):
		for jogador in self.__jogadores_cadastrados:
			if jogador.nome == nome:
				return jogador
		raise JogadorNotFoundException

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
			nome_usuario = self.__tela_inicial.pegar_dados_jogador("Login", "Informe seu login(Digite 0 para fazer um novo cadastro):")
			try:
				if nome_usuario == "0":
					raise Exception
				jogador = self.seleciona_jogador_por_nome(nome_usuario)
			except JogadorNotFoundException as e:
				self.__tela_inicial.mostra_mensagem(e)
			except Exception:
				self.add_jogador(self.__tela_inicial.pegar_dados_jogador("Digite o nome do novo jogador: "))
			else:
				self.__tela_inicial.mostra_mensagem(f'Bem vindo, {jogador.nome}')
				self.__jogador_logado = jogador
				return jogador

	def abrir_sistema(self):
		while True:
			self.__jogador_logado = self.login()
			lista_opcoes = {1: self.editar_batalhas, 2: self.editar_parties, 3: self.editar_personagens, 
							4: self.remover_jogador, 5: self.encerrar_sessao}
			while self.__jogador_logado != None:
				opcao_selecionada = self.__tela_inicial.mostra_menu(lista_opcoes)
				if opcao_selecionada == 6: #--------------> perguntar pro professor uma maneira melhor
					self.__jogador_logado = None
				else:
					lista_opcoes[opcao_selecionada]()