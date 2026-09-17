import numpy as np

k = 5.
m = 3.

omega = np.sqrt(k/m)

A = np.array([
    [0., 1.],
    [-omega**2, 0.]
    ])
 
lam, C = np.linalg.eig(A)

print("Vlastni cisla", lam)
print("Vlastni vektory", C)

#Pocatecni podminky
x0 = 1.
v0 = 0.

X0 = np.array([x0, v0])
D = np.linalg.solve(C, X0)
print("Koeficienty D", D)

#Vypocet
t_pole = np.linspace(0., 10., 100)
x_pole = t_pole * 0.

i = 0
for t in t_pole:
    X = np.real(
            D[0]*C[:,0]*np.exp(lam[0]*t)
            +D[1]*C[:,1]*np.exp(lam[1]*t)
            )
    x_pole[i] = X[0]
    print(x_pole[i])
    i += 1

#Graf   
import matplotlib.pyplot as plt
plt.plot(t_pole, x_pole)
plt.title("Harmonicky oscilator")
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.grid()
plt.show()

print("Perioda oscilaci T = ", 2*np.pi/omega)