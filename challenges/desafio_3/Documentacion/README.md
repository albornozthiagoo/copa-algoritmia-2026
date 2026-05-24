
🏟️ La Cancha Inteligente

Desafío 3 — Copa de Algoritmia y Programación UADE 2026
Carreras de Informática y Sistemas

⸻

Integrantes

* Lucas Abad
* Thiago Albornoz
* Valentino Sarniguette
* Gaston Trezeguet
* Valentin Zaccari

⸻

1. Descripción general

El proyecto La Cancha Inteligente consiste en un simulador táctico desarrollado en Python. El programa representa una cancha de fútbol mediante una matriz de 100 filas por 60 columnas, donde se pueden cargar jugadores, obstáculos y distintas situaciones de juego.

El sistema permite analizar una jugada a partir de la ubicación de los jugadores en la cancha. Entre sus funcionalidades principales se encuentran el movimiento de jugadores, el cálculo de distancia a la pelota, la detección de pases posibles y la verificación de camino libre al arco.

Además de cumplir con los requerimientos principales del desafío, el programa incorpora un menú interactivo, validaciones de datos, escenario de prueba automático, reinicio de cancha y borrado de jugadores. Estas mejoras buscan facilitar el uso del sistema y permitir una evaluación más clara por parte del usuario o evaluador.

⸻

2. Requisitos

Para ejecutar el programa se necesita:

* Python 3 instalado.
* No se requieren librerías externas.
* El programa utiliza únicamente estructuras básicas de Python, como listas, diccionarios, funciones, condicionales y ciclos.

⸻

3. Cómo ejecutar el programa

El archivo principal debe ejecutarse desde una terminal o desde un entorno como Visual Studio Code.

Ejemplo de ejecución:

python desafio_3.py

Al iniciar, el programa muestra un menú principal con las opciones disponibles.

⸻

4. Estructura general del programa

El programa está organizado en bloques funcionales:

BLOQUE 1  - Constantes y creación de la cancha
BLOQUE 2  - Validaciones básicas
BLOQUE 3  - Creación y posicionamiento de jugadores
BLOQUE 4  - Obstáculos
BLOQUE 5  - Movimiento de jugadores
BLOQUE 6  - Distancia a la pelota
BLOQUE 7  - Pases posibles
BLOQUE 8  - Camino libre al arco
BLOQUE 9  - Funciones de ingreso de datos
BLOQUE 10 - Opciones del submenú
BLOQUE 11 - Escenario de prueba
BLOQUE 12 - Menú
BLOQUE 13 - Inicio del programa

Esta separación permite que cada parte del programa tenga una responsabilidad clara.

⸻

5. Representación de la cancha

La cancha se representa mediante una matriz de 100 x 60.

Cada celda de la matriz puede contener uno de los siguientes símbolos:

Símbolo	Significado
.	Celda vacía
A	Jugador de Argentina
B	Jugador de Brasil
X	Obstáculo

Las filas válidas van de 0 a 99.
Las columnas válidas van de 0 a 59.

La cancha se crea inicialmente vacía. Esto significa que todas las posiciones comienzan con ".".

⸻

6. Representación de los jugadores

Cada jugador se representa mediante un diccionario de Python.

Estructura de un jugador:

{
    "nombre": nombre,
    "equipo": equipo,
    "fila": fila,
    "columna": columna,
    "rol": rol,
    "tiene_pelota": tiene_pelota
}

Ejemplo:

{
    "nombre": "Messi",
    "equipo": "A",
    "fila": 50,
    "columna": 20,
    "rol": "delantero",
    "tiene_pelota": "S"
}

Los jugadores se almacenan dentro de un diccionario general llamado jugadores. Cada jugador recibe un número identificador, lo que permite seleccionarlo fácilmente desde el menú.

Ejemplo:

jugadores = {
    1: {
        "nombre": "Messi",
        "equipo": "A",
        "fila": 50,
        "columna": 20,
        "rol": "delantero",
        "tiene_pelota": "S"
    }
}

⸻

7. Equipos y roles válidos

El programa acepta dos equipos:

Equipo	Significado
A	Argentina
B	Brasil

Los roles válidos son:

* arquero
* defensor
* mediocampista
* delantero

