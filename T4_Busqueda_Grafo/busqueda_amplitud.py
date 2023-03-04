from grafo import Grafo
from typing import Tuple, List

# Para amplitud con perutaciones de 
def ruta_mas_corta_amplitud(grafo: Grafo, Nodo_inicial, Nodo_final):
    # Mejor solución hasta ahora
    mejor_peso_solucion = float("inf")
    mejor_camino = ()

    # Longitud de los caminos
    profundidad_act = 1

    while True: # Por cada nivel de profundidad
        menor_peso_act = float('inf')   # Guarda el menor peso en esta produndidad
        # Checa todas las posibles rutas validas con la profundidad dada
        for ruta_actual, peso_act in generador_caminos(grafo, [Nodo_inicial], 0, profundidad_act):
            # Se guardan soluciones con menor peso
            if ruta_actual[-1] == Nodo_final and peso_act < mejor_peso_solucion:
                mejor_peso_solucion = peso_act
                mejor_camino = ruta_actual
            # Guarda peso menor de esta profundidad
            if peso_act < menor_peso_act:
                menor_peso_act = peso_act
        # Aumenta profundidad de siguiente ciclo
        profundidad_act += 1
        # Terminar ciclo si:
        # Menor peso de nivel actual es mayor a solución hallada
        # O ya no hay caminos que crear
        if menor_peso_act > mejor_peso_solucion or profundidad_act >= len(grafo.get_nodos()):
            break

    return (mejor_camino, mejor_peso_solucion)

# Generador de caminos
def generador_caminos(grafo: Grafo, lista: List, peso_act: float, profundidad :int) ->Tuple[Tuple, float]:
    #Si lista ya tiene profundidad genera la lista
    if len(lista) >= profundidad:
        yield (tuple(lista),peso_act)
    #Si no ha alcanzado la profundidad dada
    else:
        tope = lista[-1]
        #Por cada vecino del tope (que no esté ya en la lista para evitar ciclos)
        for vecino in filter(lambda x: x not in lista, grafo.get_vecinos(tope)):
            # Agrego el vecino
            lista.append(vecino)
            peso_act += grafo.adyacencias[tope][vecino]
            # Por cada camino que pueda generar el vecino
            for camino_valido, peso_val in generador_caminos(grafo,lista,peso_act,profundidad):
                yield (camino_valido, peso_val) # Genero ese camino
            #Quito el vecino
            lista.pop()
            peso_act -= grafo.adyacencias[tope][vecino]
    # Termino iteración si 
    # ya generé todos los caminos que generan todos mis vecinos
    return