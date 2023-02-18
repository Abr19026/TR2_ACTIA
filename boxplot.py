import json
import matplotlib.pyplot as plt
import math

tiempos = None

with open("resultados.json") as datos:
    tiempos = json.load(datos)

array_tiempos = []

for grafo in tiempos:
    array_tiempos.append([tiempos[grafo][nodo] for nodo in tiempos[grafo]])

escala = 20
posics = [55/escala,146/escala,147/escala]
plt.boxplot(array_tiempos, positions = posics)
plt.xticks(posics, [x*escala for x in posics])
plt.show()