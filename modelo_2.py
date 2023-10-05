import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constantes
G = 6.67430e-11  # Constante de gravitación universal en m^3/kg/s^2
M = 1.989e30     # Masa del Sol en kg
T = 60*60*24*365 # Período orbital de la Tierra en segundos
a = 1.496e11     # Semieje mayor de la órbita de la Tierra en metros

# Función para calcular la posición de la Tierra en su órbita
def calculate_earth_position(time):
    x = a * np.cos(2 * np.pi * time / T)
    y = a * np.sin(2 * np.pi * time / T)
    return x, y

# Configuración del gráfico
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', xlim=(-1.5*a, 1.5*a), ylim=(-1.5*a, 1.5*a))
earth_orbit, = ax.plot([], [], color='blue')
earth_dot, = ax.plot([], [], 'o', color='blue', markersize=6)
sun_dot, = ax.plot([], [], 'o', color='yellow', markersize=20)
ax.set_title('Órbita de la Tierra')
ax.set_xlabel('Posición en el eje X (m)')
ax.set_ylabel('Posición en el eje Y (m)')
ax.grid()

# Función de inicialización para la animación
def init():
    earth_orbit.set_data([], [])
    earth_dot.set_data([], [])
    sun_dot.set_data([], [])
    return earth_orbit, earth_dot, sun_dot

# Función de animación
def animate(time):
    x, y = calculate_earth_position(time)
    earth_orbit.set_data(x, y)
    earth_dot.set_data(x, y)
    sun_dot.set_data(0, 0)
    return earth_orbit, earth_dot, sun_dot

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, T, 3600), interval=50, blit=True)

# Mostrar la animación
plt.show()
