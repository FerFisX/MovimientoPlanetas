import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constantes
G = 6.67430e-11  # Constante de gravitación universal en m^3/kg/s^2
M = 1.989e30     # Masa del Sol en kg
T = 60*60*24*687 # Período orbital de Marte en segundos
a_earth = 1.496e11     # Semieje mayor de la órbita de la Tierra en metros
a_mars = 2.279e11     # Semieje mayor de la órbita de Marte en metros

# Función para calcular la posición de un planeta en su órbita
def calculate_planet_position(time, a):
    x = a * np.cos(2 * np.pi * time / T)
    y = a * np.sin(2 * np.pi * time / T)
    return x, y

# Configuración del gráfico
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', xlim=(-2.5*a_earth, 2.5*a_earth), ylim=(-2.5*a_earth, 2.5*a_earth))
earth_orbit, = ax.plot([], [], color='blue', linestyle='dotted')
mars_orbit, = ax.plot([], [], color='red', linestyle='dotted')
earth_dot, = ax.plot([], [], 'o', color='blue', markersize=6)
mars_dot, = ax.plot([], [], 'o', color='red', markersize=6)
sun_dot, = ax.plot([], [], 'o', color='yellow', markersize=20)
ax.set_title('Órbitas de la Tierra y Marte')
ax.set_xlabel('Posición en el eje X (m)')
ax.set_ylabel('Posición en el eje Y (m)')
ax.grid()

# Función de inicialización para la animación
def init():
    earth_orbit.set_data([], [])
    mars_orbit.set_data([], [])
    earth_dot.set_data([], [])
    mars_dot.set_data([], [])
    sun_dot.set_data([], [])
    return earth_orbit, mars_orbit, earth_dot, mars_dot, sun_dot

# Función de animación
def animate(time):
    x_earth, y_earth = calculate_planet_position(time, a_earth)
    x_mars, y_mars = calculate_planet_position(time, a_mars)
    
    earth_orbit.set_data(np.append(earth_orbit.get_xdata(), x_earth), np.append(earth_orbit.get_ydata(), y_earth))
    mars_orbit.set_data(np.append(mars_orbit.get_xdata(), x_mars), np.append(mars_orbit.get_ydata(), y_mars))
    
    earth_dot.set_data(x_earth, y_earth)
    mars_dot.set_data(x_mars, y_mars)
    sun_dot.set_data(0, 0)
    
    return earth_orbit, mars_orbit, earth_dot, mars_dot, sun_dot

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, T, 3600), interval=50, blit=True)

# Mostrar la animación
plt.show()
