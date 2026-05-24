"""
DESAFIO 3 - LA CANCHA INTELIGENTE
Copa de Algoritmia y Programacion UADE 2026
"""

"""
BLOQUE 1
CONSTANTES Y CREACION DE LA CANCHA
"""

FILAS = 100
COLUMNAS = 60

ROLES_VALIDOS = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]


def crear_cancha():

    cancha = []

    for fila in range(FILAS):

        fila_cancha = []

        for columna in range(COLUMNAS):

            fila_cancha.append(".")

        cancha.append(fila_cancha)

    return cancha


def imprimir_matriz(cancha_imprimir):

    for fila in cancha_imprimir:

        print(" ".join(fila))


"""
BLOQUE 2
VALIDACIONES BASICAS
"""

def posicion_valida(fila, columna):

    valida = True

    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:

        valida = False

    return valida


def valor_en_rango(valor, limite):

    valido = True

    if valor < 0 or valor >= limite:

        valido = False

    return valido


def equipo_valido(equipo):

    valido = True

    if equipo not in EQUIPOS_VALIDOS:

        valido = False

    return valido


def rol_valido(rol):

    valido = True

    if rol not in ROLES_VALIDOS:

        valido = False

    return valido


def celda_ocupada(cancha, fila, columna):

    ocupada = False

    if cancha[fila][columna] != ".":

        ocupada = True

    return ocupada


def pelota_valida(valor):

    valida = True

    if valor != "S" and valor != "N":

        valida = False

    return valida


def direccion_valida(direccion):

    valida = False

    if direccion == "arriba" or direccion == "abajo" or direccion == "izquierda" or direccion == "derecha":

        valida = True

    return valida


"""
BLOQUE 3
CREACION Y POSICIONAMIENTO DE JUGADORES
"""

def crear_jugador(nombre, equipo, fila, columna, rol, tiene_pelota):

    jugador = {
        "nombre": nombre,
        "equipo": equipo,
        "fila": fila,
        "columna": columna,
        "rol": rol,
        "tiene_pelota": tiene_pelota
    }

    return jugador


def obtener_proximo_id(jugadores):

    if len(jugadores) == 0:

        id_jugador = 1

    else:

        id_jugador = max(jugadores) + 1

    return id_jugador


def obtener_jugador_con_pelota(jugadores):

    jugador_con_pelota = None

    for id_jugador in jugadores:

        jugador = jugadores[id_jugador]

        if jugador["tiene_pelota"] == "S":

            jugador_con_pelota = jugador

    return jugador_con_pelota


def posicionar_jugador(cancha, jugadores, nombre, equipo, fila, columna, rol, tiene_pelota):

    agregado = False

    if not equipo_valido(equipo):

        print("Error: el equipo " + equipo + " no es valido. Use A o B.")

    elif not rol_valido(rol):

        print("Error: el rol " + rol + " no es valido.")

    elif not posicion_valida(fila, columna):

        print("Error: la posicion (" + str(fila) + ", " + str(columna) + ") esta fuera de la cancha.")

    elif celda_ocupada(cancha, fila, columna):

        print("Error: la celda (" + str(fila) + ", " + str(columna) + ") ya esta ocupada.")

    elif tiene_pelota == "S" and obtener_jugador_con_pelota(jugadores) != None:

        print("Error: ya hay un jugador con la pelota en la cancha.")

    else:

        id_jugador = obtener_proximo_id(jugadores)

        jugadores[id_jugador] = crear_jugador(nombre, equipo, fila, columna, rol, tiene_pelota)

        cancha[fila][columna] = equipo

        print("Jugador " + nombre + " agregado correctamente con el numero " + str(id_jugador) + ".")

        agregado = True

    return agregado


def listar_jugadores(jugadores):

    print("\n========== LISTADO DE JUGADORES ==========")

    if len(jugadores) == 0:

        print("No hay jugadores cargados.")

    else:

        print("Nro | Nombre | Equipo | Fila | Columna | Rol | Pelota")
        print("-------------------------------------------------------")

        for id_jugador in jugadores:

            jugador = jugadores[id_jugador]

            print(
                str(id_jugador) + " | " +
                jugador["nombre"] + " | " +
                jugador["equipo"] + " | " +
                str(jugador["fila"]) + " | " +
                str(jugador["columna"]) + " | " +
                jugador["rol"] + " | " +
                jugador["tiene_pelota"]
            )


