# con esta funcion creamos un equipo nuevo con todos sus estadisticas en cero
# cada vez que se detecte o lee un equipo nuevo va seguir esta misma estructura

#puntos = puntos del equipo
#pj = partidos jugados
#pg = partidos ganados
#pe = partidos empatados
#pp = partidos perdidos
#gf = goles a favor
#gc = goles en contra

def crear_equipo():
    equipo = {
        "puntos": 0,
        "pj": 0,
        "pg": 0,
        "pe": 0,
        "pp": 0,
        "gf": 0,
        "gc": 0
    }

    return equipo

# creamos otra funcion para preguntar si el equipo que se lee/detecta existe o no
# en caso de que no existe lo creamos con su nombre y le ponemos su estructura reutilizando la funcion crea_equipo()
# usamos un diccionario general llamado equipos para registrar los equipos nuevos con su estructura crar_equipo()


def agregar_equipo_si_no_existe(equipos, nombre):
    if nombre not in equipos:
        equipos[nombre] = crear_equipo()



#creamos una funcion para procesar los partidos

# primero recibimos datos como por ejemplo, procesar_partido(equipos, "ARG", "BRA", 2, 1)

def procesar_partido(equipos, local, visitante, goles_local, goles_visitante):

    # antes de procesar el partido nos aseguramos primero que los equipos existan y tengan su estructura
    
    agregar_equipo_si_no_existe(equipos, local)
    agregar_equipo_si_no_existe(equipos, visitante)

    equipos[local]["pj"] = equipos[local]["pj"] + 1
    equipos[visitante]["pj"] = equipos[visitante]["pj"] + 1

    equipos[local]["gf"] = equipos[local]["gf"] + goles_local
    equipos[local]["gc"] = equipos[local]["gc"] + goles_visitante

    equipos[visitante]["gf"] = equipos[visitante]["gf"] + goles_visitante
    equipos[visitante]["gc"] = equipos[visitante]["gc"] + goles_local

    if goles_local > goles_visitante:
        equipos[local]["puntos"] = equipos[local]["puntos"] + 3
        equipos[local]["pg"] = equipos[local]["pg"] + 1
        equipos[visitante]["pp"] = equipos[visitante]["pp"] + 1

    elif goles_local < goles_visitante:
        equipos[visitante]["puntos"] = equipos[visitante]["puntos"] + 3
        equipos[visitante]["pg"] = equipos[visitante]["pg"] + 1
        equipos[local]["pp"] = equipos[local]["pp"] + 1

    else:
        equipos[local]["puntos"] = equipos[local]["puntos"] + 1
        equipos[visitante]["puntos"] = equipos[visitante]["puntos"] + 1
        equipos[local]["pe"] = equipos[local]["pe"] + 1
        equipos[visitante]["pe"] = equipos[visitante]["pe"] + 1