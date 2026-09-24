import numpy as np
import matplotlib.pyplot as plt

# --- Definice úlohy ---
f = lambda t, y: -y          # y' = -y
exact = lambda t: np.exp(-t) # exaktní řešení, y(0) = 1
t_end = 5.0

# --- Metody (fixní krok) ---
def euler(f, t0, y0, h, n):
    t = t0
    y = y0
    ts, ys = [t], [y]
    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h
        ts.append(t)
        ys.append(y)
    return np.array(ts), np.array(ys)

def rk4(f, t0, y0, h, n):
    t = t0
    y = y0
    ts, ys = [t], [y]
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h/2, y + h/2 * k1)
        k3 = f(t + h/2, y + h/2 * k2)
        k4 = f(t + h,   y + h   * k3)
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        ts.append(t)
        ys.append(y)
    return np.array(ts), np.array(ys)

# --- Srovnání pro různé kroky ---
steps = [0.5, 0.25]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Levý panel: řešení
t_fine = np.linspace(0, t_end, 400)
ax1.plot(t_fine, exact(t_fine), 'k', lw=2, label='exaktně $e^{-t}$')

for h in steps:
    n = int(round(t_end / h))
    te, ye = euler(f, 0, 1.0, h, n)
    tr, yr = rk4(f, 0, 1.0, h, n)
    ax1.plot(te, ye, 'o--', label=f'Euler, h={h}')
    ax1.plot(tr, yr, 's--', label=f'RK4, h={h}')

ax1.set_xlabel('t')
ax1.set_ylabel('y')
ax1.set_title('Řešení')
ax1.legend()
ax1.grid(alpha=0.3)

# Pravý panel: globální chyba
for h in steps:
    n = int(round(t_end / h))
    te, ye = euler(f, 0, 1.0, h, n)
    tr, yr = rk4(f, 0, 1.0, h, n)
    ax2.semilogy(te, np.abs(ye - exact(te)), 'o--', label=f'Euler, h={h}')
    ax2.semilogy(tr, np.abs(yr - exact(tr)), 's--', label=f'RK4, h={h}')

ax2.set_xlabel('t')
ax2.set_ylabel('|chyba|')
ax2.set_title('Globální chyba (log škála)')
ax2.legend()
ax2.grid(alpha=0.3, which='both')

plt.tight_layout()
plt.show()