#Calculadora de descuentos
def calcular_descuentos():
    try:
        precio = float(input("Cual es el precio original del producto: "))
        descuentos = float(input("Cual es el porcentaje de descuento que deseas agregar? : "))
        valor_descuento = descuentos / 100
        ahorro = precio * valor_descuento 
        print (f"Usted se esta ahorrando con esta compra la cantidad de  : {ahorro:.2f}")

        total = precio - ahorro 

        print (f"Su total de la cuenta seria : {total:.2f}")
    except ValueError:
        print ("No se permiten letras ni caracteres")
