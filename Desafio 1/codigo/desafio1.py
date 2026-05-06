def crear_equipo():
    # Inicializa las estadísticas de un equipo
    return {
        "pts": 0,
        "gf": 0,
        "gc": 0
    }


def leer_partidos():
    n = int(input())  # cantidad de partidos (debería ser 6)
    partidos = []

    for _ in range(n):
        datos = input().split()  # separa la línea en partes

        local = datos[0]
        visitante = datos[1]
        gl = int(datos[2])  # goles del local
        gv = int(datos[3])  # goles del visitante

        partidos.append((local, visitante, gl, gv))  # agrega el partido a la lista

    return partidos


def procesar_partidos(partidos):
    tabla = {}  # diccionario donde guardamos estadísticas de cada equipo

    for local, visitante, gl, gv in partidos:

        # Si el equipo no existe, lo creamos
        if local not in tabla:
            tabla[local] = crear_equipo()
        if visitante not in tabla:
            tabla[visitante] = crear_equipo()

        # Actualizamos goles
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
    return sorted(
        tabla.items(),  # convierte el diccionario en lista de (equipo, estadísticas)

        # lambda define cómo ordenar los equipos
        key=lambda x: (
            -x[1]["pts"],  # 1. mayor cantidad de puntos
            
            -(x[1]["gf"] - x[1]["gc"]),  # 2. diferencia de gol
            
            -x[1]["gf"],  # 3. goles a favor
            
            x[0]  # 4. nombre del equipo (orden alfabético)
        )
    )


def main():
    partidos = leer_partidos()
    tabla = procesar_partidos(partidos)
    ordenados = ordenar_tabla(tabla)

    # Salida según lo que pide la consigna
    print("Clasificados:")
    print(ordenados[0][0])
    print(ordenados[1][0])
    print("Tercero:")
    print(ordenados[2][0])


if __name__ == "__main__":
    main()
