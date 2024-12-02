from abc import ABC, abstractmethod

class AbstractTela(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def mostra_menu():
		pass

#	@abstractmethod
#	def verifica_opcao():
#		pass

	def mostra_mensagem(self,msg):
		print(msg)
	