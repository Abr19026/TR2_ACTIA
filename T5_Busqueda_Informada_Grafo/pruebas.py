from grafos_ejemplo import aristas_g1, aristas_g2, aristas_g3
from busqueda_a_estrella import busqueda_a_estrella, obtener_ruta
from collections import defaultdict
from grafo import Grafo
from math import sqrt

grafos = [Grafo(aristas_g1),Grafo(aristas_g2),Grafo(aristas_g3)]


def heuristica_distancia(grafo, nodo, nodo_final):
    return sqrt((nodo_final[0] - nodo[0]) ** 2 + 
                (nodo_final[1] - nodo[1]) ** 2
               )
for grafo in grafos:
    grafo.graficar(True)

"""
for grafo in grafos:
    itera = iter(grafo.get_nodos())
    nodo_in = next(itera)
    nodo_fin = None
    for nodo_fin in itera:
        pass
    dicc_visitados = busqueda_a_estrella(grafo, nodo_in, nodo_fin, heuristica_distancia)
    costo, ruta = obtener_ruta(dicc_visitados, nodo_fin)
    print(f"costo = {costo}, ruta = {ruta} desde {nodo_in} hacia {nodo_fin}")
"""