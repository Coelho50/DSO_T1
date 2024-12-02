from telas.AbstractTela import AbstractTela
from excecoes.OpcaoInvalidaException import OpcaoInvalidaException
import PySimpleGUI as ui

class TelaInicial(AbstractTela):
	def __init__(self, controlador_principal):
		self.__controlador_principal = controlador_principal

	def mostra_menu(self, lista_opcoes):
		layout =[
					[ui.Text("1 - Batalhas")],
					[ui.Text("2 - Parties")],
					[ui.Text("3 - Personagens")],
					[ui.Text("4 - Listar/remover jogadores cadastrados")],
					[ui.Text("5 - Fechar aplicação")],
					[ui.Text("6 - Logout")],
					[ui.Text("O que deseja fazer?", size=(25,1)), ui.InputText()],
					[ui.Submit(), ui.Cancel()]
				]
		window = ui.Window('Menu principal').Layout(layout)		
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		opcao = self.verifica_opcao(lista_opcoes, dic_valores)
		return opcao

	def verifica_opcao(self, lista_opcoes, valores):
		while True:
			try:
				valor_lido = int(valores[0])
				if valor_lido not in lista_opcoes and valor_lido != 6:
					raise OpcaoInvalidaException
			except ValueError:
				print("Opção inválida")
				print()
			except OpcaoInvalidaException as e:
				print(e)
				print()
			else:
				return valor_lido

	def pegar_dados_jogador(self, window_name: str, msg: str):
		layout =[
					[ui.Text(msg, size = (25,1)), ui.InputText()],
					[ui.Submit(), ui.Cancel()]
				]
		window = ui.Window(window_name).Layout(layout)
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		return dic_valores[0]