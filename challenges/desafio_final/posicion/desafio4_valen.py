# -----------------------------------------------
# DESAFIO 4: EL ROBOT GOLEADOR
# Estrategia de control para el robot G1
# Codigo Alpha
# -----------------------------------------------

# variables globales de estado
fase     = "inicio"
contador = 0

# umbrales de distancia
DISTANCIA_LEJOS  = 1.5   # camina rapido
DISTANCIA_CERCA  = 0.6   # camina despacio
DISTANCIA_PATADA = 0.35  # zona de golpe

# cuantas iteraciones esperar en cada fase de espera
ESPERA_ESTABILIZAR = 10
ESPERA_PREPARAR    = 8
ESPERA_RECUPERAR   = 10


# -----------------------------------------------
# FUNCIONES AUXILIARES
# -----------------------------------------------

def calcular_distancia(posicion_robot, posicion_pelota):
    # calcula la distancia horizontal entre el robot y la pelota
    # usa solo x e y, ignorando la altura z
    dx = posicion_pelota[0] - posicion_robot[0]
    dy = posicion_pelota[1] - posicion_robot[1]
    distancia = (dx ** 2 + dy ** 2) ** 0.5
    return distancia

def robot_cayendo(torso):
    # devuelve True si el torso indica que el robot esta cayendo
    return torso["cayendo"] == True


# -----------------------------------------------
# TAREA 1: INICIALIZAR Y ESTABILIZAR
# -----------------------------------------------

def fase_inicio(robot):
    # al comenzar simplemente nos paramos y pasamos a detectar
    robot.pararse()
    return "detectar"


# -----------------------------------------------
# TAREA 2 Y 3: DETECTAR POSICION DEL ROBOT Y PELOTA
# TAREA 4: CALCULAR DISTANCIA Y DECIDIR
# -----------------------------------------------

def fase_detectar(robot):
    # consultamos posicion del robot y de la pelota en cada iteracion
    posicion_robot  = robot.posicion_robot()
    posicion_pelota = robot.posicion_pelota()
    torso           = robot.estado_torso()

    # si el robot esta cayendo, recuperamos antes de hacer cualquier cosa
    if robot_cayendo(torso):
        robot.pararse()
        return "detectar"

    # calculamos la distancia horizontal a la pelota
    distancia = calcular_distancia(posicion_robot, posicion_pelota)

    # decidimos la siguiente fase segun la distancia
    if distancia > DISTANCIA_CERCA:
        return "caminar"
    else:
        return "estabilizar"


# -----------------------------------------------
# TAREA 5: APROXIMARSE A LA PELOTA
# -----------------------------------------------

def fase_caminar(robot):
    posicion_robot  = robot.posicion_robot()
    posicion_pelota = robot.posicion_pelota()
    torso           = robot.estado_torso()

    # si esta cayendo, recuperamos postura
    if robot_cayendo(torso):
        robot.pararse()
        return "detectar"

    distancia = calcular_distancia(posicion_robot, posicion_pelota)

    # si ya llego a zona de golpe, pasamos a estabilizar
    if distancia <= DISTANCIA_PATADA:
        return "estabilizar"

    # si esta cerca usamos velocidad baja para no pasarnos
    # si esta lejos usamos velocidad normal
    if distancia <= DISTANCIA_CERCA:
        robot.caminar(velocidad=0.4)
    else:
        robot.caminar(velocidad=1.0)

    return "caminar"


# -----------------------------------------------
# TAREA 6: PREPARAR LA PATADA
# -----------------------------------------------

def fase_estabilizar(robot):
    global contador

    torso = robot.estado_torso()

    # si esta cayendo, recuperamos primero
    if robot_cayendo(torso):
        robot.pararse()
        contador = 0
        return "detectar"

    # nos paramos y esperamos algunas iteraciones para estabilizarnos
    robot.pararse()
    contador += 1

    if contador >= ESPERA_ESTABILIZAR:
        contador = 0
        return "preparar"

    return "estabilizar"

def fase_preparar(robot):
    global contador

    torso = robot.estado_torso()

    # si esta cayendo no preparamos
    if robot_cayendo(torso):
        robot.pararse()
        contador = 0
        return "detectar"

    # verificamos que seguimos cerca de la pelota
    posicion_robot  = robot.posicion_robot()
    posicion_pelota = robot.posicion_pelota()
    distancia = calcular_distancia(posicion_robot, posicion_pelota)

    if distancia > DISTANCIA_CERCA:
        contador = 0
        return "caminar"

    # inclinamos levemente y preparamos la pierna
    robot.inclinarse(adelante=0.1, lateral=0.0)
    robot.preparar_patada(pierna="derecha", fuerza=1.0)
    contador += 1

    if contador >= ESPERA_PREPARAR:
        contador = 0
        return "patear"

    return "preparar"


# -----------------------------------------------
# TAREA 7: EJECUTAR LA PATADA
# -----------------------------------------------

def fase_patear(robot):
    torso = robot.estado_torso()

    # si esta cayendo no pateamos
    if robot_cayendo(torso):
        robot.pararse()
        return "detectar"

    # verificamos que seguimos en zona de golpe
    posicion_robot  = robot.posicion_robot()
    posicion_pelota = robot.posicion_pelota()
    distancia = calcular_distancia(posicion_robot, posicion_pelota)

    if distancia > DISTANCIA_CERCA:
        return "caminar"

    # ejecutamos la patada
    robot.patear(pierna="derecha", potencia=1.0)

    return "recuperar"


# -----------------------------------------------
# TAREA 8: RECUPERAR POSTURA
# -----------------------------------------------

def fase_recuperar(robot):
    global contador

    # volvemos a postura estable despues de patear
    robot.pararse()
    contador += 1

    if contador >= ESPERA_RECUPERAR:
        contador = 0
        return "fin"

    return "recuperar"


# -----------------------------------------------
# FUNCION PRINCIPAL DE CONTROL
# el servidor llama a esta funcion repetidamente
# -----------------------------------------------

def control(robot):
    global fase, contador

    # tarea 1: inicializar
    if fase == "inicio":
        fase = fase_inicio(robot)

    # tarea 2, 3 y 4: detectar posiciones y decidir
    elif fase == "detectar":
        fase = fase_detectar(robot)

    # tarea 5: caminar hacia la pelota
    elif fase == "caminar":
        fase = fase_caminar(robot)

    # tarea 6: estabilizarse antes de preparar
    elif fase == "estabilizar":
        fase = fase_estabilizar(robot)

    # tarea 6: preparar la patada
    elif fase == "preparar":
        fase = fase_preparar(robot)

    # tarea 7: ejecutar la patada
    elif fase == "patear":
        fase = fase_patear(robot)

    # tarea 8: recuperar postura
    elif fase == "recuperar":
        fase = fase_recuperar(robot)

    # fin: no hacemos nada mas, la estrategia termino correctamente
    elif fase == "fin":
        pass
