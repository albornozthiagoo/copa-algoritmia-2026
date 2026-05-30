import time
import os
import robot_goleador

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
ANCHO      = 60
ALTO       = 15
FILA_JUEGO = 7

# -----------------------------------------------
# ROBOT FALSO
# imita al objeto robot del simulador oficial
# pero en vez de mover un robot real, mueve
# las coordenadas del dibujo en la terminal
# -----------------------------------------------

class RobotFalso:

    def __init__(self):
        # posicion inicial del robot
        self.x_robot  = 0.0
        self.y_robot  = 0.0

        # posicion de la pelota
        self.x_pelota = 4.5
        self.y_pelota = 0.0

        self.cayendo       = False
        self.pateo         = False
        self.ultimo_mensaje = ""

    def posicion_robot(self):
        return (self.x_robot, self.y_robot, 0.0)

    def posicion_pelota(self):
        return (self.x_pelota, self.y_pelota, 0.0)

    def velocidad_pelota(self):
        if self.pateo:
            return 5.0
        return 0.0

    def estado_torso(self):
        return {"cayendo": self.cayendo}

    def pararse(self):
        self.ultimo_mensaje = "pararse()"

    def caminar(self, velocidad=1.0):
        # mueve el robot hacia la pelota segun la velocidad
        if self.x_pelota > self.x_robot:
            self.x_robot += velocidad * 0.15
        self.ultimo_mensaje = "caminar(velocidad=" + str(velocidad) + ")"

    def inclinarse(self, adelante=0.0, lateral=0.0):
        self.ultimo_mensaje = "inclinarse(adelante=" + str(adelante) + ")"

    def preparar_patada(self, pierna="derecha", fuerza=1.0):
        self.ultimo_mensaje = "preparar_patada(pierna=" + pierna + ")"

    def patear(self, pierna="derecha", potencia=1.0):
        self.pateo    = True
        self.ultimo_mensaje = "patear(pierna=" + pierna + ")"

    def mover_articulacion(self, nombre, angulo):
        self.ultimo_mensaje = "mover_articulacion(" + nombre + ")"


# -----------------------------------------------
# FUNCIONES DE DIBUJO
# -----------------------------------------------

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def coordenada_a_col(x):
    # convierte coordenada real a columna en la terminal
    # el rango real es de 0.0 a 5.0, lo mapeamos a 0..ANCHO-1
    col = int((x / 5.5) * (ANCHO - 1))
    if col < 0:
        col = 0
    if col >= ANCHO:
        col = ANCHO - 1
    return col

def dibujar_cancha(robot_falso):
    col_robot  = coordenada_a_col(robot_falso.x_robot)
    col_pelota = coordenada_a_col(robot_falso.x_pelota)
    fase       = robot_goleador.fase

    print(VERDE + NEGRITA + "=" * (ANCHO + 4) + RESET)
    print(VERDE + NEGRITA + "   DESAFIO 4 - EL ROBOT GOLEADOR" + RESET)
    print(VERDE + NEGRITA + "=" * (ANCHO + 4) + RESET)

    for fila in range(ALTO):
        linea = VERDE + "|" + RESET

        for col in range(ANCHO):

            # arco rival derecha
            if col == ANCHO - 1 and fila >= ALTO // 2 - 2 and fila <= ALTO // 2 + 2:
                linea += AMARILLO + "H" + RESET

            # robot
            elif fila == FILA_JUEGO and col == col_robot:
                linea += AZUL + NEGRITA + "R" + RESET

            # pelota
            elif fila == FILA_JUEGO and col == col_pelota and col != col_robot:
                linea += ROJO + NEGRITA + "O" + RESET

            # linea del medio
            elif col == ANCHO // 2 and fila != 0 and fila != ALTO - 1:
                linea += BLANCO + ":" + RESET

            # bordes
            elif fila == 0 or fila == ALTO - 1:
                linea += VERDE + "-" + RESET

            # cesped
            else:
                linea += VERDE + "." + RESET

        linea += VERDE + "|" + RESET
        print(linea)

    print(VERDE + NEGRITA + "=" * (ANCHO + 4) + RESET)
    print(CIAN   + "  FASE    : " + NEGRITA + fase + RESET)
    print(BLANCO + "  ACCION  : " + robot_falso.ultimo_mensaje + RESET)
    print(BLANCO + "  ROBOT   : x=" + str(round(robot_falso.x_robot, 2)) +
          "  PELOTA: x=" + str(round(robot_falso.x_pelota, 2)) + RESET)
    print(VERDE + NEGRITA + "=" * (ANCHO + 4) + RESET)


# -----------------------------------------------
# SIMULACION PRINCIPAL
# llama a control(robot) repetidamente
# igual que lo hace el servidor real
# -----------------------------------------------

def simular():
    robot = RobotFalso()

    # reiniciamos el estado del modulo por si se importo antes
    robot_goleador.fase     = "inicio"
    robot_goleador.contador = 0

    iteracion = 0

    while robot_goleador.fase != "fin" and iteracion < 300:

        # llamamos a la funcion de control del archivo de entrega
        robot_goleador.control(robot)

        # si ya pateo, movemos la pelota hacia el arco
        if robot.pateo:
            robot.x_pelota += 0.3

        limpiar()
        dibujar_cancha(robot)

        # velocidad de la animacion segun la fase
        if robot_goleador.fase == "caminar":
            time.sleep(0.08)
        elif robot_goleador.fase in ("estabilizar", "preparar", "recuperar"):
            time.sleep(0.15)
        elif robot_goleador.fase == "patear":
            time.sleep(0.05)
        else:
            time.sleep(0.3)

        iteracion += 1

    # pantalla final
    limpiar()
    dibujar_cancha(robot)
    print(AMARILLO + NEGRITA + "\n  *** SIMULACION FINALIZADA ***" + RESET)

simular()
