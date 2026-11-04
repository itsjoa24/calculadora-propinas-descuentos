with open("nota.txt", "w") as archivo:
    archivo.write("hola\n")


with open("nota.txt", "r") as archivo:
    texto= archivo.read()
print(texto)
