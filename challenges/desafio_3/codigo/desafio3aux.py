"""
BLOQUE 1
CREACION DE LA CANCHA
"""
# declaramos las constantes del largo y ancho de la cancha
FILAS = 100 
COLUMNAS = 60

# columna donde se encuentra cada arco
# Esto despues lo vamos a usar para la tarea 6 para detectar el camino libre al ARCO 
ARCO_ARGENTINA = 0
ARCO_BRASIL    = 59

# funcion encargada de crear una cancha vacia
def crear_cancha():

    # creamos una lista vacia donde vamos a guardar toda la cancha
    cancha = []

    # recorremos el largo de la cancha
    for largo in range(FILAS):

        # creamos una nueva franja de la cancha vacia
        franja_cesped = []

        # recorremos el ancho de la cancha
        for ancho in range(COLUMNAS):

            # agregamos una posicion vacia simulada con un "."
            franja_cesped.append(".")

        # cuando la franja esta completa la agregamos a la cancha
        cancha.append(franja_cesped)

    # devolvemos la cancha ya creada
    return cancha

"""
BLOQUE 2
IMPRIMIR LA CANCHA
"""
def imprimir_matriz(cancha_imprimir):
    for fila in cancha_imprimir:
        print(" ".join(str(posicion) for posicion in fila))
"""
BLOQUE 3
LISTAS DE JUGADORES
"""

# lista que guarda todos los jugadores de argentina
jugadores_argentina = []

# lista que guarda todos los jugadores de brasil
jugadores_brasil = []

"""
BLOQUE 4
POSICIONAR JUGADORES - TAREA 2
"""

# roles y equipos validos segun el PDF
ROLES_VALIDOS  = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]

def hay_pelota_en_juego(jugadores_argentina, jugadores_brasil):
    # recorre argentina buscando si alguien ya tiene la pelota
    for jugador in jugadores_argentina:
        if jugador["tiene_pelota"] == True:
            return True
    # recorre brasil buscando si alguien ya tiene la pelota
    for jugador in jugadores_brasil:
        if jugador["tiene_pelota"] == True:
            return True
    return False

def posicionar_jugador(cancha, jugadores_argentina, jugadores_brasil, nombre, equipo, fila, columna, rol, tiene_pelota):

    # validacion: equipo valido
    if equipo not in EQUIPOS_VALIDOS:
        print("Error: el equipo " + equipo + " no es valido. Use A o B.")
        return

    # validacion: rol valido
    if rol not in ROLES_VALIDOS:
        print("Error: el rol " + rol + " no es valido.")
        return

    # validacion: posicion dentro de la cancha
    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        print("Error: la posicion (" + str(fila) + ", " + str(columna) + ") esta fuera de la cancha.")
        return

    # validacion: celda ocupada
    if cancha[fila][columna] != ".":
        print("Error: la celda (" + str(fila) + ", " + str(columna) + ") ya esta ocupada.")
        return

    # validacion: solo un jugador puede tener la pelota
    if tiene_pelota == True and hay_pelota_en_juego(jugadores_argentina, jugadores_brasil):
        print("Error: ya hay un jugador con la pelota en la cancha.")
        return

    # creamos el diccionario del jugador
    jugador = {
        "nombre":      nombre,
        "equipo":      equipo,
        "fila":        fila,
        "columna":     columna,
        "rol":         rol,
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


# ---- PRUEBA ----
matriz_cancha = crear_cancha()
imprimir_matriz(matriz_cancha)

posicionar_jugador(matriz_cancha, jugadores_argentina, jugadores_brasil,
                   "Sebita", "A", 50, 10, "defensor", False)

# verificamos que la celda se actualizo en la matriz
print("Celda (50, 10) en la matriz: " + matriz_cancha[50][10])

# verificamos que el jugador quedo guardado en la lista
print("Jugadores de Argentina: " + str(jugadores_argentina))