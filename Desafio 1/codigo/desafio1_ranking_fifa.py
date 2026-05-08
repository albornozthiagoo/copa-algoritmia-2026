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

def agregar_equipo_si_no_existe(equipos, nombre):
    if nombre not in equipos:
        equipos[nombre] = crear_equipo()