def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b

def potencia(a, b):
    return a ** b


def obtener_numeros():
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            return a, b
        except ValueError:
            print("Error: Debe ingresar valores numéricos.")


def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Salir")


def ejecutar_operacion(opcion, a, b):
    operaciones = {
        "1": suma,
        "2": resta,
        "3": multiplicacion,
        "4": division,
        "5": potencia
    }

    if opcion in operaciones:
        try:
            return operaciones[opcion](a, b)
        except ValueError as e:
            return str(e)
    else:
        return None


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Programa finalizado.")
            break

        a, b = obtener_numeros()
        resultado = ejecutar_operacion(opcion, a, b)

        if resultado is None:
            print("Opción no válida.")
        else:
            print("Resultado:", resultado)


if __name__ == "__main__":
    main()