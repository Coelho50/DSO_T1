from excecoes.OpcaoInvalidaException import OpcaoInvalidaException
from telas.AbstractTela import AbstractTela
import PySimpleGUI as ui
from excecoes.BatalhaNotFoundException import BatalhaNotFoundException
from excecoes.JogadorNotFoundException import JogadorNotFoundException
from excecoes.PartyNotFoundException import PartyNotFoundException


class TelaBatalha(AbstractTela):
	def __init__(self, controlador_batalha):
		self.__controlador_batalha = controlador_batalha


	def mostra_menu(self, lista_opcoes):
		layout =[
						[ui.Text("1 - Criar nova batalha")],
						[ui.Text("2 - Excluir batalha")],
						[ui.Text("3 - Listar batalhas")],
						[ui.Text("4 - Retornar ao menu principal")],
						[ui.Text("O que deseja fazer?", size=(20,1)), ui.InputText()],
						[ui.Submit(), ui.Exit()]
					]
		window = ui.Window('Batalhas').Layout(layout)
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		if button == 'Exit':
			dic_valores[0] = 5
		opcao = self.verifica_opcao(lista_opcoes, dic_valores)
		return opcao
	
	def verifica_opcao(self, lista_opcoes, valores):
		while True:
			try:
				valor_lido = int(valores[0])
				if valor_lido not in lista_opcoes and valor_lido != 4:
					raise OpcaoInvalidaException
			except ValueError:
				super().mostra_mensagem('Erro', 'Opção inválida')
				return 'invalida'
			except OpcaoInvalidaException as e:
				super().mostra_mensagem('Erro', e)
				return 'invalida'
			else:
				return valor_lido
			
	def menu_criacao_batalha(self, jogador1, jogadores):
		layout =[
					[ui.Text("Insira abaixo os dados para criar uma nova batalha")],
					[ui.Text("Jogador adversário: ", size=(10,1)), ui.InputText()],
					[ui.Text("Sua party: ", size=(10,1)), ui.InputText()],
					[ui.Text("Party do adversário: ", size=(10,1)), ui.InputText()],
					[ui.Text("Vencedor da batalha: ", size=(10,1)), ui.InputText()],
					[ui.Submit(), ui.Button('Return')]
				]
		window = ui.Window('Criação de batalha').Layout(layout)
		while True:
				button, dic_valores = window.Read()
				if button == 'Return':
					window.CloseNonBlocking()
					return None
				if dic_valores[0] == jogador1:
					super().mostra_mensagem("Erro", "Jogador não pode batalhar contra sigo mesmo!")
				try:
					jogador2 = self.verificador(dic_valores[0], jogadores, JogadorNotFoundException)
					party1 = self.verificador(dic_valores[1], jogador1.parties, PartyNotFoundException)
					party2 = self.verificador(dic_valores[2], dic_valores[0].parties, PartyNotFoundException)
					vencedor = self.verificador(dic_valores[3], [dic_valores[0], jogador1], JogadorNotFoundException)
				except:
					continue
				if jogador2 != None and party1 != None and party2 != None and vencedor != None:
					break
		window.CloseNonBlocking()
		return [jogador1, jogador2, party1, party2, vencedor]
			
	def le_opcao(self, lista_opcoes):
		while True:
			print("O que você deseja fazer?")
			try:
				opcao = int(input(':'))
				if opcao not in lista_opcoes and opcao != 4:
					raise OpcaoInvalidaException
			except ValueError:
				print("Opção inválida")
				print()
			except OpcaoInvalidaException as e:
				print(e)
				print()
			else:
				return opcao
			
	def pegar_dados(self, msg, tipo):
		while True:
			try:
				dado = tipo(input(msg))
			except ValueError:
				print(f'Dado passado deve ser do tipo {tipo}')
			else:
				return dado

	def verificador(self, nome, lista, exception):
		try:
			for i in lista:
				print(i.nome)
				if i.nome == nome:
					return i
			raise exception
		except exception as e:
			super().mostra_mensagem("Erro", e)
			return False
