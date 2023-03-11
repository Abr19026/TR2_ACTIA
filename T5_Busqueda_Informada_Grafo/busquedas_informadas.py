from grafo import Grafo
from typing import List, Tuple
from collections import deque

def a_inf(grafo: Grafo, inicio: str, fin: str) -> Tuple[List[str], int]:
    # Crear diccionario para almacenar costos y padres de cada nodo
    costos = {inicio: 0}
    padres = {inicio: None}

    # Crear diccionario para almacenar valores heurísticos de cada nodo
    valores_heuristicos = {nodo: grafo.costo_nodo(nodo, fin) for nodo in grafo.get_nodos()}

    # Crear cola de prioridad para almacenar nodos a explorar
    cola_prioridad = deque()
    cola_prioridad.append((inicio, 0))
    
    while cola_prioridad:
        # Obtener nodo actual de la cola de prioridad
        nodo_actual, costo_actual = cola_prioridad.popleft()

        # Si se llega al nodo objetivo, se termina el algoritmo
        if nodo_actual == fin:
            break

        # Iterar sobre las aristas del nodo actual
        for nodo_destino, costo in grafo.obtener_vecinos(nodo_actual):
            # Calcular el costo actualizado de llegar al nodo destino desde el nodo actual
            costo_actualizado = costos[nodo_actual] + costo
            # Si el nodo destino no está en el diccionario de costos o si el costo actualizado es menor que el costo previo
            if nodo_destino not in costos or costo_actualizado < costos[nodo_destino]:
                # Actualizar el costo del nodo destino y su padre
                costos[nodo_destino] = costo_actualizado
                padres[nodo_destino] = nodo_actual
                # Calcular el valor de f(n) del nodo destino
                valor_fn = costo_actualizado + valores_heuristicos[nodo_destino]
                # Agregar el nodo destino a la cola de prioridad con su valor de f(n)
                cola_prioridad.append((nodo_destino, valor_fn))

        # Ordenar la cola de prioridad en orden ascendente de valor de f(n)
        cola_prioridad = deque(sorted(cola_prioridad, key=lambda x: x[1]))

    # Construir la lista de nodos del camino óptimo
    if fin in padres:
        nodo = fin
        camino_optimo = [nodo]
        while padres[nodo] != None:
            nodo = padres[nodo]
            camino_optimo.append(nodo)
        camino_optimo.reverse()
    else:
        print("No se pudo encontrar el nodo inicial en el diccionario de padres.")
        camino_optimo = []

    # Retornar el camino óptimo y su costo total
    return camino_optimo, costos[fin]
