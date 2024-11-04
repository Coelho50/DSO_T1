

'''
arquivo usado APENAS PARA TESTES, DEVE SER EXCLUIDO ANTES DA VERSAO FINAL
'''


#----------------- CONTROLADOR PRINCIPAL -----------------

from controladores.ControladorPrincipal import ControladorPrincipal
from entidades.Healer import Healer
from entidades.Mago import Mago
from entidades.Party import Party
from entidades.Guerreiro import Guerreiro

main_control = ControladorPrincipal()
main_control.add_jogador("Coelhasso")
main_control.add_jogador("A")
main_control.add_jogador("NoobMaster69")
main_control.add_jogador("KillerXinok")
main_control.add_jogador("SonicFox")
main_control.add_jogador("Boa noite")

main_control._ControladorPrincipal__controlador_personagem._ControladorPersonagem__personagens_cadastrados.append(Healer("Laezel", 20.0, "axe", 30.2, 40.4, 50.5))
main_control._ControladorPrincipal__controlador_personagem._ControladorPersonagem__personagens_cadastrados.append(Healer("ShadowHeart", 20.0, "axe", 30.2, 40.4, 50.5))
main_control._ControladorPrincipal__controlador_personagem._ControladorPersonagem__personagens_cadastrados.append(Guerreiro("Tracer", 20.0, "axe", 30.2, 40.4, 50.5))
main_control._ControladorPrincipal__controlador_personagem._ControladorPersonagem__personagens_cadastrados.append(Mago("Reinhardt", 20.0, "axe", 30.2, 40.4, 50.5))
main_control._ControladorPrincipal__controlador_personagem._ControladorPersonagem__personagens_cadastrados.append(Guerreiro("Smoke", 20.0, "axe", 30.2, 40.4, 50.5))
main_control._ControladorPrincipal__controlador_personagem._ControladorPersonagem__personagens_cadastrados.append(Mago("Cyrax", 20.0, "axe", 30.2, 40.4, 50.5))

joao = Healer("joao",1.0,"",1.0,1.0,1.0)
matheus = Healer("joao",1.0,"",1.0,1.0,1.0)
marcos = Healer("joao",1.0,"",1.0,1.0,1.0)
lucas = Healer("joao",1.0,"",1.0,1.0,1.0)
main_control.jogadores_cadastrados[1].add_party(Party("Curandeiros",joao,matheus,marcos,lucas))
main_control.jogadores_cadastrados[0].add_party(Party("Magos de ataque",joao,matheus,marcos,lucas))
main_control.abrir_sistema()


#----------------- CONTROLADOR DE PERSONAGEM -----------------

#char_control = ControladorPersonagem()
#
# 
#char_control.cria_personagem("Healer", "Shadowheart", 20.0, "Flail", 0.0, 12.0, 200.2)
#char_control.cria_personagem("Healer", "Shadowheart", 20.0, "Flail", 0.0, 12.0, 200.2)
#char_control.remove_personagem("Shadowheart")
#'''
#char_control.cria_personagem("Healer", "Danu", 19.0, "Cajado de gelo", 1.0, 0.0, 160.2)
#char_control.cria_personagem("Healer", "Shadowheart", 20.0, "Flail", 0.0, 12.0, 200.2)
#char_control.cria_personagem("Mago", "Gale", 14.0, "Grimorio", 5.0, 300.0, 0.0)
#char_control.cria_personagem("Guerreiro", "Karlach", 28.0, "Machado infernal", 340.55, 0.0, 0.0)
#char_control.cria_personagem("Guerreiro", "Karlach", 28.0, "Machado infernal", 340.55, 0.0, 0.0)
#char_control.cria_personagem("Healer", "Demeter", 30.0, "Pluma dos deuses", 20.0, 0.0, 400.0)
#'''
#print()
#char_control.lista_personagens("Healer")
#print()
#char_control.lista_personagens("healer")
#print()
#char_control.lista_personagens("Guerreiro")
#print()
#char_control.lista_personagens("Mago")
#
#
#'''

#--------------------- TELA PERSONAGEM ------------------------
'''
tela_personagem = TelaPersonagem(char_control)

print(tela_personagem.le_opcao(4))
'''

#def pegar_dados(msg, tipo):
#	try:
#		dado = tipo(input(msg))
#	except ValueError:
#		print(f'Dado passado deve ser do tipo {tipo}')
#
#pegar_dados("bla", str)