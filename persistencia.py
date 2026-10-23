# Crear .txt
with open("datos.txt", "w") as archivo:
    archivo.write("Pepe;25;Brasil\n")
    archivo.write("Tilin;18;Perú\n")
# El primer argumento es el nombre del archivo, el segundo 'w' viene de write
# r : Read
# w : Write
# a : Append
# x : Exclusive

# Leer procesando el delimitador ;
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        # .strip() quita el salto de línea (\n) y .split(";") separa los valores
        datos = linea.strip().split(";")
        nombre, edad, pais = datos
        print(f"Nombre: {nombre}, Edad: {edad}, País: {pais}")