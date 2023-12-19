from Typing import List

Matrix = List[List[float]]

A = [[1, 2, 3],  # A has 2 rows and 3 columns
        [4, 5, 6]]

B = [[1, 2],     # B has 3 rows and 2 columns
        [3, 4],
        [5, 6]]

#verificar o numero de linhas e colunas de uma matriz
from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # number of elements in first row
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3) # 2 rows, 3 columns

Vector = List[float]

#retorna o numero de linhas de uma matriz
def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]             # A[i] is already the ith row

def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]          # jth element of row A_i
            for A_i in A]   # for each row A_i

#criar uma matriz
from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)             # given i, create a list
                for j in range(num_cols)]# [entry_fn(i, 0), ... ]
            for i in range(num_rows)]    # create one list for each i

#criar uma matriz identidade
def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 1, 0],
                                [0, 0, 0, 0, 1]]

#situacao antes
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
                (3, 4), (4, 5), (5, 6), (5, 7), (6, 8),
                (7, 8), (8, 9)]

#situacao depois
#user_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
                [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

assert friend_matrix[0][2] == 1, "0 e 2 sao amigos"
assert friend_matrix[0][8] == 0, "0 e 8 nao sao amigos"

friends_of_five = [i
                    for i, is_friend in enumerate(friend_matrix[5])
                    if is_friend]

assert friends_of_five == [4, 6, 7], "5 tem 3 amigos"

