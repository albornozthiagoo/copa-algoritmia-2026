# DESAFÍO 1 - SISTEMA DE CLASIFICACIÓN FIFA
# Copa de Algoritmia y Programación UADE 2026

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


# VALIDACION: esta funcion verifica que los goles esten dentro del rango permitido
# segun la consigna los goles deben ser enteros entre 0 y 20

def goles_validos(goles):
    return goles >= 0 and goles <= 20


# VALIDACION: esta funcion verifica que el grupo cumpla las condiciones principales
# el grupo debe tener exactamente 4 equipos
# cada equipo debe tener exactamente 3 partidos jugados

def grupo_valido(equipos):
    if len(equipos) != 4:
        print("Error: el grupo debe tener exactamente 4 equipos.")
        return False

    for nombre in equipos:
        if equipos[nombre]["pj"] != 3:
            print("Error: el equipo", nombre, "no tiene exactamente 3 partidos jugados.")
            return False

    return True



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

     try:
        #asigna el archivo en solo lectura
        archivo = open(nombre_archivo, 'r')

    except FileNotFoundError:
        #Si no encuentra el archivo da error
        print("Error: no se encontró el archivo:", nombre_archivo)
        return equipos

    # usamos readline() para que nos permita leer una linea del archivo y ya estar prepatados para leer la siguiente linea
    # como la primera linea es la cantidad de paetidos jugados se va leer "6" y utilizamos int para tomarlo como un numero
    cantidad_partidos = int(archivo.readline())

    # VALIDACION: verificamos que la cantidad de partidos sea exactamente 6
    # si no se cumple, cerramos el archivo y devolvemos None para indicar que hubo un error

    if cantidad_partidos != 6:
        print("Error: la cantidad de partidos debe ser 6.")
        archivo.close()
        return None

    # como sabemos la cantidad de partidos ahora utilizamos for para repetir la siguiente estructura 6 veces 
    # repetimos 6 veces para poder procesar todos los partidos del archivo
    for i in range(cantidad_partidos):
        # aca utilizamos readline() para que lea la siguiente linea del archivo (como ya leimos una linea antes esta seria la segunda linea)
        linea = archivo.readline()

        # aca utilizamos split() para seprar el texto de la segunda linea del archivo y ordenarlas en espacios como una lista
        # al transformar la segunda linea del archivo (que es donde se encuentra los datos un partido) en una lista podemos identificar cada espacio
        datos = linea.split()

        # VALIDACION: verificamos que la linea tenga exactamente 4 datos
        # debe tener: equipo local, equipo visitante, goles local y goles visitante

        if len(datos) != 4:
            print("Error: formato incorrecto en la linea", i + 2)
            archivo.close()
            return None

        # como split() nos trandormo la linea en una lista procedemos a relacionar los datos del partido respectivamente de su posicion de la lista
        local = datos[0]
        visitante = datos[1]

        # VALIDACION: verificamos que un equipo no juegue contra si mismo

        if local == visitante:
            print("Error: un equipo no puede jugar contra si mismo.")
            archivo.close()
            return None

        # VALIDACION: verificamos que los goles sean numeros enteros
        # isdigit() devuelve True si el texto contiene solamente numeros

        if not datos[2].isdigit() or not datos[3].isdigit():
            print("Error: los goles deben ser numeros enteros.")
            archivo.close()
            return None

        # para los goles de local y visitante usamos int para que los lea como numeros y no texto

        goles_local = int(datos[2])
        goles_visitante = int(datos[3])

        # VALIDACION: verificamos que los goles esten entre 0 y 20

        if not goles_validos(goles_local) or not goles_validos(goles_visitante):
            print("Error: los goles deben estar entre 0 y 20.")
            archivo.close()
            return None

        # por ultimo utilizamos la funcion procesar_partio() para actualizar los datos de cada equipo que jugo el partido que se leyo en el archivo

        procesar_partido(equipos, local, visitante, goles_local, goles_visitante)

        # repetimos gracias al for este proceso 6 veces para que se procese todos los datos de los equipos que jugaron que menciona el archivo

    archivo.close() # cerramos el archivo 

    return equipos  # finalmente devolvemos equipos con todo los datos actualizados de los equipos que hayan en el archivo

# creamos una funcion aparte para calcular la diferencia de gol

def calcular_diferencia_gol(datos_equipo):
    # para saber la diferencia de gol de un equipo simplemente restamos sus goles a favor con sus goles en contra
    return datos_equipo["gf"] - datos_equipo["gc"] 

# creamos una funcion para establecer el orden de criterio para clasificar a los equipos
def criterio_ordenamiento(equipo):
    puntos = equipo[1]
    diferencia_gol = equipo[2]
    goles_favor = equipo[3]
    nombre = equipo[0]

    # devolvemos en orden los datos en negativo porque mas adelante vamos a usar la funcion sort()
    # la funcion sort sirve para ordenar listas y en cuanto a los numeros lo hace de menor a mayor por eso utilizamos los puntos en negativo
    return (-puntos, -diferencia_gol, -goles_favor, nombre)

