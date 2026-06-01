"""
BLOQUE 1
CREACION DE LA CANCHA
"""



# funcion encargada de crear una cancha vacia
def crear_cancha(ancho, largo):

    # creamos una lista vacia donde vamos a guardar toda la cancha
    cancha = []

    # recorremos las filas de la cancha
    for fila in range(ancho):

        # creamos una nueva fila vacia
        fila_cancha = []

        # recorremos las columnas de la cancha
        for columna in range(largo):

            # agregamos una posicion vacia simulada con un "."
            fila_cancha.append(".")

        # cuando la fila esta completa la agregamos a la cancha
        cancha.append(fila_cancha)

    # devolvemos la cancha ya creada
    return cancha

"""
CREACION DE JUGADOR
Ingreso: Datos del jugador
Devuelve: Jugador creado para agregar al diccionario
"""
def crear_jugador(nombre, equipo, fila, columna, rol, tiene_pelota):
    return {
        "nombre": nombre,
        "equipo": equipo,
        "fila": fila,
        "columna": columna,
        "rol": rol,
        "tiene_pelota": tiene_pelota
    }

"""
CREA LOS JUGADORES
Recibe: El diccionario de jugadores y dato del jugador
Devuelve: El diccionario actualizado
"""
def agregar_jugador(jugadores_total, nombre, equipo, fila, columna, rol, tiene_pelota):
    if len(jugadores_total) == 0:
        id_jugador = 1
    else:
        id_jugador = max(jugadores_total) + 1

    jugadores_total[id_jugador] = crear_jugador(nombre, equipo, fila, columna, rol, tiene_pelota)
    return jugadores_total


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
def posicion_valida(fila, columna, filas_posibles, columnas_posibles):

    valida = True

    # la fila debe estar entre 0 y 99
    # la columna debe estar entre 0 y 59
    if fila < 0 or fila >= filas_posibles or columna < 0 or columna >= columnas_posibles:
        valida = False

    return valida


# funcion encargada de validar si el equipo ingresado es correcto
def equipo_valido(equipo, valido):

    valida = True

    # los equipos validos son solamente "A" y "B"
    if equipo not in valido:
        valida = False

    return valida


# funcion encargada de validar si el rol ingresado es correcto
def rol_valido(rol, rol_a_validar):

    valida = True

    # los roles validos son arquero, defensor, mediocampista y delantero
    if rol not in rol_a_validar:
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
#probablemente se borre
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

#probablemente se borre
# funcion auxiliar para obtener todos los jugadores en una sola lista
def obtener_todos_los_jugadores(jugadores_argentina, jugadores_brasil):

    return jugadores_argentina + jugadores_brasil


"""
BLOQUE 5
POSICIONAMIENTO DE JUGADORES
"""

# funcion encargada de posicionar un jugador en la cancha
def posicionar_jugador(cancha,jugadores_posicionar, nombre, equipo, fila, columna, rol, tiene_pelota, validar_equipo, validar_rol, fila_hasta, columna_hasta):

    agregado = False

    # validacion: equipo valido
    if not equipo_valido(equipo, validar_equipo):
        print("Error: el equipo " + equipo + " no es valido. Use A o B.")

    # validacion: rol valido
    elif not rol_valido(rol, validar_rol):
        print("Error: el rol " + rol + " no es valido.")

    # validacion: posicion dentro de la cancha
    elif not posicion_valida(fila, columna, fila_hasta, columna_hasta):
        print("Error: la posicion (" + str(fila) + ", " + str(columna) + ") esta fuera de la cancha.")

    # validacion: celda ocupada
    elif celda_ocupada(cancha, fila, columna):
        print("Error: la celda (" + str(fila) + ", " + str(columna) + ") ya esta ocupada.")

    # validacion: solo un jugador puede tener la pelota
    elif tiene_pelota == True and obtener_jugador_con_pelota(jugadores_posicionar) != None:
        print("Error: ya hay un jugador con la pelota en la cancha.")

    else:

        # creamos el diccionario del jugador
        if len(jugadores_posicionar) == 0:
            id_jugador = 1
        else:
            id_jugador = max(jugadores_posicionar) + 1

        jugadores_posicionar[id_jugador] = crear_jugador(nombre, equipo, fila, columna, rol, tiene_pelota)
        agregado = True
        cancha [fila][columna] = equipo
    return jugadores_posicionar


"""
BLOQUE 6
OBSTACULOS
"""

# funcion encargada de agregar un obstaculo en la cancha
def agregar_obstaculo(cancha, fila, columna, fila_hasta, columna_hasta):

    agregado = False

    # validamos que la posicion este dentro de la cancha
    if not posicion_valida(fila, columna, fila_hasta, columna_hasta):
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
def mover_jugador(cancha, jugador, direccion, fila_hasta, columna_hasta):

    movimiento_exitoso = False

    # calculamos la nueva posicion segun la direccion elegida
    nueva_fila, nueva_columna = calcular_destino(jugador["fila"], jugador["columna"], direccion)

    # verificamos si la direccion ingresada existe
    if nueva_fila is None:
        print("Movimiento invalido: direccion '" + direccion + "' no reconocida.")

    # verificamos que la nueva posicion este dentro de la cancha
    elif not posicion_valida(nueva_fila, nueva_columna, fila_hasta, columna_hasta):
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

