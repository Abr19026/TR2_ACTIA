from random import *
from math import sqrt


def generador_nodos(max_x, max_y, cantidad_vertices):
    set_vertices = set()
    while len(set_vertices) < cantidad_vertices:
        pos = randrange(0,max_x*max_y)
        pos_x = pos % max_x
        pos_y = int(pos/max_x)
        set_vertices.add((pos_x,pos_y))
    return tuple(set_vertices)

# genera grafos con nodos tipo tupla (x,y)
def generador_aristas(lista_nodos, cantidad_aristas):
    set_aristas = set()
    while len(set_aristas) < cantidad_aristas:
        indice_1 = randrange(0,len(lista_nodos))
        indice_2 = randrange(0,len(lista_nodos))
        while indice_2 == indice_1:
            indice_2 = randrange(0,len(lista_nodos))
        nodo_1, nodo_2 = lista_nodos[indice_1], lista_nodos[indice_2]
        peso_arista = sqrt((nodo_2[0] - nodo_1[0]) ** 2 + 
                           (nodo_2[1] - nodo_1[1]) ** 2
                          )
        set_aristas.add( ((nodo_1,nodo_2),peso_arista) )
    return tuple(set_aristas)

def generador_adyacencias(max_x,max_y,cantidad_vertices, cantidad_aristas):
    seed()
    nodos = generador_nodos(max_x,max_y,cantidad_vertices)
    return generador_aristas(nodos,cantidad_aristas)

if __name__ == "__main__":
    aristas_grafo = generador_adyacencias(20,30,45,80)
    for arista in aristas_grafo:
        miembros, peso = arista[0], arista[1]
        print(f"Arista(({miembros[0]},{miembros[1]}), {round(peso, 2)}),")