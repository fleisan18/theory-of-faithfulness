import sys
sys.path.insert(1, 'C:/Users/1645295/Desktop/Разработчик/Теория вероятности/Семинар 1/')
import my_library

# 1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
# Стрелок выстрелил 100 раз. 
# Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
result = my_library.Bernoulli(k = 85, n = 100, p = 0.8)
print(f'Вероятность того, что стрелок попадет в цель 85 раз = {result}')

# 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность, что ни одна из них не перегорит в первый день? 
result = my_library.Poisson_distribution(k = 0, n = 5000, p = 0.0004)
print(f'Вероятность того, что ни одна из лампочек не перегорит в 1 день = {result}')

# Какова вероятность, что перегорят ровно две?

# 3. Монету подбросили 144 раза. 
# Какова вероятность, что орел выпадет ровно 70 раз?

# 4. В первом ящике находится 10 мячей, из которых 7 - белые. 
# Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. 
# Какова вероятность того, что все мячи белые? 
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?