Si el usuario ingresa un equipo o rol inválido, el programa muestra un mensaje de error y vuelve a pedir el dato.

⸻

8. Funcionalidades principales

8.1 Crear cancha

La función crear_cancha() genera una matriz de 100 filas y 60 columnas.

Cada celda se inicializa con ".".

Esto permite comenzar la simulación con una cancha vacía.

⸻

8.2 Agregar jugadores

El usuario puede agregar jugadores indicando:

* Nombre.
* Equipo.
* Fila.
* Columna.
* Rol.
* Si tiene o no la pelota.

El programa valida que:

* El equipo sea válido.
* El rol sea válido.
* La posición esté dentro de la cancha.
* La celda no esté ocupada.
* No haya más de un jugador con pelota.

Si el jugador se agrega correctamente, se guarda en el diccionario de jugadores y se marca su posición en la matriz con "A" o "B" según el equipo.

⸻

8.3 Agregar obstáculos

El programa permite agregar obstáculos en la cancha mediante el símbolo "X".

Antes de agregar un obstáculo, se valida que:

* La posición esté dentro de los límites de la cancha.
* La celda no esté ocupada por un jugador u otro obstáculo.

⸻

8.4 Mover jugadores

El usuario puede mover un jugador en cuatro direcciones:

* arriba
* abajo
* izquierda
* derecha

Antes de realizar el movimiento, el programa verifica:

* Que la dirección ingresada sea válida.
* Que el jugador no salga de la cancha.
* Que la celda destino no esté ocupada.

Si el movimiento es válido, el sistema:

1. Limpia la posición anterior con ".".
2. Actualiza la fila y columna del jugador en su diccionario.
3. Marca la nueva posición en la matriz con el equipo correspondiente.

⸻

8.5 Calcular distancia a la pelota

El programa busca al jugador que tiene la pelota y calcula la distancia Manhattan entre cada jugador y el portador de la pelota.

La fórmula utilizada es:

abs(fila_jugador - fila_pelota) + abs(columna_jugador - columna_pelota)

El sistema muestra la distancia de cada jugador y también informa cuál o cuáles son los jugadores más cercanos a la pelota.

Para el cálculo de jugador más cercano, se excluye al jugador que ya posee la pelota, porque su distancia siempre sería 0.

⸻

8.6 Detectar pases posibles

El programa analiza los pases posibles para el jugador que tiene la pelota.

Un pase se considera posible si:

* Ambos jugadores pertenecen al mismo equipo.
* Están en la misma fila o en la misma columna.
* No hay obstáculos entre ellos.
* No hay rivales entre ellos.
* Los compañeros del mismo equipo no bloquean el pase.

El sistema solo detecta e informa los pases posibles. No ejecuta el pase ni cambia la posesión de la pelota, ya que la consigna solicita detectar posibilidades de pase, no simular la acción completa.

⸻

8.7 Detectar camino libre al arco

El programa analiza qué delanteros tienen camino libre hacia el arco rival.

Para que un jugador tenga camino libre al arco:

* Debe tener rol delantero.
* Debe estar en la mitad ofensiva.
* No debe haber rivales en la misma fila hacia el arco.
* No debe haber obstáculos en la misma fila hacia el arco.

Criterio de mitad ofensiva:

Equipo	Mitad ofensiva
Argentina A	Columnas 30 a 59
Brasil B	Columnas 0 a 29

Argentina ataca hacia la derecha.
Brasil ataca hacia la izquierda.

⸻

8.8 Listar jugadores

El programa permite listar todos los jugadores cargados.

El listado muestra:

* Número identificador.
* Nombre.
* Equipo.
* Fila.
* Columna.
* Rol.
* Si tiene pelota o no.

Esto permite seleccionar jugadores fácilmente para moverlos o borrarlos.

⸻

8.9 Borrar jugador

El sistema permite borrar un jugador seleccionado por número.

Al borrar un jugador:

* Se elimina del diccionario de jugadores.
* Se libera su celda en la matriz, volviéndola ".".
* Si el jugador tenía la pelota, el sistema informa que ya no hay pelota en juego.

Esta opción permite corregir errores de carga sin reiniciar toda la cancha.

⸻

8.10 Reiniciar cancha