"""
BLOQUE 4
OBSTACULOS
"""

def agregar_obstaculo(cancha, fila, columna):

    agregado = False

    if not posicion_valida(fila, columna):

        print("Error: la posicion del obstaculo esta fuera de la cancha.")

    elif celda_ocupada(cancha, fila, columna):

        print("Error: no se puede agregar el obstaculo porque la celda esta ocupada.")

    else:

        cancha[fila][columna] = "X"

        print("Obstaculo agregado correctamente en (" + str(fila) + ", " + str(columna) + ").")

        agregado = True

    return agregado


"""
BLOQUE 5
MOVIMIENTO DE JUGADORES - TAREA 3
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


def mover_jugador(cancha, jugador, direccion):

    movimiento_exitoso = False

    nueva_fila, nueva_columna = calcular_destino(jugador["fila"], jugador["columna"], direccion)

    if nueva_fila == None:

        print("Movimiento invalido: direccion '" + direccion + "' no reconocida.")

    elif not posicion_valida(nueva_fila, nueva_columna):

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
BLOQUE 6
DISTANCIA A LA PELOTA - TAREA 4
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

            distancia = abs(jugador["fila"] - jugador_con_pelota["fila"]) + abs(jugador["columna"] - jugador_con_pelota["columna"])

            print(jugador["nombre"] + ": " + str(distancia))

            if jugador != jugador_con_pelota:

                if distancia_minima == None:

                    distancia_minima = distancia
                    jugadores_mas_cercanos = [jugador]

                elif distancia < distancia_minima:

                    distancia_minima = distancia
                    jugadores_mas_cercanos = [jugador]

                elif distancia == distancia_minima:

                    jugadores_mas_cercanos.append(jugador)

        if distancia_minima == None:

            print("No hay otros jugadores para comparar cercania con la pelota.")

        else:

            print("\nJugador/es mas cercano/s a la pelota, sin contar al poseedor:")

            for jugador in jugadores_mas_cercanos:

                print(jugador["nombre"] + " con distancia " + str(distancia_minima))


"""
BLOQUE 7
PASES POSIBLES - TAREA 5
"""

def pase_posible(cancha, jugador_origen, jugador_destino):

    posible = True

    if jugador_origen["equipo"] != jugador_destino["equipo"]:

        posible = False

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

        if hay_pases == False:

            print("No hay pases posibles disponibles.")


"""
BLOQUE 8
CAMINO LIBRE AL ARCO - TAREA 6
"""

def esta_en_mitad_ofensiva(jugador):

    en_mitad = False

    if jugador["equipo"] == "A" and jugador["columna"] >= 30 and jugador["columna"] <= 59:

        en_mitad = True

    elif jugador["equipo"] == "B" and jugador["columna"] >= 0 and jugador["columna"] <= 29:

        en_mitad = True

    return en_mitad


def camino_libre_al_arco(cancha, jugador):

    camino_libre = True

    if jugador["rol"] != "delantero":

        camino_libre = False

    elif not esta_en_mitad_ofensiva(jugador):

        camino_libre = False

    else:

        fila = jugador["fila"]

        if jugador["equipo"] == "A":

            columna = jugador["columna"] + 1

            while columna < COLUMNAS and camino_libre == True:

                if cancha[fila][columna] == "X" or cancha[fila][columna] == "B":

                    camino_libre = False

                columna = columna + 1

        elif jugador["equipo"] == "B":

            columna = jugador["columna"] - 1

            while columna >= 0 and camino_libre == True:

                if cancha[fila][columna] == "X" or cancha[fila][columna] == "A":

                    camino_libre = False

                columna = columna - 1

    return camino_libre


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
BLOQUE 9
FUNCIONES DE INGRESO DE DATOS
"""

def pedir_entero(mensaje):

    numero_correcto = False

    while numero_correcto == False:

        try:

            numero = int(input(mensaje))

            numero_correcto = True

        except ValueError:

            print("Error: debe ingresar un numero entero.")

    return numero


