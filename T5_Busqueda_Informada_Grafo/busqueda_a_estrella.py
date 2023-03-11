from grafo import Grafo, tipo_nodo
from typing import Tuple, List
from heapq import *

def busqueda_a_estrella(grafo: Grafo, nodo_inicial, nodo_final, heuristica):
    # Creo una estructura buscables que se ordene de menor a mayor respecto a f(x)
    # Contiene tuplas (f(nodo),g(nodo),nodo, nodo_anterior)
    buscables: List(Tuple[float,float,tipo_nodo]) = []
    # agrego primer nodo a buscables con peso 0
    heappush(buscables, (0,0,nodo_inicial, None))
    # Creo mapeo con nodos visitados, hacia una tupla, Nodo -> (g(Nodo), nodo_ant)
    visitados: dict[tipo_nodo, Tuple[float,tipo_nodo]] = {}
    # mientras haya buscables
    # y nodo_final no se halle en buscados
    while len(buscables) > 0:
        # Saco buscable menor y lo agrego a mapeo de visitados con (g(x), nodo_anterior)
        heuristico, peso_sacado, nodo_sacado, nodo_anterior = heappop(buscables)
        visitados[nodo_sacado] = (peso_sacado, nodo_anterior)
        # Si saqué el nodo final termino el ciclo
        if nodo_sacado == nodo_final:
            break
        # Agrego sus hijos a buscables con su valor f(x) = g(x) + h(x)
        for vecino in grafo.get_vecinos(nodo_sacado):
            peso = peso_sacado + grafo.costo_nodo(nodo_sacado, vecino)
            heur = heuristica(grafo, vecino, nodo_final)
            f_nodo = peso + heur
            # Lo agrego a menos que ya exista y su peso anterior sea menor.
            if  vecino not in visitados  or  visitados[vecino][0] > peso:
                heappush(buscables,(f_nodo, peso, vecino, nodo_sacado))
    # retorno mapeo
    return visitados

def obtener_ruta(nodos_visitados, Nodo_final):
    peso_ruta = 0
    ruta = [Nodo_final]
    while ruta[-1] is not None:
        peso, anterior = nodos_visitados[ruta[-1]]
        ruta.append(anterior)
        peso_ruta += peso
    return ( peso_ruta, tuple(reversed(ruta)) )