def calcular_propina(cuenta, porcentaje):
    total_cuenta = cuenta
    propinas = porcentaje / 100
    ahorro  = total_cuenta * propinas
    cuenta_mas_propina =  total_cuenta + ahorro

    return cuenta_mas_propina


def pedir_propina():
    cuenta = float(input("Ingrese el total de su cuenta: "))
    propina = float(input("Cuanta propina desea agregar \n 10%, 15%, 20% : " ))
    total = calcular_propina(cuenta, propina)
    ahorro = total - cuenta 
    print(f"su cuenta es de {total:.2f}")
    print(f"La propina es de {ahorro:.2f}")
    try:
        clientes = int(input("Numero de personas que pagaran su cuenta: "))
        cuenta_por_persona = total / clientes
        print (f"El total de su cuenta a pagar por persona con la propina incluida es de : {cuenta_por_persona:.2f}")
    except ValueError:
        print("Solo puedes colocar numeros enteros")
    except ZeroDivisionError:
        print ("NO SE PUEDE DIVIDIR ENTRE 0 , ESCRIBA 1 O MAS PERSONAS")
    

    return total


    

