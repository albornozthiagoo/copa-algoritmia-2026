"""
DESAFIO 4 - ROBOT GOLEADOR
Copa de Algoritmia y Programacion UADE 2026

Estrategia:
El robot detecta su posicion, detecta la pelota, calcula distancia horizontal,
se acerca, se estabiliza, prepara la patada, patea y recupera postura.

El simulador oficial llama repetidamente a la funcion control(robot).

Para correr la simulacion visual en terminal:
    python robot_goleador.py
"""

import time
import os
import random


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


# ============================================================
# SIMULACION VISUAL EN TERMINAL
# ============================================================

# -----------------------------------------------
# CODIGOS ANSI
# -----------------------------------------------
RESET    = "\033[0m"
VERDE    = "\033[92m"
AMARILLO = "\033[93m"
ROJO     = "\033[91m"
AZUL     = "\033[94m"
CIAN     = "\033[96m"
BLANCO   = "\033[97m"
NEGRITA  = "\033[1m"

# -----------------------------------------------
# DIMENSIONES DE LA CANCHA EN TERMINAL
# -----------------------------------------------
ANCHO = 60
ALTO  = 15

X_MIN = 0.0
X_MAX = 5.5
Y_MIN = 0.0
Y_MAX = 1.4

X_PELOTA_FIJA = X_MAX * 0.70
Y_PELOTA_FIJA = Y_MAX / 2


# -----------------------------------------------
# ROBOT FALSO
# imita la API del simulador oficial
# -----------------------------------------------

class RobotFalso:

    def __init__(self):
        # robot aparece random en la mitad defensiva
        self.x_robot = round(random.uniform(X_MIN, X_MAX * 0.45), 2)
        self.y_robot = round(random.uniform(Y_MIN, Y_MAX), 2)

        # pelota siempre en el mismo lugar
        self.x_pelota = X_PELOTA_FIJA
        self.y_pelota = Y_PELOTA_FIJA

        self.cayendo        = False
        self.pateo          = False
        self.ultimo_mensaje = ""

        # inestabilidad aleatoria
        self.iteraciones_hasta_caida     = random.randint(15, 35)
        self.iteraciones_caminadas       = 0
        self.recuperando                 = False
        self.iteraciones_recuperando     = 0
        self.duracion_recuperacion       = 0

        print(CIAN + "Robot arranca en : x=" + str(self.x_robot) +
              "  y=" + str(self.y_robot) + RESET)
        print(CIAN + "Pelota en        : x=" + str(round(self.x_pelota, 2)) +
              "  y=" + str(round(self.y_pelota, 2)) + RESET)
        time.sleep(1.5)

    def posicion_robot(self):
        return (self.x_robot, self.y_robot, 0.0)

    def posicion_pelota(self):
        return (self.x_pelota, self.y_pelota, 0.0)

    def velocidad_pelota(self):
        return 5.0 if self.pateo else 0.0

    def estado_torso(self):
        # devuelve diccionario con clave "cayendo" tal como dice el PDF
        return {"cayendo": self.cayendo}

    def pararse(self):
        if self.recuperando:
            self.iteraciones_recuperando += 1
            if self.iteraciones_recuperando >= self.duracion_recuperacion:
                self.cayendo                 = False
                self.recuperando             = False
                self.iteraciones_recuperando = 0
                self.iteraciones_hasta_caida = random.randint(15, 35)
                self.iteraciones_caminadas   = 0
        self.ultimo_mensaje = "pararse()"

    def caminar(self, velocidad=1.0):
        if self.pateo:
            return

        paso = velocidad * 0.12

        if self.x_pelota > self.x_robot:
            self.x_robot += paso
        elif self.x_pelota < self.x_robot:
            self.x_robot -= paso

        if abs(self.y_pelota - self.y_robot) > 0.05:
            if self.y_pelota > self.y_robot:
                self.y_robot += paso * 0.5
            else:
                self.y_robot -= paso * 0.5

        # cuenta pasos y decide si se cae
        self.iteraciones_caminadas += 1
        if self.iteraciones_caminadas >= self.iteraciones_hasta_caida:
            self.cayendo             = True
            self.recuperando         = True
            self.iteraciones_recuperando = 0
            self.duracion_recuperacion   = random.randint(6, 14)

        self.ultimo_mensaje = "caminar(velocidad=" + str(velocidad) + ")"

    def inclinarse(self, adelante=0.0, lateral=0.0):
        self.ultimo_mensaje = "inclinarse(adelante=" + str(adelante) + ")"

    def preparar_patada(self, pierna="derecha", fuerza=1.0):
        self.ultimo_mensaje = "preparar_patada(pierna=" + pierna + ")"

    def patear(self, pierna="derecha", potencia=1.0):
        self.pateo          = True
        self.ultimo_mensaje = "patear(pierna=" + pierna + ")"

    def mover_articulacion(self, nombre, angulo):
        self.ultimo_mensaje = "mover_articulacion(" + nombre + ")"