El programa incluye una opción para reiniciar la cancha.

Al reiniciar:

* Se crea una nueva matriz vacía.
* Se eliminan todos los jugadores.
* Se eliminan todos los obstáculos.

Esta opción permite comenzar una nueva jugada sin cerrar el programa.

⸻

8.11 Mostrar cancha

El usuario puede imprimir la cancha completa en consola.

Antes de mostrarla, el programa informa que la matriz tiene 100 filas y 60 columnas, ya que la salida puede ser extensa.

⸻

8.12 Escenario de prueba automático

El programa incluye un escenario de prueba automático para facilitar la evaluación.

Este escenario carga jugadores, obstáculos y una situación táctica ya preparada. Permite probar rápidamente:

* Distancias a la pelota.
* Pase bloqueado por rival.
* Pase posible entre compañeros.
* Camino al arco bloqueado por obstáculo.
* Camino libre o no libre según posición y bloqueo.

El escenario de prueba reemplaza la cancha actual por un escenario automático.

⸻

9. Menú del sistema

Al iniciar el programa, se muestra el menú principal:

========== MENU PRINCIPAL ==========
1 - Modo de uso
2 - Ejecutar cancha inteligente
3 - Acerca de
0 - Salir

Al ingresar al simulador, se muestra el siguiente submenú:

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

Esta estructura permite utilizar el programa sin modificar el código fuente.

⸻

10. Validaciones implementadas

El programa incorpora distintas validaciones para evitar errores de uso y mantener la consistencia de la simulación.

Validaciones principales:

* Validación de equipo: solo se acepta A o B.
* Validación de rol: solo se aceptan roles definidos.
* Validación de posición dentro de la cancha.
* Validación de celda libre antes de agregar jugador.
* Validación de celda libre antes de agregar obstáculo.
* Validación de pelota única.
* Validación de dirección para movimiento.
* Validación de números enteros mediante try/except.
* Validación de nombre no vacío.
* Cancelación de carga de jugadores escribiendo NO.
* Impedimento de movimiento fuera de cancha.
* Impedimento de movimiento hacia celdas ocupadas.
* Control de análisis si no hay suficientes jugadores.
* Control de análisis si no hay jugador con pelota.
* Liberación de celda al borrar un jugador.
* Aviso si se borra un jugador que tenía la pelota.

⸻

11. Casos de prueba recomendados

Caso 1: cargar escenario automático

Pasos:

2 - Ejecutar cancha inteligente
7 - Cargar escenario de prueba
5 - Listar jugadores
4 - Analizar jugada

Resultado esperado:

* Se cargan jugadores y obstáculos.
* Se muestra el listado de jugadores.
* Se calculan distancias a la pelota.
* Se detectan pases posibles.
* Se analiza camino libre al arco.

⸻

Caso 2: agregar jugador válido

Datos de prueba:

Nombre: Messi
Equipo: A
Fila: 50
Columna: 20
Rol: delantero
Pelota: S

Resultado esperado:

* El jugador se agrega correctamente.
* La pelota queda asignada a Messi.
* La celda correspondiente queda marcada con A.

⸻

Caso 3: evitar superposición

Pasos:

* Agregar un jugador en una posición válida.
* Intentar agregar otro jugador en la misma fila y columna.

Resultado esperado:

* El programa informa que la celda ya está ocupada.
* No se agrega el segundo jugador en esa posición.

⸻

Caso 4: controlar pelota única

Pasos:

* Agregar un jugador con pelota.
* Agregar un segundo jugador.

Resultado esperado:

* El segundo jugador no puede recibir la pelota si ya existe un jugador con pelota.

⸻

Caso 5: mover jugador fuera de cancha

Pasos:

* Agregar un jugador en la fila 0.
* Intentar moverlo hacia arriba.

Resultado esperado:

* El programa informa que el jugador no puede salir de la cancha.
* La posición no se modifica.

⸻

Caso 6: mover jugador hacia celda ocupada

Pasos:

* Agregar dos jugadores en posiciones cercanas.
* Intentar mover uno hacia la celda del otro.

Resultado esperado:

* El programa informa que la celda destino está ocupada.
* El movimiento no se realiza.

⸻

Caso 7: agregar obstáculo

Pasos:

