"""
BLOQUE 1
CREACION DE LA CANCHA
"""

# declaramos las constantes de filas y columnas de la cancha
FILAS = 100
COLUMNAS = 60

# roles y equipos validos segun la consigna
ROLES_VALIDOS = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]


# funcion encargada de crear una cancha vacia
def crear_cancha():

    # creamos una lista vacia donde vamos a guardar toda la cancha
    cancha = []

    # recorremos las filas de la cancha
    for fila in range(FILAS):

        # creamos una nueva fila vacia
        fila_cancha = []

        # recorremos las columnas de la cancha
        for columna in range(COLUMNAS):

            # agregamos una posicion vacia simulada con un "."
            fila_cancha.append(".")

        # cuando la fila esta completa la agregamos a la cancha
        cancha.append(fila_cancha)

    # devolvemos la cancha ya creada
    return cancha


"""
BLOQUE 2
IMPRIMIR LA CANCHA
"""

# funcion encargada de imprimir la matriz de la cancha
def imprimir_matriz(cancha_imprimir):

    # recorremos cada fila de la cancha
    for fila in cancha_imprimir:

        # join une todos los elementos de la fila en un solo texto,
        # separando cada posicion con un espacio
        # de esta forma imprimimos una fila completa por cada print
        print(" ".join(fila))


"""
BLOQUE 3
VALIDACIONES BASICAS
"""

# funcion encargada de validar si una posicion esta dentro de los limites de la cancha
def posicion_valida(fila, columna):

    valida = True

    # la fila debe estar entre 0 y 99
    # la columna debe estar entre 0 y 59
    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        valida = False

    return valida


# funcion encargada de validar si el equipo ingresado es correcto
def equipo_valido(equipo):

    valida = True

    # los equipos validos son solamente "A" y "B"
    if equipo not in EQUIPOS_VALIDOS:
        valida = False

    return valida


# funcion encargada de validar si el rol ingresado es correcto
def rol_valido(rol):

    valida = True

    # los roles validos son arquero, defensor, mediocampista y delantero
    if rol not in ROLES_VALIDOS:
        valida = False

    return valida


# funcion encargada de verificar si una celda de la cancha esta ocupada
def celda_ocupada(cancha, fila, columna):

    ocupada = False

    # si la celda no contiene ".", significa que tiene un jugador o un obstaculo
    if cancha[fila][columna] != ".":
        ocupada = True

    return ocupada


"""
BLOQUE 4
CREACION Y GESTION DE JUGADORES
"""

# funcion encargada de verificar si alguien ya tiene la pelota
def hay_pelota_en_juego(jugadores_argentina, jugadores_brasil):

    hay_pelota = False

    # recorremos los jugadores de Argentina
    for jugador in jugadores_argentina:
        if jugador["tiene_pelota"] == True:
            hay_pelota = True

    # recorremos los jugadores de Brasil
    for jugador in jugadores_brasil:
        if jugador["tiene_pelota"] == True:
            hay_pelota = True

    return hay_pelota


# funcion auxiliar para obtener todos los jugadores en una sola lista
def obtener_todos_los_jugadores(jugadores_argentina, jugadores_brasil):

    return jugadores_argentina + jugadores_brasil


"""
BLOQUE 5
POSICIONAMIENTO DE JUGADORES
"""

