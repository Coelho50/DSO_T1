from abc import ABC, abstractmethod
import PySimpleGUI as ui

class AbstractTela(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def mostra_menu():
		pass

#	@abstractmethod  -------> manter comentado até que seja implementado em todas as classes
#	def verifica_opcao():
#		pass

	def mostra_mensagem(self, header, msg):
		layout =[
					[ui.Text(msg)],
					[ui.Exit()]
				]
		dic_valores = 0
		while dic_valores == 0:
			window = ui.Window(header).Layout(layout)		
			button, dic_valores = window.Read()
		window.CloseNonBlocking()
	