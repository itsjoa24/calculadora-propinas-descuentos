# Listas

print("--Bienvenido--")

precios = [120, 45.5, 80, 200, 15]

print ("Esta es la lista de precios: ")

for precio in precios:
    print (f"{precio:.2f}")

print (f"Cantidad: {len(precios)}")

total = 0.0

for precio in precios: 
    total = total + precio

print(f"total: {total:.2f}")

promedio = total / len(precios)

for  precio in precios:
        if precio >= 100:
            print (f"Los precios mayores a 100 son : {precio:.2f}")

print (f"El promedio es de : {promedio:.2f}")

            
    