# funcion encargada de posicionar un jugador en la cancha
def posicionar_jugador(cancha, jugadores_argentina, jugadores_brasil, nombre, equipo, fila, columna, rol, tiene_pelota):

    agregado = False

    # validacion: equipo valido
    if not equipo_valido(equipo):
        print("Error: el equipo " + equipo + " no es valido. Use A o B.")

    # validacion: rol valido
    elif not rol_valido(rol):
        print("Error: el rol " + rol + " no es valido.")

    # validacion: posicion dentro de la cancha
    elif not posicion_valida(fila, columna):
        print("Error: la posicion (" + str(fila) + ", " + str(columna) + ") esta fuera de la cancha.")

    # validacion: celda ocupada
    elif celda_ocupada(cancha, fila, columna):
        print("Error: la celda (" + str(fila) + ", " + str(columna) + ") ya esta ocupada.")

    # validacion: solo un jugador puede tener la pelota
    elif tiene_pelota == True and hay_pelota_en_juego(jugadores_argentina, jugadores_brasil):
        print("Error: ya hay un jugador con la pelota en la cancha.")

    else:

        # creamos el diccionario del jugador
        jugador = {
            "nombre": nombre,
            "equipo": equipo,
            "fila": fila,
            "columna": columna,
            "rol": rol,
            "tiene_pelota": tiene_pelota
        }

        # lo agregamos a la lista correspondiente y actualizamos la matriz
        if equipo == "A":
            jugadores_argentina.append(jugador)
            cancha[fila][columna] = "A"

        else:
            jugadores_brasil.append(jugador)
            cancha[fila][columna] = "B"

        print("Jugador " + nombre + " agregado correctamente en (" + str(fila) + ", " + str(columna) + ").")

        agregado = True

    return agregado


"""
BLOQUE 6
OBSTACULOS
"""

# funcion encargada de agregar un obstaculo en la cancha
def agregar_obstaculo(cancha, fila, columna):

    agregado = False

    # validamos que la posicion este dentro de la cancha
    if not posicion_valida(fila, columna):
        print("Error: la posicion del obstaculo esta fuera de la cancha.")

    # validamos que la celda no este ocupada
    elif celda_ocupada(cancha, fila, columna):
        print("Error: no se puede agregar el obstaculo porque la celda esta ocupada.")

    else:
        cancha[fila][columna] = "X"
        print("Obstaculo agregado correctamente en (" + str(fila) + ", " + str(columna) + ").")
        agregado = True

    return agregado


"""
BLOQUE 7
MOVER JUGADOR - TAREA 3
"""

# funcion que calcula la nueva posicion segun la direccion
def calcular_destino(fila, columna, direccion):

    nueva_fila = None
    nueva_columna = None

    if direccion == "arriba":
        nueva_fila = fila - 1
        nueva_columna = columna

    elif direccion == "abajo":
        nueva_fila = fila + 1
        nueva_columna = columna

    elif direccion == "izquierda":
        nueva_fila = fila
        nueva_columna = columna - 1

    elif direccion == "derecha":
        nueva_fila = fila
        nueva_columna = columna + 1

    return nueva_fila, nueva_columna


# funcion encargada de mover un jugador en la cancha
def mover_jugador(cancha, jugador, direccion):

    movimiento_exitoso = False

    # calculamos la nueva posicion segun la direccion elegida
    nueva_fila, nueva_columna = calcular_destino(jugador["fila"], jugador["columna"], direccion)

    # verificamos si la direccion ingresada existe
    if nueva_fila is None:
        print("Movimiento invalido: direccion '" + direccion + "' no reconocida.")

    # verificamos que la nueva posicion este dentro de la cancha
    elif not posicion_valida(nueva_fila, nueva_columna):
        print("Movimiento invalido: no se puede salir de la cancha.")

    # verificamos que la nueva celda no este ocupada por jugador u obstaculo
    elif celda_ocupada(cancha, nueva_fila, nueva_columna):
        print("Movimiento invalido: la celda destino esta ocupada.")

    else:

        # guardamos la posicion actual antes de mover
        fila_anterior = jugador["fila"]
        columna_anterior = jugador["columna"]

        # limpiamos la posicion anterior en la matriz
        cancha[fila_anterior][columna_anterior] = "."

        # actualizamos la posicion del jugador en su diccionario
        jugador["fila"] = nueva_fila
        jugador["columna"] = nueva_columna

        # actualizamos la nueva posicion en la matriz con el equipo del jugador
        cancha[nueva_fila][nueva_columna] = jugador["equipo"]

        print("Movimiento exitoso: " + jugador["nombre"] + " se movio hacia " + direccion + ".")

        movimiento_exitoso = True

    return movimiento_exitoso



"""

BLOQUE 8

DISTANCIA A LA PELOTA - TAREA 4

"""

# funcion encargada de buscar y devolver el jugador que tiene la pelota

