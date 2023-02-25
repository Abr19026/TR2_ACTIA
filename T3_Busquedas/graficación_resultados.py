import matplotlib.pyplot as plt
import numpy as np
import json
import os
from collections import defaultdict

carpeta_script = os.path.dirname(os.path.abspath(__file__))

# Carga resultados
resultados = {}
with open(carpeta_script + "/resultados.json") as arch_result:
    resultados = json.load(arch_result)

# Acomoda resultados
instancias = tuple(x for i, x in enumerate(resultados.keys()))
algoritmos = tuple(x for x in resultados[next(iter(resultados))]["comparacion"])
algoritmos_tiempos = defaultdict(list)

for algoritmo in algoritmos:
    for inst in instancias:
        algoritmos_tiempos[algoritmo].append(resultados[inst]["comparacion"][algoritmo]["tiempo"])

for alg in algoritmos_tiempos:
    print(f"{alg}: {algoritmos_tiempos[alg]}")

#Grafica resultados
x = np.arange(len(instancias))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0.4

fig, ax = plt.subplots(constrained_layout=True)


for attribute, measurement in algoritmos_tiempos.items():
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
