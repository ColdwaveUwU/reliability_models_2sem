import matplotlib.pyplot as plt
import numpy as np

t_vals = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
cum_percent = [32.91, 54.83, 69.62, 79.48, 85.86, 90.42, 93.54, 95.82, 97.22, 98.15,
               98.71, 99.09, 99.38, 99.55, 99.70]

r_gpss = [1 - cp / 100 for cp in cum_percent]

lambda_ = 0.1
t_analytic = np.linspace(0, 30, 300)
r_analytic = np.exp(-2 * lambda_ * t_analytic)

plt.figure(figsize=(10, 6))
plt.plot(t_analytic, r_analytic, label="Аналитическая формула: $e^{-2\\lambda t}$", color='blue')
plt.scatter(t_vals, r_gpss, color='red', label='Данные из GPSS (эмпирические)', zorder=5)

plt.xlabel("Время t (часы)")
plt.ylabel("Вероятность безотказной работы R(t)")
plt.title("Сравнение аналитической и эмпирической вероятности безотказной работы")
plt.grid(True)
plt.legend()
plt.show()
