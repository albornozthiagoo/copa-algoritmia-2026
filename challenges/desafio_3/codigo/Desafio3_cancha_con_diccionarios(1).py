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
def posicion_valida(valor, numero_posible):

    valida = True

    # la fila debe estar entre 0 y 99
    # la columna debe estar entre 0 y 59
    if valor < 0 or valor >= numero_posible:
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

def pelota_validar(mensaje):
    valida = True
    if mensaje != "S" and mensaje != "N":
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

"""
BLOQUE 5
POSICIONAMIENTO DE JUGADORES
"""

# funcion encargada de posicionar un jugador en la cancha
def posicionar_jugador(cancha,jugadores_posicionar, nombre, equipo, fila, columna, rol, tiene_pelota):
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
def agregar_obstaculo(cancha, fila, columna):
    cancha[fila][columna] = "X"
    print("Obstaculo agregado correctamente en (" + str(fila) + ", " + str(columna) + ").")


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
    
    
    temp_nombre = ""
    # declaramos las constantes de filas y columnas de la cancha
    filas = 100
    columnas = 60
    # roles y equipos validos segun la consigna
    roles_validos = ["arquero", "defensor", "mediocampista", "delantero"]
    equipos_validos = ["A", "B"]
    valor_valido = False
    jugadores = {}
    # creamos la matriz de la cancha

    matriz_cancha = crear_cancha(filas, columnas)

    print("Cancha creada correctamente.")
    temp_nombre = input("Ingresar Nombre del jugador (NO para cancelar): ")
    while temp_nombre != "NO":
        # posicionamos jugadores de prueba
        temp_equipo = input("Ingresar el equipo del jugador: " )
        while not equipo_valido(temp_equipo, equipos_validos):
            print("Error: el equipo " + temp_equipo + " no es valido. Use A o B.")
            temp_equipo = input("Ingresar el equipo del jugador: " )
        while valor_valido == False:
            try:
                temp_fila= int(input("Ingresar la fila donde se ubica el jugador: "))
                while not posicion_valida(temp_fila, filas):
                    print("Error: la fila (" + str(temp_fila) + ") esta fuera de la cancha.")
                    temp_fila= int(input("Ingresar la fila donde se ubica el jugador: "))
                valor_valido = True
            except ValueError:
                print("La opcion ingresada no es valida. Debe ingresar un numero.")
        valor_valido = False
        while valor_valido == False:
            try:
                temp_columna= int(input("Ingresar la columna donde se ubica el jugador: "))
                while not posicion_valida(temp_columna, columnas):
                    print("Error: la columna (", str(temp_columna), ") esta fuera de la cancha.")
                    temp_columna= int(input("Ingresar la columna donde se ubica el jugador: "))
                valor_valido = True
            except ValueError:
                print("La opcion ingresada no es valida. Debe ingresar un numero.")
        temp_rol = input("Ingresar el rol jugador: " )
        while not rol_valido(temp_rol, roles_validos):
            print("Error: el rol " + temp_rol + " no es valido.")
            temp_rol = input("Ingresar el rol jugador: " )
    
        if obtener_jugador_con_pelota(jugadores) != None:
            temp_pelota = "N"
        else:
            temp_pelota = input("El jugador tiene la pelota? (S/N): " )
            while not pelota_validar(temp_pelota):
                print("Error: el valor no es valido.")
                temp_pelota = input("El jugador tiene la pelota? (S/N): " )
        jugadores = posicionar_jugador(matriz_cancha, jugadores, temp_nombre, temp_equipo, temp_fila, temp_columna, temp_rol, temp_pelota)
        temp_nombre = input("Ingresar Nombre del jugador (NO para cancelar): ")
    # agregamos un obstaculo para probar movimientos invalidos
        
    obstaculo_fila = int(input("Agregar fila del obstaculo (-1 para cancelar): "))
    while obstaculo_fila != -1:
        while not posicion_valida(obstaculo_fila, filas):
            print("Error: la fila (" + str(obstaculo_fila) + ") esta fuera de la cancha.")
            obstaculo_fila = int(input("Agregar fila del obstaculo (-1 para cancelar): "))
        obstaculo_columna= int(input("Ingresar la columna donde se ubica el obstaculo: "))
        while not posicion_valida(obstaculo_columna, columnas):
            print("Error: la columna (", str(obstaculo_columna), ") esta fuera de la cancha.")
            obstaculo_columna= int(input("Ingresar la columna donde se ubica el jugador: "))
        agregar_obstaculo(matriz_cancha, obstaculo_fila, obstaculo_columna)
        obstaculo_fila = int(input("Agregar fila del obstaculo (-1 para cancelar): "))
            
    # probamos movimiento hacia obstaculo
    
    #mover_jugador(matriz_cancha, jugadores[1], "arriba", filas, columnas)

    # probamos movimiento valido

    #mover_jugador(matriz_cancha, jugadores[1], "derecha", filas, columnas)

    #print("Nueva posicion de Otamendi:", jugadores[1])

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