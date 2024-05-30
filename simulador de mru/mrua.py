def obtener_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def calcular_posicion(x0, v0, a, t):
    return x0 + v0 * t + 0.5 * a * t**2

def calcular_velocidad(v0, a, t):
    return v0 + a * t

def calcular_aceleracion(v, v0, t):
    if t == 0:
        raise ValueError("El tiempo no puede ser cero.")
    return (v - v0) / t

def calcular_tiempo(v, v0, a):
    if a == 0:
        raise ValueError("La aceleración no puede ser cero.")
    return (v - v0) / a

def main():
    print("Seleccione la variable que desea calcular:")
    print("1. Posición final (x)")
    print("2. Velocidad final (v)")
    print("3. Aceleración (a)")
    print("4. Tiempo (t)")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == '1':
        x0 = obtener_float("Ingrese la posición inicial (x0): ")
        v0 = obtener_float("Ingrese la velocidad inicial (v0): ")
        a = obtener_float("Ingrese la aceleración (a): ")
        t = obtener_float("Ingrese el tiempo (t): ")
        x = calcular_posicion(x0, v0, a, t)
        print(f"La posición final (x) es: {x} metros")

    elif opcion == '2':
        v0 = obtener_float("Ingrese la velocidad inicial (v0): ")
        a = obtener_float("Ingrese la aceleración (a): ")
        t = obtener_float("Ingrese el tiempo (t): ")
        v = calcular_velocidad(v0, a, t)
        print(f"La velocidad final (v) es: {v} m/s")

    elif opcion == '3':
        v = obtener_float("Ingrese la velocidad final (v): ")
        v0 = obtener_float("Ingrese la velocidad inicial (v0): ")
        t = obtener_float("Ingrese el tiempo (t): ")
        a = calcular_aceleracion(v, v0, t)
        print(f"La aceleración (a) es: {a} m/s²")

    elif opcion == '4':
        v = obtener_float("Ingrese la velocidad final (v): ")
        v0 = obtener_float("Ingrese la velocidad inicial (v0): ")
        a = obtener_float("Ingrese la aceleración (a): ")
        t = calcular_tiempo(v, v0, a)
        print(f"El tiempo (t) es: {t} segundos")

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
