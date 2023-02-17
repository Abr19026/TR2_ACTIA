import matplotlib.pyplot as plt
import networkx as nx

from typing import (Iterable, List, Iterator, FrozenSet, Set, Tuple, NamedTuple )

tipo_nodo = str
class RutaToNodo(NamedTuple):
    nodo_anterior: tipo_nodo
    distancia_min: float
    def __repr__(self) -> str:
        return f"({self.nodo_anterior}, {self.distancia_min})"
ruta_out = dict[tipo_nodo, RutaToNodo]

class Arista:
    
    def __init__(self, vecinos: Tuple[tipo_nodo, tipo_nodo], peso: float=0):
        if len(vecinos) != 2:
            raise Exception("Arista no valida")
        self.vecinos: tuple[tipo_nodo, tipo_nodo] = vecinos
        self.peso = peso

    def __repr__(self):
        nodos_string = ", ".join(map(str, self.vecinos))
        return f"( {nodos_string} :: {self.peso} )"

    def __eq__(self, o):
        return isinstance(o, Arista) \
            and frozenset(self.vecinos) == frozenset(o.vecinos) \
            and self.peso == o.peso

    def __hash__(self):
        return hash(frozenset(self.vecinos))

    def __iter__(self):
        return iter(self.vecinos)

    def arista_nx(self)-> Tuple[tipo_nodo, tipo_nodo, dict]:
        return (self.vecinos[0], self.vecinos[1], {"weight": self.peso})

# Función para agregar valores a diccionario aunque no exista
def aumentar_dict_dict(diccionario: dict[tipo_nodo, dict[tipo_nodo, float]], nodo1, nodo2, peso):
    if nodo1 in diccionario:
        diccionario[nodo1][nodo2] = peso
    else:
        diccionario[nodo1] = {nodo2: peso}


class Grafo:

    def __init__(self, adyacencias: set[Arista]):
        self.adyacencias: dict[tipo_nodo, dict[tipo_nodo,float]] = {}
        for arista in adyacencias:
            self.agregar_arista(arista)

    def __str__(self):
        salida = ""
        for nodo in migrafo.adyacencias.keys():
            salida += f"{nodo}: {migrafo.adyacencias[nodo]}\n"
        return salida

    # Limitante: Solo puede haber 1 arista entre cada par de nodos
    def agregar_arista(self, arista: Arista):
        for i, nodo in enumerate(arista.vecinos):
            nodo_vecino = arista.vecinos[1 - i]
            aumentar_dict_dict(self.adyacencias, nodo, nodo_vecino, arista.peso)

    # Elimina la arista con el par de vecinos dados sin importar el peso
    def eliminar_arista(self, arista: Arista):
        for i, nodo in enumerate(arista.vecinos):
            nodo_vecino = arista.vecinos[1 - i]
            del self.adyacencias[nodo][nodo_vecino]
            if nodo_vecino == nodo:
                break

    def get_nodos(self):
        return self.adyacencias.keys()

    def get_vecinos(self, nodo: tipo_nodo) -> FrozenSet[tipo_nodo]:
        return frozenset(self.adyacencias[nodo].keys())

    def get_aristas(self) -> FrozenSet[Arista]:
        set_aristas: set[Arista] = set()
        for nodo in self.get_nodos():
            for vecino in self.get_vecinos(nodo):
                set_aristas.add(Arista((nodo, vecino), self.adyacencias[nodo][vecino]))
        return frozenset(set_aristas)

    def costo_nodo(self, nodo1:tipo_nodo, nodo2: tipo_nodo):
        return self.adyacencias[nodo1][nodo2]

    def dijkstra(self, nodo_inicial: tipo_nodo) -> ruta_out:
        
        nodo_cercano: tipo_nodo = nodo_inicial                  # Nodo mas cercano
        ruta_corta: RutaToNodo = RutaToNodo(nodo_inicial,0)     # Distancia del nodo mas cercano
        
        dicc_optimizados: ruta_out = {nodo_cercano: ruta_corta} # Nodos optimizados
        dicc_busqueda: ruta_out = {nodo_cercano: ruta_corta}    # Candidatos a optimizar

        while True:
            # Agrega nodo mas cercano a optimizados
            dicc_optimizados[nodo_cercano] = ruta_corta

            # Quita nodo optimizado de diccionario de busqueda
            del dicc_busqueda[nodo_cercano]

            # Halla vecinos de nodo optimizado (candidatos de busqueda)
            # excepto los que ya se optimizaron
            nodos_candidatos = set(self.get_vecinos(nodo_cercano)).\
                           difference(set(dicc_optimizados.keys()))
            
            # Las rutas de nodos candidato son agregadas a diccionario de búsqueda
            # Si nodo ya tenía rutas anteriores, las reemplaza solo si nueva ruta
            # tiene costo menor
            for vecino in nodos_candidatos:
                costo_candidato = dicc_optimizados[nodo_cercano].distancia_min \
                              + self.costo_nodo(nodo_cercano, vecino)
                ruta_candidato = RutaToNodo(nodo_cercano, costo_candidato)

                if vecino in dicc_busqueda:
                    if costo_candidato < dicc_busqueda[vecino].distancia_min:
                        dicc_busqueda[vecino] = ruta_candidato
                else:
                    dicc_busqueda[vecino] = ruta_candidato

            # Halla el nuevo nodo mas cercano
            # Termina algoritmo su ya no hay nodos que buscar
            try:
                nodo_cercano = min(dicc_busqueda.keys(), 
                                  key = lambda x: dicc_busqueda[x].distancia_min)
                ruta_corta = dicc_busqueda[nodo_cercano]
            except ValueError:
                return dicc_optimizados

    def graficar(self):
        # Convierte grafo a networkx
        grafo_nx = nx.Graph()
        grafo_nx.add_edges_from([arista.arista_nx() for arista in self.get_aristas()])
        # Grafica grafo
        pos=nx.spring_layout(grafo_nx)
        nx.draw_networkx(grafo_nx, pos)
        labels = nx.get_edge_attributes(grafo_nx,'weight')
        nx.draw_networkx_edge_labels(grafo_nx, pos, edge_labels=labels)
        plt.show()

aristas = set([
    ##Arista(('A', 'B'), 1),
    ##Arista(('A', 'D'), 3),
    ##Arista(('A', 'C'), 2),
    ##Arista(('B', 'C'), 4),
    ##Arista(('C', 'D'), 5),

    Arista(("A","D"),3),
    Arista(("C","D"),4),
    Arista(("A","B"),5),
    Arista(("B","C"),1),
    Arista(("A","E"),8),
    Arista(("E","C"),2),
    Arista(("E","F"),4),
    Arista(("C","F"),5),
    Arista(("C","H"),2),
    Arista(("H","G"),7),
    Arista(("F","G"),6),
])

migrafo = Grafo(aristas)
distancias_a = migrafo.dijkstra("A")
print(distancias_a)