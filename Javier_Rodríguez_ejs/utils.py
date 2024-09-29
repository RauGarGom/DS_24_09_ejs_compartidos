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



def seleccionar_idioma():
    while True:
        idioma = input("Seleccione el idioma / Select language (Español/English): ").lower()
        if idioma in ["español", "english"]:
            return idioma
        else:
            print("Idioma no válido / Invalid language. Por favor elija 'Español' o 'English'.")


traducciones = {
    "español": {
        "bienvenida": "Bienvenido a Hundir la Flota",
        "elige_modo": "Hay dos modos de juego: Corto (6 barcos de eslora 1) o Largo (6 barcos de diferentes esloras). Introduzca (Corto/Largo): ",
        "creando_tablero": "Creando tablero de juego...",
        "te_gusta_el_tablero": "¿Te gusta tu tablero o generamos otro? (True/False)",
        "buena_suerte": "Entonces jugarás con este, ¡BUENA SUERTE!",
        "tocado": "Tocado",
        "agua": "Agua",
        "barco_hundido": "Barco Hundido",
        "barcos_hundidos": "Barcos hundidos",
        "quedan_barcos": "Barcos restantes",
        "turno_maquina": "Turno de la Máquina",
        "turno_usuario": "Tu turno",
        "ganas": "Has ganado",
        "pierdes": "Has perdido",
        "disparar": "Introduce la fila (0-9) a la que quieres disparar: ",
        "cordenadas_fuera": "Cordenadas fuera de rango, intentelo de nuevo.",
        "numero_invalido": "Introduce un número entre el 0 y el 9.",
        "fallaste": "Fallaste. Fin de tu turno.",
        "acierto": "Has acertado sigue disparando.",
        "fin_turno_maquina": "La máquina falló. Fin de su turno.",
        "maquina_acierto": "La máquina acertó. Sigue disparando.",
        "disparo_maquina": "La máquina disparó a",
        "modo_no_valido": "Modo no válido. Por favor, introduzca 'Corto' o 'Largo'.",
        "casilla_repetida": "Casilla repetida",
        "nuevo_tablero_generado": "Nuevo tablero Generado",
        "tablero_maquina": "Tablero de la maquina",
        "jugaras_con_este": "Entonces jugarás con este, ¡BUENA SUERTE!",
        "barcos_restantes": "Barcos restantes de la maquina :",
        "te_quedan": "Te quedan",
        "barcos":"barcos",
        "disparastes_a": "disparaste a",
        "jugar_de_nuevo": "¿Quieres jugar de nuevo? (True/False): ",
        "salir_juego":"Saliendo del juego, que tenga buen día. No dude en volver a jugar.",
        "actualizaciones":"Con un pull de git, compruebe las nuevas actualizaciones.",
        "corto":"corto",
        "largo":"largo",
        "tu_tablero":"\n   Tu tablero",
        "juego":"Que empiezen los cañonazos"

    },
    "english": {
        "bienvenida": "Welcome to Battleship",
        "elige_modo": "There are two game modes: Short (6 ships of length 1) or Long (6 ships of different lengths). Enter (Short/Long): ",
        "creando_tablero": "Creating game board...",
        "te_gusta_el_tablero": "Do you like your board or shall we generate another? (True/False)",
        "buena_suerte": "You will play with this one, GOOD LUCK!",
        "tocado": "Hit",
        "agua": "Miss",
        "barco_hundido": "Ship Sunk",
        "barcos_hundidos": "Ships sunk",
        "quedan_barcos": "Ships remaining",
        "turno_maquina": "Machine's turn",
        "turno_usuario": "Your turn",
        "ganas": "You win",
        "pierdes": "You lose",
        "disparar": "Enter the row (0-9) you want to shoot at: ",
        "cordenadas_fuera": "Coordinates out of range, try again.",
        "numero_invalido": "Enter a number between 0 and 9.",
        "fallaste": "You missed. End of your turn.",
        "acierto": "You hit! Keep shooting.",
        "fin_turno_maquina": "The machine missed. End of its turn.",
        "maquina_acierto": "The machine hit. Keep shooting.",
        "disparo_maquina": "The machine shot at",
        "modo_no_valido": "Invalid mode. Please enter 'Short' or 'Long'.",
        "casilla_repetida": "Repeated square",
        "nuevo_tablero_generado": "New board generated",
        "tablero_maquina": "Machine's board",
        "jugaras_con_este": "You will play with this one, GOOD LUCK!",
        "barcos_restantes": "Remaining ships of the machine:",
        "te_quedan": "You have",
        "barcos": "ships left",
        "disparastes_a":"you shot at",
        "jugar_de_nuevo": "Do you want to play again? (True/False):",
        "salir_juego":"Quitting game, have a nice day. Feel free to come back to play.",
        "actualizaciones":"Check out new updates with a git pull.",
        "corto":"short",
        "largo":"long",
        "tu_tablero":"\n   Your game track",
        "juego":"Let the cannon fire begin"
    }
}