# -----------------------------------------------
# FUNCIONES DE DIBUJO
# -----------------------------------------------

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def coordenada_a_col(x):
    col = int((x / X_MAX) * (ANCHO - 1))
    if col < 0:      col = 0
    if col >= ANCHO: col = ANCHO - 1
    return col

def coordenada_a_fila(y):
    fila = int((y / Y_MAX) * (ALTO - 2)) + 1
    if fila < 1:        fila = 1
    if fila > ALTO - 2: fila = ALTO - 2
    return fila

def dibujar_cancha(robot_falso):
    col_robot   = coordenada_a_col(robot_falso.x_robot)
    col_pelota  = coordenada_a_col(robot_falso.x_pelota)
    fila_robot  = coordenada_a_fila(robot_falso.y_robot)
    fila_pelota = coordenada_a_fila(robot_falso.y_pelota)

    if robot_falso.cayendo:
        simbolo_robot = ROJO + NEGRITA + "R" + RESET
    else:
        simbolo_robot = AZUL + NEGRITA + "R" + RESET

    print(VERDE + NEGRITA + "=" * (ANCHO + 4) + RESET)
    print(VERDE + NEGRITA + "   DESAFIO 4 - EL ROBOT GOLEADOR" + RESET)
    print(VERDE + NEGRITA + "=" * (ANCHO + 4) + RESET)

    for fila in range(ALTO):
        linea = VERDE + "|" + RESET

        for col in range(ANCHO):

            if col == ANCHO - 1 and fila >= ALTO // 2 - 2 and fila <= ALTO // 2 + 2:
                linea += AMARILLO + "A" + RESET

            elif fila == fila_robot and col == col_robot:
                linea += simbolo_robot

            elif fila == fila_pelota and col == col_pelota and not (fila == fila_robot and col == col_robot):
                linea += ROJO + NEGRITA + "O" + RESET

            elif col == ANCHO // 2 and fila != 0 and fila != ALTO - 1:
                linea += BLANCO + ":" + RESET

            elif fila == 0 or fila == ALTO - 1:
                linea += VERDE + "-" + RESET

            else:
                linea += VERDE + "." + RESET

        linea += VERDE + "|" + RESET
        print(linea)

    print(VERDE + NEGRITA + "=" * (ANCHO + 4) + RESET)
    print(CIAN   + "  FASE    : " + NEGRITA + fase + RESET)
    print(BLANCO + "  ACCION  : " + robot_falso.ultimo_mensaje + RESET)
    print(BLANCO + "  ROBOT   : x=" + str(round(robot_falso.x_robot, 2)) +
                   "  y=" + str(round(robot_falso.y_robot, 2)) + RESET)
    print(BLANCO + "  PELOTA  : x=" + str(round(robot_falso.x_pelota, 2)) +
                   "  y=" + str(round(robot_falso.y_pelota, 2)) + RESET)

    if robot_falso.cayendo:
        print(ROJO + NEGRITA + "  ! INESTABILIDAD DETECTADA - RECUPERANDO..." + RESET)
    else:
        print(BLANCO + "  " + RESET)

    print(VERDE + NEGRITA + "=" * (ANCHO + 4) + RESET)


# -----------------------------------------------
# SIMULACION PRINCIPAL
# -----------------------------------------------

def simular():
    global fase, contador_estabilizar, contador_preparacion, contador_recuperacion, pateado

    robot = RobotFalso()

    # reiniciamos el estado de la maquina de estados
    fase                  = "acercarse"
    contador_estabilizar  = 0
    contador_preparacion  = 0
    contador_recuperacion = 0
    pateado               = False

    iteracion = 0

    while fase != "final" and iteracion < 500:

        control(robot)

        if robot.pateo:
            robot.x_pelota += 0.25
            if robot.y_pelota > Y_MAX / 2:
                robot.y_pelota -= 0.03
            elif robot.y_pelota < Y_MAX / 2:
                robot.y_pelota += 0.03

        limpiar()
        dibujar_cancha(robot)

        if robot.cayendo:
            time.sleep(0.15)
        elif fase == "acercarse":
            time.sleep(0.08)
        elif fase in ("estabilizar", "preparar", "recuperar"):
            time.sleep(0.12)
        elif fase == "patear":
            time.sleep(0.05)
        else:
            time.sleep(0.3)

        iteracion += 1

    limpiar()
    dibujar_cancha(robot)


# -----------------------------------------------
# PUNTO DE ENTRADA
# -----------------------------------------------

if __name__ == "__main__":
    simular()
