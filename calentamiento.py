# calentamiento


def calcular_total(productos):
    total = 0.0
    for producto in productos:
        total += producto["precio"] * producto["cantidad"]
    return total


inventario = [
    {"nombre": "pan", "cantidad": 10, "precio": 12.5},
    {"nombre": "leche", "cantidad": 5, "precio": 24.0},
    {"nombre": "queso", "cantidad": 2, "precio": 80.0},
]

print(calcular_total(inventario))


def buscar_producto(productos, nombre):
    for producto in productos:
        if nombre == producto["nombre"]:
            return producto

        return None


inventario = [
    {"nombre": "pan", "cantidad": 10, "precio": 12.5},
    {"nombre": "leche", "cantidad": 5, "precio": 24.0},
    {"nombre": "queso", "cantidad": 2, "precio": 80.0},
]

print(buscar_producto(inventario, "leche"))
print(buscar_producto(inventario, "jamon"))
producto = buscar_producto(inventario, "pan")
producto["cantidad"] = 20
print(inventario[0])


def productos_bajos(productos, minimo):
    bajos = []
    for producto in productos:
        if producto["cantidad"] < minimo:
            bajos.append(producto["nombre"])

    return bajos


inventario = [
    {"nombre": "pan", "cantidad": 10, "precio": 12.5},
    {"nombre": "leche", "cantidad": 5, "precio": 24.0},
    {"nombre": "queso", "cantidad": 2, "precio": 80.0},
]


print(productos_bajos(inventario, 6))
print(productos_bajos(inventario, 1))
print(productos_bajos([], 6))


def actualizar_cantidad(productos, nombre, nueva_cantidad):
    for producto in productos:
        if nombre == producto["nombre"]:
            producto["cantidad"] = nueva_cantidad
            return True
    return False


inventario = [
    {"nombre": "pan", "cantidad": 10, "precio": 12.5},
    {"nombre": "leche", "cantidad": 5, "precio": 24.0},
    {"nombre": "queso", "cantidad": 2, "precio": 80.0},
]

print(actualizar_cantidad(inventario, "pan", 20))
print(inventario[0]["cantidad"])
print(actualizar_cantidad(inventario, "leche", 50))
print(inventario[1]["cantidad"])
print(actualizar_cantidad(inventario, "jamon", 5))


def contar_agotados(productos):
    agotados = 0
    for producto in productos:
        if producto["cantidad"] == 0:
            agotados += 1
    return agotados


inventario = [
    {"nombre": "pan", "cantidad": 10, "precio": 12.5},
    {"nombre": "leche", "cantidad": 0, "precio": 24.0},
    {"nombre": "queso", "cantidad": 2, "precio": 80.0},
    {"nombre": "jamon", "cantidad": 0, "precio": 45.0},
]

print(contar_agotados(inventario))
print(contar_agotados([]))


