import numpy as np
import random
import time
import utils

class Game:
    def __init__(self, idioma):
        self.idioma = idioma
        self.tablero_usuario = None
        self.tablero_maquina = None
        self.flota_usuario = None
        self.flota_maquina = None
        self.modo = None

    def iniciar(self):
        self.interfaz_del_juego()
        self.sistema_de_turnos()

    def interfaz_del_juego(self):
        print(utils.traducciones[self.idioma]["bienvenida"])
        time.sleep(1)
        utils.dibujar_batalla_barcos()
        time.sleep(2)

        while True:
            self.modo = input(utils.traducciones[self.idioma]["elige_modo"]).lower()
            if self.modo in [utils.traducciones[self.idioma]["corto"], utils.traducciones[self.idioma]["largo"]]:
                break
            else:
                print(utils.traducciones[self.idioma]["modo_no_valido"])

        print(utils.traducciones[self.idioma]["creando_tablero"])
        time.sleep(1)

        self.tablero_usuario = utils.crear_tablero(10)
        self.tablero_maquina = utils.crear_tablero(10)

        if self.modo == utils.traducciones[self.idioma]["corto"]:
            self.flota_usuario = utils.crear_flota(self.tablero_usuario, [1] * 6)
            self.flota_maquina = utils.crear_flota(self.tablero_maquina, [1] * 6)
        else:
            self.flota_usuario = utils.crear_flota(self.tablero_usuario, [2, 2, 2, 3, 3, 4])
            self.flota_maquina = utils.crear_flota(self.tablero_maquina, [2, 2, 2, 3, 3, 4])

        utils.colocar_flota(self.flota_usuario, self.tablero_usuario)
        utils.colocar_flota(self.flota_maquina, self.tablero_maquina)

        time.sleep(0.5)
        print(utils.traducciones[self.idioma]["tu_tablero"])
        utils.mostrar_tablero(self.tablero_usuario)

        while True:
            respuesta = input(utils.traducciones[self.idioma]["te_gusta_el_tablero"]).lower()
            if respuesta == "true":
                print(utils.traducciones[self.idioma]["jugaras_con_este"])
                break
            else:
                time.sleep(0.5)
                self.tablero_usuario = utils.crear_tablero(10)
                if self.modo == utils.traducciones[self.idioma]["corto"]:
                    self.flota_usuario = utils.crear_flota(self.tablero_usuario, [1] * 6)
                else:
                    self.flota_usuario = utils.crear_flota(self.tablero_usuario, [2, 2, 2, 3, 3, 4])
                utils.colocar_flota(self.flota_usuario, self.tablero_usuario)
                print(utils.traducciones[self.idioma]["nuevo_tablero_generado"])
                utils.mostrar_tablero(self.tablero_usuario)

    def sistema_de_turnos(self):
        time.sleep(1)
        print(f"{utils.traducciones[self.idioma]['juego']}!")
        time.sleep(1)
        barcos_hundidos_usuario = 0
        barcos_hundidos_maquina = 0
        total_barcos = len(self.flota_maquina)

        limite_puntos = 3 if self.modo == utils.traducciones[self.idioma]["corto"] else len(self.tablero_maquina[self.tablero_maquina == "O"])

        while barcos_hundidos_usuario < limite_puntos and barcos_hundidos_maquina < limite_puntos:
            print(f"\n--- {utils.traducciones[self.idioma]['turno_usuario']} ---")
            barcos_hundidos_maquina += self.turno_usuario()
            print(f"{utils.traducciones[self.idioma]['barcos_restantes']} {total_barcos - barcos_hundidos_maquina}")

            if barcos_hundidos_maquina >= limite_puntos:
                print(f"{utils.traducciones[self.idioma]['ganas']}!")
                break

            time.sleep(2)

            print(f"\n--- {utils.traducciones[self.idioma]['turno_maquina']} ---")
            barcos_hundidos_usuario += self.turno_maquina()
            utils.mostrar_tablero(self.tablero_usuario)
            print(f"\n {utils.traducciones[self.idioma]['te_quedan']} {total_barcos - barcos_hundidos_usuario} {utils.traducciones[self.idioma]['barcos']}")

            if barcos_hundidos_usuario >= limite_puntos:
                print(f"{utils.traducciones[self.idioma]['pierdes']}!")
                break

    def turno_usuario(self):
        while True:
            utils.mostrar_tablero_oculto(self.tablero_maquina, self.idioma)
            try:
                fila = int(input(utils.traducciones[self.idioma]["disparar"]))
                columna = int(input(utils.traducciones[self.idioma]["disparar"]))
                if not (0 <= fila <= 9) or not (0 <= columna <= 9):
                    print(utils.traducciones[self.idioma]["cordenadas_fuera"])
                    continue
            except ValueError:
                print(utils.traducciones[self.idioma]["numero_invalido"])
                continue

            resultado = self.disparar((fila, columna), self.tablero_maquina)
            print(f"{utils.traducciones[self.idioma]['disparastes_a']} {(fila, columna)}:\n {resultado}")

            if resultado == utils.traducciones[self.idioma]["agua"]:
                print(utils.traducciones[self.idioma]["fallaste"])
                return 0
            elif resultado == utils.traducciones[self.idioma]["tocado"]:
                print(utils.traducciones[self.idioma]["acierto"])
                for barco in self.flota_maquina:
                    if self.barco_hundido(barco):
                        print(utils.traducciones[self.idioma]["barco_hundido"])
                        return 1

    def turno_maquina(self):
        while True:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)

            resultado = self.disparar((fila, columna), self.tablero_usuario)
            print(f"{utils.traducciones[self.idioma]['disparo_maquina']} {(fila, columna)}: \n {resultado}")

            if resultado == utils.traducciones[self.idioma]["agua"]:
                print(utils.traducciones[self.idioma]["fin_turno_maquina"])
                return 0
            elif resultado == utils.traducciones[self.idioma]["tocado"]:
                print(utils.traducciones[self.idioma]["maquina_acierto"])
                for barco in self.flota_usuario:
                    if self.barco_hundido(barco):
                        print(utils.traducciones[self.idioma]["barco_hundido"])
                        return 1

    def disparar(self, casilla, tablero):
        fila, columna = casilla
        if tablero[fila, columna] == "O":
            tablero[fila, columna] = "X"
            return utils.traducciones[self.idioma]["tocado"]
        elif tablero[fila, columna] == '_':
            tablero[fila, columna] = "A"
            return utils.traducciones[self.idioma]["agua"]
        else:
            return utils.traducciones[self.idioma]["casilla_repetida"]

    def barco_hundido(self, barco):
        for i, j in barco:
            if self.tablero_maquina[i][j] != "X":
                return False
        return True


class Juego:
    def __init__(self):
        self.idioma = utils.seleccionar_idioma()

    def jugar(self):
        while True:
            game = Game(self.idioma)
            game.iniciar()
            jugar_nuevamente = input(utils.traducciones[self.idioma]["jugar_de_nuevo"]).lower()
            if jugar_nuevamente != "true":
                print(utils.traducciones[self.idioma]["salir_juego"])
                print(utils.traducciones[self.idioma]["actualizaciones"])
                break


if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