def pedir_posicion_valida(mensaje, limite, nombre_posicion):

    posicion = pedir_entero(mensaje)

    while not valor_en_rango(posicion, limite):

        print("Error: la " + nombre_posicion + " (" + str(posicion) + ") esta fuera de la cancha.")

        posicion = pedir_entero(mensaje)

    return posicion


def pedir_nombre_jugador():

    nombre = input("Ingresar nombre del jugador (NO para cancelar): ").strip()

    while nombre == "":

        print("Error: el nombre no puede estar vacio.")

        nombre = input("Ingresar nombre del jugador (NO para cancelar): ").strip()

    return nombre

"""
BLOQUE 10
OPCIONES DEL SUBMENU
"""

def opcion_crear_jugador(jugadores, cancha):

    nombre = pedir_nombre_jugador()

    while nombre.upper() != "NO":

        equipo = input("Ingresar el equipo del jugador (A/B): ").strip().upper()

        while not equipo_valido(equipo):

            print("Error: el equipo " + equipo + " no es valido. Use A o B.")

            equipo = input("Ingresar el equipo del jugador (A/B): ").strip().upper()

        fila = pedir_posicion_valida("Ingresar la fila donde se ubica el jugador: ", FILAS, "fila")

        columna = pedir_posicion_valida("Ingresar la columna donde se ubica el jugador: ", COLUMNAS, "columna")

        while celda_ocupada(cancha, fila, columna):

            print("Error: la celda ya esta ocupada. Ingrese otra posicion.")

            fila = pedir_posicion_valida("Ingresar la fila donde se ubica el jugador: ", FILAS, "fila")

            columna = pedir_posicion_valida("Ingresar la columna donde se ubica el jugador: ", COLUMNAS, "columna")

        rol = input("Ingresar el rol del jugador: ").strip().lower()

        while not rol_valido(rol):

            print("Error: el rol " + rol + " no es valido.")

            rol = input("Ingresar el rol del jugador: ").strip().lower()

        if obtener_jugador_con_pelota(jugadores) != None:

            tiene_pelota = "N"

            print("El jugador no tiene pelota porque ya hay una pelota en juego.")

        else:

            tiene_pelota = input("El jugador tiene la pelota? (S/N): ").strip().upper()

            while not pelota_valida(tiene_pelota):

                print("Error: el valor no es valido. Ingrese S o N.")

                tiene_pelota = input("El jugador tiene la pelota? (S/N): ").strip().upper()

        agregado = posicionar_jugador(cancha, jugadores, nombre, equipo, fila, columna, rol, tiene_pelota)

        if agregado == True and tiene_pelota == "S":

            print("La pelota quedo asignada a " + nombre + ".")

        nombre = pedir_nombre_jugador()

    return jugadores, cancha

def opcion_borrar_jugador(cancha, jugadores):

    listar_jugadores(jugadores)

    if len(jugadores) == 0:

        print("No hay jugadores cargados para borrar.")

    else:

        jugador_seleccionado = pedir_entero("Elegir el Nro del jugador a borrar (0 para cancelar): ")

        while jugador_seleccionado != 0 and jugador_seleccionado not in jugadores:

            print("Error: no existe un jugador con ese numero.")

            jugador_seleccionado = pedir_entero("Elegir el Nro del jugador a borrar (0 para cancelar): ")

        if jugador_seleccionado == 0:

            print("Borrado cancelado.")

        else:

            jugador = jugadores[jugador_seleccionado]

            fila = jugador["fila"]
            columna = jugador["columna"]

            # limpiamos la posicion del jugador en la matriz
            cancha[fila][columna] = "."

            # guardamos datos para mostrar el mensaje antes de eliminarlo
            nombre = jugador["nombre"]
            tenia_pelota = jugador["tiene_pelota"]

            # eliminamos el jugador del diccionario
            del jugadores[jugador_seleccionado]

            print("Jugador " + nombre + " borrado correctamente.")

            if tenia_pelota == "S":

                print("Atencion: el jugador borrado tenia la pelota. Ahora no hay pelota en juego.")

    return cancha, jugadores


