import scipy.stats as stats
import numpy as np

# 2) Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные автоматическим станком, 
# имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, 
# проверить эту гипотезу, если в выборке из n=100 шариков 
# средний диаметр оказался равным 17.5 мм, 
# а дисперсия известна и равна 4 кв. мм.
m_1 = 17
m_2 = 17.5

n = 100
d = 4

z_score_fact = (m_2 - m_1) / (d**2 / n**0.5)
z_score_teor = stats.norm.ppf(0.95)
print(f'При z_score_fact = {z_score_fact}, z_score_teor = {z_score_teor} подтверждается 0 гипотеза')

# 3) Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%? (Провести двусторонний тест.)
x = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
m_x = np.mean(x)
std_x = np.std(x, ddof=1)

t_fact = (200 - m_x) / (std_x / len(x)**0.5)
t_teor = stats.t.ppf(0.005, len(x) - 1)
print(f'При t_fact = {t_fact}, t_teor = {t_teor} подтверждается 0 гипотеза')

# 4) Есть ли статистически значимые различия в росте дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160
