from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18,
                18, 16, 15, 15, 15, 15, 14, 14, 13, 13,
                13, 13, 12, 12, 11, 10, 10, 10, 10, 10]

friend_counts = Counter(num_friends)
xs = range(101)                         # valor máximo é 100
ys = [friend_counts[x] for x in xs]     # altura é apenas # de amigos
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histograma da Contagem de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("# de pessoas")
plt.show()

num_points = len(num_friends)           # 30

largest_value = max(num_friends)        # 100
smallest_value = min(num_friends)       # 10

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]       # 10
second_smallest_value = sorted_values[1]# 10
second_largest_value = sorted_values[-2]# 49

def mean(x):
    return sum(x) / len(x)

mean(num_friends)                       # 14.333333333333334

#os sublinhados significam funcoes privadas

def _median_odd(x):
    return sorted(x)[len(x) // 2]

def _median_even(x):
    sorted_x = sorted(x)
    hi_midpoint = len(x) // 2
    return (sorted_x[hi_midpoint - 1] + sorted_x[hi_midpoint]) / 2

def median(v):
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

print(median(num_friends))              # 15

#quantile
def quantile(x, p):
    """retorna o p-ésimo percentil em x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.10)             # 10
quantile(num_friends, 0.25)             # 13
quantile(num_friends, 0.75)             # 18
quantile(num_friends, 0.90)             # 100

#calcular a moda
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

mode(num_friends)                       # 10, 13, 15, 19

#dispersao

def data_range(x):
    return max(x) - min(x)

data_range(num_friends)                 # 90

#variancia

from scratch.linear_algebra import sum_of_squares

def de_mean(x):
    """desloca x subtraindo sua media (entao o resultado tem media 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """supoe que x tem pelo menos dois elementos"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

variance(num_friends)                   # 81.54

#desvio padrao

import math

def standard_deviation(x):
    return math.sqrt(variance(x))

standard_deviation(num_friends)         # 9.03

#interquartile range

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

interquartile_range(num_friends)        # 5

#correlacao

