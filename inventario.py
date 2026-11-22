# Inventario

print("--MENU--")

listas = [
    "1. AGREGAR PRODUCTO",
    "2. VER PRODUCTO",
    "3. ELIMINAR PRODUCTO",
    "4. SALIR",
    "5. CAMBIAR CANTIDAD",
]

productos = []
try:
    with open("inventario.txt", "r") as archivo:
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(",")
            productos.append(
                {"nombre": nombre, "cantidad": int(cantidad), "precio": float(precio)}
            )
except FileNotFoundError:
    print(
        "No se encontro el archivo inventario.txt, se creara uno nuevo al salir del programa"
    )


while True:
    try:
        for lista in listas:
            print(lista)
    except NameError:
        print("Error al mostrar el menu")
    try:
        opcion = int(input("Eliga la opcion que quiera realizar: "))
        if opcion == 1:
            nombre = input("Nombre del producto: ").strip().lower()
            if nombre == "":
                print("No se puede agregar un producto vacio")
            else:
                cantidad = int(input("cantidad del producto: "))
                precio = float(input("Precio del producto: "))
                if cantidad < 0 or precio < 0:
                    print("No pueden ser negativos")
                else:
                    existente = None
                    for producto in productos:
                        if producto["nombre"] == nombre:
                            existente = producto
                            break
                    if existente is None:
                        producto = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad,
                        }
                        productos.append(producto)
                        print(f"se ha agregado correctamente {nombre}")
                    else:
                        existente["cantidad"] += cantidad

                        print("se ha actualizado la cantidad")
        elif opcion == 2:
            if len(productos) == 0:
                print("No hay productos añadidos")
            else:
                total = 0.0
                for producto in productos:
                    print(
                        f"{producto['nombre']} : unidades : {producto['cantidad']} a un precio de ${producto['precio']:.2f}"
                    )
                    total += producto["precio"] * producto["cantidad"]
                print(f"El total de la compra es de ${total:.2f}")
        elif opcion == 3:
            nombre = input("Producto a eliminar : ").strip().lower()
            encontrado = False
            if nombre == "":
                print("No se puede eliminar un producto vacio")
            else:
                for producto in productos:
                    if nombre == producto["nombre"]:
                        productos.remove(producto)
                        encontrado = True
                        break
                if encontrado:
                    print(f"Se ha eliminado exitosamente {nombre} de la lista")
                else:
                    print(f"No se encontro {nombre} en la lista")
        elif opcion == 4:
            with open("inventario.txt", "w") as archivo:
                for producto in productos:
                    archivo.write(
                        f"{producto['nombre']},{producto['cantidad']},{producto['precio']}\n"
                    )
            print("Que tenga un lindo dia")
            break
        elif opcion == 5:
            nombre = input("Producto a editar: ").strip().lower()
            encontrado = False
            if nombre == "":
                print("escriba el nombre del producto")
            else:
                for producto in productos:
                    if nombre == producto["nombre"]:
                        encontrado = True
                        nueva_cantidad = int(input("Nueva cantidad : "))
                        if nueva_cantidad < 0:
                            print("No puede ser una cantidad negativa")
                        else:
                            producto["cantidad"] = nueva_cantidad
                            print("Se ha cambiado la cantidad")
                        break
                if not encontrado:
                    print("No existe este producto")
        else:
            print("Opcion no valida")
    except ValueError:
        print("ERROR : Solo se permite numero enteros")
