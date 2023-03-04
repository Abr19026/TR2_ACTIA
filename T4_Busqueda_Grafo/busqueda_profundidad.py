import heapq
from grafo import Grafo
from itertools import permutations, pairwise, filterfalse

def dijkstra(grafo, origen):
    """Implementación del algoritmo de Dijkstra para encontrar las distancias más cortas desde un nodo origen a todos los demás nodos en el grafo."""
    distancias = {v: float('inf') for v in grafo.get_nodos()}
    distancias[origen] = 0
    heap = [(0, origen)]
    while heap:
        (dist, v) = heapq.heappop(heap)
        if dist > distancias[v]:
            continue
        for w in grafo.obtener_vertices_adyacentes(v):
            distancia_nueva = dist + grafo.obtener_peso_arista(v, w)
            if distancia_nueva < distancias[w]:
                distancias[w] = distancia_nueva
                heapq.heappush(heap, (distancia_nueva, w))
    return distancias


def ruta_mas_corta_profundidad(grafo, origen, destino):
    """Encuentra la ruta más corta entre dos nodos utilizando 
    el algoritmo de búsqueda en profundidad, comenzando desde 
    la ruta más corta encontrada por el algoritmo de Dijkstra."""
    distancias = dijkstra(grafo, origen)
    if destino not in distancias:
        return None
    ruta_mas_corta = []
    actual = destino
    while actual != origen:
        ruta_mas_corta.append(actual)
        for v in grafo.obtener_vertices_adyacentes(actual):
            if distancias[v] == distancias[actual] - grafo.obtener_peso_arista(v, actual):
                actual = v
                break
    ruta_mas_corta.append(origen)
    ruta_mas_corta.reverse()
    ruta = buscar_profundidad(grafo, origen, destino, ruta_mas_corta)
    if ruta is None:
        return None
    peso = 0
    for v, w in pairwise(ruta):
        peso += grafo.obtener_peso_arista(v, w)
    return peso, ruta

def buscar_profundidad(grafo, inicio, fin, ruta_mas_corta):
    """Implementación del algoritmo de búsqueda en profundidad que
      se utiliza para encontrar la ruta más corta entre dos nodos."""
    visitados = set(ruta_mas_corta[:-1])
    pila = [(ruta_mas_corta[-1], ruta_mas_corta)]
    while pila:
        (vertice, camino) = pila.pop()
        if vertice == fin:
            return camino
        if vertice not in visitados:
            visitados.add(vertice)
            for vecino in grafo.obtener_vertices_adyacentes(vertice):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))
    return None