def crear_tablero(tamaño): 
    return np.full((tamaño,tamaño), "_")


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


def crear_flota(tablero,esloras):
    return [crear_barco(eslora,tablero) for eslora in esloras]


def colocar_flota(barcos, tablero): 
    for barco in barcos:
        for i, j in barco:
            tablero[i][j] = 'O'  
    return tablero


def sistema_de_turnos(tablero_usuario, tablero_maquina, flota_usuario, flota_maquina, modo, idioma):
    time.sleep(1)
    print(f"{traducciones[idioma]["juego"]}!")
    time.sleep(1)
    barcos_hundidos_usuario = 0
    barcos_hundidos_maquina = 0
    total_barcos = len(flota_maquina)
    
    if modo == traducciones[idioma]["corto"]:
        limite_puntos = 3
    else:
        limite_puntos = len(tablero_maquina[tablero_maquina == "O"])
    
    while barcos_hundidos_usuario < limite_puntos and barcos_hundidos_maquina < limite_puntos:
        print(f"\n--- {traducciones[idioma]['turno_usuario']} ---")    
        barcos_hundidos_maquina += turno_usuario(tablero_maquina,flota_maquina,idioma)
        print(f"{traducciones[idioma]['barcos_restantes']} {total_barcos - barcos_hundidos_maquina}")

        if barcos_hundidos_maquina >= limite_puntos:   
            print(f"{traducciones[idioma]['ganas']}!")
            break

        time.sleep(2)

        print(f"\n--- {traducciones[idioma]['turno_maquina']} ---")   
        barcos_hundidos_usuario += turno_maquina(tablero_usuario, flota_usuario,idioma)
        mostrar_tablero(tablero_usuario)
        print(f"\n {traducciones[idioma]['te_quedan']} {total_barcos - barcos_hundidos_usuario} {traducciones[idioma]['barcos']}")

        if barcos_hundidos_usuario >= limite_puntos:      
            print(f"{traducciones[idioma]['pierdes']}!")
            break


def turno_usuario(tablero_maquina,flota_maquina,idioma):
    while True: 
        mostrar_tablero_oculto(tablero_maquina,idioma) 
        try:                                                                 #Mientras no se pierda el turno
            fila = int(input(traducciones[idioma]["disparar"]))
            columna = int(input(traducciones[idioma]["disparar"]))
            if not (0 <= fila <= 9) or not (0 <= columna <= 9):
                print(traducciones[idioma]["cordenadas_fuera"])
                continue
        except ValueError:
            print(traducciones[idioma]["numero_invalido"])
            continue

        resultado = disparar((fila, columna), tablero_maquina,idioma)             #llamada ala función disparar
        print(f"{traducciones[idioma]['disparastes_a']} {(fila, columna)}:\n {resultado}")     #Ubicación del tiro por pantalla
        
        if resultado == traducciones[idioma]["agua"]:                                    #Posibilidades
            print(traducciones[idioma]["fallaste"])
            return 0
        elif resultado == traducciones[idioma]["tocado"]:
            print(traducciones[idioma]["acierto"])
            for barco in flota_maquina:
                if barco_hundido(barco, tablero_maquina):
                    print(traducciones[idioma]["barco_hundido"])
                    return 1
                

def turno_maquina(tablero_usuario, flota_usuario,idioma):
    while True:                      #Mientras acierte seguirá disparando de forma random
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        
        resultado = disparar((fila, columna), tablero_usuario,idioma)
        print(f"{traducciones[idioma]['disparo_maquina']} {(fila, columna)}: \n {resultado}")

        
        if resultado ==  traducciones[idioma]["agua"]:
            print(traducciones[idioma]["fin_turno_maquina"])
            return 0  

        elif resultado == traducciones[idioma]["tocado"]:
            print(traducciones[idioma]["maquina_acierto"])
            for barco in flota_usuario:
                if barco_hundido(barco,tablero_usuario):
                    print(traducciones[idioma]["barco_hundido"])
                    return 1
        

def disparar(casilla, tablero,idioma):
    fila, columna = casilla
    if tablero[fila, columna] == "O":              #la O es barco, la X tocado y la A agua
        tablero[fila, columna] = "X"
        return traducciones[idioma]["tocado"]
    elif tablero[fila,columna] == '_': 
        tablero[fila,columna] = "A"
        return traducciones[idioma]["agua"]
    else:
        return traducciones[idioma]["casilla_repetida"]
    
def barco_hundido(barco, tablero):
    for i,j in barco:
        if tablero[i][j] != "X":
            return False
    return True

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

def mostrar_tablero_oculto(tablero,idioma):
    print(traducciones[idioma]['tablero_maquina'])
    for fila in tablero:      
        nueva_fila = []
        for celda in fila:
            if celda == 'O':
                nueva_fila.append('_')  
            else:
                nueva_fila.append(celda)  
        fila_str = " ".join(nueva_fila)
        print(fila_str)   
            

