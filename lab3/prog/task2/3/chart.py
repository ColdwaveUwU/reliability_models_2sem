import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Данные из таблицы T с добавленным последним интервалом
time_intervals = np.array([
    2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
    42,44,46,48,50,52,54,56,58,60
])

cum_percent = np.array([
    0.12,1.34,3.55,8.19,15.77,22.25,29.34,38.39,46.70,54.16,
    61.25,66.99,72.13,76.77,79.46,84.11,87.53,90.22,92.54,93.77,
    95.35,97.43,98.04,98.66,98.66,99.27,99.63,99.76,99.76,100.00
]) / 100  # в долях

# Эмпирическая функция безотказной работы
R_empirical = 1 - cum_percent

# Параметры гамма-распределения, рассчитанные из MEAN и STD.DEV.
mean_sim = 20.803
std_sim = 10.642

m = (mean_sim / std_sim) ** 2       # shape
theta = std_sim / np.sqrt(m)        # scale

print(f"Параметры гамма-распределения: shape (m) = {m:.2f}, scale (theta) = {theta:.2f}")

# Теоретическая функция безотказной работы для гамма-распределения
R_theoretical = 1 - gamma.cdf(time_intervals, a=m, scale=theta)

# График сравнения
plt.figure(figsize=(10,6))
plt.step(time_intervals, R_empirical, where='post', label='Эмпирическая ВБР из GPSS', linewidth=2)
plt.plot(time_intervals, R_theoretical, 'r--', label=f'Теоретическая ВБР Gamma(m={m:.2f}, scale={theta:.2f})', linewidth=2)

plt.xlabel('Время, t')
plt.ylabel('Вероятность безотказной работы R(t)')
plt.title('Сравнение эмпирической и теоретической функции безотказной работы')
plt.legend()
plt.grid(True)
plt.show()
