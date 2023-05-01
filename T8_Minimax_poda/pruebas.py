from gato import JuegoGato, imprimir_tablero, pos_a_coord
from minimax_poda import minimax
from timeit import default_timer
import colorama as cr

# puede ser 1 o 2
turno_algoritmo = 1

#Ajusta la profundidad máxima
profundidad_minimax = 9

# 1er turno es algoritmo, 2do es jugador
# prueba juego de gato manual
if __name__ == "__main__":
    nuevo_juego = True
    turnos_completados = 0
    while nuevo_juego:
        tablero = JuegoGato()
        lista_tiempos = []
        buffer_vid = buffer_vid = JuegoGato.tablero_con_numeros()
        imprimir_tablero(buffer_vid, True)
        while True:

            # Pide entrada
            print(f"Turno de [{tablero.simbolos_turno[tablero.turno - 1]}]")
            pos_input = -1
            
            if tablero.turno == turno_algoritmo:
                t_0 = default_timer()
                valor_minimax = minimax(tablero, True, turno_algoritmo, profundidad_minimax)
                t_1 = default_timer()
                periodo_tiempo = round(t_1 - t_0, 6)
                lista_tiempos.append(periodo_tiempo)
                pos_input = valor_minimax[0]
                print(f"Algoritmo colocó en posición: {pos_input + 1} después de {periodo_tiempo} segundos")
            else:
                # Valida entrada
                while pos_input == -1:
                    try:
                        # Checa que sea un numero
                        entrada = input("introduzca posición del 1 al 9: ")
                        pos_input = int(entrada) - 1

                        # Checa que no esté ocupada en el tablero
                        if not tablero.posicion_valida(pos_input):
                            print("No puede colocar ahí")
                            pos_input = -1

                    except Exception:
                        print("Entrada no válida")
                        pos_input = -1

            # Inserta jugada
            coordx, coordy = pos_a_coord(pos_input)
            tablero.insertar_jugada(coordx, coordy, buffer_vid)
            print("-------------------")
            imprimir_tablero(buffer_vid, True)
            turnos_completados += 1

            if tablero.juego_terminado != 0:
                if tablero.juego_terminado == 1:
                    print( f"{cr.Fore.GREEN}FIN DEL JUEGO: GANARON LAS [{tablero.simbolos_turno[tablero.turno - 1]}]{cr.Fore.RESET}")
                elif tablero.juego_terminado == 2:
                    print(f"{cr.Fore.YELLOW}FIN DEL JUEGO: EMPATE{cr.Fore.RESET}")
                
                print(f"tiempos algoritmo {lista_tiempos}")
                break
            tablero.alternar_turno()
        nuevo_juego = False