#Inventario

print ("--MENU--")

listas = ["1. AGREGAR PRODUCTO", "2. VER PRODUCTO" ,"3. ELIMINAR PRODUCTO", "4. SALIR"]

productos = []
while True:
    try:
        for lista in listas:
            print (lista)
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
            nombre = input("Producto a eliminar : ")
            if nombre in productos:
                productos.remove(nombre)
                print(f"Se ah eliminado exitosamente {nombre} de la lista")
            else:
                print (f"No se encontro {nombre} En la lista")
        elif opcion == 4:
            print("Que tenga un lindo dia") 
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print ("ERROR : Solo se permite numero entero de las opciones 1 - 4 ")
        


    
        
    
    