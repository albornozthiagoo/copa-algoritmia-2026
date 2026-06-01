"""
DESAFIO 4 - ROBOT GOLEADOR
Copa de Algoritmia y Programacion UADE 2026

Estrategia:
El robot detecta su posicion, detecta la pelota, calcula distancia horizontal,
se acerca, se estabiliza, prepara la patada, patea y recupera postura.

El simulador oficial llama repetidamente a la funcion control(robot).
"""

# ============================================================
# CONSTANTES GENERALES
# ============================================================

DISTANCIA_PATADA = 0.35
DISTANCIA_CERCA = 0.70

VELOCIDAD_RAPIDA = 1.0
VELOCIDAD_LENTA = 0.4

CICLOS_ESTABILIZAR = 3
CICLOS_PREPARACION = 4
CICLOS_RECUPERACION = 5


# ============================================================
# VARIABLES GLOBALES DE CONTROL
# ============================================================

fase = "acercarse"

contador_estabilizar = 0
contador_preparacion = 0
contador_recuperacion = 0

pateado = False


# ============================================================
# TAREA 1 - ESTABILIZAR AL ROBOT
# TAREA 2 - DETECTAR POSICION DEL ROBOT
# TAREA 3 - DETECTAR POSICION DE LA PELOTA
# TAREA 4 - CALCULAR DISTANCIA HORIZONTAL
# ============================================================

def calcular_distancia_horizontal(posicion_robot, posicion_pelota):
    """
    Calcula la distancia horizontal entre el robot y la pelota.

    Parametros:
    posicion_robot: coordenadas actuales del robot en formato (x, y, z).
    posicion_pelota: coordenadas actuales de la pelota en formato (x, y, z).

    Retorna:
    distancia: distancia horizontal usando las coordenadas x e y.
    dx: diferencia entre pelota y robot en el eje x.
    dy: diferencia entre pelota y robot en el eje y.
    """
    dx = posicion_pelota[0] - posicion_robot[0]
    dy = posicion_pelota[1] - posicion_robot[1]

    distancia = (dx ** 2 + dy ** 2) ** 0.5

    return distancia, dx, dy


def verificar_estado_y_obtener_datos(robot):
    """
    Verifica si el robot esta cayendo. Si esta estable, obtiene la posicion
    del robot, la posicion de la pelota y calcula la distancia horizontal.

    Parametros:
    robot: objeto del simulador que contiene los metodos del desafio.

    Retorna:
    None si el robot esta cayendo.
    Si esta estable, retorna posicion_robot, posicion_pelota, distancia, dx y dy.
    """
    torso = robot.estado_torso()

    # estado_torso() devuelve un diccionario, accedemos con la clave "cayendo"
    cayendo = torso["cayendo"]

    if cayendo:
        robot.pararse()
        return None

    posicion_robot = robot.posicion_robot()
    posicion_pelota = robot.posicion_pelota()

    distancia, dx, dy = calcular_distancia_horizontal(posicion_robot, posicion_pelota)

    return posicion_robot, posicion_pelota, distancia, dx, dy


def decidir_fase_por_distancia(distancia):
    """
    Decide si el robot debe acercarse o estabilizarse segun la distancia
    horizontal a la pelota.

    Parametros:
    distancia: distancia horizontal entre robot y pelota.

    Retorna:
    "acercarse" si la pelota esta lejos.
    "estabilizar" si el robot ya esta en zona de patada.
    """
    if distancia > DISTANCIA_PATADA:
        nueva_fase = "acercarse"
    else:
        nueva_fase = "estabilizar"

    return nueva_fase


# ============================================================
# TAREA 5 - APROXIMARSE A LA PELOTA
# ============================================================

def fase_acercarse(robot):
    """
    Aproxima el robot hacia la pelota.

    Parametros:
    robot: objeto del simulador que contiene los metodos del desafio.

    Retorna:
    None si el robot estaba cayendo.
    "estabilizar" si ya llego a zona de patada.
    "acercarse" si debe seguir caminando.
    """
    datos = verificar_estado_y_obtener_datos(robot)

    if datos == None:
        return None

    posicion_robot, posicion_pelota, distancia, dx, dy = datos

    if distancia <= DISTANCIA_PATADA:
        robot.pararse()
        return "estabilizar"

    if distancia <= DISTANCIA_CERCA:
        robot.caminar(velocidad=VELOCIDAD_LENTA)
    else:
        robot.caminar(velocidad=VELOCIDAD_RAPIDA)

    return "acercarse"


# ============================================================
# TAREA 6 - ESTABILIZAR Y PREPARAR LA PATADA
# ============================================================

