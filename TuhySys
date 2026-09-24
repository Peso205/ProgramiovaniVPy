import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import time

# --- Tuhá rovnice ---
lam = 1000.0
f = lambda t, y: -lam * (y - np.cos(t))
t_span = (0.0, 10.0)
y0 = [0.0]

# Exaktní řešení (odvoditelné lineární ODE – pro kontrolu):
# y(t) = lam^2/(lam^2+1) * (cos t + sin t/lam) - lam^2/(lam^2+1) * exp(-lam t)
def exact(t):
    lam2 = lam**2
    return lam2/(lam2+1)*(np.cos(t) + np.sin(t)/lam) \
           - lam2/(lam2+1)*np.exp(-lam*t)

methods = ['RK45', 'BDF']
results = {}

for method in methods:
    tic = time.perf_counter()
    sol = solve_ivp(f, t_span, y0, method=method, rtol=1e-6, atol=1e-9)
    toc = time.perf_counter()
    results[method] = (sol, toc - tic)

# --- Graf ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8), sharex=True)

# Horní panel: řešení
t_fine = np.linspace(*t_span, 1000)
ax1.plot(t_fine, exact(t_fine), 'k', lw=2, label='exaktně')
for method, (sol, _) in results.items():
    ax1.plot(sol.t, sol.y[0], 'o', ms=3, label=method)
ax1.set_ylabel('y')
ax1.set_title(r"Tuhá rovnice $y' = -1000\,(y - \cos t)$")
ax1.legend()
ax1.grid(alpha=0.3)

# Dolní panel: velikost kroku v čase
for method, (sol, _) in results.items():
    dt = np.diff(sol.t)
    ax2.semilogy(sol.t[1:], dt, 'o', ms=3, label=method)
ax2.set_xlabel('t')
ax2.set_ylabel('velikost kroku h')
ax2.set_title('Velikost kroku (log škála)')
ax2.legend()
ax2.grid(alpha=0.3, which='both')

plt.tight_layout()
plt.show()

# --- Statistiky do komentáře ---
print(f"{'metoda':<8}{'počet kroků':>14}{'počet vyhodnocení f':>22}{'čas [s]':>10}")
for method, (sol, dt) in results.items():
    print(f"{method:<8}{len(sol.t):>14}{sol.nfev:>22}{dt:>10.4f}")