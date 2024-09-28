
#Import de bibliotecas necesarias:
import time
import numpy as np
import utils

print(f"Welcome to Battleship")
time.sleep(1)
utils.dibujar_batalla_barcos()
time.sleep(2)

print(f"Creating your new the game track...")

time.sleep(1)
tablero_usuario = utils.crear_tablero(10)
tablero_maquina = utils.crear_tablero(10)

time.sleep(0.5)
print(f"Your fleet will be made up of 6 ships and they will be placed randomly on the game track.")

flota_usuario = utils.crear_flota(tablero_usuario)
flota_maquina = utils.crear_flota(tablero_maquina)
#print(flota_usuario) if you want to see yours boats before placing in the game track

tablero_final = utils.colocar_flota(flota_usuario,tablero_usuario)
tablero_maquina_final = utils.colocar_flota(flota_maquina,tablero_maquina)
print(f"\n               Here you are")
print(tablero_final)

while True: 
    respuesta = input("Te gusta tu tablero o generamos otro?(True/False)")    
    if respuesta == "True":
        print(f"Then you will play with this, GOOD LUCK!")
        break
    else:
        print("Generando nuevo tablero")
        time.sleep(1)
        tablero_final = utils.generar_nuevo_tablero()
        print(tablero_final)
    
utils.sistema_de_turnos(tablero_final, tablero_maquina)

jugar_nuevamente = input("¿Quieres jugar de nuevo? (True/False): ").lower()
if jugar_nuevamente == "True":
    jugar()
else:
    print(f"Saliendo del juego, que tenga buen día no dude en volver a jugar")
    print(f"Con un pull de git compruebe las nuevas actualizaciones")