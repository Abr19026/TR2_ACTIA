from typing import (List, Iterator, FrozenSet, Set )
import matplotlib.pyplot as plt
import networkx as nx

tipo_nodo = str

tipo_vecinos = FrozenSet[tipo_nodo]


class Arista:
    def __init__(self, vecinos: List[tipo_nodo], peso=0):
        if len(vecinos) != 2:
            raise Exception("Arista no valida")
        self.vecinos: tipo_vecinos = frozenset(vecinos)
        self.peso = peso

    def __repr__(self):
        contador = 0
        nodos_string = ", ".join(map(str, self.vecinos))
        return f"{{ {nodos_string} :: {self.peso}}}"

    def __eq__(self, o):
        return isinstance(o, Arista) \
            and self.vecinos == o.vecinos \
            and self.peso == o.peso

    def __hash__(self):
        return hash(self.vecinos)

    def __iter__(self):
        return iter(self.vecinos)


class Vecino:

    def __init__(self, vecino: tipo_nodo, peso: int = 0):
        self.nodo_vecino: tipo_nodo = vecino
        self.peso = peso

    def __repr__(self):
        return f"[{self.nodo_vecino} <{self.peso}>]"

    def __eq__(self, o):
        return isinstance(o, Vecino)\
            and self.nodo_vecino == o.nodo_vecino

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
        for vecino in arista.vecinos:
            for otro in arista.vecinos:
                # Si hay un aro es de longitud 1
                if otro != vecino or len(arista.vecinos) == 1:
                    aumentar_set_dict(self.adyacencias, vecino,
                                      Vecino(otro, arista.peso))

    # Elimina la arista con el par de vecinos dados sin importar el peso
    def eliminar_arista(self, arista: Arista):
        for vecino in arista.vecinos:
            for otro in arista.vecinos:
                # Acepta aros (longitud 1)
                if otro != vecino or len(arista.vecinos) == 1:
                    self.adyacencias[vecino].remove(Vecino(otro, arista.peso))

    def get_nodos(self):
        return self.adyacencias.keys()

    def get_aristas(self) -> FrozenSet[Arista]:
        set_aristas: set[Arista] = set()
        for nodo in self.get_nodos():
            set_aristas.update([
                Arista([nodo, vecino.nodo_vecino], vecino.peso)
                for vecino in self.adyacencias[nodo]
                ])
        return frozenset(set_aristas)

    def __str__(self):
        salida = ""
        for nodo in migrafo.adyacencias.keys():
            salida += f"{nodo}: {migrafo.adyacencias[nodo]}\n"
        return salida

    def graficar(self):
        grafo_nx = nx.Graph()
        grafo_nx.add_edges_from()

aristas = set([
    Arista(['A', 'B'], 1),
    Arista(['A', 'D'], 3),
    Arista(['A', 'C'], 2),
    Arista(['B', 'C'], 4),
    Arista(['C', 'D'], 5),
])

migrafo = Grafo(aristas)

print(migrafo)
