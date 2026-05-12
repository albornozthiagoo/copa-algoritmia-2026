seleccion=0
#Vector para los grupos ya creados
grupos_creados=[]
#Vector que indica los grupos totales
grupos_totales=["A","B","C","D","E","F","G","H","I","J","K","L"]
#Matriz para calcular los resultados del grupo A  ----- VER SI SE NECESITA
matriz_grupo_A=[]
#Creación de los equipos por grupo con sus puntajes y puestos
equipos_xgrupo=[{
    "grupo":"A",
    "equipo":"MEXICO",
    "puntos":"0",
    "puesto":"0",
},
{
    "grupo":"A",
    "equipo":"SUDAFRICA",
    "puntos":"0",
    "puesto":"0",
},{
    "grupo":"A",
    "equipo":"KOREA",
    "puntos":"0",
    "puesto":"0",
},{
    "grupo":"A",
    "equipo":"CHECOSLOVAQUIA",
    "puntos":"0",
    "puesto":"0",
}]
#Comprueba de si el grupo fue creado para luego preguntar si se quiere modificar o no 
def comprueba_grupo_creado(grupo,equipos_xgrupo):
    estado=""
    modificar=""
    for i in range(len(grupos_creados)):
        if grupo == grupos_creados[i]:
            estado="cargado"
    if estado == "cargado":
        modificar=input("Desea modificar la opción cargada?(y/n): ")
        while modificar!="Y" and modificar!="N":
            modificar=input("Ingrese 'y' o 'n': ")
        if modificar == "Y":
            partidos(grupo);
        else:
            print ("No se modificaran los datos")
    return estado
#Validacion que indica si el equipo esta en el grupo
def controlarequipo(equipo_local,grupo):
    estado="mal_equipo"
    for equipo in equipos_xgrupo:
        if equipo_local == equipo["equipo"]:
            estado="mal_grupo"
            if grupo == equipo["grupo"]:
                estado="correcto"
    return estado;
#Ingreso de los datos de los distintos partidos
def partidos(grupo):
    flag=""
    cont=0
    #Son 6 partidos acordarse de cambiarlo a 6 (Esta en 1 para pruebas)
    while cont !=1:
            #Ingresa datos del partido
            print("Ingrese partido N°"+ str(cont + 1) + ":")
            equipo_local=input("Ingrese primer equipo:")
            flag=controlarequipo(equipo_local,grupo)
            #Si la bandera es "mal_equipo" el equipo ingresado no está en el grupo
            while flag == "mal_equipo":
                equipo_local= input("El nombre ingresado no corresponde a ninguna selección, ingrese un nombre correcto:")
                flag=controlarequipo(equipo_local,grupo)
            #Ingresa cantidad de goles del primer equipo
            cant_goles_local = int(input ("Ingrese cantidad de goles locales:"))
            #Validación de datos de los goles
            while cant_goles_local < 0 or cant_goles_local > 20:
                cant_goles_local = int(input ("La cantidad ingresada debe ser entre 0 y 20:"))
            #Lo mismo para el 2° equipo
            equipo_visitante=input("Ingrese segundo equipo:")
            flag=controlarequipo(equipo_visitante,grupo)
            #También valida que no sea el mismo equipo que el que se ingreso primero
            while flag == "mal_equipo" or equipo_visitante == equipo_local:
                equipo_visitante= input("El nombre ingresado no corresponde a ninguna selección del grupo \n o ya ingreso ese equipo, ingrese un nombre correcto:")
                flag=controlarequipo(equipo_visitante,grupo)
            cant_goles_visitante = int(input ("Ingrese cantidad de goles locales:"))
            while cant_goles_visitante < 0 or cant_goles_visitante > 20:
                cant_goles_visitante = input ("La cantidad ingresada debe ser entre 0 y 20:")
            #Crea la Matriz para calcular los puestos y el puntaje
            #crearmatriz(grupo,equipo_local,equipo_visitante,cant_goles_local,cant_goles_visitante)
            cont += 1
#Funcion que muestra todos los equipos por grupo
def mostrar_listado_grupos(equipos_xgrupo):
    for i in equipos_xgrupo:
         print("GRUPO: " + i["grupo"] + " SELECCION: "+ i["equipo"])
#Funcion que muestra los grupos cargados y que faltan cargar
def grupos_cargados(grupos_creados):
    print("Grupos cargados:")
    for i in grupos_creados:
        print(i)

#Menú principal - Si Ingresa la letra de un grupo carga el grupo - Si ingresa la O muestra el listado total de equipos - La S los Grupos cargados (Falta mostrar los resultados con la R)
grupo=input ("Ingrese grupo de la A - L para cargar partidos\nO para mostrar el listado por grupos\nS para mostrar los grupos cargados\nX para finalizar: ")
while grupo!= "X":
    if grupo in grupos_totales:
        estado=comprueba_grupo_creado(grupo,equipos_xgrupo);
        if estado !="cargado":
            grupos_creados.append(grupo)
            partidos(grupo);
    if grupo == "O":
            mostrar_listado_grupos(equipos_xgrupo)
    if grupo == "S":
            grupos_cargados(grupos_creados)
    grupo=input ("Ingrese grupo de la A - L para cargar partidos\nO para mostrar el listado por grupos\nR para mostrar los grupos cargados\nX para finalizar: ")

    