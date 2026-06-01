import random
"""
BLOQUE
CREACION DE JUGADOR, CANCHA, OBSTACULO
"""

"""
CREA LA CANCHA
RECIBE EL ANCHO Y EL LARGO
DEVUELVE LA MATRIZ CREADA
"""
def crear_cancha(ancho, largo):
    cancha = []
    for fila in range(ancho):
        fila_cancha = []
        for columna in range(largo):
            fila_cancha.append(".")
        cancha.append(fila_cancha)
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
POSICIONA EL JUGADOR EN LA CANCHA
RECIBE: LA MATRIZ, EL DICCIONARIO, LOS DATOS DEL JUGADOR
AGREGA EL JUGADOR AL DICCIONARIO Y POSICIONA EL JUGADOR EN LA MATRIZ
DEVUELVE: EL DICCIONARIO Y LA CANCHA
"""
def posicionar_jugador(cancha,jugadores_posicionar, nombre, equipo, fila, columna, rol, tiene_pelota):
    if len(jugadores_posicionar) == 0:
        id_jugador = 1
    else:
        id_jugador = max(jugadores_posicionar) + 1

    jugadores_posicionar[id_jugador] = crear_jugador(nombre, equipo, fila, columna, rol, tiene_pelota)
    agregado = True
    cancha [fila][columna] = equipo
    return jugadores_posicionar, cancha

"""
AGREGA UN OBSTACULO
RECIBE: MATRIZ Y LA POSICION DEL OBSTACULO
DEVUELVE LA MATRIZ
"""
def agregar_obstaculo(cancha, fila, columna):
    cancha[fila][columna] = "X"
    print("Obstaculo agregado correctamente en (" + str(fila) + ", " + str(columna) + ").")
    return cancha

"""
CREA EL ARBITRO
"""
def crear_arbitro(fila, columna):
    return {
        "fila": fila,
        "columna": columna
    }

"""
COLOCA LA SOMBRA Y EL ARBITRO
"""
def colocar_arbitro_y_sombra(cancha, arbitro, filas, columnas):
    fila_arbitro = arbitro["fila"]
    columna_arbitro = arbitro["columna"]

    for fila in range(fila_arbitro - 1, fila_arbitro + 2):
        for columna in range(columna_arbitro - 1, columna_arbitro + 2):

            if posicion_valida(fila, filas) and posicion_valida(columna, columnas):

                if fila == fila_arbitro and columna == columna_arbitro:
                    cancha[fila][columna] = "X"

                elif cancha[fila][columna] == ".":
                    cancha[fila][columna] = "X"

    return cancha

"""
PONE EL ARBITRO CERCA DE LA JUGADA
"""

def mover_arbitro_cerca_jugada(cancha, jugadores, arbitro, filas, columnas):
    cancha = limpiar_arbitro_y_sombra(cancha)

    jugador_con_pelota = obtener_jugador_con_pelota(jugadores)

    if jugador_con_pelota == None:
        cancha = colocar_arbitro_y_sombra(cancha, arbitro, filas, columnas)
        return cancha

    intentos = 0
    movido = False

    while intentos < 20 and movido == False:
        nueva_fila = jugador_con_pelota["fila"] + random.randint(-2, 2)
        nueva_columna = jugador_con_pelota["columna"] + random.randint(-2, 2)

        if posicion_valida(nueva_fila, filas) and posicion_valida(nueva_columna, columnas):

            if cancha[nueva_fila][nueva_columna] == ".":
                arbitro["fila"] = nueva_fila
                arbitro["columna"] = nueva_columna
                movido = True

        intentos = intentos + 1

    cancha = colocar_arbitro_y_sombra(cancha, arbitro, filas, columnas)

    return cancha


"""
LIMPIA SOMBRA Y ARBITRO
"""
def limpiar_arbitro_y_sombra(cancha):
    for fila in range(len(cancha)):
        for columna in range(len(cancha[fila])):
            if cancha[fila][columna] == "R" or cancha[fila][columna] == "S":
                cancha[fila][columna] = "."

    return cancha
"""
IMPRIME LA CANCHA
INGRESA LA MATRIZ
NO DEVUELVE VALOR
"""
def imprimir_matriz(cancha_imprimir):
    for fila in cancha_imprimir:
        print(" ".join(fila))
        
        
"""
IMPRIME LOS JUGADORES
RECIBE: EL DICCIONARIO DE JUGADORES
"""
def listar_jugadores(jugadores_lista):
    print("\n========== LISTADO DE JUGADORES ==========")
    print("Nro | Nombre | Equipo | Fila | Columna")
    print("------------------------------------------")

    for numero in jugadores_lista:
        jugador = jugadores_lista[numero]

        print(
            str(numero) + " | " +
            jugador["nombre"] + " | " +
            jugador["equipo"] + " | " +
            str(jugador["fila"]) + " | " +
            str(jugador["columna"])
            )

"""
CARGA LOS JUGADORES
"""
def cargar_jugadores_predefinidos(cancha, jugadores):

    # EQUIPO A - Argentina
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Dibu Martinez", "A", 20, 2, "arquero", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Molina", "A", 8, 12, "defensor", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Romero", "A", 17, 10, "defensor", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Otamendi", "A", 23, 10, "defensor", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Tagliafico", "A", 32, 12, "defensor", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "De Paul", "A", 10, 22, "mediocampista", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Enzo", "A", 20, 24, "mediocampista", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Mac Allister", "A", 30, 22, "mediocampista", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Di Maria", "A", 8, 35, "delantero", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Messi", "A", 20, 32, "delantero", "S")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Julian Alvarez", "A", 31, 35, "delantero", "N")

    # EQUIPO B - Brasil
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Alisson", "B", 20, 57, "arquero", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Danilo", "B", 8, 47, "defensor", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Marquinhos", "B", 17, 49, "defensor", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Thiago Silva", "B", 23, 49, "defensor", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Lodi", "B", 32, 47, "defensor", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Casemiro", "B", 10, 38, "mediocampista", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Paqueta", "B", 20, 36, "mediocampista", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Bruno Guimaraes", "B", 30, 38, "mediocampista", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Raphinha", "B", 8, 25, "delantero", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Neymar", "B", 20, 27, "delantero", "N")
    jugadores, cancha = posicionar_jugador(cancha, jugadores, "Vinicius", "B", 31, 25, "delantero", "N")

    return jugadores, cancha
        
"""
BLOQUE
MOVER JUGADOR
"""
        
"""
CAMBIA LA POSICION DEL JUGADOR
RECIBE: POSICION DEL JUGADOR Y A DONDE SE MUEVE
DEVUELVE: LA NUEVA POSICION DEL JUGADOR
"""
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

"""
MUEVE AL JUGADOR - ACTUALIZA LA POSICION
RECIBE: MATRIZ, DICCIONARIO DE JUGADORES, HACIA DONDE SE MUEVE Y LIMITES DE LA CANCHA
DEVUELVE: SI EL MOVIMIENTO FUE EXITOSO
"""
def mover_jugador(cancha, jugador, direccion, fila_hasta, columna_hasta):

    movimiento_exitoso = False

    nueva_fila, nueva_columna = calcular_destino(jugador["fila"], jugador["columna"], direccion)

    if nueva_fila is None:
        print("Movimiento invalido: direccion '" + direccion + "' no reconocida.")

    elif not posicion_valida(nueva_fila, fila_hasta) or not posicion_valida(nueva_columna, columna_hasta):
        print("Movimiento invalido: no se puede salir de la cancha.")

    elif celda_ocupada(cancha, nueva_fila, nueva_columna):
        print("Movimiento invalido: la celda destino esta ocupada.")

    else:
        fila_anterior = jugador["fila"]
        columna_anterior = jugador["columna"]

        cancha[fila_anterior][columna_anterior] = "."

        jugador["fila"] = nueva_fila
        jugador["columna"] = nueva_columna

        cancha[nueva_fila][nueva_columna] = jugador["equipo"]

        print("Movimiento exitoso: " + jugador["nombre"] + " se movio hacia " + direccion + ".")

        movimiento_exitoso = True

    return movimiento_exitoso

"""
VALIDACIONES BASICAS
"""

"""
VALIDA POSICION
RECIBE: VALOR DE LA POSICION Y EL NUMERO MAXIMO QUE PUEDE SER
DEVUELVE: SI ES VALIDA O NO
"""
def posicion_valida(valor, numero_posible):

    valida = True

    # la fila debe estar entre 0 y 99
    # la columna debe estar entre 0 y 59
    if valor < 0 or valor >= numero_posible:
        valida = False

    return valida


"""
VALIDA EQUIPO
RECIBE: EL VALOR INGRESADO POR EL USUARIO Y EL VECTOR CON LOS EQUIPOS POSIBLES 
DEVUELVE: SI ES VALIDA O NO
"""
def equipo_valido(equipo, valido):
    valida = True
    # los equipos validos son solamente "A" y "B"
    if equipo not in valido:
        valida = False

    return valida

"""
VALIDA ROL
RECIBE: EL VALOR INGRESADO POR EL USUARIO Y EL VECTOR CON LOS ROLES POSIBLES 
DEVUELVE: SI ES VALIDA O NO
"""
def rol_valido(rol, rol_a_validar):

    valida = True

    # los roles validos son arquero, defensor, mediocampista y delantero
    if rol not in rol_a_validar:
        valida = False

    return valida

"""
VALIDA EL MENSAJE AL PREGUNTAR SI POSEE PELOTA
RECIBE: EL VALOR INGRESADO POR EL USUARIO 
DEVUELVE: SI ES VALIDA O NO
"""
def pelota_validar(mensaje):
    valida = True
    if mensaje != "S" and mensaje != "N":
        valida = False
    return valida

"""
VALIDA SI LA CELDA SE ENCUENTRA OCUPADA
RECIBE: LA MATRIZ, LA FILA Y LA COLUMNA 
DEVUELVE: SI SE ENCUENTRA OCUPADA O NO
"""
def celda_ocupada(cancha, fila, columna):

    ocupada = False

    # si la celda no contiene ".", significa que tiene un jugador o un obstaculo
    if cancha[fila][columna] != ".":
        ocupada = True

    return ocupada

"""
SOLICITA INGRESO DE POSICION
RECIBE LA FILA O COLUMNA INGRESADA POR EL USUARIO
DEVUELVE LA POSICION
"""
def pedir_posicion_valida(mensaje, limite, nombre_posicion):
    posicion = pedir_entero(mensaje)

    while not posicion_valida(posicion, limite):
        print("Error: la " + nombre_posicion + " (" + str(posicion) + ") esta fuera de la cancha.")
        posicion = pedir_entero(mensaje)

    return posicion

"""
SOLICITA INGRESO DEL NOMBRE Y VERIFICA QUE NO ESTE VACIO
RECIBE NADA
DEVUELVE EL NOMBRE UNA VEZ QUE NO ESTA VACIO
"""
def pedir_nombre_jugador():
    nombre = input("Ingresar Nombre del jugador (NO para cancelar): ").strip()

    while nombre == "":
        print("Error: el nombre no puede estar vacio.")
        nombre = input("Ingresar Nombre del jugador (NO para cancelar): ").strip()

    return nombre

"""
FUNCION PARA PEDIR UN NUMERO Y VALIDAR SI ES NUMERO
RECIBE: MENSAJE DEL USUARIO
IMPRIME ERROR 
DEVUELVE: SI ES CORRECTO DEVUELVE EL NUMERO
"""
def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debe ingresar un numero entero.")
            

"""
VALIDA LA DIRECCION INGRESADA
RECIBE: LA DIRECCION INGRESADA POR EL USUARIO
DEVUELVE: SI EL INGRESO ES UNA DIRECCION POSIBLE
"""
def direccion_valida(direccion):
    direcciones_validas = ["arriba", "abajo", "izquierda", "derecha"]

    if direccion in direcciones_validas:
        return True
    else:
        return False

"""
VERIFICA SI EL JUGADOR ESTA EN LA MITAD OFENSIVA
INGRESA: DICCIONARIO DE JUGADORES
DEVUELVE: SI ESTA O NO EN CAPACIDAD DE IR CONTRA EL ARCO
"""
def esta_en_mitad_ofensiva(jugador):
    if jugador["equipo"] == "A" and jugador["columna"] >= 30:
        return True

    elif jugador["equipo"] == "B" and jugador["columna"] <= 29:
        return True

    else:
        return False
    
"""
VERIFICA SI EL JUGADOR TIENE CAMINO AL ARCO LIBRE
INGRESA: MATRIZ Y DICCIONARIO DE JUGADORES
DEVUELVE SI TIENE O NO EL CAMINO LIBRE
"""
def camino_libre_al_arco(cancha, jugador):
    if jugador["rol"] != "delantero":
        return False

    if not esta_en_mitad_ofensiva(jugador):
        return False

    fila = jugador["fila"]
    columnas = len(cancha[0])

    # Argentina ataca hacia la derecha, arco rival en columna 59
    if jugador["equipo"] == "A":
        columna = jugador["columna"] + 1

        while columna < columnas:
            if cancha[fila][columna] == "B" or cancha[fila][columna] == "X":
                return False

            columna = columna + 1

        return True

    # Brasil ataca hacia la izquierda, arco rival en columna 0
    elif jugador["equipo"] == "B":
        columna = jugador["columna"] - 1

        while columna >= 0:
            if cancha[fila][columna] == "A" or cancha[fila][columna] == "X":
                return False

            columna = columna - 1

        return True

    return False
    
"""
BLOQUE
ESTADISTICAS
"""

"""
OBTIENE EL JUGADOR QUE POSEE LA PELOTA
RECIBE: DICCIONARIO CON JUGADORES
DEVUELVE: EL JUGADOR QUE POSEE LA PELOTA O NONE EN CASO DE QUE NO ESTE LA PELOTA
"""
def obtener_jugador_con_pelota(jugadores):
    for id_jugador in jugadores:
        jugador = jugadores[id_jugador]

        if jugador["tiene_pelota"] == "S":
            return jugador

    return None

"""
CALCULA LA DISTANCIAS DE LOS JUGADORES CON LA PELOTA
RECIBE: DICCIONARIO CON LOS JUGADORES, Y EL EQUIPO QUE TIENE LA PELOTA
DEVUELVE: NADA
"""
def calcular_distancias_a_pelota(jugadores):
    jugador_con_pelota = obtener_jugador_con_pelota(jugadores)

    if jugador_con_pelota == None:
        print("Error: no hay ningun jugador con la pelota.")

    else:
        distancia_minima = None
        jugadores_mas_cercanos = []

        print("\nDistancias a la pelota:")

        for id_jugador in jugadores:
            jugador = jugadores[id_jugador]

            if jugador != jugador_con_pelota:

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
            print("No hay otros jugadores para calcular distancia.")

        else:
            print("\nJugador/es mas cercano/s a la pelota:")

            for jugador in jugadores_mas_cercanos:
                print(jugador["nombre"] + " con distancia " + str(distancia_minima))


"""
BUSCA SI HAY PASES POSIBLES
INGRESA: MATRIZ, Y LOS DOS POSIBLES PASES
INCLUYE SI EL PASE ES INTERCEPTADO POR UN JUGADOR DEL EQUIPO CONTRARIO
O BLOQUEADO POR UN OBSTACULO
DEVUELVE: SI ES POSIBLE O NO
"""
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
        if jugador_origen["fila"] == jugador_destino["fila"]:
            fila = jugador_origen["fila"]
            if jugador_origen["columna"] < jugador_destino["columna"]:
                inicio = jugador_origen["columna"] + 1
                fin = jugador_destino["columna"]
            else:
                inicio = jugador_destino["columna"] + 1
                fin = jugador_origen["columna"]
            columna = inicio
            while columna < fin and posible == True:
                if cancha[fila][columna] == "X":
                    posible = False
                elif cancha[fila][columna] != "." and cancha[fila][columna] != jugador_origen["equipo"]:
                    posible = False
                columna = columna + 1
        elif jugador_origen["columna"] == jugador_destino["columna"]:
            columna = jugador_origen["columna"]
            if jugador_origen["fila"] < jugador_destino["fila"]:
                inicio = jugador_origen["fila"] + 1
                fin = jugador_destino["fila"]
            else:
                inicio = jugador_destino["fila"] + 1
                fin = jugador_origen["fila"]
            fila = inicio
            while fila < fin and posible == True:
                if cancha[fila][columna] == "X":
                    posible = False
                elif cancha[fila][columna] != "." and cancha[fila][columna] != jugador_origen["equipo"]:
                    posible = False
                fila = fila + 1
    return posible

"""
ANALIZA SI HAY PASES POSIBLES
INGRESA: MATRIZ, DICCIONARIO DE JUGADORES
DEVUELVE: NADA
"""
def listar_pases_posibles(cancha, jugadores):
    jugador_con_pelota = obtener_jugador_con_pelota(jugadores)
    if jugador_con_pelota == None:
        print("Error: no hay ningun jugador con la pelota.")
    else:
        hay_pases = False
        print("\nPases posibles para " + jugador_con_pelota["nombre"] + ":")
        for id_jugador in jugadores:
            jugador = jugadores[id_jugador]
            if jugador != jugador_con_pelota:
                if jugador["equipo"] == jugador_con_pelota["equipo"]:
                    if pase_posible(cancha, jugador_con_pelota, jugador):
                        print("- Pase posible a " + jugador["nombre"])
                        hay_pases = True
                    else:
                        print("- Pase bloqueado hacia " + jugador["nombre"])
        if hay_pases == False:
            print("No hay pases posibles disponibles.")
            

"""
BUSCA SI EL JUGADOR TIENE CAMINO LIBRE AL ARCO
INGRESA: MATRIZ Y DICCIONARIO DE JUGADORES
DEVUELVE: NADA
"""
def detectar_caminos_libres_al_arco(cancha, jugadores):
    hay_delanteros = False

    print("\nCamino libre al arco:")

    for id_jugador in jugadores:
        jugador = jugadores[id_jugador]

        if jugador["rol"] == "delantero":
            hay_delanteros = True

            if camino_libre_al_arco(cancha, jugador):
                print("- " + jugador["nombre"] + " tiene camino libre al arco.")
            else:
                print("- " + jugador["nombre"] + " no tiene camino libre al arco.")

    if hay_delanteros == False:
        print("No hay delanteros cargados para analizar camino libre al arco.")


"""
BLOQUE OPCIONES
"""

"""
OPCION CREAR JUGADORES
RECIBE: EL DICCIONARIO DE JUGADORES, EQUIPOS VALIDOS, LOS LIMITES DE LA CANCHA, LOS ROLES VALIDOS Y LA MATRIZ
DEVUELVE: EL DICCIONARIO DE JUGADORES Y LA MATRIZ
"""
def opcion_crear_jugador(anexo_jugadores, equipos, filas_validas, columnas_validas, roles, cancha_jugador):

    temp_nombre = pedir_nombre_jugador()

    while temp_nombre != "NO":

        temp_equipo = input("Ingresar el equipo del jugador: ").upper()

        while not equipo_valido(temp_equipo, equipos):
            print("Error: el equipo " + temp_equipo + " no es valido. Use A o B.")
            temp_equipo = input("Ingresar el equipo del jugador: ").upper()

        celda = True

        while celda == True:

            temp_fila = pedir_posicion_valida(
                "Ingresar la fila donde se ubica el jugador: ",
                filas_validas,
                "fila"
            )

            temp_columna = pedir_posicion_valida(
                "Ingresar la columna donde se ubica el jugador: ",
                columnas_validas,
                "columna"
            )

            celda = celda_ocupada(cancha_jugador, temp_fila, temp_columna)

            if celda == True:
                print("Error: la celda ya esta ocupada. Ingrese otra posicion.")

        temp_rol = input("Ingresar el rol jugador: ")

        while not rol_valido(temp_rol, roles):
            print("Error: el rol " + temp_rol + " no es valido.")
            temp_rol = input("Ingresar el rol jugador: ")

        if obtener_jugador_con_pelota(anexo_jugadores) != None:
            temp_pelota = "N"
            print("El jugador no tiene pelota porque ya hay una en juego")
        else:
            temp_pelota = input("El jugador tiene la pelota? (S/N): ").upper()

            while not pelota_validar(temp_pelota):
                print("Error: el valor no es valido.")
                temp_pelota = input("El jugador tiene la pelota? (S/N): ").upper()

        anexo_jugadores, cancha_jugador = posicionar_jugador(cancha_jugador, anexo_jugadores, temp_nombre, temp_equipo, temp_fila, temp_columna, temp_rol, temp_pelota)
        print("Jugador agregado correctamente: " + temp_nombre)
        temp_nombre = pedir_nombre_jugador()

    return anexo_jugadores, cancha_jugador

"""
OPCION OBSTACULOS
RECIBE: LOS LIMITES DE LA CANCHA Y LA MATRIZ
DEVUELVE: LA MATRIZ
"""
def opcion_crear_obstaculo(filas_validas, columnas_validas, obstaculo_cancha):

    obstaculo_fila = pedir_entero("Agregar fila del obstaculo (-1 para cancelar): ")

    while obstaculo_fila != -1:

        while not posicion_valida(obstaculo_fila, filas_validas):
            print("Error: la fila (" + str(obstaculo_fila) + ") esta fuera de la cancha.")
            obstaculo_fila = pedir_entero("Agregar fila del obstaculo (-1 para cancelar): ")

            if obstaculo_fila == -1:
                return obstaculo_cancha

        obstaculo_columna = pedir_entero("Ingresar la columna donde se ubica el obstaculo: ")

        while not posicion_valida(obstaculo_columna, columnas_validas):
            print("Error: la columna (" + str(obstaculo_columna) + ") esta fuera de la cancha.")
            obstaculo_columna = pedir_entero("Ingresar la columna donde se ubica el obstaculo: ")

        if celda_ocupada(obstaculo_cancha, obstaculo_fila, obstaculo_columna):
            print("Error: la celda ya esta ocupada.")
        else:
            obstaculo_cancha = agregar_obstaculo(obstaculo_cancha, obstaculo_fila, obstaculo_columna)

        obstaculo_fila = pedir_entero("Agregar fila del obstaculo (-1 para cancelar): ")

    return obstaculo_cancha

"""
OPCION MOVER JUGADOR
RECIBE: MATRIZ, DICCIONARIO DE JUGADORES, LIMITES DE LA CANCHA
DEVUELVE: MATRIZ Y EL DICCIONARIO DE JUGADORES
"""
def opcion_mover_jugador(cancha, jugadores, filas_validas, columnas_validas):
    listar_jugadores(jugadores)

    jugador_seleccion = pedir_entero("Elegir el Nro del jugador a mover (0 para cancelar): ")

    while jugador_seleccion != 0 and jugador_seleccion not in jugadores:
        print("Error: no existe un jugador con ese numero.")
        jugador_seleccion = pedir_entero("Elegir el Nro del jugador a mover (0 para cancelar): ")

    if jugador_seleccion == 0:
        print("Movimiento cancelado.")
        return cancha, jugadores

    movimiento_exitoso = False

    while movimiento_exitoso == False:
        direccion = input("Elegir hacia donde mover el jugador (arriba/abajo/izquierda/derecha/NO para cancelar): ").strip().lower()

        if direccion == "no":
            print("Movimiento cancelado.")
            return cancha, jugadores

        while not direccion_valida(direccion):
            print("Error: direccion invalida.")
            direccion = input("Elegir hacia donde mover el jugador (arriba/abajo/izquierda/derecha/NO para cancelar): ").strip().lower()

            if direccion == "no":
                print("Movimiento cancelado.")
                return cancha, jugadores

        movimiento_exitoso = mover_jugador(cancha, jugadores[jugador_seleccion], direccion, filas_validas, columnas_validas)

        if movimiento_exitoso == False:
            print("El movimiento no se pudo realizar. Intente con otra direccion.")

    return cancha, jugadores

"""
OPCION ESTADISTICAS
SOLO EN CASO DE SER DOS O MAS JUGADORES
INGRESA: LA MATRIZ Y EL DICCIONARIO CON JUGADORES
"""
def opcion_analizar_jugada(cancha, jugadores):

    if len(jugadores) == 0:
        print("No hay jugadores cargados para analizar.")
    else:
        jugador_con_pelota = obtener_jugador_con_pelota(jugadores)

        print("\n========== ANALISIS DE JUGADA ==========")

        if jugador_con_pelota == None:
            print("No hay ningun jugador con la pelota.")
            print("No se pueden analizar pases ni distancias a la pelota.")
        else:
            print("Jugador con pelota: " + jugador_con_pelota["nombre"])
            print("Equipo con pelota: " + jugador_con_pelota["equipo"])

            if len(jugadores) < 2:
                print("Debe haber al menos dos jugadores cargados para analizar pases y distancias.")
            else:
                listar_pases_posibles(cancha, jugadores)
                calcular_distancias_a_pelota(jugadores)

        detectar_caminos_libres_al_arco(cancha, jugadores)

"""
BLOQUE
MENU
"""

"""
FUNCION QUE SIMULA BORRAR UNA PANTALLA
"""
def borrar_pantalla():

    print("\n" * 50)

"""
SUBMENU
"""
def submenu():
    # declaramos las constantes de filas y columnas de la cancha
    filas = 40
    columnas = 60
    # roles y equipos validos segun la consigna
    roles_validos = ["arquero", "defensor", "mediocampista", "delantero"]
    equipos_validos = ["A", "B"]
    jugadores = {}
    submenu_seleccion = -1

    matriz_cancha = crear_cancha(filas, columnas)

    jugadores, matriz_cancha = cargar_jugadores_predefinidos(matriz_cancha, jugadores)

    arbitro = crear_arbitro(20, 30)
    matriz_cancha = colocar_arbitro_y_sombra(matriz_cancha, arbitro, filas, columnas)
    imprimir_matriz(matriz_cancha)
    while submenu_seleccion != 0:

        # mostramos las opciones disponibles para el usuario

        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Agregar jugador")
        print("2 - Agregar obstaculo")
        print("3 - Mover jugador")
        print("4 - Mostrar estadísticas")
        print("0 - Volver")

        try:
            submenu_seleccion = int(input("\nIngrese una opcion: "))
        
        except ValueError:
            borrar_pantalla()
            print("La opcion ingresada no es valida. Debe ingresar un numero de las opciones del menu.")
            continue
        #1 - AGREGAR JUGADOR
        if submenu_seleccion == 1:
            jugadores, matriz_cancha = opcion_crear_jugador(jugadores, equipos_validos, filas, columnas, roles_validos, matriz_cancha)
            matriz_cancha = mover_arbitro_cerca_jugada(matriz_cancha, jugadores, arbitro, filas, columnas)
            borrar_pantalla()
            imprimir_matriz(matriz_cancha)
        #2 - AGREGAR OBSTACULO
        elif submenu_seleccion == 2:
            matriz_cancha=opcion_crear_obstaculo(filas, columnas, matriz_cancha)
            borrar_pantalla()
            imprimir_matriz(matriz_cancha)
        #3 - MOVER UN JUGADOR
        elif submenu_seleccion == 3:
            if len(jugadores) == 0:
                print("Primero debe cargar un jugador.")
            else:
                matriz_cancha, jugadores = opcion_mover_jugador(matriz_cancha, jugadores, filas, columnas)
                matriz_cancha = mover_arbitro_cerca_jugada(matriz_cancha, jugadores, arbitro, filas, columnas)
                borrar_pantalla()
                imprimir_matriz(matriz_cancha)
        #4 - ESTADISTICAS
        elif submenu_seleccion == 4:
            borrar_pantalla()
            opcion_analizar_jugada(matriz_cancha, jugadores)
        else:
            borrar_pantalla()
            print("La opcion ingresada no existe. Por favor, ingresar una opcion valida.")    
"""
MENU PRINCIPAL
"""
def main():
    menu_seleccion = -1
    while menu_seleccion != 0:

        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Modo de uso")
        print("2 - Ejecutar Jugada")
        print("3 - Acerca de")
        print("0 - Salir")

        try:
            menu_seleccion = int(input("\nIngrese una opcion: "))      
        except ValueError:
            borrar_pantalla()
            print("La opcion ingresada no es valida. Debe ingresar un numero de las opciones del menu.")
            continue
        
        #1 - MODO DE USO
        if menu_seleccion == 1:
            borrar_pantalla()
            print("\n========== MODO DE USO ==========\n")

            print("1. Seleccionar la opción 2 del menú")
            print("2. Ingresar los jugadores y los obstaculos, junto con su posición")
            print("3. Los únicos equipos que pueden cargarse son: A (Argentina) y B (Brasil)")
            print("4. Los roles permitidos son: arquero, defensor, mediocampista o delantero")
            print("5. Tener en cuenta que la cancha es de 40 filas x 60 columnas")
            print("6. En el caso necesario es posible mover un jugador")
            print("4. Ejecutar la opción 4, para mostrar estadísticas")
            
        #2 - SUBMENU
        elif menu_seleccion == 2:
            borrar_pantalla()
            submenu()
            borrar_pantalla()
        #3 - ACERCA DE
        elif menu_seleccion == 3:

            borrar_pantalla()

            print("\n========== ACERCA DE ==========\n")

            print("Proyecto realizado para la Copa de Algoritmia y Programacion UADE 2026.\n")

            print("Integrantes del equipo:")
            print("- Lucas Abad")
            print("- Thiago Albornoz")
            print("- Valentino Sarniguette")
            print("- Gaston Trezeguet")
            print("- Valentin Zaccari")

            

            print("""        ___________
       '._==_==_=_.'
       .-\\:      /-.
      |   \\     /   |
       \\   \\   /   /
        '.  \\ /  .'
          '-._.-'
            | |
           _| |_
          '-----'""")
    
        elif menu_seleccion == 0:
            borrar_pantalla()
            print("Saliendo del programa...")
        else:
            borrar_pantalla()
            print("La opcion ingresada no existe. Por favor, ingresar una opcion valida.")
    

"""
BLOQUE
INICIO
"""
if __name__ == "__main__":

    main()