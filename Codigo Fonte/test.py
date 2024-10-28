from controladores.ControladorPrincipal import ControladorPrincipal
from controladores.ControladorPersonagem import ControladorPersonagem
from entidades.Personagem import Personagem
from entidades.Healer import Healer
from entidades.Mago import Mago
from entidades.Guerreiro import Guerreiro
from telas.TelaPersonagem import TelaPersonagem

'''
arquivo usado APENAS PARA TESTES, DEVE SER EXCLUIDO ANTES DA VERSAO FINAL
'''


#----------------- CONTROLADOR PRINCIPAL -----------------

main_control = ControladorPrincipal()


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