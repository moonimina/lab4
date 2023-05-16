from algorithms import first_alg, second_alg, mean, deviation, cv, rand
from scipy import stats
import time
import timeit


for i in range(1, 11):
    f = first_alg(i*time.time(), 100)
    print('Первый способ:', f)
    m_f = mean(f)
    print('Среднее:', m_f)
    d_f = deviation(f, m_f)
    print('Отклонение:', d_f)
    cv_f = cv(d_f, m_f)
    print('Коэффициент вариации:', cv_f)
    if cv_f>33:
        print('Выборка неоднородна')
    else:
        print('Выборка однородна')

    # Inters - список для разбиения на интервалы области значений сл. величин
    # Inters = [0, 625, 1250, 1875, 2500, 3125, 3750, 4375, 5000, 5625, 6250, 6875, 7500, 8125, 8750, 9375, 10000] ---> [0,625)[625,1250)...[9375,10000]
    # C - список с количеством сл.величин, попавших в каждый интервал. Кол-во интервалов = len(Inters)-1
    Inters = [0, 625, 1250, 1875, 2500, 3125, 3750, 4375, 5000, 5625, 6250, 6875, 7500, 8125, 8750, 9375, 10000]
    C = [0] * (len(Inters) - 1)
    # Подсчет теоретической вероятности попасть в каждый интервал
    p = []
    for i in range(len(Inters) - 1):
        p.append((Inters[i + 1] - Inters[i]) / 10000)

    for k in range(100):
        # Подсчет количества сл. величин, попавших в каждый интервал
        for j in range(1, len(Inters)):
            my_filter = filter(lambda x: Inters[j - 1] <= x < Inters[j], f)
            C[j - 1] = len(list(my_filter))

        # Подсчет статистики Пирсона
    Pirson = sum([C[i] ** 2 / (100 * p[i]) for i in range(len(p))]) - 100
    print('Статистика Пирсона:', Pirson)
    # гипотеза простая -> N-1 степень свободы, где N - кол-во интервалов
    if Pirson >= stats.chi2.ppf(0.95, len(p) - 1):
        print('Отвергаем')
    else:
        print('Не отвергаем')

    s = second_alg(i*time.time(), 100)
    print('Второй способ:',s)
    m_s = mean(s)
    print('Среднее:', m_s)
    d_s = deviation(s, m_s)
    print('Отклонение:', d_s)
    cv_s = cv(d_s, m_s)
    print('Коэффициент вариации:', cv_s)
    if cv_s > 33:
        print('Выборка неоднородна')
    else:
        print('Выборка однородна')

    C = [0] * (len(Inters) - 1)
    for k in range(100):
        # Подсчет количества сл. величин, попавших в каждый интервал
        for j in range(1, len(Inters)):
            my_filter = filter(lambda x: Inters[j - 1] <= x < Inters[j], s)
            C[j - 1] = len(list(my_filter))

        # Подсчет статистики Пирсона
    Pirson = sum([C[i] ** 2 / (100 * p[i]) for i in range(len(p))]) - 100
    print('Статистика Пирсона:', Pirson)
    if Pirson >= stats.chi2.ppf(0.95, len(p) - 1):
        print('Отвергаем')
    else:
        print('Не отвергаем')

n_ = [1000, 5000, 10000, 100000, 500000, 1000000]
t_f, t_s, t_rand = [], [], []
for i in n_:
    time_start = timeit.default_timer()
    v = first_alg(i*time.time(), i)
    time_end = timeit.default_timer() - time_start
    t_f.append(time_end)
    time_start = timeit.default_timer()
    v = second_alg(i*time.time(), i)
    time_end = timeit.default_timer() - time_start
    t_s.append(time_end)
    time_start = timeit.default_timer()
    v = rand(i)
    time_end = timeit.default_timer() - time_start
    t_rand.append(time_end)
print('Первый способ:', t_f)
print('Второй способ:', t_s)
print('Стандартный способ:', t_rand)