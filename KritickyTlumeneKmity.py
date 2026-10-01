import numpy as np
import matplotlib.pyplot as plt

#Proměnné
k = 1.0
m = 1.0

omega = np.sqrt(k/m)
xiList = [0.1, 1, 1.5] 
bList = [2 * xi * omega * m for xi in xiList]
xi1 = 0.1
xi2 = 1
xi3 = 1.5
b1 = 2 * xi1 * omega * m
b2 = 2 * xi2 * omega * m
b3 = 2 * xi3 * omega * m

x0 = 1
v0 = 0

#Počáteční podmínky
y = np.array([
    x0,
    v0,
])

#Pravá strana diferenciální rovnice
def f(y, b, t):
    x = y[0]
    v = y[1]
    dxdt = v
    dvdt = -k/m * x - b/m * v
    return np.array([dxdt, dvdt])

#Eulerova metoda
t = 0
T = 30
dt = 0.01

#Definice pro ukládání hodnot pro graf
t_plot = []
x_plot = []
x_plot.append(y[0])
t_plot.append(t)

#Cyklus vypočítávající hodnoty v čase
while t < T:
    y = y + dt * f(y, b1, t)
    t = t + dt

    #Uložení hodnot pro graf
    x_plot.append(y[0])
    t_plot.append(t)


plt.plot(t_plot, x_plot)
t_plot = []
x_plot = []
t = 0
y = np.array([
    x0,
    v0,
])

#Cyklus vypočítávající hodnoty v čase
while t < T:
    y = y + dt * f(y, b2, t)
    t = t + dt

    #Uložení hodnot pro graf
    x_plot.append(y[0])
    t_plot.append(t)


plt.plot(t_plot, x_plot)
t_plot = []
x_plot = []
t = 0
y = np.array([
    x0,
    v0,
])

#Cyklus vypočítávající hodnoty v čase
while t < T:
    y = y + dt * f(y, b3, t)
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
