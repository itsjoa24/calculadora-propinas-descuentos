def calcular_descuento(precio, porcentaje):
    fraccion = porcentaje / 100
    ahorro = precio * fraccion
    precio_final = precio - ahorro

    return precio_final


print(calcular_descuento(800, 25))


def calcular_propina(cuenta, porcentaje):
    total_cuenta = cuenta
    propinas = porcentaje / 100
    ahorro  = total_cuenta * propinas
    cuenta_mas_propina =  total_cuenta + ahorro

    return cuenta_mas_propina


print(calcular_propina(500, 20))
