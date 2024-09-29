import utils
import time
import numpy as np
import random

def interfaz_del_juego(idioma):

    print(utils.traducciones[idioma]["bienvenida"])
    time.sleep(1)
    utils.dibujar_batalla_barcos()
    time.sleep(2)

    while True:
        modo = input(utils.traducciones[idioma]["elige_modo"]).lower()
        if modo == utils.traducciones[idioma]["corto"] or modo == utils.traducciones[idioma]["largo"]:
            break
        else:
            print(utils.traducciones[idioma]["modo_no_valido"])

    print(utils.traducciones[idioma]["creando_tablero"])
    time.sleep(1)

    #Crear tableros
    tablero_usuario = utils.crear_tablero(10)
    tablero_maquina = utils.crear_tablero(10)

    #Crear flotas
    if modo == utils.traducciones[idioma]["corto"]:
        flota_usuario = utils.crear_flota(tablero_usuario, [1] *6)
        flota_maquina = utils.crear_flota(tablero_maquina, [1] *6)
    elif modo == utils.traducciones[idioma]["largo"]:
        flota_usuario = utils.crear_flota(tablero_usuario, [2,2,2,3,3,4])
        flota_maquina = utils.crear_flota(tablero_maquina, [2,2,2,3,3,4])

    #Colocar flotas
    utils.colocar_flota(flota_usuario,tablero_usuario)
    utils.colocar_flota(flota_maquina,tablero_maquina)

    time.sleep(0.5)
    print(utils.traducciones[idioma]["tu_tablero"])
    utils.mostrar_tablero(tablero_usuario)

    while True: 
        respuesta = input(utils.traducciones[idioma]["te_gusta_el_tablero"]).lower()    
        if respuesta == "true":
            print(utils.traducciones[idioma]["jugaras_con_este"])
            break
        else:
            time.sleep(0.5)
            tablero_usuario = utils.crear_tablero(10)
            if modo == utils.traducciones[idioma]["corto"]:
                flota_usuario = utils.crear_flota(tablero_usuario, [1] * (6))
            else:
                flota_usuario = utils.crear_flota(tablero_usuario, [2, 2, 2, 3, 3, 4])
            utils.colocar_flota(flota_usuario,tablero_usuario)  
            print(utils.traducciones[idioma]["nuevo_tablero_generado"])
            utils.mostrar_tablero(tablero_usuario)

    utils.sistema_de_turnos(tablero_usuario, tablero_maquina, flota_usuario, flota_maquina, modo,idioma)

def hundir_la_flota(idioma):
    while True:
        interfaz_del_juego(idioma)
        jugar_nuevamente = input(utils.traducciones[idioma]["jugar_de_nuevo"]).lower()
        if jugar_nuevamente == "true":  
            hundir_la_flota()  
        else:
            print(utils.traducciones[idioma]["salir_juego"])
            print(utils.traducciones[idioma]["actualizaciones"])
            break 

idioma = utils.seleccionar_idioma()
hundir_la_flota(idioma)