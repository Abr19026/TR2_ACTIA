from grafo import Grafo
from grafos_ejemplo import aristas_g1,aristas_g2,aristas_g3
from busqueda_amplitud import ruta_mas_corta_amplitud
from busqueda_profundidad import ruta_mas_corta_profundidad
import timeit

# En este archivo se realizarán las pruebas

lista_grafos = [Grafo(aristas_g1),Grafo(aristas_g2),Grafo(aristas_g3)]

iterador = iter(lista_grafos[0].get_nodos())
nodo_fin = "F1"
for nodo in lista_grafos[0].get_nodos():
    t_0 = timeit.default_timer()
    sol = ruta_mas_corta_amplitud(lista_grafos[0], nodo, nodo_fin)
    t_1 = timeit.default_timer() - t_0
    print(f"inicial: {nodo}, final: {nodo_fin}, solucion: {sol}, tiempo {t_1}s")