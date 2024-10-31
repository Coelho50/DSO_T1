from telas.TelaInicial import TelaInicial
from entidades.Jogador import Jogador
from controladores.ControladorPersonagem import ControladorPersonagem
from controladores.ControladorParty import ControladorParty
from controladores.ControladorBatalha import ControladorBatalha
from excecoes.JogadorNotFoundException import JogadorNotFoundException

class ControladorPrincipal:

	def __init__(self):
		self.__jogadores_cadastrados = []
		self.__controlador_personagem = ControladorPersonagem(self)
		self.__controlador_party = ControladorParty(self,self.__controlador_personagem.lista_personagens)
		self.__controlador_batalhas = ControladorBatalha(self)
		self.__tela_inicial = TelaInicial(self)
		self.__jogador_logado = None

	def editar_batalhas(self):
		self.__controlador_batalhas.abrir_menu()

	def editar_parties(self):
		print("Gostaria de editar as parties de qual jogador?")
		self.lista_jogadores_cadastrados()
		while True:
			try:
				nome_jogador = self.__tela_inicial.pegar_dados_jogador("Nome do jogador(digite 0 para retornar):")
				if nome_jogador == "0":
					return None
				self.__controlador_party.jogador = self.seleciona_jogador_por_nome(nome_jogador)
				self.__controlador_party.abrir_menu()
				break
			except JogadorNotFoundException as e:
				print(e)
		
		

	def editar_personagens(self):
		self.__controlador_personagem.abrir_menu()

	def remover_jogador(self):
		self.lista_jogadores_cadastrados()
		while True:
			try:
				nome_jogador = self.__tela_inicial.pegar_dados_jogador("Nome do jogador a ser modificado(digite 0 para retornar):")
				if nome_jogador == '0':
					return None
				if nome_jogador == self.__jogador_logado.nome:
					raise Exception
				jogador_excluir = self.seleciona_jogador_por_nome(nome_jogador)
			except JogadorNotFoundException as e:
				print(e)
			except Exception:
				print("Excluindo o cadastro e encerrando sessão...")
				self.__jogadores_cadastrados.remove(self.__jogador_logado)
				self.encerrar_sessao()
			else:
				self.__jogadores_cadastrados.remove(jogador_excluir)
				print(f'Jogador "{nome_jogador}" excluido')

	def encerrar_sessao(self):
		print("Sessão encerrada.")
		exit()

	def abrir_sistema(self):
		self.__jogador_logado = self.login()
		lista_opcoes = {1: self.editar_batalhas, 2: self.editar_parties, 3: self.editar_personagens, 
						4: self.remover_jogador, 5: self.encerrar_sessao}
		while True:
			opcao_selecionada = self.__tela_inicial.mostra_menu(lista_opcoes)
			lista_opcoes[opcao_selecionada]()

	def add_jogador(self, nome: str):
		while True:
			try:
				self.seleciona_jogador_por_nome(nome)
			except JogadorNotFoundException:
				self.__jogadores_cadastrados.append(Jogador(nome))
				print(f'{nome} cadastrado')
				return None
			else:
				print("Jogador já cadastrado")
				return None

	def lista_jogadores_cadastrados(self):
		print("Jogadores cadastrados:")
		for i in self.__jogadores_cadastrados:
			print(f'[{i.nome}]')

	def seleciona_jogador_por_nome(self, nome):
		for jogador in self.__jogadores_cadastrados:
			if jogador.nome == nome:
				return jogador
		raise JogadorNotFoundException

	def login(self):
		while True:
			nome_usuario = self.__tela_inicial.pegar_dados_jogador("Login (digite 0 para cadastrar um novo jogador): ")
			try:
				if nome_usuario == "0":
					raise Exception
				jogador = self.seleciona_jogador_por_nome(nome_usuario)
			except JogadorNotFoundException as e:
				print(e)
			except Exception:
				self.add_jogador(self.__tela_inicial.pegar_dados_jogador("Digite o nome do novo jogador: "))
			else:
				print(f'Bem vindo, {jogador.nome}')
				print()
				return jogador