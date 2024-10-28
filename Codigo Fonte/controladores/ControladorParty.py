from entidades.Jogador import Jogador
from entidades.Party import Party
from telas.TelaParty import TelaParty

#Controle responsavel pelas parties do jogador. Instancia a tela de personagens a ser utilizada pelo usuario
class ControladorParty():
	def __init__(self, jogador: Jogador):
		self.__tela_party = TelaParty(self)
		self.__jogador = jogador
	