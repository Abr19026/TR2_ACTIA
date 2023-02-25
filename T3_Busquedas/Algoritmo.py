from typing import NamedTuple, Tuple

class Instancia_Mochila(NamedTuple):
    capacidad: float
    valores: list[float]
    pesos: list[float]

    def __repr__(self) -> str:
        str_ret = f"cap = {self.capacidad}\n" + \
                   "valor / peso"
        for i in range(len(self.valores)):
            str_ret += f"\n{i + 1}) {self.valores[i]} {self.pesos[i]}"
        return str_ret

def busqueda_exhaustiva(inst_mochila: Instancia_Mochila):

    n = len(inst_mochila.pesos) # número de elementos
    mejor_valor = 0 # variable para almacenar el mejor valor encontrado
    mejor_solucion = [] # variable para almacenar la mejor solución encontrada
    
    # Iterar sobre todas las combinaciones de elementos posibles
    for i in range(2**n):
        solucion_actual = [] # variable para almacenar la solución actual
        peso_actual = 0 # variable para almacenar el peso actual
        valor_actual = 0 # variable para almacenar el valor actual
        
        # Convertir el índice de la iteración a binario y agregar ceros a la izquierda para que tenga longitud n
        binario = format(i, '0' + str(n) + 'b')
        
        # Verificar qué elementos están incluidos en la solución actual y calcular su peso y valor
        for j in range(n):
            if binario[j] == '1':
                solucion_actual.append(j)
                peso_actual += inst_mochila.pesos[j]
                valor_actual += inst_mochila.valores[j]
        
        # Verificar si la solución actual es mejor que la mejor solución encontrada hasta el momento
        if peso_actual <= inst_mochila.capacidad and valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_solucion = solucion_actual
    
    return (mejor_valor, mejor_solucion)

def busqueda_profundidad(inst_mochila: Instancia_Mochila):
    n = len(inst_mochila.valores)
    mejor_valor = 0
    stack = [(0, 0, 0)]
    #camino_act = []
    #mejor_camino = []
    while stack:
        i, valor, peso = stack.pop()
        if peso > inst_mochila.capacidad:
            continue
        if i == n:
            mejor_valor = max(mejor_valor, valor)
            #mejor_camino = list(camino_act)
            continue
        nuevo_valor, nuevo_peso = inst_mochila.valores[i], inst_mochila.pesos[i]
        stack.append((i+1, valor+nuevo_valor, peso+nuevo_peso))
        stack.append((i+1, valor, peso))

    return (mejor_valor, [])

def busqueda_voraz(inst_mochila: Instancia_Mochila):
    disponibles = list(range(len(inst_mochila.valores)))
    disponibles.sort(key = lambda x: inst_mochila.valores[x]/inst_mochila.pesos[x])
    peso = 0
    valor = 0
    camino = []
    #Voraz
    while(len(disponibles) > 0 and peso <= inst_mochila.capacidad):
        #Halla el que tiene mayor valor por peso
        mejor_nodo = disponibles.pop()
        #Lo agrega al camino
        camino.append(mejor_nodo)
        peso += inst_mochila.pesos[mejor_nodo]
        valor += inst_mochila.valores[mejor_nodo]
    if peso > inst_mochila.capacidad:
        #Quita último paso
        ultimo = camino.pop()
        peso -= inst_mochila.pesos[ultimo]
        valor -= inst_mochila.valores[ultimo]
        #Halla el que aumenta valor sin romper restricciones
        posibles = filter(lambda x: peso + inst_mochila.pesos[x] <= inst_mochila.capacidad ,disponibles)
        try:
            mejor_nodo = max(posibles,key=lambda x: inst_mochila.valores[x])
            #Lo agrega al camino
            camino.append(mejor_nodo)
            peso += inst_mochila.pesos[mejor_nodo]
            valor += inst_mochila.valores[mejor_nodo]
        except ValueError:
            pass
    return (valor,camino)

#Escoge el que minimiza f(x) = peso(x) + peso(x) / valor(x)
def busqueda_a_aster(inst_mochila: Instancia_Mochila):
    disponibles = set(range(len(inst_mochila.valores)))
    peso = 0
    valor = 0
    camino = []
    while(len(disponibles) > 0 and peso <= inst_mochila.capacidad):
        #Halla el que tiene minimiza peso + 1/densidad_valor
        mejor_nodo = min(disponibles, key = lambda x: inst_mochila.pesos[x] * (1 + 1/inst_mochila.valores[x]))
        disponibles.remove(mejor_nodo)
        #Lo agrega al camino
        camino.append(mejor_nodo)
        peso += inst_mochila.pesos[mejor_nodo]
        valor += inst_mochila.valores[mejor_nodo]
    if peso > inst_mochila.capacidad:
        #Quita último paso
        ultimo = camino.pop()
        peso -= inst_mochila.pesos[ultimo]
        valor -= inst_mochila.valores[ultimo]
        #Halla el que aumenta valor sin romper restricciones
        posibles = filter(lambda x: peso + inst_mochila.pesos[x] <= inst_mochila.capacidad ,disponibles)
        try:
            mejor_nodo = max(posibles,key=lambda x: inst_mochila.valores[x])
            #Lo agrega al camino
            camino.append(mejor_nodo)
            peso += inst_mochila.pesos[mejor_nodo]
            valor += inst_mochila.valores[mejor_nodo]
        except ValueError:
            pass
    return (valor,camino)
