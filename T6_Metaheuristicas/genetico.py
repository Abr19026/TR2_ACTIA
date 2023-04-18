"""
QUITAR ELEMENTOS DE DEBUG EN LAS PRUEBAS FINALES
MARCADOS CON __debug__
"""

# Cada individuo de la población consiste en una lista de nodos adyacentes
# además de su costo total
from grafo import Grafo, tipo_nodo
import random
from itertools import pairwise
from math import floor,inf
import heapq

#Elementos(Individuos) que forman parte de la población
class Ind_ruta:
    __slots__ = ("camino", "peso", "heuristica","grafo", "factible", "objetivo")
    def __init__(self, grafo: Grafo, nodo_obj: tipo_nodo) -> None:
        self.grafo = grafo
        self.camino: list[tipo_nodo] = []
        self.peso = 0
        self.heuristica = 0
        self.factible = False
        self.objetivo = nodo_obj

    #retorna el peso del camino hasta el nodo en el indice dado
    def peso_hasta_indice(self, indice:int)-> float:
        suma = 0
        inicio = 0
        fin = len(self.camino)
        if len(self.camino) - indice > indice:
            fin = indice + 1
        else:
            inicio = indice
            suma = -self.peso

        for nodo1, nodo2 in pairwise(self.camino[inicio:fin:]):
            suma += self.grafo.costo_nodo(nodo1,nodo2)
        return abs(suma)

    # corta una cantidad de elementos del camino
    def corte(self, elementos: int, heuristica):
        peso_quitar = self.peso - self.peso_hasta_indice(len(self.camino) - 1 - elementos)
        del self.camino[-elementos::]
        self.peso -= peso_quitar
        self.heuristica = heuristica(self.camino[-1], self.objetivo)

        if __debug__:
            peso_real = self.peso_hasta_indice(len(self.camino) - 1)
            if self.peso != peso_real:
                raise Exception(f"Hijo cortado no tiene peso válido, peso = {self.peso}, real = {peso_real}")

    # expande al azar
    def expandir_azar(self, elementos: int, heuristica):
        for i in range(elementos):
            lista_vecinos = list(self.grafo.get_vecinos(self.camino[-1]))
            nuevo_nodo = random.choice(lista_vecinos)
            self.peso += self.grafo.costo_nodo(self.camino[-1], nuevo_nodo)
            self.camino.append(nuevo_nodo)
        self.heuristica = heuristica(self.camino[-1], self.objetivo)
        
        if __debug__:
            peso_real = self.peso_hasta_indice(len(self.camino) - 1)
            if self.peso != peso_real:
                raise Exception(f"Hijo expandido no tiene peso válido, peso = {self.peso}, real = {peso_real}")

    # corta si se pasa del final,y retorna 1 si llega al final
    def hijo_checar(self, heuristica) -> bool:
        for ind, nodo in enumerate(self.camino):
            if nodo == self.objetivo:
                self.corte(len(self.camino) - 1 - ind, heuristica)
                return True
        return False
    
#población del algoritmo
class Poblacion:
    __slots__ = ("elems", "caminos_cruzados","grafo")
    def __init__(self, grafo: Grafo, copiar = None) -> None:
        if copiar is None:
            self.elems: set[Ind_ruta] = set()
            self.caminos_cruzados = {nodo: set() for nodo in grafo.get_nodos()}
            self.grafo = grafo
        else:
            self.elems = copiar.elems.copy()
            self.caminos_cruzados = copiar.caminos_cruzados.copy()
            self.grafo = copiar.grafo

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
        for i, nodo in enumerate(individuo.camino[inicio_busqueda::], start=inicio_busqueda):
            for p_inter in self.caminos_cruzados[nodo]:
                if p_inter[0] is not individuo:
                    return (p_inter[0], i, p_inter[1])
        return (None, 0, 0)