def obtener_jugador_con_pelota(jugadores_argentina, jugadores_brasil):

    # juntamos todos los jugadores en una sola lista

    jugadores = obtener_todos_los_jugadores(jugadores_argentina, jugadores_brasil)

    # creamos una variable para guardar al jugador con pelota

    jugador_con_pelota = None

    # recorremos todos los jugadores

    for jugador in jugadores:

        # si encontramos un jugador que tiene la pelota, lo guardamos

        if jugador["tiene_pelota"] == True:

            jugador_con_pelota = jugador

    return jugador_con_pelota

# funcion encargada de calcular y mostrar la distancia Manhattan de cada jugador a la pelota

def calcular_distancias_a_pelota(jugadores_argentina, jugadores_brasil):

    # obtenemos el jugador que tiene la pelota

    jugador_con_pelota = obtener_jugador_con_pelota(jugadores_argentina, jugadores_brasil)

    # verificamos que exista un jugador con pelota

    if jugador_con_pelota == None:

        print("Error: no hay ningun jugador con la pelota.")

    else:

        # juntamos todos los jugadores en una sola lista

        jugadores = obtener_todos_los_jugadores(jugadores_argentina, jugadores_brasil)

        # usamos una variable para guardar la distancia minima encontrada

        distancia_minima = None

        # usamos una lista para guardar los jugadores mas cercanos

        jugadores_mas_cercanos = []

        print("\nDistancias a la pelota:")

        # recorremos todos los jugadores

        for jugador in jugadores:

            # calculamos la distancia Manhattan:

            # diferencia entre filas + diferencia entre columnas

            distancia = abs(jugador["fila"] - jugador_con_pelota["fila"]) + abs(jugador["columna"] - jugador_con_pelota["columna"])

            print(jugador["nombre"] + ": " + str(distancia))

            # si distancia_minima todavia no tiene valor, guardamos la primera distancia

            if distancia_minima == None:

                distancia_minima = distancia

                jugadores_mas_cercanos = [jugador]

            # si encontramos una distancia menor, actualizamos la distancia minima

            # y reiniciamos la lista de jugadores mas cercanos

            elif distancia < distancia_minima:

                distancia_minima = distancia

                jugadores_mas_cercanos = [jugador]

            # si encontramos una distancia igual a la minima, agregamos al jugador a la lista

            elif distancia == distancia_minima:

                jugadores_mas_cercanos.append(jugador)

        print("\nJugador/es mas cercano/s a la pelota:")

        for jugador in jugadores_mas_cercanos:

            print(jugador["nombre"] + " con distancia " + str(distancia_minima))






"""

BLOQUE 9

PASES POSIBLES - TAREA 5

"""

# funcion encargada de verificar si existe un pase posible entre dos jugadores

def pase_posible(cancha, jugador_origen, jugador_destino):

    posible = True

    # validamos que los jugadores pertenezcan al mismo equipo

    if jugador_origen["equipo"] != jugador_destino["equipo"]:

        posible = False

    # validamos que el pase sea en linea recta

    # esto significa que deben estar en la misma fila o en la misma columna

    elif jugador_origen["fila"] != jugador_destino["fila"] and jugador_origen["columna"] != jugador_destino["columna"]:

        posible = False

    else:

        # si estan en la misma fila, analizamos las columnas que hay entre ambos jugadores

        if jugador_origen["fila"] == jugador_destino["fila"]:

            fila = jugador_origen["fila"]

            # determinamos desde que columna hasta que columna hay que revisar

            if jugador_origen["columna"] < jugador_destino["columna"]:

                inicio = jugador_origen["columna"] + 1

                fin = jugador_destino["columna"]

            else:

                inicio = jugador_destino["columna"] + 1

                fin = jugador_origen["columna"]

            # recorremos las celdas intermedias entre los dos jugadores

            columna = inicio

            while columna < fin and posible == True:

                # un obstaculo bloquea el pase

                if cancha[fila][columna] == "X":

                    posible = False

                # un rival bloquea el pase

                elif cancha[fila][columna] != "." and cancha[fila][columna] != jugador_origen["equipo"]:

                    posible = False

                columna = columna + 1

        # si estan en la misma columna, analizamos las filas que hay entre ambos jugadores

        elif jugador_origen["columna"] == jugador_destino["columna"]:

            columna = jugador_origen["columna"]

            # determinamos desde que fila hasta que fila hay que revisar

            if jugador_origen["fila"] < jugador_destino["fila"]:

                inicio = jugador_origen["fila"] + 1

                fin = jugador_destino["fila"]

            else:

                inicio = jugador_destino["fila"] + 1

                fin = jugador_origen["fila"]

            # recorremos las celdas intermedias entre los dos jugadores

            fila = inicio

            while fila < fin and posible == True:

                # un obstaculo bloquea el pase

                if cancha[fila][columna] == "X":

                    posible = False

                # un rival bloquea el pase

                elif cancha[fila][columna] != "." and cancha[fila][columna] != jugador_origen["equipo"]:

                    posible = False

                fila = fila + 1

    return posible

