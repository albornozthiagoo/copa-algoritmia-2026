"""
BLOQUE 1
CREACION DE LA CANCHA
"""
# declaramos las constantes del largo y ancho de la cancha
FILAS = 100 
COLUMNAS = 60

# roles y equipos validos segun el PDF
ROLES_VALIDOS  = ["arquero", "defensor", "mediocampista", "delantero"]
EQUIPOS_VALIDOS = ["A", "B"]

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
        # join une todos los elementos de la fila en un solo texto,
        # separando cada posicion con un espacio
        # de esta forma imprimimos una fila completa por cada print
        print(" ".join(str(posicion) for posicion in fila))
"""
BLOQUE 3
VALIDACIONES BASICAS
"""

# funcion encargada de validar si una posicion esta dentro de los limites de la cancha
def posicion_valida(fila, columna):

    valida = True

    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        valida = False

    return valida


# funcion encargada de validar si el equipo ingresado es correcto
def equipo_valido(equipo):

    valida = True

    if equipo != "A" and equipo != "B":
        valida = False

    return valida


# funcion encargada de validar si el rol ingresado es correcto
def rol_valido(rol):

    valida = True

    if rol != "arquero" and rol != "defensor" and rol != "mediocampista" and rol != "delantero":
        valida = False

    return valida


# funcion encargada de verificar si una celda de la cancha esta ocupada
def celda_ocupada(cancha, fila, columna):

    ocupada = False

    if cancha[fila][columna] != ".":
        ocupada = True

    return ocupada

#   ARRANCO TAREA 3 funcion encargada de calcular la nueva posicion segun la direccion
def calcular_destino(fila, columna, direccion):

    if direccion == "arriba":
        return fila - 1, columna
    if direccion == "abajo":
        return fila + 1, columna
    if direccion == "izquierda":
        return fila, columna - 1
    if direccion == "derecha":
        return fila, columna + 1

    return None, None

"""
BLOQUE 4
CREACION Y GESTION DE JUGADORES
"""

# funcion encargada de verificar si alguien ya tiene la pelota
def hay_pelota_en_juego(jugadores_argentina,jugadores_brasil):

    # recorremos argentina
    for jugador in jugadores_argentina:
        if jugador["tiene_pelota"] == True:
            return True


    # recorremos brasil
    for jugador in jugadores_brasil:
        if jugador["tiene_pelota"] == True:
            return True
        
    return False

"""
BLOQUE 5
POSICIONAMIENTO DE JUGADORES
"""

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

"""
BLOQUE 

PROGRAMA PRINCIPAL
"""

def main():

    # creamos la matriz de la cancha

    matriz_cancha = crear_cancha()

    # creamos listas vacias para los jugadores de cada equipo

    jugadores_argentina = []
    jugadores_brasil = []

    # mostramos un mensaje para confirmar que la cancha fue creada

    print("Cancha creada correctamente.")

    # posicionamos un jugador y verificamos que quede en la matriz y en la lista

    posicionar_jugador(matriz_cancha, jugadores_argentina, jugadores_brasil,
                       "Otamendi", "A", 50, 10, "defensor", False)

    imprimir_matriz(matriz_cancha)

    # verificamos que la celda se actualizo en la matriz
    print("Celda (50, 10) en la matriz: " + matriz_cancha[50][10])

    # verificamos que el jugador quedo guardado en la lista
    print("Jugadores de Argentina: " + str(jugadores_argentina))


# este bloque indica el punto de inicio del programa

# si este archivo se ejecuta directamente, se llama a main()

if __name__ == "__main__":

    main()