from os import system
import time

class Videojuego:
    nombre = None
    fecha_lanzamiento = None
    precio = 0.0
    disponible = False
    consola = None
    
    def __init__(self,nombre,fecha_lanzamiento,precio,disponible,consola):
        self.nombre = nombre
        self.fecha_lanzamiento = fecha_lanzamiento
        self.precio = precio
        self.disponible = disponible
        self.consola = consola

class Genero:
    nombre = None
    popularidad = None
    edad_minima = None
    jugabilidad = None
    videojuegos = []
    
    def __init__(self, nombre, popularidad, edad_minima, jugabilidad,videojuegos=[]): # self = this  Constructor
        self.nombre = nombre
        self.popularidad = popularidad
        self.edad_minima = edad_minima
        self.jugabilidad = jugabilidad
        self.videojuegos = videojuegos

def agregar_genero():
    try:
        path = "./generos.txt"
        archivo_abierto = open(path,'a')
        nuevo_Genero = Genero(input("Nombre del Género: "), input("Qué tan popular es: "),
                            int(input("Edad minima: ")),input("Jugabilidad: "))
        archivo_abierto.write(f"{nuevo_Genero.nombre};{nuevo_Genero.popularidad};{nuevo_Genero.edad_minima};{nuevo_Genero.jugabilidad};{nuevo_Genero.videojuegos}\n")
        archivo_abierto.close()
    except Exception as error:
        print(error)

def videojuego_genero(genero,nombre):
    try:
        path = "generos.txt"
        lectura = open(path,'r')
        lineas = lectura.readlines()
        lectura.close()
        valor = 0
        for linea in lineas:
            palabras = linea.split(";")
            for palabra in palabras:
                if palabra == genero:
                    valor = lineas.index(linea)
                    break
        escritura = open(path,'w')
        lineas[valor] = lineas[valor][:-2]+f" {nombre}]\n"
        escritura.writelines(lineas)
        escritura.close()
    except Exception as error:
        print(error)

def agregar_videojuego():
    try:
        path = "videojuegos.txt"
        archivo_abierto = open(path,'a')
        nuevo_Videojuego = Videojuego(input("Ingrese el nombre: "),input("Ingrese la fecha: ")
                                      ,float(input("Ingrese el precio: ")),bool(int(input("Disponible: "))),input("Consola: "))
        archivo_abierto.write(f"{nuevo_Videojuego.nombre};{nuevo_Videojuego.fecha_lanzamiento};{nuevo_Videojuego.precio};{nuevo_Videojuego.disponible};{nuevo_Videojuego.consola}\n")
        archivo_abierto.close()
    except Exception as error:
        print(error)
    genero = input("A qué categoria pertenece: ")
    videojuego_genero(genero,nuevo_Videojuego.nombre)

def modificar_genero():
    genero = input("Qué genero desea modificar: ")
    try:
        path = "generos.txt"
        lectura = open(path,'r')
        lineas = lectura.readlines()
        lectura.close()
        valor = 0
        for linea in lineas:
            palabras = linea.split(";")
            for palabra in palabras:
                if palabra == genero:
                    valor = lineas.index(linea)
                    break
        palabras = lineas[valor].split(";")
        print("\nCaracterísticas: ")
        for palabra in palabras:
            print(palabra+" ")
        modificar_Genero = Genero(palabras[0], input(f"Popularidad-{palabras[1]}: "),
                            input(f"Edad minima-{palabras[2]}: "),input(f"Jugabilidad-{palabras[3]}: "),palabras[4])
        escritura = open(path,'w')
        lineas[valor] = modificar_Genero.nombre+";"+modificar_Genero.popularidad+";"+str(modificar_Genero.edad_minima)+";"+modificar_Genero.jugabilidad+";"+palabras[4]
        escritura.writelines(lineas)
        escritura.close()
    except Exception as error:
        print(error)

def modificar_videojuego():
    videojuego = input("Qué videojuego desea modificar: ")
    try:
        path = "videojuegos.txt"
        lectura = open(path,'r')
        lineas = lectura.readlines()
        lectura.close()
        valor = 0
        for linea in lineas:
            palabras = linea.split(";")
            for palabra in palabras:
                if palabra == videojuego:
                    valor = lineas.index(linea)
                    break
        palabras = lineas[valor].split(";")
        print("\nCaracterísticas: ")
        for palabra in palabras:
            print(palabra+" ")
        modificar_Videojuego = Videojuego(palabras[0],input(f"Fecha-{palabras[1]}: ")
                                      ,float(input(f"Precio-{palabras[2]}: ")),bool(int(input(f"Disponible-{palabras[3]}: "))),
                                      input(f"Consola-{palabras[4][:-1]}: "))
        escritura = open(path,'w')
        lineas[valor] = modificar_Videojuego.nombre+";"+modificar_Videojuego.fecha_lanzamiento+";"+str(modificar_Videojuego.precio)+";"+str(modificar_Videojuego.disponible)+";"+modificar_Videojuego.consola+"\n"
        escritura.writelines(lineas)
        escritura.close()
    except Exception as error:
        print(error)

while True:
    print("\nBienvenido a mi programa\n")
    print("1. Genero")
    print("2. Videojuego")
    opcion = int(input("Elija una Opcion: "))
    if opcion == 1:
        system("cls")
        print("\nEste es el menu de Genero\n")
        print("1. Agregar nuevo Genero")
        print("2. Modificar Genero")
        print("3. Eliminar Genero")
        opcion2 = int(input("Elija una Opcion: "))
        if opcion2 == 1:
            print("\n")
            agregar_genero()
        elif opcion2 == 2:
            print("Modificar un Genero")
            modificar_genero()
        elif opcion2 == 3:
            print("Eliminar un Genero")

    elif opcion == 2:
        system("cls")
        print("\nEste es el menu de Videojuego\n")
        print("1. Agregar nuevo Videojuego")
        print("2. Modificar Videojuego")
        print("3. Eliminar Videojuego")
        opcion2 = int(input("Elija una Opcion: "))
        if opcion2 == 1:
            print("\n")
            agregar_videojuego()
        elif opcion2 == 2:
            print("\n")
            modificar_videojuego()
        elif opcion2 == 3:
            print("Eliminar un Videojuego")

    time.sleep(2)
    system("cls")