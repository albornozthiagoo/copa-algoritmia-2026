# Prediccion de Penales - Copa UADE 2026
# Desafio 2

"""
BLOQUE 1
LECTURA Y APERTURA DEL ARCHIVO
"""

# creamos una funcion para abrir el archivo y poder leerlo

def lee_archivo(nombre_archivo):

    # creamos una variable error como una bandera de referencia para saber si el codigo anduvo o no
    # si el valor de error=0 significa que el archivo se abrio con exito

    error=0

    # creamos un try except para que en caso de que haya un error con el archivo no se rompa el programa y devuelva except

    try:

        # aca creamos una variable y le asignamos el archivo.txt. lo abrimos en modo lectura 'r' para poder leerlo
        archivo = open(nombre_archivo, "r")

        # leemos solamente la primera linea del archivo con readline()
        # si el archivo tiene mas lineas, no se toman en cuenta porque la consigna pide una sola secuencia
        # usamos strip() para eliminar el salto de linea y los espacios del principio y el final si hay

        datos_archivo = archivo.readline().strip()
        
        
        # cerramos el archivo.txt

        archivo.close()

        # devolvemos el valor de la variable donde recolectamos los datos leidos y tambien el valor de error de referencia

        return datos_archivo,error
    
    # creamos ahora el except que nos va ayudar a evitar que se rompa el programa en caso de error

    except FileNotFoundError:

        # creamos la variable de referencia error=1 
        # si error=1 significa que hubo un problema al abrir o leer el archivo.txt

        error=1
        
        print("No se encuentra el archivo: \nRecordá que debe ingresarse el archivo penales.txt")
        return None,error


"""
BLOQUE 1.1
VALIDACION DE LA SECUENCIA
"""   

# creamos una funcion para validar que la secuencia leida desde el archivo sea correcta
# el parametro secuencia va a ser el texto leido desde el archivo.txt
# la funcion devuelve error=0 si la secuencia es valida
# y devuelve error=1 si encuentra algun problema

def validar_secuencia(secuencia):

    # creamos una variable error como bandera
    # error=0 significa que la secuencia es valida
    # error=1 significa que la secuencia tiene algun problema

    error = 0

    # VALIDACION:

    # verificamos que la secuencia no este vacia
    # esto puede pasar si el archivo txt no tiene nada escrito

    if secuencia == "":

        print("Error: el archivo se encuentra vacio")
        print("Si no sabe como llenarlo puede acceder al Modo de uso desde el menu")

        error = 1

    # VALIDACION:

    # verificamos que la cantidad de penales este entre 1 y 1000
    # len(secuencia) cuenta cuantos caracteres tiene la secuencia
    # 1 y 1000 son valores validos, por eso el error es menor a 1 o mayor a 1000

    elif len(secuencia) < 1 or len(secuencia) > 1000:

        print("Error: la secuencia debe tener entre 1 y 1000 penales.")

        error = 1

    else:

        # VALIDACION:

        # verificamos que todos los caracteres de la secuencia sean validos
        # la consigna solo permite las letras L, R y C
        # si aparece un numero, espacio, simbolo, minuscula o una letra distinta, marcamos error

        # usamos i como posicion inicial para recorrer la secuencia desde el primer caracter
        i = 0

        # recorremos la secuencia mientras no lleguemos al final
        # y mientras no se haya detectado ningun error
        # de esta forma, si aparece un caracter invalido, el while se corta

        while i < len(secuencia) and error == 0:

            # secuencia[i] representa el caracter actual que estamos revisando
            # con if preguntamos si el caracter esta fuera de los valores permitidos

            if secuencia[i] not in "LRC":

                print("Error: se detectaron caracteres fuera de lo permitido.")
                print("La secuencia solo puede contener L, R y C en mayusculas.")
                print("Verifique que no haya numeros, espacios, minusculas o letras invalidas.")
                print("Puede consultar el modo de uso desde el menu.")

                error = 1

            # avanzamos a la siguiente posicion de la secuencia

            i = i + 1

    # devolvemos una sola vez el valor de error al final de la funcion
    # si error=0, la secuencia es valida
    # si error=1, la secuencia tiene algun problema

    return error


