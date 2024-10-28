from entidades.Jogador import Jogador
from entidades.Party import Party
from excecoes import GrupoCheioException
from telas.TelaParty import TelaParty

#Controle responsavel pelas parties do jogador. Instancia a tela de personagens a ser utilizada pelo usuario
class ControladorParty():
	def __init__(self, jogador: Jogador):
		self.__tela_party = TelaParty(self)
		self.__jogador = jogador
	
	def cria_party(self, nome: str, personagens: list):
		try:
			self.__jogador.add_parties(Party(personagens))
		except ValueError:
			pass
		except GrupoCheioException:
			pass

	def remover_party(self, nome:str):
		try:
			self.__jogador.remove_party(nome)
		except:
			pass
		
	def listar_parties(self):
		return self.__jogador.parties
	