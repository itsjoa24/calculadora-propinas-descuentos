productos = [
    {"Nombre": "libreta", "precio": 10.5, "cantidad": 20},
    {"Nombre": "Lapiz", "precio": 5.5, "cantidad": 30},
    {"Nombre": "borrador", "precio": 3.5, "cantidad": 15},
]

total = 0.0

for producto in productos:
    print(f"{producto['Nombre']}: {producto['cantidad']} unidades a un precio de:{producto['precio']:.2f} cada una")
    total = total + (producto['precio'] * producto['cantidad'])
    


print(f"El total de la compra es de {total:.2f}")