"""
BLOQUE 2
PROCESAMIENTO Y CONTEO DE DIRECCIONES
"""

# creamos una funcion ahora para realizar el conteo de cada direccion
# el parametro secuencia va ser los datos leidos del archivo.txt

def contar_direcciones(secuencia):
    # creamos un contador para cada direccion
    contador_l = 0
    contador_r = 0
    contador_c = 0

    # creamos un for para leer todos los datos posicion por posicion y verificar cada direccion
    # gracias al range(len()) podemos repetir i 10 veces (del 0 al 9) en donde cada repeticion va tomar una posicion diferente por ende una direccion diferente

    for i in range(len(secuencia)):

        # ahora verificamos que posicion toma i en cada repeticion y vamos sumando al contador de direccion correspondiente

        if secuencia[i] == "L":
            contador_l += 1
        elif secuencia[i] == "R":
            contador_r += 1
        elif secuencia[i] == "C":
            contador_c += 1

    # finalmente devolvemos todos los valores de los contadores

    return contador_l, contador_r, contador_c


"""
BLOQUE 3
ANALISIS Y DETERMINACION DE RESULTADOS
"""

# creamos una funcion para saber cual es la direccion mas dominante de las tres

def direccion_dominante(contador_l, contador_r, contador_c):

    # Prioridad en empate: L > R > C
    # Se chequea primero L, luego R, luego C
    # asi si empatan L gana sobre R, y R gana sobre C

    mejor_dir   = "L"
    mejor_count = contador_l

    if contador_r > mejor_count:
        mejor_dir   = "R"
        mejor_count = contador_r

    if contador_c > mejor_count:
        mejor_dir   = "C"
        mejor_count = contador_c

    return mejor_dir, mejor_count

"""
BLOQUE 4
EJECUCION DE LA PREDICCION
"""

# creamos una funcion que se encarga de ejecutar la prediccion de penales
# esta funcion coordina la lectura del archivo, la validacion de la secuencia,
# el conteo de direcciones, el calculo de la direccion dominante y la salida final

def ejecutar_prediccion():

    # asignamos a la variable archivo el nombre del archivo txt
    # como usamos solo "penales.txt", el archivo debe estar en la misma carpeta que el programa
    archivo = "penales.txt"

    # creamos dos variables y le asignamos los valores de la funcion lee_archivo
    # secuencia guarda los datos leidos del archivo
    # error sirve como bandera para saber si hubo un problema al leer el archivo
    secuencia, error = lee_archivo(archivo)

    # preguntamos si la variable error es distinta de 1
    # si error es distinto de 1 significa que el archivo se leyo correctamente
    if error != 1:

        # validamos que la secuencia tenga datos correctos antes de contar las direcciones
        error_secuencia = validar_secuencia(secuencia)

        # si error_secuencia es distinto de 1, significa que la secuencia es valida
        # recien ahi hacemos el conteo y buscamos la direccion dominante
        if error_secuencia != 1:
            contador_l, contador_r, contador_c = contar_direcciones(secuencia)
            direccion, cantidad = direccion_dominante(contador_l, contador_r, contador_c)

            # mostramos la salida final pedida por la consigna:
            # primera linea: direccion dominante
            # segunda linea: cantidad de apariciones
            print(direccion)
            print(cantidad)


# funcion para "limpiar" la pantalla
# imprime varios saltos de linea para que el menu se vea mas ordenado

def borrar_pantalla():

    print("\n" * 50)


"""
BLOQUE 5
INTERFAZ DE USUARIO Y MENU PRINCIPAL
"""

# creamos una funcion para mostrar el menu principal
# desde este menu el usuario puede ver el modo de uso,
# ejecutar la prediccion, ver informacion del proyecto o salir

