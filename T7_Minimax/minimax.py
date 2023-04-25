# Implementación de minimax para el juego del gato
from gato import JuegoGato, coord_a_pos, pos_a_coord
#from copy import deepcopy
import operator

# mientras mayor, mas cerca esta de ganar el jugador dado
# heuristica es mis formas posibles de ganar menos las formas posibles de ganar del otro
def heuristica(estado: JuegoGato, jugador: int):
    mi_signo = 1
    if jugador == 2:
        mi_signo = -1
    rango_bueno = range(0,mi_signo*4,mi_signo)
    
    valor_heur = 0
    for forma_ganar in estado.estado_formas_ganar:
        if forma_ganar in rango_bueno:
            valor_heur += 1
            #valor_heur += abs(forma_ganar)
        elif forma_ganar != 11:
            valor_heur -= 1
            #valor_heur -= abs(forma_ganar)
    return valor_heur

def get_transiciones(estado: JuegoGato)-> list[int]:
    return [x for x in range(9) if estado.posicion_valida(x)]

def minimax(estado: JuegoGato, maximizando: bool, jugador, max_prof)-> tuple[int,float]:
    transiciones = get_transiciones(estado)
    if len(transiciones) > 0 and max_prof > 0:
        mejor_transicion = (None, float("-inf") if maximizando else float("inf"))
        for accion in transiciones:
            # aplica estado al cada rama
            acc_x, acc_y = pos_a_coord(accion)
            hijo = estado.copiar()
            hijo.insertar_jugada(acc_x, acc_y)
            hijo.alternar_turno()
            # continua minimax
            resultado_minimax = minimax(hijo, not maximizando, jugador, max_prof - 1)
            
            # Guarda (accion, heuristica) que mejora la condición
            nueva_transicion = (accion, resultado_minimax[1])
            if maximizando:
                mejor_transicion = max(mejor_transicion, nueva_transicion, key=operator.itemgetter(1))
            else:
                mejor_transicion = min(mejor_transicion, nueva_transicion, key=operator.itemgetter(1))
        
        return mejor_transicion
    else:
        # mejor accion es none, valor es heuristica(estado)
        return (None, heuristica(estado, jugador))