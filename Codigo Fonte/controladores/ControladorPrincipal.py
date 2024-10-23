from telas.TelaPrincipal import TelaPrincipal
from controladores.ControladorPersonagem import ControladorPersonagem
from controladores.ControladorParty import ControladorParty
#from controladores.ControladorBatalhas import Controlador -> ainda nao implementado

class ControladorPrincipal:

	def __init__(self):
		self.__controlador_personagem = ControladorPersonagem(self)
		self.__controlador_party = ControladorParty(self)
		#self__controlador_batalhas = controlador_batalha -> ainda nao implementado
		self.__tela_inicial = TelaInicial(self)

		