import numpy as np

k = 1.
m = 2.

omega = np.sqrt(k/m)

A = np.array([
    [0., 1.],
    [-omega**2, 0.]
    ])
 
lam, C = np.linalg.eig(A)

print("Vlastni cisla", lam)
print("Vlastni vektory", C)