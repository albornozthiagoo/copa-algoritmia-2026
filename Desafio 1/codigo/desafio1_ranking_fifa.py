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
