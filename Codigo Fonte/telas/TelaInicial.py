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
					[ui.Text("O que deseja fazer?", size=(20,1)), ui.InputText()],
					[ui.Submit(), ui.Exit()]
				]
		window = ui.Window('Menu principal').Layout(layout)
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
				if valor_lido not in lista_opcoes and valor_lido != 6:
					raise OpcaoInvalidaException
			except ValueError:
				super().mostra_mensagem('Erro', 'Opção inválida')
				return 'invalida'
			except OpcaoInvalidaException as e:
				super().mostra_mensagem('Erro', e)
				return 'invalida'
			else:
				return valor_lido

	def pegar_dados_jogador(self, window_name: str, msg: str):
		layout =[
					[ui.Text(msg, size = (len(msg),1)), ui.InputText()],
					[ui.Submit(), ui.Exit()]
				]
		window = ui.Window(window_name).Layout(layout)
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		return dic_valores[0]

	def tela_remocao_jogador(self, lista_jogadores):
		list_box = ui.Listbox(lista_jogadores, size=(70,20), expand_y = True)
		layout =[
					[ui.Text("Jogador a ser removido:", size=(20,1)), ui.InputText(), ui.Submit(), ui.Exit()],
					[list_box]
				]
		window = ui.Window('Remover jogador').Layout(layout)
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		if button == 'Exit':
			return None
		return dic_valores[0]
