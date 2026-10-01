import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

#Proměnné
k = 1.0
m = 1.0
xi = 0.1
F0 = 1.0
b = 2 * xi * np.sqrt(k*m)
omega = np.sqrt(k/m)

omegaBList = [0.7 * omega, 0.99 * omega, 1.3 * omega]

x0 = 0
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
def f(y, b, omegaBList, t):
    x = y[0:3]
    v = y[3:7]
    dxdt = v
    dvdt = -k/m * x - b/m * v + F0 * np.array([np.sin(omegaBList[0] * t), np.sin(omegaBList[1] * t), np.sin(omegaBList[2] * t)])
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
    y = y + dt * f(y, b, omegaBList, t)
    t = t + dt

    #Uložení hodnot pro graf
    x1_plot.append(y[0])
    x2_plot.append(y[1])
    x3_plot.append(y[2])
    t_plot.append(t)

#t_eval = np.arange(0, T, dt)
#sol = integrate.solve_ivp(f, [0, T], y, method="RK45" , args=(b, omegaBList), t_eval=t_plot)
 

#plt.plot(sol.t, sol.y[0], label=f'ωB = {omegaBList[0]:.2f}')
#plt.plot(sol.t, sol.y[1], label=f'ωB = {omegaBList[1]:.2f}')
#plt.plot(sol.t, sol.y[2], label=f'ωB = {omegaBList[2]:.2f}')

plt.plot(t_plot, x1_plot)
plt.plot(t_plot, x2_plot)
plt.plot(t_plot, x3_plot)
plt.xlabel('Čas [s]')
plt.ylabel('Výchylka [m]')
plt.title('Tlumené oscilace')
plt.legend([f'ωB = {omegaBList[0]:.2f}', f'ωB = {omegaBList[1]:.2f}', f'ωB = {omegaBList[2]:.2f}'])
plt.grid()
plt.show()
