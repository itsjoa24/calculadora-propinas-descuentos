# Calentamiento
lista_num = [5, 12, 8, 20, 3]

for numero in lista_num:
    if numero > 10:
        print(f"Los numeros mayores a 10 son : {numero}")




while True:
    palabra = str(input("Dime una palabra : "))
    try:
        if palabra == "salir":
            print("Adios")
            break
        else:
            print (f"Escribiste {palabra}")
    except ValueError:
        print("Ocurrió un error, tienes que ingresar solo una palabra")
        
        
        
def calcular_iva_precio (precio, iva):
    precio_iva = precio + (precio * iva)
    
    return precio_iva

print (calcular_iva_precio(100, 0.16))




        
