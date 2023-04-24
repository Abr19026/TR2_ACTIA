# Dada coordenada de 0 a 2
# Retorna posición de 0 a 8
def coord_a_pos(intx,inty):
    return inty*3 + intx

# dada posición de de 0 a 8
# retorna coordenada tupla (x, y) de 0 a 2
def pos_a_coord(posicion):
    return (int(posicion%3),int(posicion/3))

class JuegoGato:
    otro_turno = (0, 2, 1)
    simbolos_turno = ('O','X')
    str_video = " | | \n-----\n | | \n-----\n | | "
    
    def __init__(self) -> None:
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]
        # 0-2 filas de arriba a abajo
        # 3-5 columnas de izquierda a derecha
        # 6-7 diagonal y diagonal inversa respectivamente
        # si es 0 no ha sido ocupada, 
        # si es >0 ocupado por jugador 1
        # si es <0 por jugador 2
        # si es 11 ocupado por ambos
        # Ganó jugador 1, 2 si llega a 3,-3 respectivamente
        self.estado_formas_ganar = [0,0,0,0,0,0,0,0]
        self.formas_ganar_anuladas = 0 # si llega a 8 ya no puede ganar nadie
        self.juego_terminado = 0 # 0 si no, 1 si ganó alguien, 2 si empate
        self.turno = 1

    def copiar(self):
        copia = JuegoGato()
        
        for x in range(len(self.tablero)):
            copia.tablero[x] = [y for y in self.tablero[x]]
        copia.estado_formas_ganar = [x for x in self.estado_formas_ganar]
        copia.formas_ganar_anuladas = self.formas_ganar_anuladas
        copia.juego_terminado = self.juego_terminado
        copia.turno = self.turno
        return copia

    def posicion_valida(self, posicion):
        posx, posy = pos_a_coord(posicion)
        return (posicion in range(9) and self.tablero[posy][posx] == 0)

    def set_ganancia(self, rango_valido: range, pos_ganancia):
        if self.estado_formas_ganar[pos_ganancia] in rango_valido:
            self.estado_formas_ganar[pos_ganancia] += rango_valido[1]
            # Marca si alguien ya ganó el juego
            if self.estado_formas_ganar[pos_ganancia] == rango_valido[-1]:
                self.juego_terminado = 1
        else:
            # Quita esa forma de ganar
            if self.estado_formas_ganar != 11:
                self.formas_ganar_anuladas += 1
                self.estado_formas_ganar[pos_ganancia] = 11
                # Marca empate si ya no hay formas de ganar
                if self.formas_ganar_anuladas == 8:
                    self.juego_terminado = 2

    def actualizar_estado_juego(self, posx, posy):
        signo_ganancia = 1
        if self.turno == 2:
            signo_ganancia = -1
        rango_valido = range(0, signo_ganancia*4, signo_ganancia)
        #actualiza fila
        self.set_ganancia(rango_valido, posy)

        #actualiza columna
        self.set_ganancia(rango_valido, 3 + posx)
        
        #actualiza diagonal principal
        if posx == posy:
            self.set_ganancia(rango_valido, 6)
        
        #actualiza diagonal inversa
        if posx == 2 - posy:
            self.set_ganancia(rango_valido, 7)
    
    # inserta jugada, actualiza buffer de video dado (si es que hay)
    # el buffer de video tiene que estar basado en JuegoGato.str_video
    def insertar_jugada(self, posx, posy, buffer_video = None):
        self.tablero[posy][posx] = self.turno
        self.actualizar_estado_juego(posx, posy)
        if buffer_video is not None:
            buffer_video[12*posy + 2*posx] = self.simbolos_turno[self.turno - 1]

    def tablero_con_numeros():
        buffer_vid = list(JuegoGato.str_video)
        for x in range(3):
            for y in range(3):
                buffer_vid[12*y + 2*x] = str(3*y + x + 1)
        return buffer_vid
    # cambia el jugador
    def alternar_turno(self):
        self.turno = self.otro_turno[self.turno]

def imprimir_tablero(buffer_vid: list[chr]):
    print(''.join(buffer_vid))

# prueba juego de gato manual
if __name__ == "__main__":
    nuevo_juego = True
    turnos_completados = 0
    while nuevo_juego:
        tablero = JuegoGato()
        buffer_vid = JuegoGato.tablero_con_numeros()
        imprimir_tablero(buffer_vid)
        while True:

            # Pide entrada
            print(f"Turno de [{tablero.simbolos_turno[tablero.turno - 1]}]")
            pos_input = -1
            
            # Valida entrada
            while pos_input == -1:
                try:
                    # Checa que sea un numero
                    entrada = input("introduzca posición del 1 al 9: ")
                    pos_input = int(entrada) - 1
                    
                    # Checa que no esté ocupada en el tablero
                    if not tablero.posicion_valida(pos_input):
                        print("No puede colocar ahí")
                        pos_input = -1
                
                except Exception:
                    print("Entrada no válida")
                    pos_input = -1

            # Inserta jugada
            coordx, coordy = pos_a_coord(pos_input)
            tablero.insertar_jugada(coordx, coordy, buffer_vid)
            print("--------------------------")
            imprimir_tablero(buffer_vid)
            turnos_completados += 1

            if tablero.juego_terminado == 1:
                print( f"FIN DEL JUEGO: GANARON LAS [{tablero.simbolos_turno[tablero.turno - 1]}]")
                break
            elif tablero.juego_terminado == 2:
                print("FIN DEL JUEGO: EMPATE")
                break
            tablero.alternar_turno()
        nuevo_juego = False