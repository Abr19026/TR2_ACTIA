# Cada individuo de la población consiste en una lista de nodos adyacentes
# además de su costo total
from grafo import Grafo, tipo_nodo
import random

#Elementos(Individuos) que forman parte de la población
class Ind_ruta:
    def __init__(self) -> None:
        self.camino: list[tipo_nodo] = []
        self.peso = 0
        self.heuristica = 0

#población del algoritmo
class Poblacion:
    def __init__(self, grafo: Grafo, copiar = None) -> None:
        if copiar is None:
            self.elems: set[Ind_ruta] = set()
            self.caminos_cruzados = {nodo: set() for nodo in grafo.get_nodos}
        else:
            self.elems = copiar.elems.copy()
            self.caminos_cruzados = self.caminos_cruzados.copy()

    def agregar_individuo(self, individuo: Ind_ruta):
        if individuo not in self.elems:
            self.elems.add(individuo)
            for i, nodo in enumerate(individuo.camino):
                self.caminos_cruzados[nodo].add((individuo,i))

    def quitar_individuo(self, individuo: Ind_ruta):
        if individuo in self.elems:
            self.elems.remove(individuo)
            for i, nodo in enumerate(individuo.camino):
                self.caminos_cruzados[nodo].remove((individuo,i))
    
    #retorna una pareja al azar compatible en la forma (pareja, indice_corte_mio, indice_corte_pareja)
    #pareja es None si no halló
    def hallar_pareja_azar(self, individuo: Ind_ruta) -> tuple[Ind_ruta, int, int]:
        inicio_busqueda = random.randrange(len(individuo.camino))
        for i, nodo in enumerate(individuo.camino[:inicio_busqueda:], start=inicio_busqueda):
            for p_inter in self.caminos_cruzados[nodo]:
                return (p_inter[0], i, p_inter[1])
        return (None, 0, 0)

# Crea un hijo tomando en cuenta los 2 padres y su punto de corte
# No olvidar agregar valor heuristico y peso al hijo
def reproduccion(padre1: Ind_ruta, i: int, padre2: Ind_ruta, j: int) -> Ind_ruta:
    #crea hijo con inicio de padre 1 y final de padre 2
    #crea hijo con inicio de padre 2 y final de padre 1
    #escoge hijo con mejor heuristica + peso
    pass

def genetico_ruta_mas_corta(grafo: Grafo, poblacion_inicial: Poblacion, minimas_generaciones: int, Nodo_obj: tipo_nodo):
    num_gene_actual = 0
    sols_halladas = set()
    poblacion_actual = Poblacion(copiar=poblacion_inicial);
    while len(sols_halladas) == 0 or (len(sols_halladas) == 0 and num_gene_actual < minimas_generaciones):
        nueva_poblacion = Poblacion(grafo)
        #recombinación
        for individuo in poblacion_actual:
            pareja, i, j = poblacion_actual.hallar_pareja_azar(individuo)
            if pareja is not None:
                hijo = reproduccion(individuo, i, pareja, j)
                #mutación
                    #expansion al azar
                    pass
                    #corte y reemplazo de cola
                    pass
                #quitar ciclos y checar que no se pase del objetivo
                nueva_poblacion.agregar_individuo(hijo)
        
        #selección de población (Mezcla población 1 y 2 para determinar cuales individuos forman nueva gen)
        pass
    return sols_halladas