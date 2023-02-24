from Algoritmo import busqueda_profundidad, Instancia_Mochila
import timeit
import json
from json import JSONEncoder

# NOMBRES DE ARCHIVOS CON INSTANCIAS

direcc_instancias = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt", "f6.txt", "f7.txt", "f8.txt", "f9.txt", "f10.txt"]
carpeta_instancias = "./T3_Busquedas/instancias/"

# CONVIERTE EL ARCHIVO EN UNA INSTANCIA
def archivo_a_instancia(archivo):
    with open(archivo, 'r') as f:
        # Leer las primeras dos líneas del archivo
        n, capacidad = map(int, f.readline().split())

        # Crear listas para almacenar los pesos y valores de los elementos
        pesos = []
        valores = []
        valor_optimo = 0

        # Leer el resto del archivo y agregar los pesos y valores a las listas correspondientes
        for linea in f.readlines():
            v, w = linea.strip().split()
            if v == "op":
                valor_optimo = float(w.replace(',', '.'))
            else:
                valores.append(float(v))
                pesos.append(float(w))

    return (Instancia_Mochila(capacidad,valores,pesos),valor_optimo)

def resultados_instancia(archivo_instancia):
    instancia, valor_optimo = archivo_a_instancia(carpeta_instancias + arch_instancia)
    
    # Calcular la mejor solución y su valor
    t_0 = timeit.default_timer()
    mejor_valor, mejor_solucion = busqueda_profundidad(instancia)
    t_1 = timeit.default_timer()
    tiempo_ejecucion= round((t_1 - t_0), 6)

    # Imprimir los resultados de la instancia
    return {
        "valores": str(instancia.valores),
        "pesos": str(instancia.pesos),
        "tiempo": tiempo_ejecucion,
        "sol_hallada": str(mejor_solucion),
        "val_hallado": mejor_valor,
        "val_optimo": valor_optimo
    }


# REALIZA PRUEBAS
dicc_resultados = {}
for arch_instancia in direcc_instancias:
    resultado_busqueda = resultados_instancia(carpeta_instancias + arch_instancia)
    dicc_resultados[arch_instancia] = resultado_busqueda

with open("./T3_Busquedas/resultados.json","w") as arch_salida:
    json.dump(dicc_resultados,arch_salida, indent=1)