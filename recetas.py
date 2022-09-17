from pathlib import Path
import os

from os.path import isfile, join
print('hola te doy la bienvenida!')
directorio = os.getcwd()
print(f'El directorio actual de recetas es: {directorio}')
directorios = Path(directorio).glob("**/*.txt")
# print(f'A continuacion te muestro las recetas que hay ')
# for txt in directorios:
#     print(txt)

def mostrarMenuPrincipal():
    print('[1] - Leer Receta')
    print('[2] - Crear Receta')
    print('[3] - Crear Categoria')
    print('[4] - Eliminar Receta')
    print('[5] - Eliminar Categoria')
    print('[6] - Finalizar programa')

def obtiene_option_menu_principal():
    opcion = input('Ingrese una opcion: ')
    return opcion

def obtiene_categoria_del_cliente():
    for directory in os.listdir(directorio):
        if directory != 'recetas.py':
            print(directory)
    categoria = input('Ingrese una categoria: ')
    return categoria

def crea_categoria():
    categoria = input("Ingrese el nombre de la categoria: ")
    directorio_nuevo = Path(directorio + '\\' + categoria)
    if not directorio_nuevo.exists():
        os.makedirs(directorio + '\\' + categoria)
    return categoria



#
option_principal = 1
# leer receta
while option_principal != 6:
    mostrarMenuPrincipal()
    option_principal = obtiene_option_menu_principal()
    if option_principal == '1':
        categoria = obtiene_categoria_del_cliente()
        print(f"Estas son las recetas de la categoria {categoria} :")
        recetas = Path(directorio,categoria).glob("**/*.txt")
        for receta in recetas:
            print(f'-- {receta.stem}')

        nombre_receta = input('Ingresa el nombre de la receta: ')
        ruta = Path(directorio,categoria,nombre_receta+".txt")
        print(ruta.read_text())

    if option_principal == '2':
        categoria = crea_categoria()
        receta = input("Ingrese el nombre de la receta: ")
        contenido = input("Ingrese el contenido de la receta: ")

        os.chdir(directorio + '\\' + categoria)
        archivo_receta = open(directorio+'\\'+categoria+'\\'+receta+'.txt',"w")
        archivo_receta.write(contenido)
        archivo_receta.close()

    if option_principal == '3':
        categoria = crea_categoria()
        print(f"La categoria {categoria} ha sido creada")

    if option_principal == '4':
        categoria = obtiene_categoria_del_cliente()
        print(f"Estas son las recetas de la categoria {categoria} :")
        recetas = Path(directorio,categoria).glob("**/*.txt")
        for receta in recetas:
            print(f'-- {receta.stem}')
        nombre_receta = input('Ingresa el nombre de la receta: ')
        ruta = Path(directorio,categoria,nombre_receta+".txt")
        os.remove(ruta)
        print("La receta ha sido eliminada")

    if option_principal == '5':
        categoria = input('Ingrese la categoria que desea eliminar: ')
        directorio_eliminar = Path(directorio + '\\' + categoria)
        if directorio_eliminar.exists():
            os.rmdir(directorio+'\\'+categoria)

        print(f"La {categoria} ha sido eliminada")

    if option_principal == '6':
        break