#adminitrador de receta
from pathlib import Path
import os

ruta = Path("C:\\Users\\victo\\OneDrive\\Escritorio\\receta")


def biembenida(ruta):
    print("           Menu pricipal")
    print(f"Su ruta es {ruta}")
    print("""
          [1]-Ver recetas
          [2]-Mostrar categorias
          [3]-Crear recetas
          [4]-Crear categoria
          [5]-Borrar receta
          [6]-Borrar categoria
          [7]-salir(S)
          
          
          
          """)
    opcion = int(input("ingrese accion: "))
    return opcion

def ver_receta(ruta):
    contador=1
    lista_receta = []
    for receta in Path(ruta).glob("*/*.txt"):
        print(f"[{contador}]-{Path(receta).name}")
        lista_receta.append(Path(receta).name)
        contador +=1
    return lista_receta



def ver_categoria(ruta):
    contador = 1
    lista_categoria = []
    for categoria in os.listdir(ruta):
        print(f"[{contador}]-{categoria}")
        lista_categoria.append(categoria)
        contador += 1
    return lista_categoria
        


    
def crear_receta(ruta):
    ver_categoria(ruta)
    categoria= input("ingrese la categoria donde crear la receta: ")
    nombre = input("nombre dela receta: ")+ ".txt"
    receta_ruta = ruta / categoria
    contenido= input("Escribe contenido de la receta: ")
    
    
    with open(receta_ruta/nombre,"w") as archivo:
        archivo.write(contenido)
        print("se creo correctamente")
    
    
def crear_categoria(ruta):
    ver_categoria(ruta)
    nombre = input("ingrese el nombre de la categoria: ")
    os.makedirs(ruta/nombre)


def eliminar_receta(ruta):
    ver_receta(ruta)
    nombre = input("que receta desea eliminar: ")+".txt"
    for receta in Path(ruta).glob("*/*.txt"):
        if receta.name == nombre:
            os.remove(receta)
            print("ha sido borrado")
            
            
            
def eliminar_categoria(ruta):
    ver_categoria(ruta)
    nombre= input("Nombre dela categoria a borrar: ")
    os.removedirs(ruta/nombre)
    print("!ha sido borrado")
    
while True:
    os.system("pause")
    os.system("cls")
    opcion = biembenida(ruta)
    match opcion:
        case 1:
            ver_receta(ruta)
        case 2:
            ver_categoria(ruta)
        case 3:
            crear_receta(ruta)
        case 4:
            crear_categoria(ruta)
        case 5:
            eliminar_receta(ruta)
        case 6:
            eliminar_categoria(ruta)
        case 7:
            print("hasta pronto")
            break
        case _:
            print("introdusca una opcion valida")
