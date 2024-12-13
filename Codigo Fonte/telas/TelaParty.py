from excecoes.OpcaoInvalidaException import OpcaoInvalidaException
from telas.AbstractTela import AbstractTela
import PySimpleGUI as ui
from excecoes.PersonagemNotFoundException import PersonagemNotFoundException

class TelaParty(AbstractTela):
	def __init__(self, controlador_party):
		self.__controlador_party = controlador_party


	def mostra_menu(self, lista_opcoes):
		layout =[
						[ui.Text("1 - Criar nova party")],
						[ui.Text("2 - Excluir party")],
						[ui.Text("3 - Listar parties")],
						[ui.Text("4 - Retornar ao menu principal")],
						[ui.Text("O que deseja fazer?", size=(20,1)), ui.InputText()],
						[ui.Submit(), ui.Exit()]
					]
		window = ui.Window('Parties').Layout(layout)
		button, dic_valores = window.Read()
		window.CloseNonBlocking()
		if button == 'Exit':
			dic_valores[0] = 5
		opcao = self.verifica_opcao(lista_opcoes, dic_valores)
		return opcao

	def menu_criacao_party(self, personagens):
		layout =[
					[ui.Text("Nome da party: ", size=(10,1)), ui.InputText()],
					[ui.Text("1° Personagem", size=(10,1)), ui.InputText()],
					[ui.Text("2° Personagem", size=(10,1)), ui.InputText()],
					[ui.Text("3° Personagem", size=(10,1)), ui.InputText()],
					[ui.Text("4° Personagem", size=(10,1)), ui.InputText()],
					[ui.Submit(), ui.Button('Return')]
				]
		window = ui.Window('Criação de party').Layout(layout)
		while True:
				button, dic_valores = window.Read()
				if button == 'Return':
					window.CloseNonBlocking()
					return None
				try:
					p1 = self.verificador(dic_valores[1], personagens, PersonagemNotFoundException)
					p2 = self.verificador(dic_valores[2], personagens, PersonagemNotFoundException)
					p3 = self.verificador(dic_valores[3], personagens, PersonagemNotFoundException)
					p4 = self.verificador(dic_valores[4], personagens, PersonagemNotFoundException)
				except:
					continue
				if p1 != None and p2 != None and p3 != None and p4 != None:
					break
		window.CloseNonBlocking()
		return [dic_valores[0], p1, p2, p3, p4]


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
				if i.nome == nome:
					return i
			raise exception
		except exception as e:
			super().mostra_mensagem("Erro", f"{e}{nome}")
			return None

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