def obtener_jugador_con_pelota(jugadores):

    jugador_con_pelota = None

    for id_jugador in jugadores:

        jugador = jugadores[id_jugador]

        if jugador["tiene_pelota"] == True:

            jugador_con_pelota = jugador

    return jugador_con_pelota

# funcion encargada de calcular y mostrar la distancia Manhattan de cada jugador a la pelota

def obtener_jugador_con_pelota(jugadores):
    for id_jugador in jugadores:
        jugador = jugadores[id_jugador]

        if jugador["tiene_pelota"] == True:
            return jugador

    return None


def calcular_distancias_a_pelota(jugadores, equipo_buscado):
    jugador_con_pelota = obtener_jugador_con_pelota(jugadores)

    if jugador_con_pelota == None:
        print("Error: no hay ningun jugador con la pelota.")

    else:
        distancia_minima = None
        jugadores_mas_cercanos = []

        print("\nDistancias a la pelota del equipo", equipo_buscado + ":")

        for id_jugador in jugadores:
            jugador = jugadores[id_jugador]

            # Solo tomamos jugadores del equipo buscado
            if jugador["equipo"] == equipo_buscado:

                # Evitamos contar al mismo jugador que tiene la pelota
                # porque su distancia seria 0 y siempre ganaria
                if jugador["tiene_pelota"] == False:

                    distancia = abs(jugador["fila"] - jugador_con_pelota["fila"]) + abs(jugador["columna"] - jugador_con_pelota["columna"])

                    print(jugador["nombre"] + ": " + str(distancia))

                    if distancia_minima == None:
                        distancia_minima = distancia
                        jugadores_mas_cercanos = [jugador]

                    elif distancia < distancia_minima:
                        distancia_minima = distancia
                        jugadores_mas_cercanos = [jugador]

                    elif distancia == distancia_minima:
                        jugadores_mas_cercanos.append(jugador)

        if distancia_minima == None:
            print("No hay jugadores del equipo", equipo_buscado, "para calcular distancia.")

        else:
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

def listar_pases_posibles(cancha, jugadores):

    # buscamos al jugador que tiene la pelota
    jugador_con_pelota = obtener_jugador_con_pelota(jugadores)

    if jugador_con_pelota == None:

        print("Error: no hay ningun jugador con la pelota.")

    else:

        hay_pases = False

        print("\nPases posibles para " + jugador_con_pelota["nombre"] + ":")

        # recorremos el diccionario de jugadores
        for id_jugador in jugadores:

            jugador = jugadores[id_jugador]

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
    # declaramos las constantes de filas y columnas de la cancha
    filas = 100
    columnas = 60

    # roles y equipos validos segun la consigna
    roles_validos = ["arquero", "defensor", "mediocampista", "delantero"]
    equipos_validos = ["A", "B"]

    jugadores = {}
    # creamos la matriz de la cancha

    matriz_cancha = crear_cancha(filas, columnas)

    print("Cancha creada correctamente.")

    # posicionamos jugadores de prueba

    jugadores = posicionar_jugador(matriz_cancha, jugadores, "Otamendi", "A", 50, 10, "defensor", True, equipos_validos, roles_validos, filas, columnas)
    jugadores = posicionar_jugador(matriz_cancha, jugadores, "Messi", "A", 50, 20, "defensor", False, equipos_validos, roles_validos, filas, columnas)

    # agregamos un obstaculo para probar movimientos invalidos

    agregar_obstaculo(matriz_cancha, 49, 10, filas, columnas)

    # verificamos algunas celdas puntuales

    print("Celda Otamendi:", matriz_cancha[50][10])

    print("Celda Messi:", matriz_cancha[50][20])

    print("Celda Neymar:", matriz_cancha[50][30])

    print("Celda obstaculo:", matriz_cancha[49][10])

    # probamos movimiento hacia obstaculo

    mover_jugador(matriz_cancha, jugadores[1], "arriba", filas, columnas)

    # probamos movimiento valido

    mover_jugador(matriz_cancha, jugadores[1], "derecha", filas, columnas)

    print("Nueva posicion de Otamendi:", jugadores[1])

    # calculamos las distancias de todos los jugadores a la pelota

    calcular_distancias_a_pelota(jugadores, "A")
    calcular_distancias_a_pelota(jugadores, "B")

    # listamos los pases posibles para el jugador que tiene la pelota

    listar_pases_posibles(matriz_cancha, jugadores)

    # si quieren ver la cancha completa, descomentar esta linea

    imprimir_matriz(matriz_cancha)

# este bloque indica el punto de inicio del programa

if __name__ == "__main__":

    main()