# creamos otra funcion donde aca se va ordenar la tabla/ranking de los equipos con sus estadisticas
def obtener_ranking(equipos):

    # creamos ahora una lista vacia llamada ranking donde van a ir los equipos y su estadisticas mejor ordenadas horizontalmente
    ranking = []

    # creamos un for para recorrer todos los nombres de los equipos 

    for nombre in equipos:

        # por cada nombre de equipo que recorra le estamos pidiendo aca todos sus datos del equipo
        datos = equipos[nombre]

        # creamos una lista ahora con los datos mas impornates de cada equipo ordenados por posicion
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

        # finalmente al final de cada recorrido agregamos cada estadistica importante de equipo_ranking a la lista vacia ranking
        # usamos la funcion append() para agregarla al final de la lista de ranking los datos de la lista equipo_ranking
        ranking.append(equipo_ranking)

        # utilizamos la funcion sort() ahora para ordenar y clasificar los equipos 
        # dentro de sort utilizamos una key con la funcion de criterio_ordenamiento para decirle que caada equipo que tenga el ranking lo ordene 
        # teniendo en cuenta el orden la posicion que establecimos en la funcion criterio_ordenamiento

    ranking.sort(key=criterio_ordenamiento)

    # devolvemos finalemnte ranking 
    return ranking

# creamos otra funcion para hacer la ultima tarea que es ordenar la salida de los equipos del ranking y mostrar quien calisfico y quien no

def mostrar_clasificados(ranking):
    print("Clasificados:")
    # aca estamos diciendo que imprimamos la primera fila de la lista de ranking y su nombre
    print(ranking[0][0])
    # aca estamos diciendo que imprimamos la segunda fila de la lista de ranking y su nombre
    print(ranking[1][0])
    print("Tercero:")
    # aca estamos diciendo que imprimamos la tercera fila de la lista de ranking y su nombre
    print(ranking[2][0])

def borrar_pantalla():
    print("\n" * 50)

equipos = leer_partidos_desde_archivo("codigos/partidos.txt")

# inicializamos la variable menu_seleccion en -1 para poder entrar al while
menu_seleccion = -1

# mientras menu_seleccion sea distinto de 0 el menu va seguir ejecutandose
while menu_seleccion != 0:

    # mostramos el menu principal
    print("\n========== MENU PRINCIPAL ==========")
    print("1 - Modo de uso")
    print("2 - Tabla de posiciones")
    print("3 - Acerca de")
    print("0 - Salir")

    # pedimos al usuario que ingrese una opcion
    # usamos int() para convertir el dato ingresado a numero
    menu_seleccion = int(input("\nIngrese una opcion: "))

    # si el usuario ingresa 1 mostramos la seccion modo de uso
    if menu_seleccion == 1:
        borrar_pantalla()
        print("\n========== MODO DE USO ==========")

        # mostramos los pasos necesarios para usar el programa
        print("1. Crear un archivo llamado partidos.txt")
        print("2. Colocar el archivo dentro de la carpeta codigos")
        print("3. Ingresar los partidos siguiendo el formato:")
        print("   EQUIPO_LOCAL EQUIPO_VISITANTE GOLES_LOCAL GOLES_VISITANTE")
        print("4. Ejecutar el programa")
        print("5. Seleccionar la opcion correspondiente en el menu")

        # mostramos un ejemplo visual de como deberia verse el archivo txt
        print("\nEjemplo de archivo:\n")

        print("6")
        print("ARG BRA 2 1")
        print("BRA ESP 1 1")
        print("ESP ARG 3 0")
        print("ARG JPN 2 0")
        print("BRA JPN 2 1")
        print("ESP JPN 1 0")

    # si el usuario ingresa 2 mostramos la tabla de posiciones
    elif menu_seleccion == 2:
        borrar_pantalla()
        print("\nMostrando tabla de posiciones...\n")
        # VALIDACION FINAL: si equipos no es None y el grupo es valido, recien ahi calculamos el ranking
        # esto evita que el programa intente ordenar datos cuando el archivo tiene algun error

        if equipos is not None and grupo_valido(equipos):
            ranking = obtener_ranking(equipos)
            mostrar_clasificados(ranking)
            # si el usuario ingresa 3 mostramos informacion del proyecto
    elif menu_seleccion == 3:
        borrar_pantalla()
        print("\n========== ACERCA DE ==========")

        print("Proyecto realizado para la Copa de Algoritmia 2026.\n")

        print("Integrantes del equipo:")
        print("- Thiago Albornoz")
        print("- Lucas Abad")
        print("- Valentino Sarniguette")
        print("- Gaston Trezeguet")
        print("- Valentin Zaccari")
        print("""        ___________\n       '._==_==_=_.'\n       .-\\:      /-.\n      |   \\     /   |\n       \\   \\   /   /\n        '.  \\ /  .'\n          '-._.-'\n            | |\n           _| |_\n          `-----'""")
   
    # si el usuario ingresa 0 finalizamos el programa
    elif menu_seleccion == 0:
        
        print("\nSaliendo del programa...")

    # si el usuario ingresa cualquier otro numero mostramos error
    else:

        print("\nLa opcion ingresada no existe.")



