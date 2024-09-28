import numpy as np
import random
import time

def dibujar_batalla_barcos():
    escena = [
        "      __|__                     __|__      ",
        "     |o o o|                   |o o o|     ",
        "  ___/_____/\\__             ___/_____/\\__   ",
        "  \\           /             \\           /   ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "               #-------->>                    ",
        "                BOOOOOM!                      ",]
    for linea in escena:
        print(linea)


def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero


def crear_barco(eslora, tablero):
    while True:
        casilla_0 = (random.randint(0, 9), random.randint(0, 9))
        orientacion = random.choice(["Vertical", "Horizontal"])

        barco = [casilla_0]
        casilla = casilla_0

        for _ in range(1, eslora): #_sifnifica que se va iterar tantas veces se necesite, es una convencion de python
            if orientacion == "Vertical":
                nueva_casilla = (casilla[0] + 1, casilla[1])
            else:
                nueva_casilla = (casilla[0], casilla[1] + 1)

            if nueva_casilla[0] > 9 or nueva_casilla[1] > 9:
                break  
            barco.append(nueva_casilla)
            casilla = nueva_casilla

        if len(barco) == eslora: 
            if not comprobar_colision(barco, tablero):
                return barco

def comprobar_colision(barco, tablero): 
    for i, j in barco:
        if tablero[i][j] == 'O':  
            return True
    return False

def crear_flota(tablero):
    flota_barcos = [
        crear_barco(2, tablero),
        crear_barco(2, tablero),
        crear_barco(2, tablero),
        crear_barco(3, tablero),
        crear_barco(3, tablero),
        crear_barco(4, tablero)]
    return flota_barcos

def colocar_flota(flota, tablero): 
    for barco in flota:
        for i, j in barco:
            tablero[i][j] = 'O'  
    return tablero

def generar_nuevo_tablero():
    tablero_usuario = crear_tablero(10)
    flota_usuario = crear_flota(tablero_usuario)
    tablero_final = colocar_flota(flota_usuario, tablero_usuario)
    return tablero_final

#Hasta aquí funciones para preparar el juego
#Apartir de aqui empieza el sistema de turnos

def sistema_de_turnos(tablero_final, tablero_maquina):
    print("Que comience el juego")
    
    while not verificar_victoria(tablero_maquina) and not verificar_victoria(tablero_final): #Mientras ninguno haya ganado..
        print("\n--- Tu turno ---")    
        turno_usuario(tablero_maquina)
        print(tablero_maquina)
        
        if verificar_victoria(tablero_maquina):   #Verifica si gana
            print("Has ganado makena.")
            break
        time.sleep(1)

        print("\n--- Turno de la Máquina ---")   
        turno_maquina(tablero_final)
        print(tablero_final)
        if verificar_victoria(tablero_final):      
            print("La máquina te ha ganado crack")
            break


def turno_usuario(tablero):
    while True:  
        try:                                                                 #Mientras no se pierda el turno
            fila = int(input("Introduce la fila (1-9) a la que quieres disparar: "))
            columna = int(input("Introduce la columna (0-9) a la que quieres disparar: "))
            if fila > 0 or fila > 9 or columna <0 or columna > 9:
                print("Cordenadas fuera de rango, intentelo de nuevo")
        except ValueError:
            print("Intruce numero entre el 0 y 9.")

        resultado = disparar((fila-1, columna), tablero)             #llamada ala función disparar
        print(f"Disparaste a {(fila, columna)}:\n {resultado}")     #Ubicación del tiro por pantalla
        
        if resultado == "Agua":                                     #Posibilidades
            print("Fallaste. Fin de tu turno.")
            break
        elif resultado == "Tocado":
            print("Has acertado sigue disparando.")
            continue
        else:
            print("Casilla repetida,perdiste el turno")
            break

def verificar_victoria(tablero_oponente):
    return not np.any(tablero_oponente == "O")
#Si quedan alguna "O" nos dá True, nadie ha ganado


def turno_maquina(tablero):
    while True:                      #Mientras acierte seguirá disparando de forma random
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        
        resultado = disparar((fila, columna), tablero)
        print(f"La máquina disparó a {(fila, columna)}: \n {resultado}")
        
        if resultado == "Agua":
            print("La máquina falló. Fin de su turno.")
            break  

        elif resultado == "Tocado":
            print("La máquina acertó. Sigue disparando.")
            continue 
        
        else:
            print("Casilla repetida, pierde el turno")
            break

def disparar(casilla, tablero):
    if tablero[casilla] == "O":              #la O es barco, la X tocado y la A agua
        print("Tocado")
        tablero[casilla] = "X"
        return "Tocado"
    elif tablero[casilla] == '_': 
        print("Agua")
        tablero[casilla] = "A"
        return "Agua"
    else:
        print("Casilla ya disparada.")
        return "Casilla ya disparada"