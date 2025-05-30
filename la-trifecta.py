
def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def calcular_factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

while True:
    entrada = input("Ingrese un número entero distinto de 0 para iniciar (0 o no entero para salir): ")

    if not es_entero(entrada):
        print("No ingresó un número entero. Saliendo del programa.")
        break

    numero = int(entrada)

    if numero == 0:
        print("Ingresó 0. Saliendo del programa.")
        break

    frase = input("Ingrese una palabra o frase: ")
    cantidad_caracteres = len(frase)
    print("Cantidad de caracteres:", cantidad_caracteres)

    factorial = calcular_factorial(cantidad_caracteres)
    print("Factorial de la cantidad de caracteres:", factorial)

    if factorial % 2 == 0:
        print("El factorial es un número par.")
        print("Fin del ciclo.")
    else:
        print("El factorial es un número impar.")
        print("Fin del ciclo.")
