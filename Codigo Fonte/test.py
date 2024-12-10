#----------------- CONTROLADOR PRINCIPAL -----------------

from controladores.ControladorPrincipal import ControladorPrincipal
from entidades.Healer import Healer
from entidades.Mago import Mago
from entidades.Party import Party
from entidades.Guerreiro import Guerreiro
import PySimpleGUI as ui

main_control = ControladorPrincipal()
main_control.abrir_sistema()

