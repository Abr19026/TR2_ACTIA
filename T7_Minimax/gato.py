# Dada coordenada de 0 a 2
# Retorna posición de 0 a 8
def coord_a_pos(intx,inty):
    return inty*3 + intx

# dada posición de de 0 a 8
# retorna coordenada tupla (x, y) de 0 a 2
def pos_a_coord(posicion):
    return (int(posicion%3),int(posicion/3))

class JuegoGato:
    simbolos_turno = ['O','X']
    str_video = " | | \n-----\n | | \n-----\n | | "
    def __init__(self) -> None:
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]
        self.turno = 1

    def posicion_valida(self, posicion):
        posx, posy = pos_a_coord(posicion)
        return (posicion in range(9) and self.tablero[posy][posx] == 0)

    # Retorna True si se gana el juego al 
    # insertar en esa posición en el turno actual
    def posicion_ganadora(self, posx, posy):
        # si toda la columna es self.turno
        for fila in range(3):
            if self.tablero[fila][posx] != self.turno:
                break
            if fila == 2:
                return True
        # si toda la columna es self.turno
        for columna in range(3):
            if self.tablero[posy][columna] != self.turno:
                break
            if columna == 2:
                return True
            
        # si puede ser diagonal y la diagonal es self.turno
        if posx == posy:
            for pos in range(3):
                if self.tablero[pos][pos] != self.turno:
                    break
                if pos == 2:
                    return True

        if posx == 2-posy:
            for pos in range(3):
                if self.tablero[pos][2 - pos] != self.turno:
                    break
                if pos == 2:
                    return True
        return False

    def insertar_jugada(self, posx, posy, buffer_video = None):
        self.tablero[posy][posx] = self.turno
        if buffer_video is not None:
            buffer_video[12*posy + 2*posx] = self.simbolos_turno[self.turno - 1]

    def alternar_turno(self):
        if self.turno == 1:
            self.turno = 2
        else:
            self.turno = 1

def imprimir_tablero(buffer_vid: list[chr]):
    print(''.join(buffer_vid))

if __name__ == "__main__":
    nuevo_juego = True
    turnos_completados = 0
    while nuevo_juego:
        tablero = JuegoGato()
        buffer_vid = list(JuegoGato.str_video)
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
            imprimir_tablero(buffer_vid)
            turnos_completados += 1

            if tablero.posicion_ganadora(coordx, coordy):
                print( f"FIN DEL JUEGO: GANARON LAS [{tablero.simbolos_turno[tablero.turno - 1]}]")
                break
            
            if turnos_completados >= 9:
                print("FIN DEL JUEGO: LÍMITE DE TURNOS")
            tablero.alternar_turno()
        nuevo_juego = False