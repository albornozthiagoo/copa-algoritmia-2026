# La Cancha Inteligente

**Desafio 3 - Copa de Algoritmia y Programacion UADE 2026**  
**Carreras de Informatica y Sistemas**

## Integrantes

- Lucas Abad
- Thiago Albornoz
- Valentino Sarniguette
- Gaston Trezeguet
- Valentin Zaccari

## 1. Descripcion general

El proyecto **La Cancha Inteligente** consiste en un simulador tactico desarrollado en Python. El programa representa una cancha de futbol mediante una matriz de **100 filas por 60 columnas**, donde se pueden cargar jugadores, obstaculos y distintas situaciones de juego.

El sistema permite analizar una jugada a partir de la ubicacion de los jugadores en la cancha. Entre sus funcionalidades principales se encuentran el movimiento de jugadores, el calculo de distancia a la pelota, la deteccion de pases posibles y la verificacion de camino libre al arco.

Ademas de cumplir con los requerimientos principales del desafio, el programa incorpora un menu interactivo, validaciones de datos, escenario de prueba automatico, reinicio de cancha y borrado de jugadores. Estas mejoras buscan facilitar el uso del sistema y permitir una evaluacion mas clara por parte del usuario o evaluador.

## 2. Requisitos

Para ejecutar el programa se necesita:

- Python 3 instalado.
- No se requieren librerias externas.
- El programa utiliza unicamente estructuras basicas de Python, como listas, diccionarios, funciones, condicionales y ciclos.

## 3. Como ejecutar el programa

El archivo principal debe ejecutarse desde una terminal o desde un entorno como Visual Studio Code.

```bash
python desafio_3.py
```

Al iniciar, el programa muestra un menu principal con las opciones disponibles.

## 4. Estructura general del programa

```text
BLOQUE 1  - Constantes y creacion de la cancha
BLOQUE 2  - Validaciones basicas
BLOQUE 3  - Creacion y posicionamiento de jugadores
BLOQUE 4  - Obstaculos
BLOQUE 5  - Movimiento de jugadores
BLOQUE 6  - Distancia a la pelota
BLOQUE 7  - Pases posibles
BLOQUE 8  - Camino libre al arco
BLOQUE 9  - Funciones de ingreso de datos
BLOQUE 10 - Opciones del submenu
BLOQUE 11 - Escenario de prueba
BLOQUE 12 - Menu
BLOQUE 13 - Inicio del programa
```

Esta separacion permite que cada parte del programa tenga una responsabilidad clara.

## 5. Representacion de la cancha

La cancha se representa mediante una matriz de **100 x 60**.

| Simbolo | Significado |
|---|---|
| `.` | Celda vacia |
| `A` | Jugador de Argentina |
| `B` | Jugador de Brasil |
| `X` | Obstaculo |

Las filas validas van de `0` a `99`.  
Las columnas validas van de `0` a `59`.

La cancha se crea inicialmente vacia. Esto significa que todas las posiciones comienzan con `.`.

## 6. Representacion de los jugadores

Cada jugador se representa mediante un diccionario de Python.

```python
{
    "nombre": nombre,
    "equipo": equipo,
    "fila": fila,
    "columna": columna,
    "rol": rol,
    "tiene_pelota": tiene_pelota
}
```

Ejemplo:

```python
{
    "nombre": "Messi",
    "equipo": "A",
    "fila": 50,
    "columna": 20,
    "rol": "delantero",
    "tiene_pelota": "S"
}
```

Los jugadores se almacenan dentro de un diccionario general llamado `jugadores`. Cada jugador recibe un numero identificador, lo que permite seleccionarlo facilmente desde el menu.

## 7. Equipos y roles validos

| Equipo | Significado |
|---|---|
| `A` | Argentina |
| `B` | Brasil |

Los roles validos son:

- `arquero`
- `defensor`
- `mediocampista`
- `delantero`

Si el usuario ingresa un equipo o rol invalido, el programa muestra un mensaje de error y vuelve a pedir el dato.

## 8. Funcionalidades principales

### 8.1 Crear cancha

La funcion `crear_cancha()` genera una matriz de 100 filas y 60 columnas. Cada celda se inicializa con `.`.

### 8.2 Agregar jugadores

El usuario puede agregar jugadores indicando nombre, equipo, fila, columna, rol y si tiene o no la pelota. El programa valida que el equipo sea valido, que el rol sea valido, que la posicion este dentro de la cancha, que la celda no este ocupada y que no haya mas de un jugador con pelota.

