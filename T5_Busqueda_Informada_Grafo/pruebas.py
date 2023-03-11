from grafos_ejemplo import aristas_g1, aristas_g2, aristas_g3
from busqueda_a_estrella import busqueda_a_estrella, obtener_ruta
from busquedas_informadas import dijkstra, a_inf
from collections import defaultdict
from grafo import Grafo
from math import sqrt
import timeit

import heapq

grafos =        [Grafo(aristas_g1),Grafo(aristas_g2),Grafo(aristas_g3)]
nodos_in_fin =  [((1, 4),(14, 19)),((4, 1),(1, 1)),((18, 28),(4, 6))]


def heuristica_distancia(grafo, nodo, nodo_final):
    return sqrt((nodo_final[0] - nodo[0]) ** 2 + 
                (nodo_final[1] - nodo[1]) ** 2)


def pruebas_a_estrella():
    for grafo, nodos_busqueda in zip(grafos,nodos_in_fin):
        # Obtiene nodo inicial y final
        nodo_in = nodos_busqueda[0]
        nodo_fin = nodos_busqueda[1]

        t_0 = timeit.default_timer()
        dicc_visitados = busqueda_a_estrella(grafo, nodo_in, nodo_fin, heuristica_distancia)
        t_1 = round(timeit.default_timer() - t_0, 6)
        costo, ruta = obtener_ruta(dicc_visitados, nodo_fin)

        print(f"costo = {costo}, ruta = {ruta} desde {nodo_in} hacia {nodo_fin} tardó: {t_1}s")
    
def pruebas_dijkstra():
    for grafo, nodos_busqueda in zip(grafos,nodos_in_fin):
        # Obtiene nodo inicial y final
        nodo_in = nodos_busqueda[0]
        nodo_fin = nodos_busqueda[1]

        t_0 = timeit.default_timer()
        dicc_visitados = dijkstra(grafo, nodo_in)
        t_1 = round(timeit.default_timer() - t_0, 6)
        costo, ruta = obtener_ruta(dicc_visitados, nodo_fin)

        print(f"costo = {costo}, ruta = {ruta} desde {nodo_in} hacia {nodo_fin} tardó: {t_1}s")

def pruebas_a_informada():
    for grafo, nodos_busqueda in zip(grafos,nodos_in_fin):
        # Obtiene nodo inicial y final
        nodo_in = nodos_busqueda[0]
        nodo_fin = nodos_busqueda[1]

        t_0 = timeit.default_timer()
        ruta, costo = a_inf(grafo, nodo_in, nodo_fin, heuristica_distancia)
        t_1 = round(timeit.default_timer() - t_0, 6)

        print(f"costo = {costo}, ruta = {ruta} desde {nodo_in} hacia {nodo_fin} tardó: {t_1}s")

print("Pruebas a estrella")
pruebas_a_estrella()
print("Pruebas a informada")
pruebas_a_informada()
print("Pruebas a dijkstra")
pruebas_dijkstra()