# funcion encargada de listar todos los pases posibles para el jugador que tiene la pelota

def listar_pases_posibles(cancha, jugadores_argentina, jugadores_brasil):

    # buscamos al jugador que tiene la pelota

    jugador_con_pelota = obtener_jugador_con_pelota(jugadores_argentina, jugadores_brasil)

    if jugador_con_pelota == None:

        print("Error: no hay ningun jugador con la pelota.")

    else:

        jugadores = obtener_todos_los_jugadores(jugadores_argentina, jugadores_brasil)

        hay_pases = False

        print("\nPases posibles para " + jugador_con_pelota["nombre"] + ":")

        for jugador in jugadores:

            # no tiene sentido analizar pase hacia si mismo

            if jugador != jugador_con_pelota:

                # solo analizamos compañeros del mismo equipo

                if jugador["equipo"] == jugador_con_pelota["equipo"]:

                    if pase_posible(cancha, jugador_con_pelota, jugador):

                        print("- Pase posible a " + jugador["nombre"])

                        hay_pases = True

        if hay_pases == False:

            print("No hay pases posibles disponibles.")


"""

BLOQUE 10

PROGRAMA PRINCIPAL DE PRUEBA

"""

def main():

    # creamos la matriz de la cancha

    matriz_cancha = crear_cancha()

    # creamos listas vacias para los jugadores de cada equipo

    jugadores_argentina = []

    jugadores_brasil = []

    print("Cancha creada correctamente.")

    # posicionamos jugadores de prueba

    posicionar_jugador(matriz_cancha, jugadores_argentina, jugadores_brasil,

                       "Otamendi", "A", 50, 10, "defensor", False)

    posicionar_jugador(matriz_cancha, jugadores_argentina, jugadores_brasil,

                       "Messi", "A", 50, 20, "delantero", True)

    posicionar_jugador(matriz_cancha, jugadores_argentina, jugadores_brasil,

                       "Neymar", "B", 50, 30, "delantero", False)

    # agregamos un obstaculo para probar movimientos invalidos

    agregar_obstaculo(matriz_cancha, 49, 10)

    # verificamos algunas celdas puntuales

    print("Celda Otamendi:", matriz_cancha[50][10])

    print("Celda Messi:", matriz_cancha[50][20])

    print("Celda Neymar:", matriz_cancha[50][30])

    print("Celda obstaculo:", matriz_cancha[49][10])

    # probamos movimiento hacia obstaculo

    mover_jugador(matriz_cancha, jugadores_argentina[0], "arriba")

    # probamos movimiento valido

    mover_jugador(matriz_cancha, jugadores_argentina[0], "derecha")

    print("Nueva posicion de Otamendi:", jugadores_argentina[0])

    # calculamos las distancias de todos los jugadores a la pelota

    calcular_distancias_a_pelota(jugadores_argentina, jugadores_brasil)

    # listamos los pases posibles para el jugador que tiene la pelota

    listar_pases_posibles(matriz_cancha, jugadores_argentina, jugadores_brasil)

    # si quieren ver la cancha completa, descomentar esta linea

    # imprimir_matriz(matriz_cancha)

# este bloque indica el punto de inicio del programa

if __name__ == "__main__":

    main()