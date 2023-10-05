import numpy as np
from mayavi import mlab

# Constantes
G = 6.67430e-11  # Constante de gravitación universal en m^3/kg/s^2
M = 1.989e30     # Masa del Sol en kg
T = 60*60*24*365 # Período orbital de la Tierra en segundos
a = 1.496e11     # Semieje mayor de la órbita de la Tierra en metros

# Función para calcular la posición de la Tierra en su órbita
def calculate_earth_position(time):
    x = a * np.cos(2 * np.pi * time / T)
    y = a * np.sin(2 * np.pi * time / T)
    return x, y, np.zeros_like(x)

# Crear la figura
fig = mlab.figure(size=(800, 800), bgcolor=(0, 0, 0))

# Crear la órbita de la Tierra
theta = np.linspace(0, 2*np.pi, 1000)
x_orbit = a * np.cos(theta)
y_orbit = a * np.sin(theta)
z_orbit = np.zeros_like(x_orbit)
orbit = mlab.plot3d(x_orbit, y_orbit, z_orbit, color=(0.5, 0.5, 0.5), tube_radius=None)

# Crear la Tierra y el Sol
earth = mlab.points3d([0], [0], [0], color=(0, 0, 1), scale_factor=1)
sun = mlab.points3d([0], [0], [0], color=(1, 1, 0), scale_factor=10)

# Función de actualización de la animación
@mlab.animate(delay=100)
def update_plot():
    t = 0
    while t < T:
        x, y, z = calculate_earth_position(t)
        earth.mlab_source.set(x=x, y=y, z=z)
        sun.mlab_source.set(x=0, y=0, z=0)
        t += 3600  # Incrementar en 1 hora
        yield

# Iniciar la animación
update_plot()
mlab.show()
