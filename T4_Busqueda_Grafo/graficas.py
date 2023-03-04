import matplotlib.pyplot as plt
import numpy as np
import json
import os

carpeta_script = os.path.dirname(os.path.abspath(__file__))

# Carga resultados



resultados_amplitud = {}
resultados_dijkstra = {}
resultados_profundidad = {}
with open(carpeta_script + "/resultado_profundidad.json") as arch_result:
    resultados_profundidad = json.load(arch_result)
with open(carpeta_script + "/resultado_amplitud.json") as arch_result:
    resultados_amplitud = json.load(arch_result)
with open(carpeta_script + "/resultado_dijkstra.json") as arch_result:
    resultados_dijkstra = json.load(arch_result)

instancias = []
for grafo in resultados_amplitud:
    instancias.append(grafo)

def iterar_llave_nodo(dicc: dict, grafo, key):
    for nodo in dicc[grafo]:
        if nodo != "Nodo_inicial":
            yield dicc[grafo][nodo][key]
    return

# Diccionario con resultados
resumen = {}

for grafo in resultados_amplitud:
    resultados_graficar = {
    "amplitud": {
        "minimo": None,
        "maximo": None,
        "promedio": None
    },
    "profundidad": {
        "minimo": None,
        "maximo": None,
        "promedio": None
    },
    "dijkstra": {
        "promedio": None
    }}
    cantidad_nodos = 0
    resultados_graficar["amplitud"]["minimo"] = min(iterar_llave_nodo(resultados_amplitud,grafo,"tiempo"))
    resultados_graficar["amplitud"]["maximo"] = max(iterar_llave_nodo(resultados_amplitud,grafo,"tiempo"))
    promedio = 0
    cuenta = 0
    for valor in iterar_llave_nodo(resultados_amplitud,grafo,"tiempo"):
        cuenta += 1
        promedio += valor
    resultados_graficar["amplitud"]["promedio"] = promedio / cuenta


    resultados_graficar["profundidad"]["promedio"] = promedio / cuenta
    resultados_graficar["profundidad"]["minimo"] = min(iterar_llave_nodo(resultados_profundidad,grafo,"tiempo"))
    resultados_graficar["profundidad"]["maximo"] = max(iterar_llave_nodo(resultados_profundidad,grafo,"tiempo"))
    promedio = 0
    cuenta = 0
    for valor in iterar_llave_nodo(resultados_profundidad,grafo,"tiempo"):
        cuenta += 1
        promedio += valor
    resultados_graficar["profundidad"]["promedio"] = promedio / cuenta
    
    resultados_graficar["dijkstra"]["promedio"] = resultados_dijkstra[grafo]["tiempo"]

    resumen[grafo] = resultados_graficar

def iterar_llave_result(dicc: dict, key1,key2):
    for grafo in dicc:
        yield dicc[grafo][key1][key2]
    return
resumen_formato = {}
resumen_formato["min_amp"] = set(iterar_llave_result(resumen,"amplitud","minimo"))
resumen_formato["max_amp"] = set(iterar_llave_result(resumen,"amplitud","maximo"))
resumen_formato["prom_amp"] = set(iterar_llave_result(resumen,"amplitud","promedio"))
resumen_formato["min_prof"] = set(iterar_llave_result(resumen,"amplitud","minimo"))
resumen_formato["max_prof"] = set(iterar_llave_result(resumen,"amplitud","maximo"))
resumen_formato["prom_prof"] = set(iterar_llave_result(resumen,"amplitud","promedio"))
resumen_formato["djikstra"] = set(iterar_llave_result(resumen,"dijkstra","promedio"))

#Graficar resultados de resumen

#Grafica resultados
x = np.arange(len(instancias))  # the label locations
width = 0.12  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(constrained_layout=True)


for attribute, measurement in resumen_formato.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1
plt.yscale('log')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('tiempo (segundos)')
ax.set_title('Tiempos de resolución algoritmos')
ax.set_xticks(x + width, instancias)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 1000)

plt.show()