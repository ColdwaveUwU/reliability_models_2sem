import numpy as np
import matplotlib.pyplot as plt

Tmodel = 10000
shape = 2    # k
scale = 5    # θ

# Сумма двух гамма-распределенных случайных величин
values = np.random.gamma(shape, scale, Tmodel) + np.random.gamma(shape, scale, Tmodel)

# Бины по GPSS: от 0 до 40 с шагом 2
bins = np.arange(0, 80, 2)

# Гистограмма
plt.hist(values, bins=bins, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Время отказа')
plt.ylabel('Плотность вероятности')
plt.title('графика вероятности безотказной работы ')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Статистики
print(f"Среднее: {np.mean(values):.3f}")
print(f"Стандартное отклонение: {np.std(values):.3f}")