def mostrar_menu():

    # inicializamos menu_seleccion en -1 para poder entrar al while
    # usamos -1 porque es distinto de 0, entonces el menu se ejecuta al menos una vez

    menu_seleccion = -1

    # mientras el usuario no ingrese 0, el menu seguira ejecutandose
    # la opcion 0 se usa para salir del programa

    while menu_seleccion != 0:

        # mostramos las opciones disponibles para el usuario

        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Modo de uso")
        print("2 - Ejecutar prediccion")
        print("3 - Acerca de")
        print("0 - Salir")

        # pedimos al usuario que ingrese una opcion del menu
        # usamos try/except porque int() puede fallar si el usuario escribe una letra,
        # deja el campo vacio o ingresa cualquier dato que no pueda convertirse a numero

        try:
            menu_seleccion = int(input("\nIngrese una opcion: "))
        
        except ValueError:

            # si el usuario no ingresa un numero valido, limpiamos la pantalla
            # mostramos un mensaje de error y usamos continue para volver al inicio del while
            # de esta forma evitamos que el programa se rompa o que siga evaluando opciones invalidas

            borrar_pantalla()
            print("La opcion ingresada no es valida. Debe ingresar un numero de las opciones del menu.")
            continue
        
        # si el usuario ingresa 1, mostramos las instrucciones de uso del programa

        if menu_seleccion == 1:

            borrar_pantalla()

            print("\n========== MODO DE USO ==========\n")

            # explicamos como debe llamarse el archivo, donde debe ubicarse
            # y que caracteres se pueden utilizar en la secuencia

            print("1. Crear un archivo llamado penales.txt")
            print("2. Colocar el archivo en la misma carpeta del programa")
            print("3. Ingresar una secuencia utilizando:")
            print("   L = izquierda")
            print("   R = derecha")
            print("   C = centro")
            print("4. Ejecutar la opcion 2 del menu")

            print("\nEjemplo de archivo:\n")

            print("LRRCLRRLLR")

        # si el usuario ingresa 2, ejecutamos la prediccion de penales

        elif menu_seleccion == 2:

            borrar_pantalla()

            print("\n========== RESULTADO ==========\n")

            # llamamos a ejecutar_prediccion(), que se encarga de leer el archivo,
            # validar la secuencia, contar direcciones,
            # calcular la direccion dominante e imprimir el resultado

            ejecutar_prediccion()

        # si el usuario ingresa 3, mostramos informacion general del proyecto

        elif menu_seleccion == 3:

            borrar_pantalla()

            print("\n========== ACERCA DE ==========\n")

            print("Proyecto realizado para la Copa de Algoritmia y Programacion UADE 2026.\n")

            print("Integrantes del equipo:")
            print("- Lucas Abad")
            print("- Thiago Albornoz")
            print("- Valentino Sarniguette")
            print("- Gaston Trezeguet")
            print("- Valentin Zaccari")

            

            print("""        ___________
       '._==_==_=_.'
       .-\\:      /-.
      |   \\     /   |
       \\   \\   /   /
        '.  \\ /  .'
          '-._.-'
            | |
           _| |_
          '-----'""")
    
        # si el usuario ingresa 0, se corta el ciclo porque menu_seleccion deja de ser distinto de 0

        elif menu_seleccion == 0:

            borrar_pantalla()

            print("Saliendo del programa...")

        # si el usuario ingresa un numero que no corresponde a ninguna opcion,
        # mostramos un mensaje de error y el while vuelve a mostrar el menu

        else:

            borrar_pantalla()

            print("La opcion ingresada no existe. Por favor, ingresar una opcion valida.")


# este bloque indica el punto de inicio del programa
# si este archivo se ejecuta directamente, se llama a mostrar_menu()
# esto deja el codigo mas ordenado y evita ejecutar el menu automaticamente si el archivo fuera importado desde otro programa

if __name__ == "__main__":
    mostrar_menu()
