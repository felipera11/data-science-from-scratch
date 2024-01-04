from typing import Tuple
import math

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Retorna mu e sigma correspondentes a uma Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# A função de distribuição cumulativa de uma variável aleatória
# é a probabilidade de que a variável aleatória seja menor ou igual a um determinado valor.

from scratch.probability import normal_cdf

# A probabilidade de que a variável aleatória seja menor ou igual a um determinado valor
normal_probability_below = normal_cdf

#está acima do limite se não estiver abaixo do limite
def normal_probability_above(lo: float,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    """A probabilidade de que uma N(mu, sigma) seja maior que lo."""
    return 1 - normal_cdf(lo, mu, sigma)

#está entre se for menor que hi, mas não menor que lo
def normal_probability_between(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """A probabilidade de que uma N(mu, sigma) seja maior que lo e menor que hi."""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

#está fora se não estiver entre
def normal_probability_outside(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """A probabilidade de que uma N(mu, sigma) não esteja entre lo e hi."""
    return 1 - normal_probability_between(lo, hi, mu, sigma)

from scratch.probability import inverse_normal_cdf

def normal_upper_bound(probability: float,
                          mu: float = 0,
                          sigma: float = 1) -> float:
     """Retorna z para que P(Z <= z) = probability"""
     return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> float:
         """Retorna z para que P(Z >= z) = probability"""
         return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
     """
     Retorna os limites simétricos (sobre a média) que contêm a probabilidade especificada
     """
     tail_probability = (1 - probability) / 2

     # limite superior deve ter a probabilidade da cauda superior
     upper_bound = normal_lower_bound(tail_probability, mu, sigma)

     # limite inferior deve ter a probabilidade da cauda inferior
     lower_bound = normal_upper_bound(tail_probability, mu, sigma)

     return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

print(mu_0, sigma_0)  # 500.0 15.811388300841896

lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)

print(lower_bound, upper_bound)  # 469.01026640487555 530.9897335951244

#limites de 95% baseados em suposições de probabilidade de 50% de que a moeda é justa
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0) # (469.01026640487555, 530.9897335951244)

#mu e sigma baseados em p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

#um erro tipo II significa que falhamos em rejeitar a hipótese nula,
# o que acontecerá quando X ainda estiver em nosso intervalo original
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability # 0.887

print(power) # 0.887

#p-value é a probabilidade sob a hipótese nula de obter um valor de teste extremo ou mais extremo do que o que realmente observamos

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
        """
        Quantas vezes a média de uma variável aleatória normalmente distribuída
        seria pelo menos tão extrema quanto x (em qualquer direção)?
        """
        if x >= mu:
            # se x for maior que a média, a cauda é maior que x
            return 2 * normal_probability_above(x, mu, sigma)
        else:
            # se x for menor que a média, a cauda é menor que x
            return 2 * normal_probability_below(x, mu, sigma)

two_sided_p_value(529.5, mu_0, sigma_0) # 0.062

import random

extreme_value_count = 0
for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0    # Contagem do número de caras
                    for _ in range(1000))                # em 1000 lançamentos
    if num_heads >= 530 or num_heads <= 470:             # e conte quantas são "extremas"
        extreme_value_count += 1

# p-value foi de 0,062 => ~62 extremos de 1000
#assert 59 < extreme_value_count < 65, f"{extreme_value_count}"

print(two_sided_p_value(531.5, mu_0, sigma_0)) # 0.0463

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

print(upper_p_value(524.5, mu_0, sigma_0)) # 0.0606

print(upper_p_value(526.5, mu_0, sigma_0)) # 0.0463

#intervalo de confiança de 95% para a probabilidade de sucesso da moeda

p_hat = 525 / 1000 # 0.525
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000) # 0.0158

print(normal_two_sided_bounds(0.95, mu, sigma)) # [0.4940, 0.5560]

#p-hacking

from typing import List

def run_experiment() -> List[bool]:
    """Lança uma moeda 1000 vezes, True = cara, False = coroa"""
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment: List[bool]) -> bool:
    """Usando o teste de 5% de significância"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)])

assert num_rejections == 46
print(num_rejections) # 46

def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
    """
    Retorna z-score de um teste A/B dado o número de conversões de cada
    """
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistic(1000, 200, 1000, 180) # -1.14
print(two_sided_p_value(z)) # 0.254

z = a_b_test_statistic(1000, 200, 1000, 150) # -2.94
print(two_sided_p_value(z)) # 0.003

def B(alpha: float, beta: float) -> float:
    """Uma função normalização para garantir que a probabilidade total seja 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0 or x >= 1: # sem suporte fora [0, 1]
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)

import matplotlib.pyplot as plt

xs = [x / 100 for x in range(100)]
plt.plot(xs, [beta_pdf(x, 1, 1) for x in xs], '-', label='Beta(1,1)')
plt.plot(xs, [beta_pdf(x, 10, 10) for x in xs], '--', label='Beta(10,10)')
plt.plot(xs, [beta_pdf(x, 4, 16) for x in xs], ':', label='Beta(4,16)')
plt.plot(xs, [beta_pdf(x, 16, 4) for x in xs], '-.', label='Beta(16,4)')
plt.legend()
plt.title("Densidades de probabilidade de priori Beta")
plt.show()


