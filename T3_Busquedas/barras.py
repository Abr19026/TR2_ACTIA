import matplotlib.pyplot as plt
import numpy as np

# Definimos los 10 tiempos que se van a comparar
tiempos = [0.002, 3.319, 0.0, 0.0, 0.0977, 0.002, 0.001, 29.1322, 0.001, 3.299]

# Gráfica de barras
fig, ax = plt.subplots()
ax.bar(range(len(tiempos)), tiempos)
ax.set_xticks(range(len(tiempos)))
ax.set_xticklabels(["Tiempo " + str(i+1) for i in range(len(tiempos))])
ax.set_ylabel("Tiempo (segundos)")
ax.set_title("Comparación de tiempos")
plt.show()