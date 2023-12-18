from typing import List

Vector = List[float]

height_weight_age = [70,  # polegadas,
                        170, # libras,
                        40]  # anos

grades = [95, # exame 1
            80, # exame 2
            75, # exame 3
            62] # exame 4

#soma de dois vetores - compacta com zip e list comprehension
def add(v: Vector, w: Vector) -> Vector:
    """Soma elementos correspondentes"""
    assert len(v) == len(w), "vetores precisam ter o mesmo tamanho"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

#subtrair dois vetores - compacta com zip e list comprehension
def subtract(v: Vector, w: Vector) -> Vector:
    """Subtrai elementos correspondentes"""
    assert len(v) == len(w), "vetores precisam ter o mesmo tamanho"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

#somar uma lista de vetores por componente
def vector_sum(vectors: List[Vector]) -> Vector:
    """Soma todos os elementos correspondentes"""
    # checa se o vetor nao esta vazio
    assert vectors, "vetores nao podem ser vazios"

    # checa se os vetores tem o mesmo tamanho
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "vetores de tamanhos diferentes"

    # a i-esima componente do resultado é a soma de todas as i-esimas componentes dos vetores
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

#multiplicar um vetor por um escalar
def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplica cada elemento por c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

#media de um vetor
def vector_mean(vectors: List[Vector]) -> Vector:
    """Computa a media dos elementos"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

#produto escalar de dois vetores
def dot(v: Vector, w: Vector) -> float:
    """Computa v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vetores precisam ter o mesmo tamanho"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32 # 1 * 4 + 2 * 5 + 3 * 6

#soma dos quadrados de um vetor
def sum_of_squares(v: Vector) -> float:
    """Retorna v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14 # 1 * 1 + 2 * 2 + 3 * 3

#magnitude (ou tamanho) de um vetor
import math

def magnitude(v: Vector) -> float:
    """Retorna a magnitude (ou tamanho) de v"""
    return math.sqrt(sum_of_squares(v)) # math.sqrt é a função de raiz quadrada

assert magnitude([3, 4]) == 5

#distancia entre dois vetores
def squared_distance(v: Vector, w: Vector) -> float:
    """Computa (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Computa a distancia entre v e w"""
    return math.sqrt(squared_distance(v, w))

#distancia entre dois vetores - mais facil
def distance(v: Vector, w: Vector) -> float: # type: ignore
    return magnitude(subtract(v, w))

