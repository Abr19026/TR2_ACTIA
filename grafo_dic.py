import enum
from typing import (List, Iterator, FrozenSet, Set, Tuple )
import matplotlib.pyplot as plt
import networkx as nx

tipo_nodo = str

tipo_vecinos = FrozenSet[tipo_nodo]


class Arista:
    
    def __init__(self, vecinos: Tuple[tipo_nodo, tipo_nodo], peso=0):
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


#Por simplicidad hice que dos vecinos son iguales sin importar su peso
class Vecino:

    def __init__(self, vecino: tipo_nodo, peso: float = 0):
        self.nodo_vecino: tipo_nodo = vecino
        self.peso = peso

    def __repr__(self):
        return f"[{self.nodo_vecino} <{self.peso}>]"

    #Ignora peso
    def __eq__(self, o):
        return isinstance(o, Vecino)\
            and self.nodo_vecino == o.nodo_vecino
    
    #Ignora peso
    def __hash__(self):
        return hash(self.nodo_vecino)


# Función que agrega valor a set de diccionario si existe, lo crea si no
# Retorna 1 si se agregó un valor
def aumentar_set_dict(diccionario: dict, llave, valor):
    if llave in diccionario:
        diccionario[llave].add(valor)
    else:
        diccionario[llave] = set([valor])


class Grafo:

    def __init__(self, adyacencias: set[Arista]):
        self.adyacencias: dict[tipo_nodo, set[Vecino]] = {}
        for arista in adyacencias:
            self.agregar_arista(arista)

    # Limitante: Solo puede haber 1 arista entre cada par de nodos
    def agregar_arista(self, arista: Arista):
        for i, nodo in enumerate(arista.vecinos):
            nodo_vecino = arista.vecinos[1 - i]
            aumentar_set_dict(self.adyacencias, nodo,
                                      Vecino(nodo_vecino, arista.peso))

    # Elimina la arista con el par de vecinos dados sin importar el peso
    def eliminar_arista(self, arista: Arista):
        for i, nodo in enumerate(arista.vecinos):
            nodo_vecino = arista.vecinos[1 - i]
            self.adyacencias[nodo].remove(Vecino(nodo_vecino))
            if nodo_vecino == nodo:
                break

    def get_nodos(self):
        return self.adyacencias.keys()

    def get_aristas(self) -> FrozenSet[Arista]:
        set_aristas: set[Arista] = set()
        for nodo in self.get_nodos():
            for vecino in self.get_vecinos(nodo):
                set_aristas.add(Arista((nodo, vecino.nodo_vecino),vecino.peso))
        return frozenset(set_aristas)

    def get_vecinos(self, nodo: tipo_nodo) -> FrozenSet[Vecino]:
        return frozenset(self.adyacencias[nodo])

    def __str__(self):
        salida = ""
        for nodo in migrafo.adyacencias.keys():
            salida += f"{nodo}: {migrafo.adyacencias[nodo]}\n"
        return salida

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

    def djikstra(self, nodo_inicial: tipo_nodo) -> dict[tipo_nodo, float]:
        distancias_minimas: dict[tipo_nodo,float] = {}
        posibles_rutas = dict[tipo_nodo,float] = {}
        return distancias_minimas

aristas = set([
    Arista(('A', 'B'), 1),
    Arista(('A', 'D'), 3),
    Arista(('A', 'C'), 2),
    Arista(('B', 'C'), 4),
    Arista(('C', 'D'), 5),
])

migrafo = Grafo(aristas)

print(migrafo)
