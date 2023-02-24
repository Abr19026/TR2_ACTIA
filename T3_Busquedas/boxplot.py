import matplotlib.pyplot as plt
import numpy as np

# Definimos los 10 tiempos que se van a comparar
tiempos = [0.002, 3.319, 0.0, 0.0, 0.0977, 0.002, 0.001, 29.1322, 0.001, 3.299]

# Boxplot
fig, ax = plt.subplots()
ax.boxplot(tiempos)
ax.set_xticklabels(["Tiempo"])
ax.set_ylabel("Tiempo (segundos)")
ax.set_title("Comparación de tiempos")
plt.show()