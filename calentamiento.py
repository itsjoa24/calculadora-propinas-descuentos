# calentamineto

productos = [
    {"nombre": "Libreta", "precio": 35.5, "cantidad": 20},
    {"nombre": "lapiz", "precio": 5.5, "cantidad": 10},
    {"nombre": "sacapuntas", "precio": 5.0, "cantidad": 20},
]


total = 0.0
for producto in productos:
    print(
        f"{producto['nombre']} : con un precio de ${producto['precio']:.2f} y un stock de {producto['cantidad']}"
    )
    total += producto["precio"] * producto["cantidad"]


print(f"el total de la compra es de ${total:.2f}")
