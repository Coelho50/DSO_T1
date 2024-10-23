from entidades.Personagem import Personagem
from entidades.Healer import Healer
from entidades.Mago import Mago
from entidades.Guerreiro import Guerreiro
from telas.TelaPersonagem import TelaPersonagem

#Controle responsavel pela lista de personagens. Instancia a tela de personagens a ser utilizada pelo usuario
class ControladorPersonagem:
	def __init__(self, controlador_principal):
		self.__tela_personagem = TelaPersonagem(self)
		self.__personagens_cadastrados = []

	'''
	Personagens devem ter HP > 1 e nao podem ter nome repetido
	Guerreiros devem ter DPS > 1 e nao possuem mana ou hps
	Magos devem ter mana > 1, caso possuam DPS, esse nao pode ser negativo
	Healers devem ter HPS > 1, caso possuam DPS ou mana, esse nao pode ser negativo
	Caso um healer ou um mago nao possua algum dos parametros opcionais a suas classes,
	esses devem ser iguais a 0
	Todos os valores devem ser passados como float
	'''
	def cria_personagem(self, classe: str, nome: str, hp: float, item: str, dps: float = 0, mana: float = 0, hps: float = 0):
		#checando por nome repetido
		for char in self.__personagens_cadastrados:
			if char.nome == nome:
				print(f'Personagem com nome {nome} já adicionado a lista')
				return None
		if not isinstance(classe, str):
			raise ValueError("O nome da classe deve ser uma string")
		elif classe == "Guerreiro":
			if not isinstance(nome, str):
				raise ValueError("Nome de um guerreiro deve ser uma string")
			elif not isinstance(hp, float) and not isinstance(hp, int) or hp < 1:
				raise ValueError("HP de um guerreiro deve ser um número e maior que 1") 
			elif not isinstance(item, str): 
				raise ValueError("Item de um guerreiro deve ser declarado como uma string")
			elif not isinstance(dps, float) and not isinstance(dps, int) or dps < 1:
				raise ValueError("DPS de um guerreiro deve ser um número e maior que 1")
			elif mana != 0 or hps != 0:
				raise ValueError("Guerreiros não possuem mana ou HPS!")
			else:
				self.__personagens_cadastrados.append(Guerreiro(nome, hp, item, dps))
				print(f'Guerreiro(a) {nome} adicionado à lista')
		elif classe == "Mago":
			if not isinstance(nome, str):
				raise ValueError("Nome de um mago deve ser uma string")
			elif not isinstance(hp, float) and not isinstance(hp, int) or hp < 1:
				raise ValueError("HP de um mago deve ser um número e maior que 1") 
			elif not isinstance(item, str): 
				raise ValueError("Item de um mago deve ser declarado como uma string")
			elif not isinstance(dps, float) and not isinstance(dps, int) or dps < 0:
				raise ValueError("DPS de um mago deve ser um número não negativo")
			elif not isinstance(mana, float) and not isinstance(mana, int) or mana < 1:
				raise ValueError("Mana de um mago deve ser um número maior que 1")
			elif hps != 0:
				raise ValueError("Magos não possuem HPS!")
			else:
				self.__personagens_cadastrados.append(Mago(nome, hp, item, dps, mana))
				print(f'Mago(a) {nome} adicionado à lista')
		elif classe == "Healer":
			if not isinstance(nome, str):
				raise ValueError("Nome de um healer deve ser uma string")
			elif not isinstance(hp, float) and not isinstance(hp, int) or hp < 1:
				raise ValueError("HP de um healer deve ser um número e maior que 1") 
			elif not isinstance(item, str): 
				raise ValueError("Item de um healer deve ser declarado como uma string")
			elif not isinstance(dps, float) and not isinstance(dps, int) or dps < 0:
				raise ValueError("DPS de um healer deve ser um número não negativo")
			elif not isinstance(mana, float) and not isinstance(mana, int) or mana < 0:
				raise ValueError("Mana de um healer deve ser um número não negativo")
			elif not isinstance (hps, float) and not isinstance(hps, int) or hps < 1:
				raise ValueError("HPS de um healer deve ser um número maior que 1")
			else:
				self.__personagens_cadastrados.append(Healer(nome, hp, item, dps, mana, hps))
				print(f'Healer {nome} adicionado à lista')

	#remove um personagem da lista apenas utilizando seu nome como referencia
	def remove_personagem(self, nome):
		for char in self.__personagens_cadastrados:
			if char.nome == nome:
				self.__personagens_cadastrados.remove(char)
				print(f'{char.nome} removido(a) da lista')

	'''
	caso seja passada algum nome de classe, serao retornados apenas os nomes de personagens da classe passada
	caso nao, serao retornados
	'''
	def lista_personagens(self, classe = 'all'):
		vazio = True
		if len(self.__personagens_cadastrados) == 0:
			print("Ainda não foram adicionados personagens")
		elif classe == 'all':
			for char in self.__personagens_cadastrados:
				if char.classe == 'Healer':
					print(f'{char.nome}: {char.hp} HP, {char.dps} DPS, {char.mana} Mana, {char.hps} HPS, item: {char.item}')
					vazio = False				
				if char.classe == 'Mago':
					print(f'{char.nome}: {char.hp} HP, {char.dps} DPS, {char.mana} Mana, item: {char.item}')
					vazio = False				
				if char.classe == 'Guerreiro':
					print(f'{char.nome}: {char.hp} HP, {char.dps} DPS, item: {char.item}')
					vazio = False
		elif classe == 'Guerreiro' or classe == 'Mago' or classe == 'Healer':
			for char in self.__personagens_cadastrados:
				if char.classe == classe:
					if char.classe == 'Healer':
						print(f'{char.nome}: {char.hp} HP, {char.dps} DPS, {char.mana} Mana, {char.hps} HPS, item: {char.item}')
						vazio = False				
					elif char.classe == 'Mago':
						print(f'{char.nome}: {char.hp} HP, {char.dps} DPS, {char.mana} Mana, item: {char.item}')
						vazio = False				
					elif char.classe == 'Guerreiro':
						print(f'{char.nome}: {char.hp} HP, {char.dps} DPS, item: {char.item}')
						vazio = False
			if vazio:
				print(f'Ainda não há personagens da classe {classe} na lista')
		else:
			print("Classe inválida")
