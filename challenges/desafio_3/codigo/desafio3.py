"""
BLOQUE 1
CREACION DE LA CANCHA
"""
# declaramos las constantes del largo y ancho de la cancha
FILAS = 100 
COLUMNAS = 60

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
PROGRAMA PRINCIPAL DE PRUEBA
"""

def main():

    # creamos la matriz de la cancha
    matriz_cancha = crear_cancha()

    # mostramos un mensaje para confirmar que la cancha fue creada
    print("Cancha creada correctamente.")

    # imprimimos la cancha para verificar que todas las posiciones esten vacias
    imprimir_matriz(matriz_cancha)


if __name__ == "__main__":
    main()