import os

FICHAS=(' ', 'X','O')

def borrar_consola():
    """limpiar consola"""
    os.system("cls")

def pulse_tecla_para_continuar():
    """Mostrar el mensaje Presione una tecla para continuar y hacer una pausa hasta que se realize la accion"""
    os.system("pause")

def crear_fila(num_columnas = 3)-> list:
    """Crear las columnas"""
    return list(0 for _ in range(num_columnas))

def comprobar_casilla(tablero: tuple, pos_ficha: dict)-> bool:
    return tablero[pos_ficha['fila']][pos_ficha['columna']] == 0

def crear_tablero(num_filas=3) ->tuple:
    """ Crear el tablero
    :para num_filas: numero de filas del tablero.
        (por defecto se establece el valor 3)
    :return: tupla con la matriz num_filas x num_columnas
    """
    return tuple(crear_fila() for _ in range(num_filas))

def mostrar_fila(fila:list):
    contenido_fila ="| "
    for celda in fila:
        contenido_fila += FICHAS[celda] + " | "
    print(contenido_fila)

def mostrar_tablero(tablero:tuple):
    """mostrar en consola el tablero con las fichas"""
    borrar_consola()
    print("-"*13)
    for fila in tablero:
        mostrar_fila(fila)
        print("-"*13)

def pedir_posicion(fila_col:str,msj:str="") ->int:
    
    pos = None
    if msj != "": print(msj)
    while pos == None:
        try:
            pos = int(input(f'elige la {fila_col} (1,2,3): ')) - 1
            if not 0 <= pos <= 2:
                raise ValueError
        except ValueError:
            pos = None
            print(f"**Error** {fila_col} no valida")
    return pos


def colocar_ficha(tablero:tuple, jugador:int):
    """solicita a un jugador las posiciones
    de la ficha que va a colocar
    :param tablero: matriz de 3x3 con la informacion del tablero
    :param jugador: numero del jugador"""
    pos_ficha={'fila':None, 'columna':None}
    pos_correcta=False
    while not pos_correcta:
        pos_ficha['fila'] = pedir_posicion("fila", f"\nJugador {jugador}, coloque una ficha..")
        pos_ficha['columna'] = pedir_posicion("columna")

        pos_correcta=comprobar_casilla(tablero,pos_ficha)
        if pos_correcta:
            tablero[pos_ficha['fila']][pos_ficha['columna']] = jugador
        else:
            pos_ficha['fila'] = pos_ficha['columna'] = None
            print("***ERROR*** movimiento  invalido")
            pulse_tecla_para_continuar()
            mostrar_tablero(tablero)


def cambiar_turnos(turno:int)-> int:
    if turno%2 == 0:
        return 1
    return 2

def jugar(tablero:tuple):
    turno = 0
    ronda = 0
    ganador=""
    hay_ganador= False
    while not hay_ganador:
        turno=cambiar_turnos(turno)
        if turno == 1:
            ronda+=1

        print(f"\nRONDA {ronda}")
        print("-"*len(f"RONDA {ronda}" + "\n"))
        print(turno)

        colocar_ficha(tablero,turno)
        mostrar_tablero(tablero) # me falta un try que no hace :")

        if ronda >= 3:
            ganador, hay_ganador= verificar_ganador(tablero,ganador, hay_ganador)

        if hay_ganador:
            print(f"\nel jugador {ganador} ha ganado")

        if ronda == 9:
            hay_ganador==True
            print('\nempate\n')

def verificar_ganador(tablero,ganador, hay_ganador) -> tuple:
    if (tablero[2][0]==1 and tablero[2][1]==1 and tablero[2][2]==1 ) or (tablero[1][0]==1 and tablero[1][1]==1 and tablero[1][2]==1 ) or (tablero[0][0]==1 and tablero[0][1]==1 and tablero[0][2]==1 ) or (tablero[0][0]==1 and tablero[1][0]==1 and tablero[2][0]==1 ) or (tablero[0][1]==1 and tablero[1][1]==1 and tablero[2][1]==1 ) or (tablero[0][2]==1 and tablero[1][2]==1 and tablero[2][2]==1 ) or (tablero[0][0]==1 and tablero[1][1]==1 and tablero[2][2]==1 ) or (tablero[0][2]==1 and tablero[1][1]==1 and tablero[2][0]==1 ):
        ganador ="jugador 1"
        hay_ganador=True
        return ganador,hay_ganador
    if (tablero[2][0]==2 and tablero[2][1]==2 and tablero[2][2]==2 ) or (tablero[1][0]==2 and tablero[1][1]==2 and tablero[1][2]==2 ) or (tablero[0][0]==2 and tablero[0][1]==2 and tablero[0][2]==2 ) or (tablero[0][0]==2 and tablero[1][0]==2 and tablero[2][0]==2 ) or (tablero[0][1]==2 and tablero[1][1]==2 and tablero[2][1]==2 ) or (tablero[0][2]==1 and tablero[1][2]==1 and tablero[2][2]==1 ) or (tablero[0][0]==1 and tablero[1][1]==1 and tablero[2][2]==1 ) or (tablero[0][2]==1 and tablero[1][1]==1 and tablero[2][0]==1 ):
        ganador ="jugador 2"
        hay_ganador=True
        return ganador,hay_ganador
    else:
        return ganador,hay_ganador

def main():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)

if __name__=="__main__":
    main()