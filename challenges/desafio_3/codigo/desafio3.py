"""
BLOQUE 1
CREACION DE LA CANCHA
"""
# declaramos las constantes del largo y ancho de la cancha
LARGO = 100 
ANCHO = 60

# funcion encargada de crear una cancha vacia
def crear_cancha():

    # creamos una lista vacia donde vamos a guardar toda la cancha
    cancha = []

    # recorremos el largo de la cancha
    for largo in range(LARGO):

        # creamos una nueva franja de la cancha vacia
        franja_cesped = []

        # recorremos el ancho de la cancha
        for ancho in range(ANCHO):

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
CREAR JUGADORES
"""

# funcion encargada de crear un jugador usando diccionario
def crear_jugador(nombre,equipo,rol,fila,columna,tiene_pelota):

    jugador={

        "nombre":nombre,
        "equipo":equipo,
        "rol":rol,
        "fila":fila,
        "columna":columna,
        "pelota":tiene_pelota
    }

    # devolvemos el jugador creado
    return jugador

"""

"""
matriz_cancha = crear_cancha()
imprimir_matriz(matriz_cancha)
