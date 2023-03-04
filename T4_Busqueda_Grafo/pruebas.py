from grafo import Grafo
from grafos_ejemplo import aristas_g1,aristas_g2,aristas_g3
from busqueda_amplitud import ruta_mas_corta_amplitud
from busqueda_profundidad import ruta_mas_corta_profundidad, dijkstra
import timeit
import json
import os

carpeta_script = os.path.dirname(os.path.abspath(__file__))

# En este archivo se realizarán las pruebas
lista_grafos = [Grafo(aristas_g1),Grafo(aristas_g2),Grafo(aristas_g3)]


def probar_amplitud():
    resultados_amplitud = {}
    for i, grafo in enumerate(lista_grafos,1):
        iterador = iter(grafo.get_nodos())
        nodo_inicio = next(iterador)
        resultados_amplitud[i] = {}
        resultados_amplitud[i]["Nodo_inicial"] = nodo_inicio
        for nodo in iterador:
            t_0 = timeit.default_timer()
            ruta, distancia = ruta_mas_corta_amplitud(lista_grafos[i - 1], nodo_inicio, nodo)
            t_1 = round(timeit.default_timer() - t_0, 6)
            resultados_amplitud[i][nodo] = {
                "ruta_hallada": str(ruta),
                "distancia": distancia,
                "tiempo": t_1
            }

    with open(carpeta_script + "./resultado_amplitud.json", "w") as salida:
        json.dump(resultados_amplitud,salida,indent=1)

def probar_dijkstra():
    resultados_dijkstra = {}
    for i, grafo in enumerate(lista_grafos,1):
        nodo_inicio = next(iter(grafo.get_nodos()))

        t_0 = timeit.default_timer()
        results_int = dijkstra(lista_grafos[i - 1], nodo_inicio)
        t_1 = round(timeit.default_timer() - t_0, 6)
        
        resultados_dijkstra[i] = {
            "Nodo_inicial": nodo_inicio,
            "tiempo": t_1
        }

        for nodo in results_int:
            resultados_dijkstra[i][nodo] = {
                "distancia": results_int[nodo]
            }

    with open(carpeta_script + "./resultado_dijkstra.json", "w") as salida:
        json.dump(resultados_dijkstra,salida,indent=1)

def probar_profundidad():
    resultados_profundidad = {}
    for i, grafo in enumerate(lista_grafos,1):
        iterador = iter(grafo.get_nodos())
        nodo_inicio = next(iterador)
        resultados_profundidad[i] = {}
        resultados_profundidad[i]["Nodo_inicial"] = nodo_inicio
        for nodo in iterador:
            t_0 = timeit.default_timer()
            distancia, ruta = ruta_mas_corta_profundidad(lista_grafos[i - 1], nodo_inicio, nodo)
            t_1 = round(timeit.default_timer() - t_0, 6)
            resultados_profundidad[i][nodo] = {
                "ruta_hallada": str(ruta),
                "distancia": distancia,
                "tiempo": t_1
            }

    with open(carpeta_script + "./resultado_profundidad.json", "w") as salida:
        json.dump(resultados_profundidad,salida,indent=1)

probar_amplitud()
probar_profundidad()
probar_dijkstra()
