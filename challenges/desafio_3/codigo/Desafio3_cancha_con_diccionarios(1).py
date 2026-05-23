"""
BLOQUE 1
CREACION DE LA CANCHA
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
IMPRIME LA CANCHA
INGRESA LA MATRIZ
NO DEVUELVE VALOR
"""
def imprimir_matriz(cancha_imprimir):
    for fila in cancha_imprimir:
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
def opcion_crear_jugador(anexo_jugadores, equipos, filas_validas, columnas_validas, roles, cancha_jugador):
    valor_valido = False
    celda = True
    temp_nombre = input("Ingresar Nombre del jugador (NO para cancelar): ")
    while temp_nombre != "NO":
        # posicionamos jugadores de prueba
        temp_equipo = input("Ingresar el equipo del jugador: " )
        while not equipo_valido(temp_equipo, equipos):
            print("Error: el equipo " + temp_equipo + " no es valido. Use A o B.")
            temp_equipo = input("Ingresar el equipo del jugador: " )
        while celda == True:
            while valor_valido == False:
                try:
                    temp_fila= int(input("Ingresar la fila donde se ubica el jugador: "))
                    while not posicion_valida(temp_fila, filas_validas):
                        print("Error: la fila (" + str(temp_fila) + ") esta fuera de la cancha.")
                        temp_fila= int(input("Ingresar la fila donde se ubica el jugador: "))
                    valor_valido = True
                except ValueError:
                    print("La opcion ingresada no es valida. Debe ingresar un numero.")
            valor_valido = False
            while valor_valido == False:
                try:
                    temp_columna= int(input("Ingresar la columna donde se ubica el jugador: "))
                    while not posicion_valida(temp_columna, columnas_validas):
                        print("Error: la columna (", str(temp_columna), ") esta fuera de la cancha.")
                        temp_columna= int(input("Ingresar la columna donde se ubica el jugador: "))
                    valor_valido = True
                except ValueError:
                    print("La opcion ingresada no es valida. Debe ingresar un numero.")
            valor_valido = False
            celda = celda_ocupada(cancha_jugador, temp_fila, temp_columna)
        temp_rol = input("Ingresar el rol jugador: " )
        while not rol_valido(temp_rol, roles):
            print("Error: el rol " + temp_rol + " no es valido.")
            temp_rol = input("Ingresar el rol jugador: " )
            
        if obtener_jugador_con_pelota(anexo_jugadores) != None:
            temp_pelota = "N"
            print("El jugador no tiene pelota porque ya hay una en juego")
        else:
            temp_pelota = input("El jugador tiene la pelota? (S/N): " )
            while not pelota_validar(temp_pelota):
                print("Error: el valor no es valido.")
                temp_pelota = input("El jugador tiene la pelota? (S/N): " )
        anexo_jugadores, cancha_jugador = posicionar_jugador(cancha_jugador, anexo_jugadores, temp_nombre, temp_equipo, temp_fila, temp_columna, temp_rol, temp_pelota)
        celda = True
        temp_nombre = input("Ingresar Nombre del jugador (NO para cancelar): ")
    return anexo_jugadores,cancha_jugador

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
    return jugadores_posicionar, cancha


"""
BLOQUE 6
OBSTACULOS
"""
def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debe ingresar un numero entero.")

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
    
# funcion encargada de agregar un obstaculo en la cancha
def agregar_obstaculo(cancha, fila, columna):
    cancha[fila][columna] = "X"
    print("Obstaculo agregado correctamente en (" + str(fila) + ", " + str(columna) + ").")
    return cancha

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

def obtener_jugador_con_pelota(pelota_jugadores):

    jugador_con_pelota = None

    for id_jugador in pelota_jugadores:

        jugador = pelota_jugadores[id_jugador]

        if jugador["tiene_pelota"] == "S":

            jugador_con_pelota = jugador

    return jugador_con_pelota


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
def borrar_pantalla():

    print("\n" * 50)
    
