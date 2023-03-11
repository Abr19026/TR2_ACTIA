from grafos_ejemplo import aristas_g1, aristas_g2, aristas_g3
from busqueda_a_estrella import busqueda_a_estrella, obtener_ruta
from collections import defaultdict
from grafo import Grafo

grafos = [Grafo(aristas_g1),Grafo(aristas_g2),Grafo(aristas_g3)]
heuristicas = defaultdict(lambda: 0)

nodo_in = "A"
nodo_fin = "Z"
for grafo in grafos:
    dicc_visitados = busqueda_a_estrella(grafo, nodo_in, nodo_fin, heuristicas)
    costo, ruta = obtener_ruta(dicc_visitados, nodo_fin)
    print(f"costo = {costo}, ruta = {ruta}")