numero = 20 # ASIGNACIÖN DE VARIABLES
## IF, ELSE
if numero == 20:
    print(numero, "es 20") # Concatenación
elif numero <20:
    print("Menor a 20")
else:
    print("Mayor o igual a 20")

## while
contador = 0

while contador < 5: ## PRIMERO EVALÚA LA CONDICIÓN, LUEGO EJECUTA
    print(f"Contador: {contador}")
    contador += 1  # Al contador sumarle 1


## do-while, no existe en Python. Se usa un while True (bucle infinito) y se rompe con un break.
while True:
    respuesta = input("Escribe 'continuar' para seguir: ")
    if respuesta == "continuar":
        break  # Rompe el bucle

## for
for i in range(5): # Genera números del 0 al 4 (el límite superior 5 no se incluye)
    print(i)

## Arreglo unidimensional
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

print('La primer fruta es: ', frutas[0])

## Arreglo bidimensional
matriz = [
##  COLUMNAS
##   0  1  2
    [1, 2, 3], ## 0 FILAS
    [4, 5, 6], ## 1
    [7, 8, 9]  ## 1
]

# Acceder a la fila 0, columna 1 (devuelve 2)
print(matriz[0][1])

# Recorrer la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea

## Manejo de excepciones (en Java try-catch) en Python try-except
print('Manejo de excepciones. Probar ingresando con un 0 o texto.')
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes ingresar un número válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

    