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
    print("Se ha agregado el nuevo genero")
    system("Pause")

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
    print("Se ha agregado el nuevo videojuego")
    system("Pause")

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
    print(f"Se ha modificado el genero {genero}")
    system("Pause")

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
    print(f"Se ha modificado el videojuego {videojuego}")
    system("Pause")

def eliminar_genero():
    genero = input("Qué genero desea eliminar: ")
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
        print("\nCaracterísticas: ")
        for palabra in palabras:
            print(palabra+" ")
        lineas.pop(valor)
        escritura = open(path,'w')
        escritura.writelines(lineas)
        escritura.close()
    except Exception as error:
        print(error)
    print(f"Se ha eliminado el genero {genero}")
    system("Pause")

def eliminar_videojuego():
    videojuego = input("Qué videojuego desea Eliminar: ")
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
        print("\nCaracterísticas: ")
        for palabra in palabras:
            print(palabra+" ")
        lineas.pop(valor)
        escritura = open(path,'w')
        escritura.writelines(lineas)
        escritura.close()
    except Exception as error:
        print(error)
    print(f"Se ha eliminado el videojuego {videojuego}")
    system("Pause")
    

def mostrar_generos():
    try:
        path = "generos.txt"
        lectura = open(path,'r')
        lineas = lectura.readlines()
        lectura.close()
        generos = []
        for linea in lineas:
            palabras = linea.split(";")
            generos.append(Genero(palabras[0],palabras[1],palabras[2],palabras[3],palabras[4]))
        print("\nLista de Género")
        for genero in generos:
            print("Nombre: "+genero.nombre+"\tPopularidad: "+genero.popularidad+
                "\tEdad mínima: "+genero.edad_minima+"\tJugabilidad:"+genero.jugabilidad+
                "\tJuegos: "+genero.videojuegos[:-1])
    except Exception as error:
        print(error)
    system("Pause")

def mostrar_videojuegos():
    try:
        path = "videojuegos.txt"
        lectura = open(path,'r')
        lineas = lectura.readlines()
        lectura.close()
        videojuegos = []
        for linea in lineas:
            palabras = linea.split(";")
            videojuegos.append(Videojuego(palabras[0],palabras[1],palabras[2],palabras[3],palabras[4]))
        print("\nLista de Videojuegos")
        for videojuego in videojuegos:
            print("Nombre: "+videojuego.nombre+"\tFecha Lanzamiento: "+videojuego.fecha_lanzamiento+
                "\tPrecio: "+str(videojuego.precio)+"\tDisponibilidad:"+str(videojuego.disponible)+
                "\tConsola: "+videojuego.consola[:-1])
    except Exception as error:
        print(error)
    system("Pause")

def buscar_genero():
    genero = input("Qué genero desea buscar: ")
    try:
        path = "generos.txt"
        lectura = open(path,'r')
        lineas = lectura.readlines()
        lectura.close()
        for linea in lineas:
            palabras = linea.split(";")
            for palabra in palabras:
                if palabra == genero:
                    break
        print("\nCaracterísticas: ")
        for palabra in palabras:
            print(palabra+" ")
    except Exception as error:
        print(error)
    system("Pause")

def buscar_videojuego():
    videojuego = input("Qué videojuego desea Buscar: ")
    try:
        path = "videojuegos.txt"
        lectura = open(path,'r')
        lineas = lectura.readlines()
        lectura.close()
        for linea in lineas:
            palabras = linea.split(";")
            for palabra in palabras:
                if palabra == videojuego:
                    break
        print("\nCaracterísticas: ")
        for palabra in palabras:
            print(palabra+" ")
    except Exception as error:
        print(error)
    system("Pause")


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
        print("4. Mostrar todos los Generos")
        print("5. Buscar un genero específico")

        opcion2 = int(input("Elija una Opcion: "))
        if opcion2 == 1:
            print("\n")
            agregar_genero()
        elif opcion2 == 2:
            print("\n")
            modificar_genero()
        elif opcion2 == 3:
            print("\n")
            eliminar_genero()
        elif opcion2 == 4:
            print("\n")
            mostrar_generos()
        elif opcion2 == 5:
            print("\n")
            buscar_genero()

    elif opcion == 2:
        system("cls")
        print("\nEste es el menu de Videojuego\n")
        print("1. Agregar nuevo Videojuego")
        print("2. Modificar Videojuego")
        print("3. Eliminar Videojuego")
        print("4. Mostrar todos los Videojuegos")
        print("5. Buscar un videojuego específico")

        opcion2 = int(input("Elija una Opcion: "))
        if opcion2 == 1:
            print("\n")
            agregar_videojuego()
        elif opcion2 == 2:
            print("\n")
            modificar_videojuego()
        elif opcion2 == 3:
            print("\n")
            eliminar_videojuego()
        elif opcion2 == 4:
            print("\n")
            mostrar_videojuegos()
        elif opcion2 == 5:
            print("\n")
            buscar_videojuego()

    system("cls")