Si el jugador se agrega correctamente, se guarda en el diccionario de jugadores y se marca su posicion en la matriz con `A` o `B` segun el equipo.

### 8.3 Agregar obstaculos

El programa permite agregar obstaculos en la cancha mediante el simbolo `X`. Antes de agregar un obstaculo, valida que la posicion este dentro de los limites de la cancha y que la celda no este ocupada.

### 8.4 Mover jugadores

El usuario puede mover un jugador en cuatro direcciones: `arriba`, `abajo`, `izquierda` y `derecha`. Antes de moverlo, el programa verifica que la direccion sea valida, que el jugador no salga de la cancha y que la celda destino no este ocupada.

Si el movimiento es valido, el sistema limpia la posicion anterior con `.`, actualiza la fila y columna del jugador en su diccionario y marca la nueva posicion en la matriz con el equipo correspondiente.

### 8.5 Calcular distancia a la pelota

El programa busca al jugador que tiene la pelota y calcula la distancia Manhattan entre cada jugador y el portador de la pelota.

```python
abs(fila_jugador - fila_pelota) + abs(columna_jugador - columna_pelota)
```

El sistema muestra la distancia de cada jugador y tambien informa cual o cuales son los jugadores mas cercanos a la pelota. Para el calculo de jugador mas cercano, se excluye al jugador que ya posee la pelota, porque su distancia siempre seria `0`.

### 8.6 Detectar pases posibles

El programa analiza los pases posibles para el jugador que tiene la pelota.

Un pase se considera posible si ambos jugadores pertenecen al mismo equipo, estan en la misma fila o columna, no hay obstaculos entre ellos y no hay rivales entre ellos. Los companeros del mismo equipo no bloquean el pase.

El sistema solo detecta e informa los pases posibles. No ejecuta el pase ni cambia la posesion de la pelota, ya que la consigna solicita detectar posibilidades de pase, no simular la accion completa.

### 8.7 Detectar camino libre al arco

El programa analiza que delanteros tienen camino libre hacia el arco rival.

Para que un jugador tenga camino libre al arco debe tener rol `delantero`, estar en la mitad ofensiva y no tener rivales ni obstaculos en la misma fila hacia el arco.

| Equipo | Mitad ofensiva |
|---|---|
| Argentina `A` | Columnas 30 a 59 |
| Brasil `B` | Columnas 0 a 29 |

Argentina ataca hacia la derecha. Brasil ataca hacia la izquierda.

### 8.8 Listar jugadores

El programa permite listar todos los jugadores cargados. El listado muestra numero identificador, nombre, equipo, fila, columna, rol y si tiene pelota o no.

### 8.9 Borrar jugador

El sistema permite borrar un jugador seleccionado por numero. Al borrar un jugador, se elimina del diccionario, se libera su celda en la matriz y, si tenia la pelota, se informa que ya no hay pelota en juego.

### 8.10 Reiniciar cancha

El programa incluye una opcion para reiniciar la cancha. Al reiniciar, se crea una nueva matriz vacia, se eliminan todos los jugadores y se eliminan todos los obstaculos.

### 8.11 Mostrar cancha

El usuario puede imprimir la cancha completa en consola. Antes de mostrarla, el programa informa que la matriz tiene 100 filas y 60 columnas, ya que la salida puede ser extensa.

### 8.12 Escenario de prueba automatico

El programa incluye un escenario de prueba automatico para facilitar la evaluacion. Este escenario carga jugadores, obstaculos y una situacion tactica ya preparada.

Permite probar rapidamente distancias a la pelota, pase bloqueado por rival, pase posible entre companeros, camino al arco bloqueado por obstaculo y camino libre o no libre segun posicion y bloqueo.

## 9. Menu del sistema

Menu principal:

```text
========== MENU PRINCIPAL ==========
1 - Modo de uso
2 - Ejecutar cancha inteligente
3 - Acerca de
0 - Salir
```

Submenu del simulador:

```text
========== SIMULADOR DE CANCHA ==========
1 - Agregar jugador
2 - Agregar obstaculo
3 - Mover jugador
4 - Analizar jugada
5 - Listar jugadores
6 - Mostrar cancha
7 - Cargar escenario de prueba
8 - Reiniciar cancha
9 - Borrar jugador
0 - Volver
```

## 10. Validaciones implementadas

