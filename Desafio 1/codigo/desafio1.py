def crear_equipo():
    # Inicializa las estadísticas de un equipo
    return {
        "pts": 0,
        "gf": 0,
        "gc": 0
    }


def leer_partidos():
    partidos = []

    # Abre el archivo input.txt en modo lectura ("r" = read)
    with open("desafio 1/codigo/input.txt", "r") as archivo:

        # Lee la primera línea del archivo
        # int() convierte el texto a número
        n = int(archivo.readline())

        for _ in range(n):

            # Lee una línea del archivo y separa los datos por espacios
            # Ejemplo:
            # "ARG BRA 2 1"
            # pasa a:
            # ["ARG", "BRA", "2", "1"]
            datos = archivo.readline().split()

            local = datos[0]
            visitante = datos[1]

            # Convierte goles a enteros
            gl = int(datos[2])
            gv = int(datos[3])

            # Guarda el partido en la lista
            partidos.append((local, visitante, gl, gv))

    return partidos


def procesar_partidos(partidos):
    tabla = {}  # diccionario donde guardamos estadísticas de cada equipo

    for local, visitante, gl, gv in partidos:

        # Si el equipo no existe, lo creamos
        if local not in tabla:
            tabla[local] = crear_equipo()

        if visitante not in tabla:
            tabla[visitante] = crear_equipo()

        # Actualizamos goles a favor y en contra
        tabla[local]["gf"] = tabla[local]["gf"] + gl
        tabla[local]["gc"] = tabla[local]["gc"] + gv

        tabla[visitante]["gf"] = tabla[visitante]["gf"] + gv
        tabla[visitante]["gc"] = tabla[visitante]["gc"] + gl

        # Asignamos puntos según el resultado
        if gl > gv:
            tabla[local]["pts"] = tabla[local]["pts"] + 3

        elif gl < gv:
            tabla[visitante]["pts"] = tabla[visitante]["pts"] + 3

        else:
            tabla[local]["pts"] = tabla[local]["pts"] + 1
            tabla[visitante]["pts"] = tabla[visitante]["pts"] + 1

    return tabla


def ordenar_tabla(tabla):

    # Función usada para definir el criterio de ordenamiento
    def clave_orden(item):

        # item tiene:
        # ("ARG", {"pts": 6, "gf": 4, "gc": 2})

        equipo, estadisticas = item

        puntos = estadisticas["pts"]
        diferencia = estadisticas["gf"] - estadisticas["gc"]
        goles_favor = estadisticas["gf"]

        # sorted ordena de menor a mayor
        # por eso usamos negativos para ordenar de mayor a menor
        return (-puntos, -diferencia, -goles_favor, equipo)

    return sorted(tabla.items(), key=clave_orden)


def main():

    partidos = leer_partidos()

    tabla = procesar_partidos(partidos)

    ordenados = ordenar_tabla(tabla)

    # Salida según formato pedido en la consigna
    print("Clasificados:")
    print(ordenados[0][0])
    print(ordenados[1][0])

    print("Tercero:")
    print(ordenados[2][0])


if __name__ == "__main__":
    main()