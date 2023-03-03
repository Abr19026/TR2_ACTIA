from grafo import Grafo
from itertools import permutations, pairwise, filterfalse
from typing import Iterable, Tuple


# AQUI PON EL CÓDIGO PARA TU BUSQUEDA NO INFORMADA

def ruta_mas_corta_profundidad(grafo: Grafo, Nodo_inicial,Nodo_final):
    pass

# Para amplitud con perutaciones de 

def ruta_mas_corta_amplitud(grafo: Grafo, Nodo_inicial, Nodo_final):
    
    nodos_grafo = set(grafo.get_nodos())
    nodos_grafo.remove(Nodo_inicial)
    nodos_grafo = tuple(nodos_grafo)
    # Mejor solución hasta ahora
    mejor_peso_solucion = float("inf")
    mejor_camino = ()

    # Longitud de los caminos
    profundidad_act = 1
    # Crea todas las rutas sin ciclos con profundidad actual
    permutaciones_profund = permutations(nodos_grafo, profundidad_act)

    while True: # Por cada nivel de profundidad
        menor_peso_act = float('inf')   # Guarda el menor peso en esta produndidad
        # Checa todas las posibles rutas validas
        for ruta_actual in filter(lambda x: cadena_valida(grafo,Nodo_inicial,x), permutaciones_profund):
            nuevo_peso = peso_cadena(grafo,ruta_actual)
            # Se guardan soluciones con menor peso
            if ruta_actual[-1] == Nodo_final and nuevo_peso < mejor_peso_solucion:
                mejor_peso_solucion = nuevo_peso
                mejor_camino = ruta_actual
            # Guarda peso menor de esta profundidad
            if nuevo_peso < menor_peso_act:
                menor_peso_act = nuevo_peso
        # Aumenta profundidad de siguiente ciclo
        profundidad_act += 1
        # Terminar ciclo si:
        # Menor peso de nivel actual es mayor a solución hallada
        # O ya no hay caminos que crear
        if menor_peso_act > mejor_peso_solucion or profundidad_act >= len(nodos_grafo):
            break
        else:
            # Genera nueva busqueda de caminos
            permutaciones_profund = permutations(nodos_grafo, profundidad_act)

    return (mejor_camino, mejor_peso_solucion)

#Dada una cadena retorna el peso
def peso_cadena(grafo: Grafo, cadena_acciones: Tuple):
    suma = 0
    for pareja in pairwise(cadena_acciones):
        suma += grafo.adyacencias[pareja[0]][pareja[1]]
    return suma

# Retorna True si el primer nodo en cadena_acciones es nodo_inicial
# y todos los nodos consecutivos en la cadena tienen una conexión en el grafo
def cadena_valida(grafo: Grafo, nodo_inicial, cadena_acciones: Tuple):
    if cadena_acciones[0] in grafo.adyacencias[nodo_inicial]:
        for invalido in filterfalse(lambda x: x[1] in grafo.adyacencias[x[0]],pairwise(cadena_acciones)):
            return False
        return True
    else:
        return False