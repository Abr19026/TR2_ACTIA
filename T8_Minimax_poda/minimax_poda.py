# Implementación de minimax para el juego del gato
from gato import JuegoGato, pos_a_coord
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
            if forma_ganar == 3:
                valor_heur += forma_ganar**2
            else:
                valor_heur += (forma_ganar + 1)**2
        elif forma_ganar != 11:
            valor_heur -= forma_ganar**2
    return valor_heur

# Dado un estado del juego del gato, obtiene las posibles
# casillas donde se puede poner un elemento
def get_transiciones(estado: JuegoGato)-> list[int]:
    return [x for x in range(9) if estado.posicion_valida(x)]

def minimax(estado: JuegoGato, maximizando: bool, jugador, profundidad_max = float("inf"), lim_inf=float("-inf"), lim_sup=float("inf"))-> tuple[int,float]:
    #obtiene las transiciones
    transiciones = get_transiciones(estado)
    # Si no es un nodo hoja
    if len(transiciones) > 0 and estado.juego_terminado == 0 and profundidad_max > 0:
        mejor_transicion = (None, float("-inf") if maximizando else float("inf"))
        # Por cada acción posible en el estado
        for accion in transiciones:
            # crea un hijo aplicando la acción al estado
            acc_x, acc_y = pos_a_coord(accion)
            hijo = estado.copiar()
            hijo.insertar_jugada(acc_x, acc_y)
            hijo.alternar_turno()
            # Obtiene valor minimax del hijo
            resultado_minimax = minimax(hijo, not maximizando, jugador, profundidad_max-1, lim_inf, lim_sup)
            nueva_transicion = (accion, resultado_minimax[1])
            
            # Si se está maximizando
            if maximizando:
                # Obtiene la mejor transición (La que maximiza el valor heuristico)
                mejor_transicion = max(mejor_transicion, nueva_transicion, key=operator.itemgetter(1))
                # Poda si el valor de la nueva transición es mayor al límite superior (beta)
                if nueva_transicion[1] >= lim_sup:
                    break
                # Actualiza valor de poda (alfa) para el siguiente hijo
                lim_inf = max(lim_inf, resultado_minimax[1])
                
            else:
                # Obtiene la mejor transición (La que minimiza el valor heuristico)
                mejor_transicion = min(mejor_transicion, nueva_transicion, key=operator.itemgetter(1))
                # Poda si el valor de la nueva transición es menor al límite inferior (alfa)                
                if nueva_transicion[1] <= lim_inf:
                    break
                # Actualiza valor de poda (beta) para el siguiente hijo
                lim_sup = min(lim_sup, resultado_minimax[1])
                
        return mejor_transicion
    else:
        # mejor accion es none, valor es heuristica(estado)
        return (None, heuristica(estado, jugador))