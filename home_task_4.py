

from scipy.stats import norm
# 1) Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
a = [200, 800]
m_x = (a[0] + a[-1]) / 2
d_x = (a[-1] - a[0]) / 12

print(f'M(x) = {m_x}')
print(f'D(x) = {d_x}')

# 2) О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.
d_x = 0.2
b = [0.5]
b.append(d_x * 12 + b[0])
m_x = (b[0] + b[-1]) / 2

print(f'Правая граница величины В = {b[1]}')
print(f'M(x) = {m_x}')

# 3) Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X)
m_x = -2

# в). std(X) (среднее квадратичное отклонение)
std_x = 4

# б). D(X)
d_x = std_x**2
print(f'M(x) = {m_x}, D(x) = {d_x}, std(x) = {std_x}')

# 4) Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
def z_score (p):
    m_x = 174
    std_x = 8
    return norm.cdf((p - m_x) / std_x)

# а). больше 182 см
result = (1 - z_score(182)) * 100
print(f'Вероятность того, что рост больше 182 см = {result}')

# б). больше 190 см
result = (1 - z_score(190)) * 100
print(f'Вероятность того, что рост больше 190 см = {result}')

# в). от 166 см до 190 см
result = (z_score(190) - z_score(166)) * 100
print(f'Вероятность того, что рост в пределах от 166 до 190 см = {result}')

# г). от 166 см до 182 см
result = (z_score(182) - z_score(166)) * 100
print(f'Вероятность того, что рост в пределах от 166 до 182 см = {result}')

# д). от 158 см до 190 см
result = (z_score(190) - z_score(158)) * 100
print(f'Вероятность того, что рост в пределах от 158 до 190 см = {result}')

# е). не выше 150 см или не ниже 190 см
result = (z_score(150) + 1 - z_score(190)) * 100
print(f'Вероятность того, что рост не выше 150 см или не ниже 190 см = {result}')

# ё). не выше 150 см или не ниже 198 см
result = (z_score(150) + 1 - z_score(198)) * 100
print(f'Вероятность того, что рост не выше 150 см или не ниже 198 см = {result}')

# ж). ниже 166 см.
result = z_score(166) * 100
print(f'Вероятность того, что рост ниже 166 см = {result}')

# 5) На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?