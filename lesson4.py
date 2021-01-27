"""Урок 4"""


def mean_x(ax, bx):
    return (ax + bx) / 2


def disp_x(ax, bx):
    return (bx - ax) ** 2 / 12


# 1. Случайная непрерывная величина A имеет равномерное распределение
# на промежутке (200, 800]. Найдите ее среднее значение и дисперсию.
# Решение:
a, b = 200, 800
DX = (800 - 200) ** 2 / 12
print('# Ответы 1:')
print(f'# Среднее значение M(X)={mean_x(a, b)}, Дисперсия D(X)={disp_x(a, b)}')
# Ответы 1:
# Среднее значение M(X)=500.0, Дисперсия D(X)=30000.0

# 2. О случайной непрерывной равномерно распределенной величине B известно,
# что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная,
# что левая граница равна 0.5?
# Если да, найдите ее.
# Решение:
DX = 0.2
a = 0.5
b = (DX * 12) ** 0.5 + a
print('# Ответы 2:')
print(f'# Правая граница b={b:.3f}, Среднее значение M(X)={mean_x(a, b):.3f}')
# Ответы 2:
# Правая граница b=2.049, Среднее значение M(X)=1.275

# 3. Непрерывная случайная величина X распределена нормально и
# задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2*pi))) * (exp(-(x+2)**2) / 32).
# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)
# Решение: исследуя формулу распределения плотности вероятности получаем:
# а). 2 = -a => M(X) = -2
# б). 32 = 2*D(X) => D(X)= 16
# в). sigma = 4 = sqrt(D(X)= 16) => std(X) = 4

# 4. Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.
# Решение: искать вероятность по таблицам - это не наш метод, используем пакет:
import scipy.stats as st

z_set = set()


def calc_z(x):
    mx, sigma = 174, 8
    z = (x - mx) / sigma
    z_set.add(z)
    return z


print('# Ответы 4:')
letters = 'абвгдеёж'
c = ['>', '>', ('>', '<'), ('>', '<'), ('>', '<'), ('<', '>'), ('<', '>'), '<']
h = [182, 190, (166, 190), (166, 182), (158, 190), (150, 190), (150, 198), 166]
for height, condition, symbol in zip(h, c, letters):
    if isinstance(height, tuple):
        p_value_low = st.norm.cdf(calc_z(height[0]))
        p_value_high = st.norm.cdf(calc_z(height[1]))
        if condition == ('>', '<'):
            ph = p_value_high - p_value_low
            cn = 'и'
        elif condition == ('<', '>'):
            ph = p_value_low + 1 - p_value_high
            cn = 'или'
        else:
            ph, cn = None, None
        situation = f'{condition[0]} {height[0]} {cn} {condition[1]} {height[1]}'
        print(f'# {symbol}). рост {situation} вероятность {ph:.5f} или {ph:.2%}')
    else:
        p_value = st.norm.cdf(calc_z(height))
        ph = 1 - p_value if condition == '>' else p_value
        print(f'# {symbol}). рост {condition} {height} вероятность {ph:.5f} или {ph:.2%}')

# для подтверждения правила трех сигм нужно было добавить условие:
# случайным образом выбранный взрослый человек имеет рост:
# з). от 150 см до 198 см
height, condition, symbol = (150, 198), ('>', '<'), 'з'
p_value_low = st.norm.cdf(calc_z(height[0]))
p_value_high = st.norm.cdf(calc_z(height[1]))
ph = p_value_high - p_value_low
situation = f'{condition[0]} {height[0]} и {condition[1]} {height[1]}'
print('# Подтверждение правила трех сигм:')
print(f'# {symbol}). рост {situation} вероятность {ph:.5f} или {ph:.2%}')

print('# Значения, используемые при расчетах:')
for z_value in sorted(z_set):
    p_value = st.norm.cdf(z_value)
    print(f'# z={z_value}, p={p_value:.4f}')
# Ответы 4:
# а). рост > 182 вероятность 0.15866 или 15.87%
# б). рост > 190 вероятность 0.02275 или 2.28%
# в). рост > 166 и < 190 вероятность 0.81859 или 81.86%
# г). рост > 166 и < 182 вероятность 0.68269 или 68.27%
# д). рост > 158 и < 190 вероятность 0.95450 или 95.45%
# е). рост < 150 или > 190 вероятность 0.02410 или 2.41%
# ё). рост < 150 или > 198 вероятность 0.00270 или 0.27%
# ж). рост < 166 вероятность 0.15866 или 15.87%
# Подтверждение правила трех сигм:
# з). рост > 150 и < 198 вероятность 0.99730 или 99.73%
# Значения, используемые при расчетах:
# z=-3.0, p=0.0013
# z=-2.0, p=0.0228
# z=-1.0, p=0.1587
# z=1.0, p=0.8413
# z=2.0, p=0.9772
# z=3.0, p=0.9987

# 5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?
# Решение
x, mx, dx = 190, 178, 25
z = (x - mx) / dx ** 0.5
print('# Ответ 5:')
print(f'# Pост человека {x}см при M(X)={mx}см и D(X)={dx}кв.см отклоняется на '
      f'{z} сигмы от математического ожидания')
# Ответ 5:
# Pост человека 190см при M(X)=178см и D(X)=25кв.см отклоняется на 2.4 сигмы от математического ожидания
