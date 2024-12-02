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
matheus = Healer("matheus",1.0,"",1.0,1.0,1.0)
marcos = Healer("marcos",1.0,"",1.0,1.0,1.0)
lucas = Healer("lucas",1.0,"",1.0,1.0,1.0)

main_control._ControladorPrincipal__jogadores_cadastrados[0]._Jogador__vitorias = 32
main_control._ControladorPrincipal__jogadores_cadastrados[1]._Jogador__vitorias = 63
main_control._ControladorPrincipal__jogadores_cadastrados[2]._Jogador__vitorias = 54
main_control._ControladorPrincipal__jogadores_cadastrados[3]._Jogador__vitorias = 12
main_control._ControladorPrincipal__jogadores_cadastrados[4]._Jogador__vitorias = 60

main_control.jogadores_cadastrados[1].add_party(Party("Curandeiros",joao,matheus,marcos,lucas))
main_control.jogadores_cadastrados[0].add_party(Party("Magos de ataque",joao,matheus,marcos,lucas))

main_control.abrir_sistema()


#------------------- PARTE 2 ---------------------

#-------------------  GUI    --------------------
'''
layout =[
			[ui.Text("Cadastro")],
			[ui.Text("Nome do novo cadastro: ", size = (25,1)), ui.InputText()],
			[ui.Text("Nome do novo cadastro2: ", size = (25,1)), ui.InputText()],
			[ui.Submit(), ui.Cancel()]
		]

window = ui.Window('Cadastro novo').Layout(layout)

button, values = window.Read()

print(button)
print(values)
'''