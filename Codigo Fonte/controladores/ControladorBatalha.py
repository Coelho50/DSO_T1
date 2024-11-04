from entidades.Batalha import Batalha
from entidades.Jogador import Jogador
from excecoes.BatalhaNotFoundException import BatalhaNotFoundException
from excecoes.JogadorNotFoundException import JogadorNotFoundException
from excecoes.PartyNotFoundException import PartyNotFoundException
from telas.TelaBatalha import TelaBatalha


class ControladorBatalha():
	def __init__(self, controlador_principal):
		self.__tela_batalha = TelaBatalha(self)
		self.__controlador_principal = controlador_principal
		self.__jogador1 = Jogador
		self.__jogadores = controlador_principal.jogadores_cadastrados

	def cria_batalha(self):
			self.__tela_batalha.mostra_mensagem("--------- CRIAÇÃO DE BATALHA ---------")
			while True:
				jogador2 = self.verificador(self.__jogadores,"Quem é o jogador adversário?(digite '0' para cancelar)",JogadorNotFoundException)
				if jogador2 == None:
					return None
				elif jogador2 == self.__jogador1:
					self.__tela_batalha.mostra_mensagem("Jogador não pode batalhar contra sigo mesmo!")
				else:
					break
			party1 = self.verificador(self.__jogador1.parties,"Qual a sua party?(digite '0' para cancelar)",PartyNotFoundException)
			if party1 == None:
				return None
			party2 = self.verificador(jogador2.parties,"Qual a party do adversário?(digite '0' para cancelar)",PartyNotFoundException)
			if party2 == None:
				return None
			vencedor = self.verificador([self.__jogador1, jogador2],"Quem ganhou a batalha?", JogadorNotFoundException)
			if vencedor == None:
				return None
			b = Batalha(self.__jogador1, jogador2, party1, party2, vencedor)
			self.__jogador1.add_batalha(b)
			jogador2.add_batalha(b)
			self.__tela_batalha.mostra_mensagem("batalha criada!")

	def remove_batalha(self):
		while True:
			try:
				self.__tela_batalha.mostra_mensagem("Qual batalha deseja remover?(digite '0' para cancelar)")
				self.lista_batalhas()
				n = self.__tela_batalha.pegar_dados("N° da batalha: ", int)
				if n == "0":
						return None
				elif n > 0 and n <= len(self.__jogador1.batalhas):
					b = self.__jogador1.batalhas[n-1]
					j1 = self.__jogador1.batalhas[n-1].jogador_1 # O jogador logado pode estar na primeira ou segunda posição
					j2 = self.__jogador1.batalhas[n-1].jogador_2 # Se remover o jogador logado primeiro não será possível remover o segundo
					j1.remove_batalha(b)
					j2.remove_batalha(b)
					self.__tela_batalha.mostra_mensagem("Batalha removida!")
					return None
				else:
					raise BatalhaNotFoundException
			except BatalhaNotFoundException as e:
				self.__tela_batalha.mostra_mensagem(e)
		
	def lista_batalhas(self):
		self.__tela_batalha.mostra_mensagem("------------ BATALHAS DO JOGADOR ------------")
		c = 1
		for b in self.__jogador1.batalhas:
			self.__tela_batalha.mostra_mensagem(f"{c}° Batalha")
			self.__tela_batalha.mostra_mensagem(f"{b.jogador_1.nome}({b.party_1.nome}) X {b.jogador_2.nome}({b.party_2.nome})")
			self.__tela_batalha.mostra_mensagem(f"Vencedor: {b.vencedor.nome}")
			self.__tela_batalha.mostra_mensagem("-----------------------------------")
		self.__tela_batalha.mostra_mensagem(f"Número total de batalhas: {len(self.__jogador1.batalhas)}")
		self.__tela_batalha.mostra_mensagem(f"Vitórias: {self.__jogador1.vitorias}")

	def abrir_menu(self):
		self.__jogador1 = self.__controlador_principal.jogador_logado
		lista_opcoes = {1: self.cria_batalha, 2: self.remove_batalha, 3: self.lista_batalhas}
		while True:
			opcao_selecionada = self.__tela_batalha.mostra_menu(lista_opcoes)
			if opcao_selecionada == 4:
				return 0
			else:
				lista_opcoes[opcao_selecionada]()

	def verificador(self, lista, mensagem, exception):
		while True:
			try:
				self.__tela_batalha.mostra_mensagem(mensagem)
				inp = self.__tela_batalha.pegar_dados("Nome: ", str)
				if inp == "0":
					return None
				for i in lista:
					if i.nome == inp:
						return i
				raise exception
			except exception as e:
				self.__tela_batalha.mostra_mensagem(e)