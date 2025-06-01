import numpy as np
import matplotlib.pyplot as plt

Tmodel = 100000  # увеличить для стабильности

shape_single = 2
scale_single = 5
shift = 0  # если есть сдвиг

# Вероятности прерываний — поставить реальные из GPSS (пример)
p_stop_after_1 = 0.3
p_stop_after_2 = 0.4
# p_stop_after_3 = 0.3 (оставшиеся случаи)

fail_times = []

for _ in range(Tmodel):
    t1 = shift + np.random.gamma(shape_single, scale_single)
    if np.random.rand() < p_stop_after_1:
        fail_times.append(t1)
        continue

    t2 = shift + np.random.gamma(shape_single, scale_single)
    if np.random.rand() < p_stop_after_2:
        fail_times.append(t1 + t2)
        continue

    t3 = shift + np.random.gamma(shape_single, scale_single)
    fail_times.append(t1 + t2 + t3)

fail_times = np.array(fail_times)

bins = np.arange(0, 60, 2)

plt.hist(fail_times, bins=bins, density=True, alpha=0.7, edgecolor='black')
plt.xlabel("Время отказа")
plt.ylabel("Плотность вероятности")
plt.title("Распределение времени отказа с прерыванием")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print("Среднее:", np.mean(fail_times))
print("Стандартное отклонение:", np.std(fail_times))
