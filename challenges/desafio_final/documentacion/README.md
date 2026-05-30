# ⚽ Desafío 4 — El Robot Goleador

> **Copa de Algoritmia y Programación · UADE 2026**
> Estrategia de control para el robot humanoide **G1**: localizar la pelota, aproximarse con estabilidad y ejecutar una patada hacia el arco rival.

---

## 📑 Índice

- [Descripción general](#-descripción-general)
- [Archivos del proyecto](#-archivos-del-proyecto)
- [Cómo funciona la evaluación](#-cómo-funciona-la-evaluación)
- [La máquina de estados](#-la-máquina-de-estados)
- [Constantes](#-constantes)
- [Variables globales de estado](#-variables-globales-de-estado)
- [Funciones auxiliares](#-funciones-auxiliares)
- [Funciones de fase](#-funciones-de-fase)
- [Función principal `control(robot)`](#-función-principal-controlrobot)
- [API del robot que usa la estrategia](#-api-del-robot-que-usa-la-estrategia)
- [Cómo probarlo localmente](#-cómo-probarlo-localmente)
- [Notas y advertencias](#-notas-y-advertencias)

---

## 🎯 Descripción general

El robot **no recibe una secuencia fija de movimientos**. En cada llamada observa el entorno y decide qué hacer. La estrategia resuelve el problema con una **máquina de estados**: cada "fase" representa una etapa de la jugada, y al terminar una fase se decide cuál sigue.

El recorrido normal de la jugada es:

```
acercarse → estabilizar → preparar → patear → recuperar → final
```

En cualquier momento, si el robot detecta que **se está cayendo**, prioriza recuperar el equilibrio antes de seguir.

---

## 📁 Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `CodigoPrincipal.py` | Archivo de entrega. Contiene la función `control(robot)` y toda la lógica de la estrategia. Es el único archivo que se sube al simulador oficial. |
| `simulacion_robot.py` | Simulación visual en terminal. Importa `CodigoPrincipal` y lo ejecuta con un robot falso. No se entrega. |

Para correr la simulación ambos archivos deben estar en la **misma carpeta**:

```bash
python simulacion_robot.py
```

---

## ⚙️ Cómo funciona la evaluación

- La entrega es **un único archivo `.py`** que define **obligatoriamente** la función `control(robot)`.
- El simulador oficial **llama a `control(robot)` muchas veces** durante la ejecución. Ese es el "reloj" del programa.
- Por eso `control()` hace **una sola acción por llamada y termina**: el avance en el tiempo lo da la repetición, no un bucle interno.
- **No se usa** `input()`, ni `time.sleep()`, ni bucles infinitos, ni librerías externas. Solo Python estándar.
- El estado entre llamadas se conserva con **variables globales** (`fase`, contadores, `pateado`).

---

## 🔄 La máquina de estados

```mermaid
stateDiagram-v2
    [*] --> acercarse
    acercarse --> acercarse: distancia > 0.35
    acercarse --> estabilizar: distancia ≤ 0.35
    estabilizar --> estabilizar: ciclos < 3
    estabilizar --> preparar: ciclos ≥ 3
    estabilizar --> acercarse: pelota se alejó (> 0.70)
    preparar --> preparar: ciclos ≤ 4
    preparar --> patear: ciclos > 4
    preparar --> acercarse: pelota se alejó (> 0.70)
    patear --> recuperar: patea (una sola vez)
    patear --> acercarse: pelota se alejó (> 0.35)
    recuperar --> recuperar: ciclos < 5
    recuperar --> final: ciclos ≥ 5
    final --> [*]
```

> 🛑 **Regla transversal:** desde *cualquier* fase, si el robot está cayendo, se ejecuta `pararse()` y la fase **no cambia** (se reintenta en la próxima llamada). Esto se logra porque las funciones de fase devuelven `None` cuando el robot cae, y `control()` solo actualiza la fase cuando el retorno **no** es `None`.

---

## 🔢 Constantes

| Constante | Valor | Para qué sirve |
|---|---|---|
| `DISTANCIA_PATADA` | `0.35` | Distancia horizontal a la que se considera que el robot está en **zona de golpe**. |
| `DISTANCIA_CERCA` | `0.70` | Umbral de "cerca": dentro de este radio el robot camina **lento**; fuera, camina **rápido**. |
| `VELOCIDAD_RAPIDA` | `1.0` | Velocidad de caminata cuando la pelota está lejos. |
| `VELOCIDAD_LENTA` | `0.4` | Velocidad reducida al estar cerca, para no pasarse de largo ni perder estabilidad. |
| `CICLOS_ESTABILIZAR` | `3` | Cuántas llamadas se queda quieto estabilizándose antes de preparar la patada. |
| `CICLOS_PREPARACION` | `4` | Cuántas llamadas dura la fase de preparación. Los primeros 2 ciclos el robot se para quieto; los siguientes ejecutan `inclinarse()` y `preparar_patada()`. |
| `CICLOS_RECUPERACION` | `5` | Cuántas llamadas se queda recuperando postura después de patear. |

---

## 🧠 Variables globales de estado

Se conservan entre las múltiples llamadas a `control()`:

| Variable | Valor inicial | Significado |
|---|---|---|
| `fase` | `"acercarse"` | Fase actual de la máquina de estados. |
| `contador_estabilizar` | `0` | Lleva la cuenta de ciclos en la fase *estabilizar*. |
| `contador_preparacion` | `0` | Lleva la cuenta de ciclos en la fase *preparar*. |
| `contador_recuperacion` | `0` | Lleva la cuenta de ciclos en la fase *recuperar*. |
| `pateado` | `False` | Evita patear más de una vez por jugada. |

---

## 🧩 Funciones auxiliares

### `calcular_distancia_horizontal(posicion_robot, posicion_pelota)`

Calcula la distancia horizontal entre robot y pelota usando **solo x e y** (ignora la altura `z`).

**Parámetros**

| Parámetro | Tipo | Descripción |
|---|---|---|
| `posicion_robot` | tupla `(x, y, z)` | Posición actual del robot. |
| `posicion_pelota` | tupla `(x, y, z)` | Posición actual de la pelota. |

**Retorna:** una tupla `(distancia, dx, dy)`, donde
`dx = pelota_x − robot_x`, `dy = pelota_y − robot_y` y `distancia = √(dx² + dy²)`.

---

### `verificar_estado_y_obtener_datos(robot)`

Función "todo en uno" que combina las Tareas 1 a 4: chequea estabilidad y, si está estable, junta los datos del entorno.

**Comportamiento**

1. Lee `robot.estado_torso()` y toma la bandera `cayendo` accediendo con `torso["cayendo"]` (diccionario).
2. Si está cayendo → ejecuta `robot.pararse()` y devuelve `None`.
3. Si está estable → lee posiciones y calcula la distancia.

**Parámetros**

| Parámetro | Tipo | Descripción |
|---|---|---|
| `robot` | objeto del simulador | Expone los métodos del desafío. |

**Retorna**

- `None` si el robot está cayendo.
- En caso contrario, la tupla `(posicion_robot, posicion_pelota, distancia, dx, dy)`.

---

### `decidir_fase_por_distancia(distancia)`

Decide la siguiente fase comparando la distancia contra `DISTANCIA_PATADA`.

**Parámetros**

| Parámetro | Tipo | Descripción |
|---|---|---|
| `distancia` | número | Distancia horizontal a la pelota. |

**Retorna:** `"acercarse"` si la pelota está lejos, `"estabilizar"` si ya está en zona de patada.

> ℹ️ **Nota:** esta función documenta la lógica de decisión pero no se llama directamente en el flujo actual ya que esa decisión está inline dentro de `fase_acercarse`.

---

## 🦿 Funciones de fase

Todas reciben el objeto `robot` y devuelven el **nombre de la próxima fase** (o `None` si el robot estaba cayendo, para que la fase no cambie).

### `fase_acercarse(robot)` — Tarea 5

Camina hacia la pelota. Usa `VELOCIDAD_LENTA` si está dentro de `DISTANCIA_CERCA`, `VELOCIDAD_RAPIDA` si está más lejos. Cuando llega a `DISTANCIA_PATADA`, llama a `pararse()` y pasa a estabilizar.

| Retorno | Cuándo |
|---|---|
| `None` | El robot estaba cayendo. |
| `"estabilizar"` | Ya llegó a zona de patada (`distancia ≤ DISTANCIA_PATADA`). |
| `"acercarse"` | Debe seguir caminando. |

---

### `fase_estabilizar(robot)` — Tarea 6 (parte 1)

Mantiene al robot quieto con `pararse()` durante `CICLOS_ESTABILIZAR` llamadas. Resetea el contador si el robot cae o si la pelota se aleja.

| Retorno | Cuándo |
|---|---|
| `None` | El robot estaba cayendo (resetea contador). |
| `"acercarse"` | La pelota volvió a quedar lejos (`> DISTANCIA_CERCA`, resetea contador). |
| `"estabilizar"` | Sigue contando ciclos. |
| `"preparar"` | Completó `CICLOS_ESTABILIZAR` (resetea contador). |

---

### `fase_preparar_patada(robot)` — Tarea 6 (parte 2)

Divide la preparación en dos etapas dentro del mismo contador:
- Ciclos 1 y 2: llama a `pararse()` para asentarse.
- Ciclos 3 y 4: llama a `inclinarse(adelante=0.15, lateral=0.05)` y `preparar_patada(pierna="derecha", fuerza=0.8)`.
- Cuando supera `CICLOS_PREPARACION`: resetea y pasa a patear.

| Retorno | Cuándo |
|---|---|
| `None` | El robot estaba cayendo (resetea contador). |
| `"acercarse"` | La pelota quedó lejos (resetea contador). |
| `"preparar"` | Sigue preparando. |
| `"patear"` | Terminó la preparación (resetea contador). |

---

### `fase_patear(robot)` — Tarea 7

Ejecuta `patear(pierna="derecha", potencia=1.0)` **una sola vez** (controlado por `pateado`) y solo si sigue en zona de golpe. Si el robot cae durante esta fase, resetea `pateado` y `contador_recuperacion`.

| Retorno | Cuándo |
|---|---|
| `None` | El robot estaba cayendo (resetea `pateado` y `contador_recuperacion`). |
| `"acercarse"` | La pelota se alejó (`> DISTANCIA_PATADA`, resetea `pateado`). |
| `"recuperar"` | Pateó o ya había pateado. |

---

### `fase_recuperar(robot)` — Tarea 8

Llama a `pararse()` durante `CICLOS_RECUPERACION` llamadas para estabilizarse tras el golpe. No verifica estabilidad con `verificar_estado_y_obtener_datos` ya que en esta fase el robot solo necesita recuperarse.

| Retorno | Cuándo |
|---|---|
| `"recuperar"` | Sigue recuperando postura. |
| `"final"` | Completó `CICLOS_RECUPERACION` (resetea contador). |

---

## 🎮 Función principal `control(robot)`

Es la **única función obligatoria** de la entrega. El simulador la llama repetidamente. Funciona como un despachador: según la `fase` actual llama a la función correspondiente y actualiza la fase con el resultado.

```python
def control(robot):
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
```

**Punto clave:** la fase solo se actualiza si `nueva_fase` **no** es `None`. Así, cuando el robot se cae, se queda en la misma fase y la reintenta en la próxima llamada.

---

## 🤖 API del robot que usa la estrategia

| Método | Qué hace | Dónde se usa |
|---|---|---|
| `posicion_robot()` | Devuelve `(x, y, z)` del robot. | `verificar_estado_y_obtener_datos` |
| `posicion_pelota()` | Devuelve `(x, y, z)` de la pelota. | `verificar_estado_y_obtener_datos` |
| `estado_torso()` | Devuelve diccionario con clave `"cayendo"`. | chequeo de estabilidad |
| `pararse()` | Postura estable de pie con corrección de balance. | estabilizar, recuperar, recuperación de caídas |
| `caminar(velocidad)` | Camina con locomoción preentrenada. | `fase_acercarse` |
| `inclinarse(adelante, lateral)` | Inclina el torso para transferir peso. | `fase_preparar_patada` (ciclos 3 y 4) |
| `preparar_patada(pierna, fuerza)` | Carga la pierna para el golpe. | `fase_preparar_patada` (ciclos 3 y 4) |
| `patear(pierna, potencia)` | Ejecuta la extensión de la pierna. | `fase_patear` |

---

## 🧪 Cómo probarlo localmente

Se usa `simulacion_robot.py`, que contiene un **robot falso** que imita la API del simulador oficial. Ambos archivos deben estar en la misma carpeta.

```bash
# Mac / Linux
python3 simulacion_robot.py

# Windows
python simulacion_robot.py
```

La simulación muestra una cancha en la terminal con:

| Símbolo | Color | Significado |
|---|---|---|
| `R` | Azul | Robot estable |
| `R` | Rojo | Robot con inestabilidad detectada |
| `O` | Rojo | Pelota |
| `A` | Amarillo | Arco rival |
| `:` | Blanco | Línea del medio de la cancha |

El robot aparece en una **posición aleatoria en la mitad defensiva** en cada corrida. La pelota siempre arranca en el mismo lugar: mitad ofensiva, centro vertical. Durante el recorrido el robot puede sufrir **caídas aleatorias** que activan la recuperación antes de retomar el camino.

Solo se sube a Teams el archivo `CodigoPrincipal.py`.

---

## ⚠️ Notas y advertencias

- **Formato de `estado_torso()`:** el código accede a la bandera como `torso["cayendo"]` (diccionario). Si el simulador oficial devuelve una tupla en vez de un diccionario, esa línea hay que cambiarla por `torso[3]`. Es el punto más frágil de la estrategia.
- **Ciclos a ojo:** `CICLOS_ESTABILIZAR`, `CICLOS_PREPARACION` y `CICLOS_RECUPERACION` son valores elegidos manualmente. Si en las pruebas oficiales el robot patea inestable o se cae después del golpe, conviene subirlos.
- **`decidir_fase_por_distancia` sin uso directo:** está definida pero la decisión equivalente está inline en `fase_acercarse`. Se puede usar para refactorizar o se puede quitar sin afectar el comportamiento.
- **Coherencia de umbrales:** `fase_acercarse` salta a *estabilizar* con `≤ DISTANCIA_PATADA` (0.35), pero las demás fases vuelven a *acercarse* con `> DISTANCIA_CERCA` (0.70). El colchón entre 0.35 y 0.70 evita que el robot oscile entre fases por pequeños movimientos.
- **Inestabilidad en la simulación:** el robot falso genera caídas aleatorias cada 15 a 35 pasos caminados, con una recuperación de 6 a 14 iteraciones. Esto no afecta al archivo de entrega, es solo parte de la simulación visual.

---

*Documento generado para el repositorio `copa-algortimia-2026`, módulo `challenges/desafio_final/posicion`.*
