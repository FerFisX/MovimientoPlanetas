import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constantes
G = 6.67430e-11  # Constante de gravitación universal en m^3/kg/s^2
M = 1.989e30     # Masa del Sol en kg
T_earth = 60*60*24*365 # Período orbital de la Tierra en segundos
a_earth = 1.496e11     # Semieje mayor de la órbita de la Tierra en metros
T_mars = 60*60*24*687 # Período orbital de Marte en segundos
a_mars = 2.279e11     # Semieje mayor de la órbita de Marte en metros
T_moon = 60*60*24*27.3 # Período orbital de la Luna en segundos
a_moon = 3.844e8       # Semieje mayor de la órbita de la Luna en metros
T_mercury = 60*60*24*88 # Período orbital de Mercurio en segundos
a_mercury = 5.791e10     # Semieje mayor de la órbita de Mercurio en metros

# Función para calcular la posición de un cuerpo celeste en su órbita
def calculate_position(time, T, a):
    x = a * np.cos(2 * np.pi * time / T)
    y = a * np.sin(2 * np.pi * time / T)
    return x, y

# Configuración del gráfico
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', xlim=(-3.5*a_mercury, 3.5*a_mercury), ylim=(-3.5*a_mercury, 3.5*a_mercury))
earth_orbit, = ax.plot([], [], color='blue', linestyle='dotted')
mars_orbit, = ax.plot([], [], color='red', linestyle='dotted')
moon_orbit, = ax.plot([], [], color='gray', linestyle='dotted')
mercury_orbit, = ax.plot([], [], color='purple', linestyle='dotted')
earth_dot, = ax.plot([], [], 'o', color='blue', markersize=6)
mars_dot, = ax.plot([], [], 'o', color='red', markersize=6)
moon_dot, = ax.plot([], [], 'o', color='gray', markersize=3)
mercury_dot, = ax.plot([], [], 'o', color='purple', markersize=4)
sun_dot, = ax.plot([], [], 'o', color='yellow', markersize=20)
ax.set_title('Órbitas de la Tierra, Marte, la Luna y Mercurio')
ax.set_xlabel('Posición en el eje X (m)')
ax.set_ylabel('Posición en el eje Y (m)')
ax.grid()

# Función de inicialización para la animación
def init():
    earth_orbit.set_data([], [])
    mars_orbit.set_data([], [])
    moon_orbit.set_data([], [])
    mercury_orbit.set_data([], [])
    earth_dot.set_data([], [])
    mars_dot.set_data([], [])
    moon_dot.set_data([], [])
    mercury_dot.set_data([], [])
    sun_dot.set_data([], [])
    return earth_orbit, mars_orbit, moon_orbit, mercury_orbit, earth_dot, mars_dot, moon_dot, mercury_dot, sun_dot

# Función de animación
def animate(time):
    x_earth, y_earth = calculate_position(time, T_earth, a_earth)
    x_mars, y_mars = calculate_position(time, T_mars, a_mars)
    x_moon, y_moon = calculate_position(time, T_moon, a_moon)
    x_mercury, y_mercury = calculate_position(time, T_mercury, a_mercury)
    
    earth_orbit.set_data(np.append(earth_orbit.get_xdata(), x_earth), np.append(earth_orbit.get_ydata(), y_earth))
    mars_orbit.set_data(np.append(mars_orbit.get_xdata(), x_mars), np.append(mars_orbit.get_ydata(), y_mars))
    moon_orbit.set_data(np.append(moon_orbit.get_xdata(), x_moon), np.append(moon_orbit.get_ydata(), y_moon))
    mercury_orbit.set_data(np.append(mercury_orbit.get_xdata(), x_mercury), np.append(mercury_orbit.get_ydata(), y_mercury))
    
    earth_dot.set_data(x_earth, y_earth)
    mars_dot.set_data(x_mars, y_mars)
    moon_dot.set_data(x_moon, y_moon)
    mercury_dot.set_data(x_mercury, y_mercury)
    sun_dot.set_data(0, 0)
    
    return earth_orbit, mars_orbit, moon_orbit, mercury_orbit, earth_dot, mars_dot, moon_dot, mercury_dot, sun_dot

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, max(T_earth, T_mars, T_moon, T_mercury), 3600), interval=30, blit=True)

# Mostrar la animación
plt.show()