def combinar_poblaciones(poblacion1: Poblacion,poblacion2: Poblacion) -> tuple[Poblacion, set]:
    union_individuos = poblacion1.elems.union(poblacion2.elems)
    
    seleccionados = heapq.nsmallest(len(poblacion1.elems),union_individuos,lambda x: x.peso + x.heuristica)
    
    factibles = set([x for x in seleccionados if x.factible == True])
    
    nueva_pobl = Poblacion(poblacion1.grafo)
    for x in seleccionados:
        nueva_pobl.agregar_individuo(x)
    return (nueva_pobl, factibles)

class Info_p:
    __slots__ = ("padre", "indice_corte", "peso_hasta_corte","peso_despues_corte")
    def __init__(self, padre, indice_corte) -> None:
        self.padre = padre
        self.indice_corte = indice_corte
        self.peso_hasta_corte = 0
        self.peso_despues_corte = 0

class Info_hijo:
    __slots__ = ("peso","valor")

var_global = -1
# Crea un hijo tomando en cuenta los 2 padres y su punto de corte
def reproduccion(padre1: Ind_ruta, i: int, padre2: Ind_ruta, j: int) -> Ind_ruta:
    global var_global
    info_padres = (Info_p(padre1,i), Info_p(padre2,j))
    valores_hijos = (Info_hijo(), Info_hijo())
    for x in info_padres:
        x.peso_hasta_corte = x.padre.peso_hasta_indice(x.indice_corte)
        x.peso_despues_corte = x.padre.peso - x.peso_hasta_corte

    for n,hijo in enumerate(valores_hijos):
        hijo.peso = \
            info_padres[n].peso_hasta_corte +\
            info_padres[1 - n].peso_despues_corte
        hijo.valor = hijo.peso + info_padres[1-n].padre.heuristica

    #indice del mejor hijo
    mejor_hijo_ind = min( range(len(valores_hijos)), key=lambda x: valores_hijos[x].valor)
    var_global = mejor_hijo_ind

    info_padre_1 = info_padres[mejor_hijo_ind]
    info_padre_2 = info_padres[1 - mejor_hijo_ind]
    hijo = Ind_ruta(padre1.grafo,padre1.objetivo)
    hijo.peso = valores_hijos[mejor_hijo_ind].peso
    hijo.heuristica = valores_hijos[mejor_hijo_ind].valor - hijo.peso
    hijo.camino = info_padre_1.padre.camino[:info_padre_1.indice_corte:] + \
                info_padre_2.padre.camino[info_padre_2.indice_corte::]
    #####
    if __debug__:
        peso_real = hijo.peso_hasta_indice(len(hijo.camino) - 1)
        if peso_real != hijo.peso:
            raise Exception(f"Hijo creado no tiene peso válido, peso = {hijo.peso}, real = {peso_real}")
    #####
    return hijo

def genetico_ruta_mas_corta(grafo: Grafo, 
                            poblacion_inicial: Poblacion, 
                            minimas_generaciones: int,
                            heurist) -> set[Ind_ruta]:
    num_gene_actual = 0
    sols_halladas: set[Ind_ruta] = set()
    poblacion_actual = Poblacion(grafo = None, copiar=poblacion_inicial)
    while len(sols_halladas) == 0 or (len(sols_halladas) == 0 and num_gene_actual < minimas_generaciones):
        nueva_poblacion = Poblacion(grafo)
        ## recombinación ##
        for individuo in poblacion_actual.elems:
            pareja, i, j = poblacion_actual.hallar_pareja_azar(individuo)
            if pareja is not None:
                hijo = reproduccion(individuo, i, pareja, j)
                ## mutación ##
                #expansion al azar (de 0 a 10 nodos)
                hijo.expandir_azar(random.randrange(10), heurist)
                ##hecar que no se pase del objetivo ##
                hijo.factible = hijo.hijo_checar(heurist)
                nueva_poblacion.agregar_individuo(hijo)

        #selección de población (Mezcla población 1 y 2 para determinar cuales individuos forman nueva gen)
        poblacion_actual, sols_halladas = combinar_poblaciones(poblacion_actual, nueva_poblacion)
    return min(sols_halladas, key = lambda x: x.peso)