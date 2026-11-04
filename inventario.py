# Inventario

print("--MENU--")

listas = ["1. AGREGAR PRODUCTO", "2. VER PRODUCTO", "3. ELIMINAR PRODUCTO", "4. SALIR"]

productos = []
try:
    with open("inventario.txt", "r") as archivo:
        for linea in archivo:
            productos.append(linea.strip())
except FileNotFoundError:
    print("No se encontro el archivo inventario.txt, se creara uno nuevo al salir del programa")



while True:
    try:
        for lista in listas:
            print(lista)
        opcion = int(input("Eliga la opcion que quiera realizar: "))
        if opcion == 1:
            nombre = input("Nombre del producto: ").strip().lower()
            productos.append(nombre)
            print(f"{nombre} Agregado exitosamente")

        elif opcion == 2:
            if len(productos) == 0:
                print("No hay productos añadidos")
            else:
                for producto in productos:
                    print(producto)
        elif opcion == 3:
            nombre = input("Producto a eliminar : ") .strip() .lower()
            if nombre in productos:
                productos.remove(nombre)
                print(f"Se ah eliminado exitosamente {nombre} de la lista")
            else:
                print(f"No se encontro {nombre} En la lista")
        elif opcion == 4:
            with open("inventario.txt", "w") as archivo:
                for producto in productos:
                    archivo.write(producto + "\n")
            print("Que tenga un lindo dia")
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("ERROR : Solo se permite numero entero de las opciones 1 - 4 ")


# Guardar: cada nombre en una línea
with open("datos.txt", "w") as archivo:
    for nombre in productos:
        archivo.write(nombre + "\n")

# Leer
with open("datos.txt", "r") as archivo:
    nombres = [linea.strip() for linea in archivo]