2 - Agregar obstaculo
Fila: 40
Columna: 50

Resultado esperado:

* El obstáculo se agrega correctamente.
* La celda queda marcada con X.

⸻

Caso 8: pase bloqueado

Ejemplo del escenario de prueba:

Messi A en (50, 20)
Otamendi A en (50, 10)
Neymar B en (50, 15)

Resultado esperado:

* El pase de Messi hacia Otamendi queda bloqueado porque Neymar se encuentra entre ambos.

⸻

Caso 9: pase posible

Ejemplo del escenario de prueba:

Messi A en (50, 20)
Di Maria A en (50, 30)

Resultado esperado:

* El programa informa que existe pase posible hacia Di María.

⸻

Caso 10: camino al arco bloqueado

Ejemplo del escenario de prueba:

Julian A en (40, 45)
Obstaculo X en (40, 50)

Resultado esperado:

* Julián no tiene camino libre al arco porque hay un obstáculo en la misma fila hacia el arco rival.

⸻

Caso 11: borrar jugador

Pasos:

5 - Listar jugadores
9 - Borrar jugador

Resultado esperado:

* El jugador seleccionado se elimina del diccionario.
* Su celda queda vacía en la matriz.
* Si tenía pelota, el sistema informa que ya no hay pelota en juego.

⸻

Caso 12: reiniciar cancha

Pasos:

8 - Reiniciar cancha
5 - Listar jugadores

Resultado esperado:

* Se eliminan jugadores y obstáculos.
* El listado de jugadores queda vacío.
* La cancha vuelve a estar inicializada con ".".

⸻

12. Decisiones de diseño

Uso de matriz

Se eligió representar la cancha como una matriz porque la consigna trabaja con posiciones de fila y columna. Esta representación permite ubicar jugadores y obstáculos de manera directa.

Uso de diccionarios para jugadores

Cada jugador se representa como un diccionario porque esta estructura permite agrupar fácilmente sus datos: nombre, equipo, posición, rol y posesión de pelota.

Además, se utiliza un diccionario general con ID numérico para que el usuario pueda seleccionar jugadores desde el menú sin tener que escribir exactamente su nombre.

Pelota como atributo del jugador

La pelota se representa mediante el campo "tiene_pelota". Esta decisión permite asociar directamente la pelota con un jugador específico.

No se usa un símbolo independiente para la pelota en la matriz, ya que la pelota siempre comparte posición con su portador.

Menú interactivo

Se incorporó un menú interactivo para mejorar la experiencia del usuario y facilitar la evaluación manual del programa.

Gracias al menú, el usuario puede cargar jugadores, obstáculos, mover jugadores y analizar jugadas sin modificar el código.

Escenario de prueba

Se agregó un escenario automático para demostrar rápidamente las principales funcionalidades del sistema. Esta decisión ayuda a que el evaluador pueda verificar el funcionamiento del programa sin cargar todos los datos manualmente.

Borrado y reinicio

Se agregaron opciones para borrar jugadores y reiniciar la cancha. Estas funcionalidades permiten corregir errores de carga y probar nuevas jugadas de manera más cómoda.

⸻

13. Restricciones y aclaraciones

El programa no simula un partido completo. Representa una situación puntual de juego sobre una cancha matricial.

El sistema detecta pases posibles, pero no ejecuta el pase ni cambia la posesión de la pelota. Esta decisión se tomó porque el desafío solicita detectar si existen pases posibles, no simular una acción completa de pase.

La pelota no ocupa una celda propia en la matriz. Está asociada al jugador que la posee.

⸻

14. Conclusión

El programa desarrollado cumple con los requerimientos principales del Desafío 3 mediante una solución modular, validada e interactiva.

La cancha se representa mediante una matriz de 100 x 60, los jugadores mediante diccionarios y las funcionalidades se organizan en funciones específicas. El sistema permite cargar y mover jugadores, agregar obstáculos, calcular distancias, detectar pases posibles y analizar camino libre al arco.

Además, se agregaron mejoras de experiencia de usuario como menú interactivo, escenario de prueba, reinicio de cancha y borrado de jugadores. Estas mejoras permiten una evaluación más clara y facilitan el uso del sistema sin modificar el código fuente.
