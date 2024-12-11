from telas.AbstractTela import AbstractTela
from excecoes.OpcaoInvalidaException import OpcaoInvalidaException
from excecoes.ClasseInvalidaException import ClasseInvalidaException
from excecoes.PersonagemJaAddException import PersonagemJaAddException
import PySimpleGUI as ui

class TelaPersonagem(AbstractTela):
	def __init__(self, controlador_personagem):
		self.__controlador_personagem = controlador_personagem

	def mostra_menu(self, lista_opcoes):
		layout =[
					[ui.Text("1 - Criar novo personagem")],
					[ui.Text("2 - Excluir personagens")],
					[ui.Text("3 - Listar personagens")],
					[ui.Text("4 - Retornar ao menu principal")],
					[ui.Text("O que deseja fazer?", size=(20,1)), ui.InputText()],
					[ui.Submit(), ui.Button('Return')]
				]
		window = ui.Window('Menu de personagens').Layout(layout)
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		if button == 'Return':
			dic_valores[0] = 4
		opcao = self.verifica_opcao(lista_opcoes, dic_valores)
		return opcao

	def menu_criacao_personagem(self):
		list_box = ui.Listbox(['Healer', 'Mago', 'Guerreiro'],
								size=(10,5),
								expand_y = True)
		layout =[
					[ui.Text("Insira abaixo os dados requisitador para criar o novo personagem")],
					[ui.Text("Nome do personagem: ", size=(20,1)), ui.InputText()],
					[ui.Text("Classe: ", size=(10,1)), ui.InputText()],
					[list_box],
					[ui.Text("HP: ", size=(10,1)), ui.InputText()],
					[ui.Text("Item: ", size=(10,1)), ui.InputText()],
					[ui.Text("DPS: ", size=(10,1)), ui.InputText()],
					[ui.Text("Mana: ", size=(10,1)), ui.InputText()],
					[ui.Text("HPS: ", size=(10,1)), ui.InputText()],
					[ui.Submit(), ui.Button('Return')]
				]
		window = ui.Window('Criação de personagem').Layout(layout)
		while True:
				button, dic_valores = window.Read()
				if button == 'Return':
					window.CloseNonBlocking()
					return None
				try:
					self.verifica_valores(dic_valores)
				except PersonagemJaAddException:
					super().mostra_mensagem('Erro', 'Personagem de mesmo nome já adicionado')
				except ClasseInvalidaException:
					super().mostra_mensagem('Erro', 'Classe deve ser Healer, Mago ou Guerreiro')
				except ValueError:
					super().mostra_mensagem('Erro', 'Todos os atributos devem ser números maiores ou iguais a 0')
				else:
					window.CloseNonBlocking()
					return dic_valores

	def menu_remover_personagem(self, lista_personagens):
		list_box = ui.Listbox(lista_personagens, size=(70,20), expand_y = True)
		layout =[
					[ui.Text("Personagem a ser removido:", size=(20,1)), ui.InputText(), ui.Submit(), ui.Button('Return')],
					[list_box]
				]
		window = ui.Window('Remover personagem').Layout(layout)
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		if button == 'Return':
			return None
		return dic_valores[0]

	def menu_lista_personagens(self, lista_personagens):
		list_box = ui.Listbox(lista_personagens, size=(70,20), expand_y = True)
		layout =[
					[ui.Text("Filtrar por classe(Todos, Mago, Healer, Guerreiro): ", size=(37,1)), ui.InputText(), ui.Submit(), ui.Button('Return')],
					[list_box]
				]
		window = ui.Window('Lista de personagens').Layout(layout)
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		if button == 'Return':
			return None
		return dic_valores[0]

	#deve ser passado para a funcao a lista de opcoes a serem escolhidas
	def verifica_opcao(self, lista_opcoes, valores):
		valor_lido = valores[0]
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

	def verifica_valores(self, dic_valores):
			classes = ['Healer', 'Mago', 'Guerreiro']
			self.__controlador_personagem.verif_nome_repetido(dic_valores[0]) #->pode disparar PersonagemJaAddException
			if dic_valores[1] not in classes:
				raise ClasseInvalidaException
			for i in range(3, len(dic_valores)):
				if i != 4:
					dic_valores[i] = float(dic_valores[i])
					if dic_valores[i] < 0:
						raise ValueError
			return None

	#passar o tipo do dado que deve ser devolvido e uma mensagem para pedir mostrar ao usuario
	def pegar_dados(self, msg, tipo):
		while True:
			try:
				dado = tipo(input(msg))
			except ValueError:
				print(f'Dado passado deve ser do tipo {tipo}')
			else:
				return dado