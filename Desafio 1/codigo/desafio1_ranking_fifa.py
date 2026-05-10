# DESAFÍO 1 - SISTEMA DE CLASIFICACIÓN FIFA
# Copa de Algoritmia y Programación UADE 2026

# Con esta función creamos un equipo nuevo con todas sus estadísticas en cero.
# Cada vez que se detecta un equipo nuevo, se le asigna esta misma estructura.

# puntos = puntos del equipo
# pj = partidos jugados
# pg = partidos ganados
# pe = partidos empatados
# pp = partidos perdidos
# gf = goles a favor
# gc = goles en contra

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


# Esta función verifica si un equipo ya existe dentro del diccionario general.
# Si el equipo no existe, lo agrega usando la estructura creada por crear_equipo().

def agregar_equipo_si_no_existe(equipos, nombre):
    if nombre not in equipos:
        equipos[nombre] = crear_equipo()


# Esta función valida que los goles estén dentro del rango permitido por la consigna.
# Los goles deben ser enteros entre 0 y 20.

def goles_validos(goles):
    return goles >= 0 and goles <= 20


# Esta función valida que el grupo cumpla las condiciones principales:
# - Debe haber exactamente 4 equipos.
# - Cada equipo debe haber jugado exactamente 3 partidos.

def grupo_valido(equipos):
    if len(equipos) != 4:
        print("Error: el grupo debe tener exactamente 4 equipos.")
        return False

    for nombre in equipos:
        if equipos[nombre]["pj"] != 3:
            print("Error: el equipo", nombre, "no tiene exactamente 3 partidos jugados.")
            return False

    return True


# Esta función procesa un partido.
# Recibe el diccionario de equipos, el equipo local, el visitante y los goles de cada uno.
# Ejemplo: procesar_partido(equipos, "ARG", "BRA", 2, 1)

def procesar_partido(equipos, local, visitante, goles_local, goles_visitante):

    # Antes de procesar el partido, nos aseguramos de que ambos equipos existan.
    # Si alguno no existe, se crea automáticamente con sus estadísticas en cero.

    agregar_equipo_si_no_existe(equipos, local)
    agregar_equipo_si_no_existe(equipos, visitante)

    # Sumamos 1 partido jugado tanto al equipo local como al visitante.

    equipos[local]["pj"] = equipos[local]["pj"] + 1
    equipos[visitante]["pj"] = equipos[visitante]["pj"] + 1

    # Actualizamos goles a favor y goles en contra del equipo local.

    equipos[local]["gf"] = equipos[local]["gf"] + goles_local
    equipos[local]["gc"] = equipos[local]["gc"] + goles_visitante

    # Actualizamos goles a favor y goles en contra del equipo visitante.

    equipos[visitante]["gf"] = equipos[visitante]["gf"] + goles_visitante
    equipos[visitante]["gc"] = equipos[visitante]["gc"] + goles_local

    # Si los goles del local son mayores, gana el local.
    # El local suma 3 puntos y 1 partido ganado.
    # El visitante suma 1 partido perdido.

    if goles_local > goles_visitante:
        equipos[local]["puntos"] = equipos[local]["puntos"] + 3
        equipos[local]["pg"] = equipos[local]["pg"] + 1
        equipos[visitante]["pp"] = equipos[visitante]["pp"] + 1

    # Si los goles del visitante son mayores, gana el visitante.
    # El visitante suma 3 puntos y 1 partido ganado.
    # El local suma 1 partido perdido.

    elif goles_local < goles_visitante:
        equipos[visitante]["puntos"] = equipos[visitante]["puntos"] + 3
        equipos[visitante]["pg"] = equipos[visitante]["pg"] + 1
        equipos[local]["pp"] = equipos[local]["pp"] + 1

    # Si los goles son iguales, el partido termina empatado.
    # Ambos equipos suman 1 punto y 1 partido empatado.

    else:
        equipos[local]["puntos"] = equipos[local]["puntos"] + 1
        equipos[visitante]["puntos"] = equipos[visitante]["puntos"] + 1
        equipos[local]["pe"] = equipos[local]["pe"] + 1
        equipos[visitante]["pe"] = equipos[visitante]["pe"] + 1


# Esta función lee el archivo de entrada y procesa todos los partidos.
# El archivo debe tener una primera línea con la cantidad de partidos.
# Luego, cada línea debe tener: EquipoLocal EquipoVisitante GolesLocal GolesVisitante.