- Validacion de equipo: solo se acepta `A` o `B`.
- Validacion de rol: solo se aceptan roles definidos.
- Validacion de posicion dentro de la cancha.
- Validacion de celda libre antes de agregar jugador.
- Validacion de celda libre antes de agregar obstaculo.
- Validacion de pelota unica.
- Validacion de direccion para movimiento.
- Validacion de numeros enteros mediante `try/except`.
- Validacion de nombre no vacio.
- Cancelacion de carga de jugadores escribiendo `NO`.
- Impedimento de movimiento fuera de cancha.
- Impedimento de movimiento hacia celdas ocupadas.
- Control de analisis si no hay suficientes jugadores.
- Control de analisis si no hay jugador con pelota.
- Liberacion de celda al borrar un jugador.
- Aviso si se borra un jugador que tenia la pelota.

## 11. Casos de prueba recomendados

| Caso | Accion | Resultado esperado |
|---|---|---|
| 1 | Cargar escenario de prueba | Se cargan jugadores, obstaculos y jugada lista para analizar |
| 2 | Agregar jugador valido | El jugador se agrega y se marca en la cancha |
| 3 | Intentar superponer jugador | El programa rechaza la celda ocupada |
| 4 | Intentar duplicar pelota | El programa evita una segunda pelota en juego |
| 5 | Mover jugador fuera de cancha | El movimiento no se realiza |
| 6 | Mover jugador hacia celda ocupada | El movimiento se bloquea |
| 7 | Agregar obstaculo valido | La celda queda marcada con `X` |
| 8 | Analizar pase bloqueado | Se detecta bloqueo por rival u obstaculo |
| 9 | Analizar pase posible | Se informa el pase disponible |
| 10 | Analizar camino bloqueado | Se informa que el delantero no tiene camino libre |
| 11 | Borrar jugador | Se elimina el jugador y se libera la celda |
| 12 | Reiniciar cancha | Se borra la jugada y se vuelve a una cancha vacia |

### Caso de prueba rapido recomendado

```text
2 - Ejecutar cancha inteligente
7 - Cargar escenario de prueba
5 - Listar jugadores
4 - Analizar jugada
9 - Borrar jugador
8 - Reiniciar cancha
0 - Volver
0 - Salir
```

## 12. Decisiones de diseno

### Uso de matriz

Se eligio representar la cancha como una matriz porque la consigna trabaja con posiciones de fila y columna. Esta representacion permite ubicar jugadores y obstaculos de manera directa.

### Uso de diccionarios para jugadores

Cada jugador se representa como un diccionario porque esta estructura permite agrupar facilmente sus datos: nombre, equipo, posicion, rol y posesion de pelota.

Ademas, se utiliza un diccionario general con ID numerico para que el usuario pueda seleccionar jugadores desde el menu sin tener que escribir exactamente su nombre.

### Pelota como atributo del jugador

La pelota se representa mediante el campo `tiene_pelota`. Esta decision permite asociar directamente la pelota con un jugador especifico.

No se usa un simbolo independiente para la pelota en la matriz, ya que la pelota siempre comparte posicion con su portador.

### Menu interactivo

Se incorporo un menu interactivo para mejorar la experiencia del usuario y facilitar la evaluacion manual del programa.

### Escenario de prueba

Se agrego un escenario automatico para demostrar rapidamente las principales funcionalidades del sistema. Esta decision ayuda a que el evaluador pueda verificar el funcionamiento del programa sin cargar todos los datos manualmente.

### Borrado y reinicio

Se agregaron opciones para borrar jugadores y reiniciar la cancha. Estas funcionalidades permiten corregir errores de carga y probar nuevas jugadas de manera mas comoda.

## 13. Restricciones y aclaraciones

El programa no simula un partido completo. Representa una situacion puntual de juego sobre una cancha matricial.

El sistema detecta pases posibles, pero no ejecuta el pase ni cambia la posesion de la pelota. Esta decision se tomo porque el desafio solicita detectar si existen pases posibles, no simular una accion completa de pase.

La pelota no ocupa una celda propia en la matriz. Esta asociada al jugador que la posee.

## 14. Conclusion

El programa desarrollado cumple con los requerimientos principales del Desafio 3 mediante una solucion modular, validada e interactiva.

La cancha se representa mediante una matriz de 100 x 60, los jugadores mediante diccionarios y las funcionalidades se organizan en funciones especificas. El sistema permite cargar y mover jugadores, agregar obstaculos, calcular distancias, detectar pases posibles y analizar camino libre al arco.

Ademas, se agregaron mejoras de experiencia de usuario como menu interactivo, escenario de prueba, reinicio de cancha y borrado de jugadores. Estas mejoras permiten una evaluacion mas clara y facilitan el uso del sistema sin modificar el codigo fuente.
