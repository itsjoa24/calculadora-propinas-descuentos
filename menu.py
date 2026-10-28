from calculadora import pedir_propina
from descuentos import calcular_descuentos


print("-Bienvenido- \n a continuacion elige las siguientes opciones : ")
while True:
    print("1.propina")
    print("2.Descuento")
    print("3.Salir")
    try:
        opciones = int(input("Elige una opcion: "))
        if opciones == 1:
            pedir_propina()

        elif opciones == 2:
            calcular_descuentos()
        elif opciones == 3:
            print("Hasta luego")
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Solo puedes poner numero entero ")