def leer_partidos_desde_archivo(nombre_archivo):

    # Creamos el diccionario general donde se van a guardar todos los equipos.
    # Cada equipo tendrá sus estadísticas actualizadas a medida que se procesen partidos.

    equipos = {}

    # Abrimos el archivo en modo lectura.
    # La letra "r" significa read, es decir, leer.

    archivo = open(nombre_archivo, "r")

    # Leemos la primera línea del archivo.
    # Esa primera línea indica la cantidad de partidos.
    # Usamos int() porque el archivo lee texto, pero nosotros necesitamos un número.

    cantidad_partidos = int(archivo.readline())

    # Validamos que la cantidad de partidos sea exactamente 6,
    # porque la consigna indica que cada grupo tiene 6 partidos.

    if cantidad_partidos != 6:
        print("Error: la cantidad de partidos debe ser 6.")
        archivo.close()
        return None

    # Usamos for para repetir el proceso de lectura una vez por cada partido.
    # Como cantidad_partidos vale 6, el bloque se repite 6 veces.

    for i in range(cantidad_partidos):

        # Leemos la siguiente línea del archivo.
        # Como la primera línea ya se leyó antes, ahora se leen los partidos.

        linea = archivo.readline()

        # split() separa la línea por espacios y la transforma en una lista.
        # Ejemplo: "ARG BRA 2 1" pasa a ser ["ARG", "BRA", "2", "1"].

        datos = linea.split()

        # Validamos que la línea tenga exactamente 4 datos.
        # Debe tener: equipo local, equipo visitante, goles local y goles visitante.

        if len(datos) != 4:
            print("Error: formato incorrecto en la línea", i + 2)
            archivo.close()
            return None

        # Guardamos los nombres de los equipos.
        # datos[0] es el equipo local.
        # datos[1] es el equipo visitante.

        local = datos[0]
        visitante = datos[1]

        # Validamos que un equipo no juegue contra sí mismo.

        if local == visitante:
            print("Error: un equipo no puede jugar contra sí mismo.")
            archivo.close()
            return None

        # Validamos que los goles sean números enteros.
        # isdigit() devuelve True si el texto contiene solamente números.

        if not datos[2].isdigit() or not datos[3].isdigit():
            print("Error: los goles deben ser números enteros.")
            archivo.close()
            return None

        # Convertimos los goles a número entero para poder hacer cálculos.

        goles_local = int(datos[2])
        goles_visitante = int(datos[3])

        # Validamos que los goles estén entre 0 y 20.

        if not goles_validos(goles_local) or not goles_validos(goles_visitante):
            print("Error: los goles deben estar entre 0 y 20.")
            archivo.close()
            return None

        # Si todos los datos son válidos, procesamos el partido
        # y actualizamos las estadísticas de ambos equipos.

        procesar_partido(equipos, local, visitante, goles_local, goles_visitante)

    # Cerramos el archivo después de terminar la lectura.

    archivo.close()

    # Devolvemos el diccionario equipos con todos los datos actualizados.

    return equipos


# Esta función calcula la diferencia de gol de un equipo.
# La diferencia de gol se obtiene restando goles en contra a goles a favor.

def calcular_diferencia_gol(datos_equipo):
    return datos_equipo["gf"] - datos_equipo["gc"]


# Esta función establece el criterio de ordenamiento del ranking.
# El orden de prioridad es:
# 1. Mayor cantidad de puntos.
# 2. Mayor diferencia de gol.
# 3. Mayor cantidad de goles a favor.
# 4. Orden alfabético en caso de empate absoluto.

def criterio_ordenamiento(equipo):
    puntos = equipo[1]
    diferencia_gol = equipo[2]
    goles_favor = equipo[3]
    nombre = equipo[0]

    # Usamos los valores numéricos en negativo porque sort() ordena de menor a mayor.
    # Al ponerlos en negativo, logramos que los mayores queden primero.
    # El nombre queda sin negativo porque debe ordenarse alfabéticamente.

    return (-puntos, -diferencia_gol, -goles_favor, nombre)


# Esta función arma y ordena el ranking final de los equipos.

def obtener_ranking(equipos):

    # Creamos una lista vacía donde vamos a guardar cada equipo con sus datos principales.

    ranking = []

    # Recorremos todos los equipos del diccionario.

    for nombre in equipos:

        # Obtenemos las estadísticas del equipo actual.

        datos = equipos[nombre]

        # Creamos una lista con los datos importantes del equipo.
        # Cada posición de esta lista representa una estadística:
        # [0] nombre
        # [1] puntos
        # [2] diferencia de gol
        # [3] goles a favor
        # [4] goles en contra
        # [5] partidos jugados
        # [6] partidos ganados
        # [7] partidos empatados
        # [8] partidos perdidos

        equipo_ranking = [
            nombre,
            datos["puntos"],
            calcular_diferencia_gol(datos),
            datos["gf"],
            datos["gc"],
            datos["pj"],
            datos["pg"],
            datos["pe"],
            datos["pp"]
        ]

        # Agregamos el equipo a la lista ranking.

        ranking.append(equipo_ranking)

    # Ordenamos el ranking usando la función criterio_ordenamiento.
    # Esta función indica qué datos se deben mirar y en qué orden.

    ranking.sort(key=criterio_ordenamiento)

    # Devolvemos el ranking ya ordenado.

    return ranking


# Esta función muestra la salida final solicitada por la consigna.
# Muestra el primer clasificado, el segundo clasificado y el tercer puesto.

def mostrar_clasificados(ranking):
    print("Clasificados:")

    # ranking[0][0] significa:
    # primera fila del ranking, nombre del equipo.

    print(ranking[0][0])

    # ranking[1][0] significa:
    # segunda fila del ranking, nombre del equipo.

    print(ranking[1][0])

    print("Tercero:")

    # ranking[2][0] significa:
    # tercera fila del ranking, nombre del equipo.

    print(ranking[2][0])


# Programa principal.
# Primero leemos los partidos desde el archivo.
# Después validamos que el grupo tenga 4 equipos y que todos hayan jugado 3 partidos.
# Si todo es correcto, se obtiene el ranking y se muestran los clasificados.

equipos = leer_partidos_desde_archivo("Desafio 1/codigo/partidos.txt")

if equipos is not None and grupo_valido(equipos):
    ranking = obtener_ranking(equipos)
    mostrar_clasificados(ranking)


