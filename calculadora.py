def calcular_propina():
    cuenta = float(input("Ingrese el total de su cuenta:"))
    propina = float(input("¿Cuanta propina desea agregar?  \n 10%,15%,20% :  "))
    valor_propina = propina / 100
    solo_propina = (cuenta * valor_propina)
    total = cuenta + solo_propina
    print ( f"su total de la cuenta con propina incluida es de : {total:.2f} ")
    print (f"su propina de la cuenta de: {cuenta:.2f} es de {solo_propina:.2f}")


    try:
        clientes = int(input("Numero de personas que pagaran su cuenta: "))
        cuenta_por_persona = total / clientes
        print (f"el total a pagar por persona con la propina incluida es de : {cuenta_por_persona:.2f}")
    except ValueError:
        print ("Solo puedes colocar numeros enteros")
    except ZeroDivisionError:
        print ("NO SE PUEDE DIVIDIR POR 0, COLOQUE NUEVAMENTE EL NUMERO DE PERSONAS IGUAL O MAYOR A 1 ")


