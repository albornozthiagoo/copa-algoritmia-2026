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

# aca recibimos datos como por ejemplo, procesar_partido(equipos, "ARG", "BRA", 2, 1) para actualizar la estructura de estadisticas de cada equipo 

def procesar_partido(equipos, local, visitante, goles_local, goles_visitante):

    # antes de procesar el partido nos aseguramos primero que los equipos existan y tengan su estructura de estadisticas

    agregar_equipo_si_no_existe(equipos, local)
    agregar_equipo_si_no_existe(equipos, visitante)

    # sumamos partido jugado en +1 tanto para el quipo visitante como el equipo local
    equipos[local]["pj"] = equipos[local]["pj"] + 1
    equipos[visitante]["pj"] = equipos[visitante]["pj"] + 1

    # calculamos los goles a favor y en contra del equipo local

    equipos[local]["gf"] = equipos[local]["gf"] + goles_local
    equipos[local]["gc"] = equipos[local]["gc"] + goles_visitante

    # calculamos los goles a favor y en contra del equipo visitante

    equipos[visitante]["gf"] = equipos[visitante]["gf"] + goles_visitante
    equipos[visitante]["gc"] = equipos[visitante]["gc"] + goles_local

    # preguntamos aca si los goles del equipo local es mayor a los goles del equipo visitante
    # si se cumple sumamos +3 en puntos y +1 en partido ganado para el equipo local
    # y como el equipo local gano sumamos +1 en el contador de partido perdido para el visitante

    if goles_local > goles_visitante:
        equipos[local]["puntos"] = equipos[local]["puntos"] + 3
        equipos[local]["pg"] = equipos[local]["pg"] + 1
        equipos[visitante]["pp"] = equipos[visitante]["pp"] + 1

    # preguntamos aca si los goles del equipo local es menor a los goles del equipo visitante
    # si se cumple sumamos +3 en puntos y +1 en partido ganado para el equipo visitante
    # y como el equipo visitante gano sumamos +1 en el contador de partido perdido para el equipo local

    elif goles_local < goles_visitante:
        equipos[visitante]["puntos"] = equipos[visitante]["puntos"] + 3
        equipos[visitante]["pg"] = equipos[visitante]["pg"] + 1
        equipos[local]["pp"] = equipos[local]["pp"] + 1

    # si el equipo lcoal y el visitante empatan sumamos 1 punto para ambos equipos 
    # y actualizamos sumando +1 en el contador de partido empatado para ambos equipos

    else:
        equipos[local]["puntos"] = equipos[local]["puntos"] + 1
        equipos[visitante]["puntos"] = equipos[visitante]["puntos"] + 1
        equipos[local]["pe"] = equipos[local]["pe"] + 1
        equipos[visitante]["pe"] = equipos[visitante]["pe"] + 1

# creamos una funcion ahora para poder leer el archivo que va entrar

def leer_partidos_desde_archivo(nombre_archivo):
    # aca creamos un diccionario vacio.
    # este va ser nuestro diccionario general donde va estar todas las estadisiticas de los equipos del archivo registradas y actualizadas
    equipos = {}   

    # el open (partidos.txt,r) es para abrir el archivo en modo lectura. 'r' viene read. leer.

    archivo = open(nombre_archivo, 'r')

    # usamos readline() para que nos permita leer una linea del archivo y ya estar prepatados para leer la siguiente linea
    # como la primera linea es la cantidad de paetidos jugados se va leer "6" y utilizamos int para tomarlo como un numero
    cantidad_partidos = int(archivo.readline())

    # como sabemos la cantidad de partidos ahora utilizamos for para repetir la siguiente estructura 6 veces 
    # repetimos 6 veces para poder procesar todos los partidos del archivo
    for i in range(cantidad_partidos):
        # aca utilizamos readline() para que lea la siguiente linea del archivo (como ya leimos una linea antes esta seria la segunda linea)
        linea = archivo.readline()

        # aca utilizamos split() para seprar el texto de la segunda linea del archivo y ordenarlas en espacios como una lista
        # al transformar la segunda linea del archivo (que es donde se encuentra los datos un partido) en una lista podemos identificar cada espacio
        datos = linea.split()

        # como split() nos trandormo la linea en una lista procedemos a relacionar los datos del partido respectivamente de su posicion de la lista
        local = datos[0]
        visitante = datos[1]

        # para los goles de local y visitante usamos int para que los lea como numeros y no texto

        goles_local = int(datos[2])
        goles_visitante = int(datos[3])

        # por ultimo utilizamos la funcion procesar_partio() para actualizar los datos de cada equipo que jugo el partido que se leyo en el archivo

        procesar_partido(equipos, local, visitante, goles_local, goles_visitante)

        # repetimos gracias al for este proceso 6 veces para que se procese todos los datos de los equipos que jugaron que menciona el archivo

    archivo.close() # cerramos el archivo 

    return equipos  # finalmente devolvemos equipos con todo los datos actualizados de los equipos que hayan en el archivo


def calcular_diferencia_gol(datos_equipo):
    return datos_equipo["gf"] - datos_equipo["gc"]

equipos = leer_partidos_desde_archivo("Desafio 1/codigo/partidos.txt")

print(equipos)





