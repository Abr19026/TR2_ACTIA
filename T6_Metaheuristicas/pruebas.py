from grafos_ejemplo import aristas_g1, aristas_g2, aristas_g3
from genetico import Ind_ruta,Poblacion, genetico_ruta_mas_corta
from grafo import Grafo, tipo_nodo
from math import sqrt, floor

grafos = (Grafo(aristas_g1),Grafo(aristas_g2),Grafo(aristas_g3))
nodos_in_fin =  [((1, 4),(14, 19)),((4, 1),(1, 1)),((18, 28),(4, 6))]

def generar_poblacion(grafo: Grafo, 
                      tamano_pob: int, 
                      tamano_cam: int, 
                      nodo_in: tipo_nodo,
                      nodo_fin: tipo_nodo,
                      heuristica
) -> Poblacion:
    pob = Poblacion(grafo)
    for i in range(tamano_pob):
        nuevo_ind = Ind_ruta(grafo,nodo_fin)
        nuevo_ind.camino.append(nodo_in)
        nuevo_ind.expandir_azar(tamano_cam, heuristica)
        pob.agregar_individuo(nuevo_ind)
    return pob

def heuristica_dist(nodo: tipo_nodo, nodo_final: tipo_nodo):
    return sqrt((nodo_final[0] - nodo[0]) ** 2 + 
                (nodo_final[1] - nodo[1]) ** 2)


for grafo,nodos_busqueda in zip(grafos, nodos_in_fin):
    minimas_generaciones = 10
    tamano_caminos_iniciales = floor(len(grafo.get_nodos())/2)

    nodo_inicial = nodos_busqueda[0]
    nodo_final = nodos_busqueda[1]
    poblacion_inicial = generar_poblacion(grafo, 20, tamano_caminos_iniciales, nodo_inicial, nodo_final, heuristica_dist)
    
    #for camino in poblacion_inicial.elems:
    #    print(camino.camino)
    
    soluciones = genetico_ruta_mas_corta(grafo, poblacion_inicial, minimas_generaciones, heuristica_dist)
    for sol in soluciones:
        print(f"peso = {sol.peso}, heur = {sol.heuristica},\ncamino{sol.camino}\n")