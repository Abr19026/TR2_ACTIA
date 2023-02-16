from typing import (List, Iterator, FrozenSet, Set)


tipo_nodo = int

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


class Grafo:

    def __init__(self, adyacencias: set[Arista]):
        self.lista_ady: Set[Arista] = set()
        self.nodos: dict[tipo_nodo, int] = {}
        for arista in adyacencias:
            self.agregar_arista(arista)

    def agregar_arista(self, arista: Arista):
        longitud_ant = len(self.lista_ady)
        self.lista_ady.add(arista)
        if longitud_ant != len(self.lista_ady):
            for nodo in arista:
                if nodo not in self.nodos:
                    self.nodos[nodo] = 0
                if nodo in self.nodos:
                    self.nodos[nodo] += 1

    def cantidad_aristas(self) -> int:
        return len(self.lista_ady)

    def quitar_arista(self, arista: Arista):
        longitud_ant = len(self.lista_ady)
        self.lista_ady.remove(arista)
        if longitud_ant != len(self.lista_ady):
            for nodo in arista:
                self.nodos[nodo] -= 1

    def get_aristas(self) -> List[Arista]:
        return list(self.lista_ady)


set_aristas = set([Arista([i, 3], 8) for i in range(0, 10)])

migrafo = Grafo(set(set_aristas))