def fase_estabilizar(robot):
    """
    Mantiene al robot quieto algunos ciclos antes de preparar la patada.

    Parametros:
    robot: objeto del simulador que contiene los metodos del desafio.

    Retorna:
    None si el robot estaba cayendo.
    "acercarse" si la pelota volvio a quedar lejos.
    "estabilizar" mientras sigue estabilizando.
    "preparar" cuando ya puede preparar la patada.
    """
    global contador_estabilizar

    datos = verificar_estado_y_obtener_datos(robot)

    if datos == None:
        contador_estabilizar = 0
        return None

    posicion_robot, posicion_pelota, distancia, dx, dy = datos

    if distancia > DISTANCIA_CERCA:
        contador_estabilizar = 0
        return "acercarse"

    robot.pararse()

    contador_estabilizar = contador_estabilizar + 1

    if contador_estabilizar >= CICLOS_ESTABILIZAR:
        contador_estabilizar = 0
        return "preparar"

    return "estabilizar"


def fase_preparar_patada(robot):
    """
    Prepara la patada cuando el robot ya esta cerca de la pelota.

    Parametros:
    robot: objeto del simulador que contiene los metodos del desafio.

    Retorna:
    None si el robot estaba cayendo.
    "acercarse" si la pelota quedo lejos.
    "preparar" mientras sigue preparando.
    "patear" cuando ya puede ejecutar la patada.
    """
    global contador_preparacion

    datos = verificar_estado_y_obtener_datos(robot)

    if datos == None:
        contador_preparacion = 0
        return None

    posicion_robot, posicion_pelota, distancia, dx, dy = datos

    if distancia > DISTANCIA_CERCA:
        contador_preparacion = 0
        return "acercarse"

    contador_preparacion = contador_preparacion + 1

    if contador_preparacion <= 2:
        robot.pararse()
        return "preparar"

    elif contador_preparacion <= CICLOS_PREPARACION:
        robot.inclinarse(adelante=0.15, lateral=0.05)
        robot.preparar_patada(pierna="derecha", fuerza=0.8)
        return "preparar"

    else:
        contador_preparacion = 0
        return "patear"


# ============================================================
# TAREA 7 - EJECUTAR LA PATADA
# ============================================================

def fase_patear(robot):
    """
    Ejecuta la patada solamente si el robot esta en zona de golpe.

    Parametros:
    robot: objeto del simulador que contiene los metodos del desafio.

    Retorna:
    None si el robot estaba cayendo.
    "acercarse" si la pelota esta lejos.
    "recuperar" si se ejecuto la patada o si ya habia pateado.
    """
    global pateado
    global contador_recuperacion

    datos = verificar_estado_y_obtener_datos(robot)

    if datos == None:
        pateado = False
        contador_recuperacion = 0
        return None

    posicion_robot, posicion_pelota, distancia, dx, dy = datos

    if distancia > DISTANCIA_PATADA:
        pateado = False
        return "acercarse"

    if not pateado:
        robot.patear(pierna="derecha", potencia=1.0)
        pateado = True
        contador_recuperacion = 0

    return "recuperar"


# ============================================================
# TAREA 8 - RECUPERAR POSTURA
# ============================================================

def fase_recuperar(robot):
    """
    Recupera la postura del robot despues de patear.

    Parametros:
    robot: objeto del simulador que contiene los metodos del desafio.

    Retorna:
    "recuperar" mientras sigue estabilizando.
    "final" cuando termino la recuperacion.
    """
    global contador_recuperacion

    robot.pararse()

    contador_recuperacion = contador_recuperacion + 1

    if contador_recuperacion >= CICLOS_RECUPERACION:
        contador_recuperacion = 0
        return "final"

    return "recuperar"


# ============================================================
# FUNCION PRINCIPAL OBLIGATORIA
# ============================================================

def control(robot):
    """
    Funcion principal llamada repetidamente por el simulador.

    Parametros:
    robot: objeto del simulador con las funciones del desafio.

    Funcionamiento:
    Usa una maquina de estados:
    acercarse -> estabilizar -> preparar -> patear -> recuperar -> final

    No usa input, no usa time.sleep y no contiene bucles bloqueantes.
    """
    global fase

    if fase == "acercarse":
        nueva_fase = fase_acercarse(robot)

    elif fase == "estabilizar":
        nueva_fase = fase_estabilizar(robot)

    elif fase == "preparar":
        nueva_fase = fase_preparar_patada(robot)

    elif fase == "patear":
        nueva_fase = fase_patear(robot)

    elif fase == "recuperar":
        nueva_fase = fase_recuperar(robot)

    elif fase == "final":
        robot.pararse()
        nueva_fase = "final"

    else:
        robot.pararse()
        nueva_fase = "acercarse"

    if nueva_fase != None:
        fase = nueva_fase
