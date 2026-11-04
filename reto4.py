# lista with

comidas = ["pan", "leche", "queso"]
with open("comidas.txt", "w") as archivo:
    for comida in comidas:
        archivo.write(comida + "\n")

with open("comidas.txt", "r") as archivo:
    texto = archivo.read()
print(texto)


leidas = []

with open("comidas.txt", "r") as archivo:
    for linea in archivo:
        leidas.append(linea.strip())

print(leidas)
