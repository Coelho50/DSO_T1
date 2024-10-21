from Party import Party

#Controle responsavel pelas parties do jogador. Instancia a tela de personagens a ser utilizada pelo usuario
class ControladorParty():
	def __init__(self):
		self.__tela_party = TelaParty(self)