import numpy as np
import matplotlib.pyplot as plt

Tmodel = 10000
scale = 10  # mean for exponential = scale

fail_times = []

for _ in range(Tmodel):
    t1 = np.random.exponential(scale)
    t2 = np.random.exponential(scale)
    total_time = t1 + t2
    fail_times.append(total_time)

fail_times = np.array(fail_times)

# Табулируем по диапазону 0..40 с шагом 2, как у тебя в GPSS
bins = np.arange(0, 80, 2)

plt.hist(fail_times, bins=bins, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Время отказа')
plt.ylabel('Плотность вероятности')
plt.title('Распределение времени отказа (сумма 2 экспоненциальных)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print(f"Среднее: {np.mean(fail_times):.3f}")
print(f"Стандартное отклонение: {np.std(fail_times):.3f}")