def opcion_crear_obstaculo(cancha):

    fila = pedir_entero("Agregar fila del obstaculo (-1 para cancelar): ")

    while fila != -1:

        while not valor_en_rango(fila, FILAS):

            print("Error: la fila (" + str(fila) + ") esta fuera de la cancha.")

            fila = pedir_entero("Agregar fila del obstaculo (-1 para cancelar): ")

            if fila == -1:

                return cancha

        columna = pedir_posicion_valida("Ingresar la columna donde se ubica el obstaculo: ", COLUMNAS, "columna")

        agregar_obstaculo(cancha, fila, columna)

        fila = pedir_entero("Agregar fila del obstaculo (-1 para cancelar): ")

    return cancha


def opcion_mover_jugador(cancha, jugadores):

    listar_jugadores(jugadores)

    if len(jugadores) == 0:

        print("Primero debe cargar un jugador.")

    else:

        jugador_seleccionado = pedir_entero("Elegir el Nro del jugador a mover (0 para cancelar): ")

        while jugador_seleccionado != 0 and jugador_seleccionado not in jugadores:

            print("Error: no existe un jugador con ese numero.")

            jugador_seleccionado = pedir_entero("Elegir el Nro del jugador a mover (0 para cancelar): ")

        if jugador_seleccionado == 0:

            print("Movimiento cancelado.")

        else:

            direccion = input("Elegir hacia donde mover el jugador (arriba/abajo/izquierda/derecha): ").strip().lower()

            while not direccion_valida(direccion):

                print("Error: direccion invalida.")

                direccion = input("Elegir hacia donde mover el jugador (arriba/abajo/izquierda/derecha): ").strip().lower()
            mover_jugador(cancha, jugadores[jugador_seleccionado], direccion)

    return cancha, jugadores


def opcion_analizar_jugada(cancha, jugadores):

    jugador_con_pelota = obtener_jugador_con_pelota(jugadores)

    if len(jugadores) < 2:

        print("Debe haber al menos dos jugadores cargados para analizar la jugada.")

    elif jugador_con_pelota == None:

        print("No hay ningun jugador con la pelota.")

    else:

        print("\n========== ANALISIS DE JUGADA ==========")

        print("Jugador con pelota: " + jugador_con_pelota["nombre"])
        print("Equipo con pelota: " + jugador_con_pelota["equipo"])

        listar_pases_posibles(cancha, jugadores)

        calcular_distancias_a_pelota(jugadores)

        detectar_caminos_libres_al_arco(cancha, jugadores)

"""
BLOQUE 11
CREAR ESCENARIO DE PRUEBA
"""

def cargar_escenario_prueba():

    cancha = crear_cancha()
    jugadores = {}

    print("\nCargando escenario de prueba...")
    print("Atencion: se reemplazara la cancha actual por un escenario automatico.")

    posicionar_jugador(cancha, jugadores, "Messi", "A", 50, 20, "delantero", "S")
    posicionar_jugador(cancha, jugadores, "Otamendi", "A", 50, 10, "defensor", "N")
    posicionar_jugador(cancha, jugadores, "Di Maria", "A", 50, 30, "mediocampista", "N")
    posicionar_jugador(cancha, jugadores, "Julian", "A", 40, 45, "delantero", "N")
    posicionar_jugador(cancha, jugadores, "Lautaro", "A", 70, 45, "delantero", "N")

    posicionar_jugador(cancha, jugadores, "Neymar", "B", 50, 15, "delantero", "N")
    posicionar_jugador(cancha, jugadores, "Vini", "B", 60, 15, "delantero", "N")

    agregar_obstaculo(cancha, 40, 50)

    print("\nEscenario de prueba cargado correctamente.")
    print("Este escenario permite probar:")
    print("- Distancias a la pelota.")
    print("- Pase bloqueado por rival entre Messi y Otamendi.")
    print("- Pase posible entre Messi y Di Maria.")
    print("- Camino al arco bloqueado para Julian por obstaculo.")
    print("- Camino libre al arco para otros delanteros segun su posicion.")

    return cancha, jugadores


"""
BLOQUE 12
MENU
"""

def borrar_pantalla():

    print("\n" * 50)