def submenu():
    # declaramos las constantes de filas y columnas de la cancha
    filas = 100
    columnas = 60
    # roles y equipos validos segun la consigna
    roles_validos = ["arquero", "defensor", "mediocampista", "delantero"]
    equipos_validos = ["A", "B"]
    jugadores = {}
    submenu_seleccion = -1
    # creamos la matriz de la cancha
    matriz_cancha = crear_cancha(filas, columnas)
    imprimir_matriz(matriz_cancha)
    while submenu_seleccion != 0:

        # mostramos las opciones disponibles para el usuario

        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Agregar jugador")
        print("2 - Agregar obstaculo")
        print("3 - Mover jugador")
        print("0 - Volver")

        # pedimos al usuario que ingrese una opcion del menu
        # usamos try/except porque int() puede fallar si el usuario escribe una letra,
        # deja el campo vacio o ingresa cualquier dato que no pueda convertirse a numero

        try:
            submenu_seleccion = int(input("\nIngrese una opcion: "))
        
        except ValueError:

            # si el usuario no ingresa un numero valido, limpiamos la pantalla
            # mostramos un mensaje de error y usamos continue para volver al inicio del while
            # de esta forma evitamos que el programa se rompa o que siga evaluando opciones invalidas

            borrar_pantalla()
            print("La opcion ingresada no es valida. Debe ingresar un numero de las opciones del menu.")
            continue
        
        # si el usuario ingresa 1, mostramos las instrucciones de uso del programa

        if submenu_seleccion == 1:
            jugadores, matriz_cancha = opcion_crear_jugador(jugadores, equipos_validos, filas, columnas, roles_validos, matriz_cancha)
            borrar_pantalla()
            imprimir_matriz(matriz_cancha)
        elif submenu_seleccion == 2:
            matriz_cancha=opcion_crear_obstaculo(filas, columnas, matriz_cancha)
            borrar_pantalla()
            imprimir_matriz(matriz_cancha)

def main():
    # inicializamos menu_seleccion en -1 para poder entrar al while
    # usamos -1 porque es distinto de 0, entonces el menu se ejecuta al menos una vez

    menu_seleccion = -1

    # mientras el usuario no ingrese 0, el menu seguira ejecutandose
    # la opcion 0 se usa para salir del programa

    while menu_seleccion != 0:

        # mostramos las opciones disponibles para el usuario

        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Modo de uso")
        print("2 - Ejecutar prediccion")
        print("3 - Acerca de")
        print("0 - Salir")

        # pedimos al usuario que ingrese una opcion del menu
        # usamos try/except porque int() puede fallar si el usuario escribe una letra,
        # deja el campo vacio o ingresa cualquier dato que no pueda convertirse a numero

        try:
            menu_seleccion = int(input("\nIngrese una opcion: "))
        
        except ValueError:

            # si el usuario no ingresa un numero valido, limpiamos la pantalla
            # mostramos un mensaje de error y usamos continue para volver al inicio del while
            # de esta forma evitamos que el programa se rompa o que siga evaluando opciones invalidas

            borrar_pantalla()
            print("La opcion ingresada no es valida. Debe ingresar un numero de las opciones del menu.")
            continue
        
        # si el usuario ingresa 1, mostramos las instrucciones de uso del programa

        if menu_seleccion == 1:

            borrar_pantalla()

            print("\n========== MODO DE USO ==========\n")

            # explicamos como debe llamarse el archivo, donde debe ubicarse
            # y que caracteres se pueden utilizar en la secuencia

            print("1. Crear un archivo llamado penales.txt")
            print("2. Colocar el archivo en la misma carpeta del programa")
            print("3. Ingresar una secuencia utilizando:")
            print("   L = izquierda")
            print("   R = derecha")
            print("   C = centro")
            print("4. Ejecutar la opcion 2 del menu")

            print("\nEjemplo de archivo:\n")

            print("LRRCLRRLLR")

        # si el usuario ingresa 2, ejecutamos la prediccion de penales

        elif menu_seleccion == 2:

            borrar_pantalla()

            print("\n========== RESULTADO ==========\n")

            # llamamos a ejecutar_prediccion(), que se encarga de leer el archivo,
            # validar la secuencia, contar direcciones,
            # calcular la direccion dominante e imprimir el resultado

            submenu()
            borrar_pantalla()

        # si el usuario ingresa 3, mostramos informacion general del proyecto

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
    
        # si el usuario ingresa 0, se corta el ciclo porque menu_seleccion deja de ser distinto de 0

        elif menu_seleccion == 0:

            borrar_pantalla()

            print("Saliendo del programa...")

        # si el usuario ingresa un numero que no corresponde a ninguna opcion,
        # mostramos un mensaje de error y el while vuelve a mostrar el menu

        else:

            borrar_pantalla()

            print("La opcion ingresada no existe. Por favor, ingresar una opcion valida.")
    
    
    

            
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
