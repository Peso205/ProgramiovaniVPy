import numpy as np
import matplotlib.pyplot as plt

#Proměnné
k = 1.0
m = 1.0
b = 0.2

x0 = 1
v0 = 0

#Počáteční podmínky
y = np.array([
    x0,
    v0
])

#Pravá strana diferenciální rovnice
def f(y, t):
    x = y[0]
    v = y[1]
    dxdt = v
    dvdt = -k/m * x - b/m * v
    return np.array([dxdt, dvdt])

#Eulerova metoda
t = 0
T = 10
dt = 0.1

#Definice pro ukládání hodnot pro graf
t_plot = []
x_plot = []
x_plot.append(y[0])
t_plot.append(t)

#Cyklus vypočítávající hodnoty v čase
while t < T:
    y = y + dt * f(y, t)
    t = t + dt

    #Uložení hodnot pro graf
    x_plot.append(y[0])
    t_plot.append(t)

plt.plot(t_plot, x_plot)
plt.xlabel('Čas [s]')
plt.ylabel('Výchylka [m]')
plt.title('Tlumené oscilace')
plt.grid()
plt.show()
