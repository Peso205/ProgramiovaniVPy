import numpy as np
import matplotlib.pyplot as plt

# Pravá strana rovnice y' = f(t, y)
f = lambda t, y: -y

# Exaktní řešení pro srovnání (pro y' = -y): y(t) = y0 * exp(-t)
exact = lambda t, y0: y0 * np.exp(-t)

# --- Směrové pole ---
T, Y = np.meshgrid(np.linspace(0, 5, 21), np.linspace(-2, 3, 21))
U = np.ones_like(T)          # jednotkový časový krok
V = f(T, Y)
N = np.hypot(U, V)           # normalizace šipek na stejnou délku
plt.quiver(T, Y, U / N, V / N, color='lightgray', angles='xy')

# --- Několik řešení (exaktních) protékajících polem ---
t = np.linspace(0, 5, 200)
for y0 in [-1.5, -0.5, 0.5, 1.5, 2.5]:
    plt.plot(t, exact(t, y0), 'b', lw=2)

plt.axhline(0, color='k', lw=0.5)
plt.xlabel('t')
plt.ylabel('y')
plt.title(r"Směrové pole $y' = -y$ a řešné křivky")
plt.xlim(0, 5)
plt.ylim(-2, 3)
plt.grid(alpha=0.3)
plt.show()