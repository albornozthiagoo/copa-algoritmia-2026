import time
import os
import random
import CodigoPrincipal as cp

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
    fase        = cp.fase

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
    robot = RobotFalso()

    # reiniciamos el estado de CodigoPrincipal
    cp.fase                  = "acercarse"
    cp.contador_estabilizar  = 0
    cp.contador_preparacion  = 0
    cp.contador_recuperacion = 0
    cp.pateado               = False

    iteracion = 0

    while cp.fase != "final" and iteracion < 500:

        cp.control(robot)

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
        elif cp.fase == "acercarse":
            time.sleep(0.08)
        elif cp.fase in ("estabilizar", "preparar", "recuperar"):
            time.sleep(0.12)
        elif cp.fase == "patear":
            time.sleep(0.05)
        else:
            time.sleep(0.3)

        iteracion += 1

    limpiar()
    dibujar_cancha(robot)

simular()
