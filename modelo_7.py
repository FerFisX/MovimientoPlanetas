import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constantes
G = 6.67430e-11  # Constante de gravitación universal en m^3/kg/s^2
M = 1.989e30     # Masa del Sol en kg

# Datos de los planetas (Períodos orbitales y semiejes mayores en metros)
planet_data = {
    "Mercurio": (60*60*24*88, 5.791e10),
    "Venus": (60*60*24*225, 1.082e11),
    "Tierra": (60*60*24*365, 1.496e11),
    "Marte": (60*60*24*687, 2.279e11),
    "Jupiter": (60*60*24*4332.59, 7.785472e11),
    "Saturno": (60*60*24*10755.7, 1.4335e12),
    "Urano": (60*60*24*30687.15, 2.8725e12),
    "Neptuno": (60*60*24*60190, 4.4951e12)
}

# Datos del asteroide
T_asteroid = 60*60*24*365.25*3  # Período orbital del asteroide en segundos
a_asteroid = 2.7e11  # Semieje mayor de la órbita del asteroide en metros

# Función para calcular la posición de un cuerpo celeste en su órbita
def calculate_position(time, T, a):
    x = a * np.cos(2 * np.pi * time / T)
    y = a * np.sin(2 * np.pi * time / T)
    return x, y

# Configuración del gráfico
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', xlim=(-5.5*a_asteroid, 5.5*a_asteroid), ylim=(-5.5*a_asteroid, 5.5*a_asteroid))
planet_orbits = {}
planet_dots = {}
for planet in planet_data:
    planet_orbits[planet], = ax.plot([], [], linestyle='dotted')
    planet_dots[planet], = ax.plot([], [], 'o', markersize=6)
asteroid_orbit, = ax.plot([], [], color='gray', linestyle='dotted')
asteroid_dot, = ax.plot([], [], 'o', color='gray', markersize=4)
sun_dot, = ax.plot([], [], 'o', color='yellow', markersize=20)
ax.set_title('Órbitas de los Planetas y un Asteroide en el Sistema Solar')
ax.set_xlabel('Posición en el eje X (m)')
ax.set_ylabel('Posición en el eje Y (m)')
ax.grid()

# Función de inicialización para la animación
def init():
    for planet in planet_data:
        planet_orbits[planet].set_data([], [])
        planet_dots[planet].set_data([], [])
    asteroid_orbit.set_data([], [])
    asteroid_dot.set_data([], [])
    sun_dot.set_data([], [])
    return (*planet_orbits.values(), *planet_dots.values(), asteroid_orbit, asteroid_dot, sun_dot)

# Función de animación
def animate(time):
    for planet in planet_data:
        T, a = planet_data[planet]
        x, y = calculate_position(time, T, a)
        planet_orbits[planet].set_data(np.append(planet_orbits[planet].get_xdata(), x), np.append(planet_orbits[planet].get_ydata(), y))
        planet_dots[planet].set_data(x, y)
    
    x_asteroid, y_asteroid = calculate_position(time, T_asteroid, a_asteroid)
    asteroid_orbit.set_data(np.append(asteroid_orbit.get_xdata(), x_asteroid), np.append(asteroid_orbit.get_ydata(), y_asteroid))
    asteroid_dot.set_data(x_asteroid, y_asteroid)
    sun_dot.set_data(0, 0)
    
    return (*planet_orbits.values(), *planet_dots.values(), asteroid_orbit, asteroid_dot, sun_dot)

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, max([data[0] for data in planet_data.values()]) * 2, 3600), interval=30, blit=True)

# Mostrar la animación
plt.show()
