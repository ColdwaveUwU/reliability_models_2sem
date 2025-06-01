import numpy as np
import matplotlib.pyplot as plt

Tmodel = 10000
scale = 10  # θ
shape = 1   # для экспоненты (k = 1)

# Сумма трёх экспоненциальных величин ~ Gamma(3, 10)
values = np.random.exponential(scale, Tmodel) + \
         np.random.exponential(scale, Tmodel) + \
         np.random.exponential(scale, Tmodel)

# Бины, как в GPSS: от 0 до 40, шаг 2
bins = np.arange(0, 80, 2)

# Построение гистограммы
plt.hist(values, bins=bins, density=True, edgecolor='black', alpha=0.7)
plt.xlabel('Суммарное время')
plt.ylabel('Плотность вероятности')
plt.title('Сумма трёх Exponential(λ=1/10)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Вывод статистик
print(f"Среднее: {np.mean(values):.3f}")
print(f"Стандартное отклонение: {np.std(values):.3f}")
