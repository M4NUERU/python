import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Función para solicitar y validar datos de entrada
def obtener_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Función para obtener los parámetros de la simulación
def obtener_parametros():
    x0 = obtener_float("Ingrese la posición inicial (m): ")
    v0 = obtener_float("Ingrese la velocidad inicial (m/s): ")
    a = obtener_float("Ingrese la aceleración (m/s^2): ")
    t_max = obtener_float("Ingrese la duración de la simulación (s): ")
    return x0, v0, a, t_max

# Funciones para calcular posición y velocidad
def calcular_posicion(t, x0, v0, a):
    return x0 + v0 * t + 0.5 * a * t**2

def calcular_velocidad(t, v0, a):
    return v0 + a * t

# Configuración de la animación
fig, ax = plt.subplots()

def update(num, t, datos_lineas):
    for line, x in datos_lineas:
        line.set_data(t[:num], x[:num])
    return [line for line, _ in datos_lineas]

datos_lineas = []

while True:
    x0, v0, a, t_max = obtener_parametros()
    dt = 0.01
    t = np.arange(0, t_max, dt)
    x = calcular_posicion(t, x0, v0, a)

    # Crear una nueva línea para la nueva serie de datos
    line, = ax.plot(t, x, label=f'Posición (m) - v0={v0}, a={a}')
    datos_lineas.append((line, x))

    # Configurar límites del gráfico
    ax.set_xlim(0, max(t))
    ax.set_ylim(min(min(x) for _, x in datos_lineas) - 1, max(max(x) for _, x in datos_lineas) + 1)

    # Preguntar al usuario si desea añadir otra serie de datos
    agregar_otra = input("¿Desea agregar otra serie de datos? (s/n): ")
    if agregar_otra.lower() != 's':
        break

ani = animation.FuncAnimation(fig, update, frames=len(t), fargs=[t, datos_lineas], interval=dt*1000, blit=True)

plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Simulación de Movimiento Rectilíneo Uniformemente Variado')
plt.legend()
plt.grid(True)
plt.show()
