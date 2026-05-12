import sys


PARTIDOS_ESPERADOS = 6
EQUIPOS_ESPERADOS = 4
PARTIDOS_POR_EQUIPO = 3
GOLES_MINIMOS = 0
GOLES_MAXIMOS = 20


def crear_estadisticas():
    """Devuelve las estadisticas iniciales de un equipo."""
    return {
        "PJ": 0,
        "PTS": 0,
        "GF": 0,
        "GC": 0,
        "DG": 0,
    }


def agregar_equipo_si_no_existe(tabla, equipo):
    if equipo not in tabla:
        tabla[equipo] = crear_estadisticas()


def validar_goles(goles_texto):
    try:
        goles = int(goles_texto)
    except ValueError:
        raise ValueError("Los goles deben ser numeros enteros.")

    if goles < GOLES_MINIMOS or goles > GOLES_MAXIMOS:
        raise ValueError("Los goles deben estar entre 0 y 20.")

    return goles


def leer_partidos(lineas):
    if not lineas:
        raise ValueError("No se recibieron datos de entrada.")

    try:
        cantidad_partidos = int(lineas[0])
    except ValueError:
        raise ValueError("La primera linea debe ser la cantidad de partidos.")

    if cantidad_partidos != PARTIDOS_ESPERADOS:
        raise ValueError("Deben recibirse exactamente 6 partidos.")

    if len(lineas) - 1 != cantidad_partidos:
        raise ValueError("La cantidad de lineas de partidos no coincide.")

    partidos = []
    cruces_vistos = []

    for numero_linea, linea in enumerate(lineas[1:], start=2):
        partes = linea.split()

        if len(partes) != 4:
            raise ValueError(f"La linea {numero_linea} debe tener 4 datos.")

        local = partes[0]
        visitante = partes[1]
        goles_local = validar_goles(partes[2])
        goles_visitante = validar_goles(partes[3])

        if local == visitante:
            raise ValueError("Un equipo no puede jugar contra si mismo.")

        cruce = sorted([local, visitante])
        if cruce in cruces_vistos:
            raise ValueError("No puede repetirse un partido entre los mismos equipos.")
        cruces_vistos.append(cruce)

        partidos.append([local, visitante, goles_local, goles_visitante])

    return partidos


def actualizar_tabla_con_partido(tabla, local, visitante, goles_local, goles_visitante):
    agregar_equipo_si_no_existe(tabla, local)
    agregar_equipo_si_no_existe(tabla, visitante)

    tabla[local]["PJ"] += 1
    tabla[visitante]["PJ"] += 1

    tabla[local]["GF"] += goles_local
    tabla[local]["GC"] += goles_visitante

    tabla[visitante]["GF"] += goles_visitante
    tabla[visitante]["GC"] += goles_local

    if goles_local > goles_visitante:
        tabla[local]["PTS"] += 3
    elif goles_local < goles_visitante:
        tabla[visitante]["PTS"] += 3
    else:
        tabla[local]["PTS"] += 1
        tabla[visitante]["PTS"] += 1


def validar_tabla_final(tabla):
    if len(tabla) != EQUIPOS_ESPERADOS:
        raise ValueError("Deben participar exactamente 4 equipos.")

    for equipo, estadisticas in tabla.items():
        if estadisticas["PJ"] != PARTIDOS_POR_EQUIPO:
            raise ValueError(f"{equipo} debe jugar exactamente 3 partidos.")


def construir_tabla(partidos):
    tabla = {}

    for partido in partidos:
        local, visitante, goles_local, goles_visitante = partido
        actualizar_tabla_con_partido(
            tabla,
            local,
            visitante,
            goles_local,
            goles_visitante,
        )

    validar_tabla_final(tabla)

    for estadisticas in tabla.values():
        estadisticas["DG"] = estadisticas["GF"] - estadisticas["GC"]

    return tabla


def ordenar_tabla(tabla):
    return sorted(
        tabla.items(),
        key=criterio_ordenamiento,
    )


def criterio_ordenamiento(equipo_y_estadisticas):
    equipo = equipo_y_estadisticas[0]
    estadisticas = equipo_y_estadisticas[1]

    return (
        -estadisticas["PTS"],
        -estadisticas["DG"],
        -estadisticas["GF"],
        equipo,
    )


def obtener_clasificacion(tabla_ordenada):
    primer_clasificado = tabla_ordenada[0][0]
    segundo_clasificado = tabla_ordenada[1][0]
    tercer_puesto = tabla_ordenada[2][0]
    return primer_clasificado, segundo_clasificado, tercer_puesto


def resolver(entrada):
    lineas = []
    for linea in entrada.splitlines():
        if linea.strip() != "":
            lineas.append(linea.strip())

    partidos = leer_partidos(lineas)
    tabla = construir_tabla(partidos)
    tabla_ordenada = ordenar_tabla(tabla)
    primero, segundo, tercero = obtener_clasificacion(tabla_ordenada)

    return f"Clasificados:\n{primero}\n{segundo}\nTercero:\n{tercero}"


def main():
    entrada = sys.stdin.read()

    try:
        salida = resolver(entrada)
    except ValueError as error:
        salida = f"Error: {error}"

    print(salida)


if __name__ == "__main__":
    main()
