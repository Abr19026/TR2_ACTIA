from typing import NamedTuple

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

def busqueda_profundidad(inst_mochila):

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
    
    return mejor_valor, mejor_solucion