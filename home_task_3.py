from my_library import combinations as combs

# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
# - среднее арифметическое, 
z = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
z.sort()
print(z)
avg_z = sum(z) / len(z)
print(f'Среднее арифметическое = {avg_z}')

# - смещенную и несмещенную оценки дисперсий для данной выборки.
biased_var = sum([(i - avg_z)**2 for i in z]) / len(z)
print(f'Смещенная оценка дисперсии = {biased_var}')

unbiased_var = sum([(i - avg_z)**2 for i in z]) / (len(z)-1)
print(f'Неcмещенная оценка дисперсии = {unbiased_var}')

# - среднее квадратичное отклонение, 
dev_g = biased_var**(0.5)
print(f'Среднее квадратическое отклонение для ген. совокупности = {dev_g}')

dev_selection = unbiased_var**(0.5)
print(f'Среднее квадратическое отклонение для выборки = {dev_selection}')

# В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?
# 1. ББ+БННН
# 2. БН+ББНН
# 3. НН+БББН
box_1 = 8
white = 5
box_2 = 12
pulled_1 = 2
pulled_2 = 4

result = (combs(pulled_1, white) / combs(pulled_1, box_1) 
        * combs(pulled_2 - 3, white) * combs(pulled_2 - 1, box_2 - white) / combs(pulled_2, box_2)
        
        + combs(pulled_1 - 1, white) * combs(pulled_1 - 1, box_1 - white) / combs(pulled_1, box_1) 
        * combs(pulled_2 - 2, white) * combs(pulled_2 - 2, box_2 - white) / combs(pulled_2, box_2)

        + combs(pulled_1, box_1 - white) / combs(pulled_1, box_1) 
        * combs(pulled_2 - 1, white) * combs(pulled_2 - 3, box_2 - white) / combs(pulled_2, box_2)
        )
print(f'Вероятность того, что 3 мяча белые = {result}')

# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: 
# a). первым спортсменом 
p_1 = 0.9
p_2 = 0.8
p_3 = 0.7

p_hit = (p_1 + p_2 + p_3) / 3
result = p_1 / 3 / p_hit
print(f'Вероятность выстрела 1 спортсменом = {result}')

# б). вторым спортсменом
result = p_2 / 3 / p_hit
print(f'Вероятность выстрела 2 спортсменом = {result}')

# в). третьим спортсменом.
result = p_3 / 3 / p_hit
print(f'Вероятность выстрела 3 спортсменом = {result}')

# В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, 
# а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: 
# a). на факультете A 
a = b = 1
c = a + b

p_a = 0.8
p_b = 0.7
p_c = 0.9

n = a + b + c
p_session = (p_a * a + p_b * b + p_c * c) / n
print(p_session)
result = p_a * a / n / p_session
print(f'Вероятность того, что студент учится на факультете А = {result}')

# б). на факультете B 
result = p_b * b / n / p_session
print(f'Вероятность того, что студент учится на факультете B = {result}')

# в). на факультете C?
result = p_c * c / n / p_session
print(f'Вероятность того, что студент учится на факультете C = {result}')

# Устройство состоит из трех деталей. 
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. 
# Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали 
p_1 = 0.1
p_2 = 0.2
p_3 = 0.25

result = p_1 * p_2 * p_3
print(f'Вероятность того, что из строя выйдут все детали = {result}')

# б). только две детали
result = (p_1 * p_2 * (1 - p_3)
        + (1 - p_1) * p_2 * p_3
        + p_1 * (1 - p_2) * p_3)
print(f'Вероятность того, что из строя выйдут только 2 детали = {result}')

# в). хотя бы одна деталь 
result = 1 - (1 - p_1) * (1 - p_2) * (1 - p_3)
print(f'Вероятность того, что из строя выйдет хотя бы одна деталь = {result}')

# г). от одной до двух деталей?
result = (p_1 * (1 - p_2) * (1 - p_3) 
        + (1 - p_1) * p_2 * (1 - p_3)
        + (1 - p_1) * (1 - p_2) * p_3
        
        * (p_1 * p_2 * (1 - p_3)
        + (1 - p_1) * p_2 * p_3
        + p_1 * (1 - p_2) * p_3))
print(f'Вероятность того, что из строя выйдут от 1 до 2 деталей = {result}')
