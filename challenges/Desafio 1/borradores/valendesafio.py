# Sistema de Clasificacion FIFA - Copa UADE 2026
# Desafio 1

# Cada equipo se representa con una lista:
# [nombre, puntos, goles_a_favor, goles_en_contra, diferencia_de_gol]
# Indices:
NOMBRE = 0
PUNTOS = 1
GF     = 2
GC     = 3
DG     = 4

def crear_equipo(nombre):
    return [nombre, 0, 0, 0, 0]

def buscar_equipo(equipos, nombre):
    for i in range(len(equipos)):
        if equipos[i][NOMBRE] == nombre:
            return i
    return -1

def agregar_si_no_existe(equipos, nombre):
    if buscar_equipo(equipos, nombre) == -1:
        equipos += [crear_equipo(nombre)]

def procesar_partido(equipos, local, visitante, goles_local, goles_visitante):
    i_local     = buscar_equipo(equipos, local)
    i_visitante = buscar_equipo(equipos, visitante)

    # Actualizar goles
    equipos[i_local][GF]     += goles_local
    equipos[i_local][GC]     += goles_visitante
    equipos[i_visitante][GF] += goles_visitante
    equipos[i_visitante][GC] += goles_local

    # Actualizar diferencia de gol
    equipos[i_local][DG]     = equipos[i_local][GF]     - equipos[i_local][GC]
    equipos[i_visitante][DG] = equipos[i_visitante][GF] - equipos[i_visitante][GC]

    # Asignar puntos segun resultado
    if goles_local > goles_visitante:
        equipos[i_local][PUNTOS] += 3
    elif goles_local < goles_visitante:
        equipos[i_visitante][PUNTOS] += 3
    else:
        equipos[i_local][PUNTOS]     += 1
        equipos[i_visitante][PUNTOS] += 1

def es_mejor(a, b):
    # Retorna True si el equipo a va antes que el equipo b
    if a[PUNTOS] != b[PUNTOS]:
        return a[PUNTOS] > b[PUNTOS]
    if a[DG] != b[DG]:
        return a[DG] > b[DG]
    if a[GF] != b[GF]:
        return a[GF] > b[GF]
    # Empate absoluto: orden alfabetico
    return a[NOMBRE] < b[NOMBRE]

def ordenar_tabla(equipos):
    # Bubble sort con criterio de desempate
    n = len(equipos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if es_mejor(equipos[j + 1], equipos[j]):
                equipos[j], equipos[j + 1] = equipos[j + 1], equipos[j]

def main():
    equipos = []

    cantidad = int(input())

    for _ in range(cantidad):
        linea = input().split()
        local      = linea[0]
        visitante  = linea[1]
        goles_local     = int(linea[2])
        goles_visitante = int(linea[3])

        agregar_si_no_existe(equipos, local)
        agregar_si_no_existe(equipos, visitante)

        procesar_partido(equipos, local, visitante, goles_local, goles_visitante)

    ordenar_tabla(equipos)

    print("Clasificados:")
    print(equipos[0][NOMBRE])
    print(equipos[1][NOMBRE])
    print("Tercero:")
    print(equipos[2][NOMBRE])

main()
