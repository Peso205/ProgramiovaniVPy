import numpy as np
import matplotlib.pyplot as plt

#Proměnné
k = 1.0
m = 1.0

omega = np.sqrt(k/m)
xiList = [0.1, 1.0, 1.5] 
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
    x0,
    x0,
    v0,
    v0,
    v0
])

#Pravá strana diferenciální rovnice
def f(y, b1, b2, b3, t):
    x = y[0:3]
    v = y[3:7]
    dxdt = v
    dvdt = np.array([-k/m * x[0] - b1/m * v[0], -k/m * x[1] - b2/m * v[1], -k/m * x[2] - b3/m * v[2]])
    return np.concatenate((dxdt, dvdt))

#Eulerova metoda
t = 0
T = 30
dt = 0.01

#Definice pro ukládání hodnot pro graf
t_plot = []
x1_plot = []
x2_plot = []
x3_plot = []
x1_plot.append(y[0])
x2_plot.append(y[0])
x3_plot.append(y[0])
t_plot.append(t)

#Cyklus vypočítávající hodnoty v čase
while t < T:
    y = y + dt * f(y, b1, b2, b3, t)
    t = t + dt

    #Uložení hodnot pro graf
    x1_plot.append(y[0])
    x2_plot.append(y[1])
    x3_plot.append(y[2])
    t_plot.append(t)


plt.plot(t_plot, x1_plot)
plt.plot(t_plot, x2_plot)
plt.plot(t_plot, x3_plot)
plt.xlabel('Čas [s]')
plt.ylabel('Výchylka [m]')
plt.title('Tlumené oscilace')
plt.grid()
plt.show()
