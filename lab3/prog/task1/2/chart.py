import matplotlib.pyplot as plt
import numpy as np

# Параметры
lambda_ = 0.1
t_vals = np.arange(2, 60, 2)  # Временные точки: 2, 4, ..., 58
r_vals = np.exp(-2 * 0.1 * t_vals)  # R(t) = e^{-0.2t}

# Строим гистограмму
plt.figure(figsize=(12, 6))
bars = plt.bar(t_vals, r_vals, width=2, align='edge', color='skyblue', edgecolor='black', label='R(t) = $e^{-0.2t}$')


# Настройка графика
plt.xlabel("Время t (часы)")
plt.ylabel("Вероятность безотказной работы R(t)")
plt.title("Гистограмма R(t) = $e^{-0.2t}$")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
