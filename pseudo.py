
def movimientos_posibles(a):
    pass

def esta_vacio(b):
    pass

NULL = 0

def heuristica(a,b):
    pass

def copia():
    pass

infinito = float("inf")

def valor_maximo():
    pass

def valor_minimo():
    pass

def opuesto_de():
    pass

# Retorna una tupla (mejor_movimiento, valor_minimax)
def minimax(estado_inicial, esta_maximizando, jugador_a_mejorar, profundidad_maxima):
    
    posibles_movs = movimientos_posibles(estado_inicial)
    
    # Si está en una hoja o ya alxanzó la profundidad máxima
    if esta_vacio(posibles_movs) or profundidad_maxima == 0:
        return [NULL, heuristica(estado_inicial, jugador_a_mejorar)]
    
    # Si aún no llega al fondo
    else:
        mejor_resultado = [NULL, -infinito if esta_maximizando else infinito]
        for movimiento in posibles_movs:
            nuevo_estado = copia(estado_inicial)
            nuevo_estado.aplicar_movimiento_y_alternar_turno(movimiento)
            
            mov_hijo, nuevo_valor = minimax(nuevo_estado, opuesto_de(esta_maximizando), jugador_a_mejorar, profundidad_maxima - 1)

            nuevo_resultado = [movimiento, nuevo_valor]

            if esta_maximizando:
                mejor_resultado = valor_maximo(mejor_resultado, nuevo_resultado)
            else:
                mejor_resultado = valor_minimo(mejor_resultado, nuevo_resultado)
        
        return mejor_resultado
    
# Checa las 8 formas de ganar en el gato (3 de fila, 3 de columna, 2 de diagonal)
# Si el jugador todavía puede ganar con esa forma (El otro jugador todavía no ha marcado
# en la fila, columna, diagonal), entonces sumo 1 a la heuristica
# Si esa forma de ganar esta del lado del oponente resto 1
# Si esa forma de ganar está vacía o ocupada por ambos a la vez, no modifico la heuristica
def heuristica(estado, jugador_mejorar):
    heuristica = 0
    for forma_ganar in estado.formas_de_ganar:
        if en_favor_de_jugador(forma_ganar, jugador_mejorar):
            heuristica += 1
        elif en_favor_de_jugador(forma_ganar, jugador_opuesto):
            heuristica -= 1
        else:
            #no hacer nada
    return heuristica