def mostrar_modo_de_uso():

    print("\n========== MODO DE USO ==========\n")

    print("1. Ingresar al simulador de cancha inteligente.")
    print("2. Agregar jugadores indicando nombre, equipo, fila, columna, rol y posesion.")
    print("3. Agregar obstaculos si se desea.")
    print("4. Mover jugadores seleccionandolos por su numero.")
    print("5. Ejecutar el analisis tactico para ver distancias, pases posibles y camino libre al arco.")
    print("6. La cancha tiene 100 filas y 60 columnas.")
    print("7. Los equipos validos son A para Argentina y B para Brasil.")
    print("8. Los roles validos son arquero, defensor, mediocampista y delantero.")
    print("9. Puede cargarse un escenario de prueba automatico desde el simulador.")
    print("10. Para cancelar la carga de jugadores, escribir NO como nombre.")
    print("11. La opcion Reiniciar cancha permite borrar jugadores y obstaculos para comenzar otra jugada.")
    print("12. Simbolos de la cancha: . = vacio, A = Argentina, B = Brasil, X = obstaculo.")
    print("13. La opcion Borrar jugador permite eliminar un jugador y liberar su posicion en la cancha.")


def submenu():

    jugadores = {}

    matriz_cancha = crear_cancha()

    submenu_seleccion = -1

    print("Cancha creada correctamente.")

    while submenu_seleccion != 0:

        print("\n========== SIMULADOR DE CANCHA ==========")
        print("1 - Agregar jugador")
        print("2 - Agregar obstaculo")
        print("3 - Mover jugador")
        print("4 - Analizar jugada")
        print("5 - Listar jugadores")
        print("6 - Mostrar cancha")
        print("7 - Cargar escenario de prueba")
        print("8 - Reiniciar cancha")
        print("9 - Borrar jugador")
        print("0 - Volver")

        try:

            submenu_seleccion = int(input("\nIngrese una opcion: "))

        except ValueError:

            borrar_pantalla()

            print("La opcion ingresada no es valida. Debe ingresar un numero de las opciones del menu.")

            continue

        if submenu_seleccion == 1:

            jugadores, matriz_cancha = opcion_crear_jugador(jugadores, matriz_cancha)

        elif submenu_seleccion == 2:

            matriz_cancha = opcion_crear_obstaculo(matriz_cancha)

        elif submenu_seleccion == 3:

            matriz_cancha, jugadores = opcion_mover_jugador(matriz_cancha, jugadores)

        elif submenu_seleccion == 4:

            opcion_analizar_jugada(matriz_cancha, jugadores)

        elif submenu_seleccion == 5:

            listar_jugadores(jugadores)

        elif submenu_seleccion == 6:

            print("\nLa cancha completa tiene 100 filas y 60 columnas.")
            print("Se mostrara la matriz completa:\n")

            imprimir_matriz(matriz_cancha)
        
        elif submenu_seleccion == 7:

            matriz_cancha, jugadores = cargar_escenario_prueba()

        elif submenu_seleccion == 8:

            matriz_cancha = crear_cancha()
            jugadores = {}

            print("Cancha reiniciada correctamente. Se eliminaron jugadores y obstaculos cargados.")
        
        elif submenu_seleccion == 9:

            matriz_cancha, jugadores = opcion_borrar_jugador(matriz_cancha, jugadores)

        elif submenu_seleccion == 0:

            print("Volviendo al menu principal...")

        else:

            print("La opcion ingresada no existe. Por favor, ingresar una opcion valida.")


def main():

    menu_seleccion = -1

    while menu_seleccion != 0:

        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Modo de uso")
        print("2 - Ejecutar cancha inteligente")
        print("3 - Acerca de")
        print("0 - Salir")

        try:

            menu_seleccion = int(input("\nIngrese una opcion: "))

        except ValueError:

            borrar_pantalla()

            print("La opcion ingresada no es valida. Debe ingresar un numero de las opciones del menu.")

            continue

        if menu_seleccion == 1:

            borrar_pantalla()

            mostrar_modo_de_uso()

        elif menu_seleccion == 2:

            borrar_pantalla()

            submenu()

            borrar_pantalla()

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
BLOQUE 13
INICIO
"""

if __name__ == "__main__":

    main()