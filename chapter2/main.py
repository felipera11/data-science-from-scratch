#------------Formatacao----------------

#barra invertida para quebrar linha
two_plus_three = 2 + \
                    3

#listas
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


#------------Funcoes----------------

#funcao com argumentos especificados
def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

print(full_name("Joel", "Grus"))     # "Joel Grus"
print(full_name("Joel"))             # "Joel Something"
print(full_name(last="Grus"))        # "What's-his-name Grus"


#------------Strings----------------

#barra invertida para caracteres especiais
tab_string = "\t"   #representa o caractere tab
len(tab_string)     #1

#r para strings brutas
not_tab_string = r"\t" #representa os caracteres '\' e 't'
len(not_tab_string)    #2

#string de varias linhas com """ """
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

#f-strings
first_name = "Joel"
last_name = "Grus"

full_name1 = first_name + " " + last_name             # string addition
full_name2 = "{0} {1}".format(first_name, last_name) # string.format

full_name3 = f"{first_name} {last_name}"    #f-string

#------------Excecoes----------------
try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

#------------Listas----------------
 
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

list_length = len(integer_list)     # 3
list_sum    = sum(integer_list)     # 6

#elemento n de uma lista usando colchetes
x = list(range(10))     # the list [0, 1, ..., 9]

zero = x[0]         # equals 0, lists are 0-indexed
one = x[1]          # equals 1
nine = x[-1]        # equals 9, 'Pythonic' for last element
eight = x[-2]       # equals 8, 'Pythonic' for next-to-last element
x[0] = -1           # now x is [-1, 1, 2, 3, ..., 9]

#colchete para fatiar lista
first_three = x[:3]                 # [-1, 1, 2]
three_to_end = x[3:]                # [3, 4, ..., 9]
one_to_four = x[1:5]                # [1, 2, 3, 4]
last_three = x[-3:]                 # [7, 8, 9]
without_first_and_last = x[1:-1]    # [1, 2, ..., 8]
copy_of_x = x[:]                    # [-1, 1, 2, ..., 9]

#stride - terceiro argumento
every_third = x[::3]                 # [-1, 3, 6, 9]
five_to_three = x[5:2:-1]            # [5, 4, 3]

#operador in
1 in [1, 2, 3]      # True
0 in [1, 2, 3]      # False

#concatenar listas
x = [1, 2, 3]
x.extend([4, 5, 6])     # x is now [1,2,3,4,5,6]

#se nao quiser modificar a lista original
x = [1, 2, 3]
y = x + [4, 5, 6]       # y is [1, 2, 3, 4, 5, 6]; x is unchanged

#append adiciona um elemento no final da lista
x = [1, 2, 3]
x.append(0)      # x is now [1, 2, 3, 0]
y = x[-1]        # equals 0
z = len(x)       # equals 4

#desempacotamento de listas
x, y = [1, 2]    # now x is 1, y is 2

#descartar valor
_, y = [1, 2]    # now y == 2, didn't care about the first element

#------------Tuplas----------------

#tuplas sao imutaveis
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3      # my_list is now [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

#tuplas sao um jeito conveniente de retornar multiplos valores
def sum_and_product(x, y):
    return (x + y),(x * y)
sp = sum_and_product(2, 3)     # equals (5, 6)
s, p = sum_and_product(5, 10)  # s is 15, p is 50

#tuplas (e listas) podem ser usadas para atribuicao multipla
x, y = 1, 2     # now x is 1, y is 2
x, y = y, x     # Pythonic way to swap variables; now x is 2, y is 1

#------------Dicionarios----------------

#criar dicionario com chaves e valores
empty_dict = {}                         # Pythonic
empty_dict2 = dict()                    # less Pythonic
grades = { "Joel" : 80, "Tim" : 95 }    # dictionary literal

#obter valor de uma chave
joels_grade = grades["Joel"]            # equals 80

#KeyError se voce pedir uma chave que nao existe
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

#verificar se uma chave existe
joel_has_grade = "Joel" in grades       # True
kate_has_grade = "Kate" in grades       # False

#obter valor com get
joels_grade = grades.get("Joel", 0)      # equals 80
kates_grade = grades.get("Kate", 0)      # equals 0
no_ones_grade = grades.get("No One")     # default default is None

#atribuir valor
grades["Tim"] = 99                      # replaces the old value
grades["Kate"] = 100                    # adds a third entry
num_students = len(grades)              # equals 3

#dados estruturados
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

#chaves, valores e itens
tweet_keys = tweet.keys()       # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items = tweet.items()     # iterable for the (key, value) tuples

"user" in tweet_keys            # True, but uses a slow list in
"user" in tweet                 # more Pythonic, uses faster dict in
"joelgrus" in tweet_values      # True

document = {}
#defaultdict
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#excecao
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

#usando get
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

#defaultdict
from collections import defaultdict

word_counts = defaultdict(int)          # int() produces 0
for word in document:
    word_counts[word] += 1

#defaultdict com lista
dd_list = defaultdict(list)             # list() produces an empty list
dd_list[2].append(1)                    # now dd_list contains {2: [1]}

#defaultdict com dicionario
dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # { "Joel" : { "City" : Seattle"}}

#defaultdict com set
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0,1]}

#------------contadores----------------

from collections import Counter
c = Counter([0, 1, 2, 0])          # c is (basically) { 0 : 2, 1 : 1, 2 : 1 }

#forma mais simples de resolver o problema do word_counts
word_counts = Counter(document)

#Counter tem uma funcao chamada most_common que retorna uma lista de tuplas
#imprima as 10 palavras mais comuns e suas contagens
for word, count in word_counts.most_common(10):
    print(word, count)

#------------Sets----------------
#------------Conjuntos----------------

primes_below_10 = {2, 3, 5, 7}

#nao funciona com vazio - usar set
s = set()
s.add(1)        # s is now { 1 }
s.add(2)        # s is now { 1, 2 }
s.add(2)        # s is still { 1, 2 }
x = len(s)      # equals 2
y = 2 in s      # equals True
z = 3 in s      # equals False

#in é muito rapido em sets/conjuntos
hundreds_of_other_words = []  # required for the below code to run

stopwords_list = ["a","an","at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list     # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set      # very fast to check

#encontraremos itens distintos em uma colecao
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)                  # 6
item_set = set(item_list)                   # {1, 2, 3}
num_distinct_items = len(item_set)          # 3
distinct_item_list = list(item_set)         # [1, 2, 3]
#vai usar conjunto com menos frequencia que listas e dicionarios

#------------Controle de Fluxo----------------

#ternario
parity = "even" if x % 2 == 0 else "odd"

#while
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1

#for e in
#range(10) é a sequencia de numeros de 0 a 9
for x in range(10):
    print(f"{x} is less than 10")

#para logica mais complexa use continue e break
for x in range(10):
    if x == 3:
        continue    # go immediately to the next iteration
    if x == 5:
        break       # quit the loop entirely
    print(x)

#------------Veracidade----------------
#------------Verdadeiro, Falso e Nenhum----------------
    
one_is_less_than_two = 1 < 2          # equals True
true_equals_false = True == False     # equals False

#none indica um valor nulo, nao existente
x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"

def some_function_that_returns_a_string():
    return ""
#pode utilizar bool para procurar strings vazias, listas vazias, etc
s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

#ou
first_char = s and s[0] #and retorna o segundo valor se o primeiro for verdadeiro

#ou
safe_x = x or 0  #or retorna o primeiro valor se ele for verdadeiro

#com certeza é um numero
safe_x = x if x is not None else 0

#funcao all
all([True, 1, { 3 }])   # True
all([True, 1, {}])      # False, {} is falsy
any([True, 1, {}])      # True, True is truthy
all([])                 # True, no falsy elements in the list
any([])                 # False, no truthy elements in the list

#------------Ordenacao----------------
#------------Classificacao----------------

x = [4,1,2,3]
y = sorted(x)       # y is [1,2,3,4], x is unchanged'
x.sort()            # now x is [1,2,3,4]
#sorted e sorted organizam do menor para o maior por padrao

#organizar do maior para o menor - parametro Reverse = True
#organizar por valor absoluto
x = sorted([-4,1,-2,3], key=abs, reverse=True)    # is [-4,3,-2,1]

#organizar por comprimento de string
wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)

#------------List Comprehensions----------------
#------------Compreensoes de lista----------------

#transformar uma lista em outra lista
even_numbers = [x for x in range(5) if x % 2 == 0]      # [0, 2, 4]
squares      = [x * x for x in range(5)]                 # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]             # [0, 4, 16]

#transformar uma lista em um dicionario ou conjunto
square_dict = { x : x * x for x in range(5) }            # { 0:0, 1:1, 2:4, 3:9, 4:16 }
square_set  = { x * x for x in [1, -1] }                 # { 1 }

#nao precisa usar o valor da lista
zeros = [0 for _ in even_numbers]      # has the same length as even_numbers

#multiplos fors
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]            # 100 pairs (0,0) (0,1) ... (9,8), (9,9)

#usando resultados de um for dentro de outro
increasing_pairs = [(x, y)                       # only pairs with x < y,
                    for x in range(10)           # range(lo, hi) equals
                    for y in range(x + 1, 10)]   # [lo, lo + 1, ..., hi - 1]

#------------Testes Automatizados e Asserção----------------

#assertions
assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't" #com mensagem de erro

#declarar uma funcao que deve lancar uma assercao
def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1

#assercao nas entradas de uma funcao
def smallest_item(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)

#------------Objetos e Classes----------------

#sempre em PascalCase e com docstrings
class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    #construtor
    def __init__(self, count = 0):
        self.count = count

#criar um objeto
clicker1 = CountingClicker() # initial count is 0
clicker2 = CountingClicker(100) # initial count is 100
clicker3 = CountingClicker(count=100) # more explicit way of doing the same

#dunder = double underscore

#__repr__ para representacao de string
class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    #implementar metodos - api publica
    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times
    
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0

#utilizar o assert para testar
clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2" 
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

#heranca
class NoResetClicker(CountingClicker):
    #substituir o metodo reset
    def reset(self):
        pass # do nothing!

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"

#------------Iteradores e Geradores----------------

#utilizando yield para criar um gerador
def generate_range(n):
    i = 0
    while i < n:
        yield i # every call to yield produces a value of the generator
        i += 1

#geradores sao iteraveis
for i in generate_range(10):
    print(f"i: {i}")

#range é lento
def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1
#nao pode fazer isso sem break

#se a geracao de valores for muito cara, usar uma lista
        
#criar gerador com for entre parenteses
evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

#nenhum valor é gerado ate que seja pedido
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
#e assim por diante

#enumerate
names = ["Alice", "Bob", "Charlie", "Debbie"]

#not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

#also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

#Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {names[i]}")

#------------Aleatoriedade----------------

import random
random.seed(10) # set the seed to 10
print(random.random()) # 0.57140259469
random.seed(10) # reset the seed to 10
print(random.random()) # 0.57140259469 again

#random.randrange
random.randrange(10) # choose randomly from range(10) = [0, 1, ..., 9]
random.randrange(3, 6) # choose randomly from range(3, 6) = [3, 4, 5]

#random.shuffle
up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten) # [2, 5, 1, 9, 7, 3, 8, 6, 4, 0], for example

#random.choice
my_best_friend = random.choice(["Alice", "Bob", "Charlie"]) # "Bob" for example

#random.sample
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]

#multiplas chamadas de random
four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]
print(four_with_replacement) # [9, 4, 4, 2]

#------------Expressoes Regulares----------------

import re

re_examples = [                        # all of these are True, because
    not re.match("a", "cat"),              # * 'cat' doesn't start with 'a'
    re.search("a", "cat"),                 # * 'cat' has an 'a' in it
    not re.search("c", "dog"),             # * 'dog' doesn't have a 'c' in it
    3 == len(re.split("[ab]", "carbs")),   # * split on a or b to ['c','r','s']
    "R-D-" == re.sub("[0-9]", "-", "R2D2") # * replace digits with dashes
    ]

assert all(re_examples), "all the regex examples should be True"

#re.match é para encontrar correspondencias no inicio de uma string
#re.search é para encontrar uma correspondencia em qualquer lugar da string

#------------Zip e Argumentos Descompactados----------------

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
#zip cria pares de tuplas

pairs = [pair for pair in zip(list1, list2)] # is [('a', 1), ('b', 2), ('c', 3)]

#extrair os elementos de uma lista
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs) # letters is ('a', 'b', 'c'), numbers is (1, 2, 3)
#* executa o unpacking de argumentos
#mesmo que
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

#descompactar com qualquer funcao
def add(a, b): return a + b

add(1, 2)      # returns 3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")
add(*[1, 2])   # returns 3

#------------args e kwargs----------------

def doubler(f):
    #essa funcao retorna outra funcao
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8, "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

#nao funciona com mais de um argumento
def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")

#usar *args para passar um numero arbitrario de argumentos
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")
# prints
# unnamed args: (1, 2)
# keyword args: {'key2': 'word2', 'key': 'word'}

#dict pode ser usado para passar argumentos nomeados
def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = { "z" : 3 }
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"

#funcoes de alta ordem com argumentos arbitrarios
def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"
#só utilizar *args e **kwargs se for realmente necessario

#------------Anotacoes de Tipos----------------

def add(a, b):
    return a + b

assert add(10, 5) == 15,                  "+ is valid for numbers"
assert add([1, 2], [3]) == [1, 2, 3],     "+ is valid for lists"
assert add("hi ", "there") == "hi there", "+ is valid for strings"

#mas nao para tipos diferentes
try:
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")

#tipada estaticamente tem que ser declarada
def add(a: int, b: int) -> int:
    return a + b

add(10, 5)      # you'd like this to be OK
add("hi ", "there") # you'd like this to be not OK

#mypi aponta o erro de tipo antes de executar

#nao informativo
def dot_product(x, y):
    return sum(xi * yi for xi, yi in zip(x, y))

class Vector:
    def __init__(self, arg):
        self.arg = arg

#informativo
def dot_product(x: Vector, y: Vector) -> float:
    return sum(xi * yi for xi, yi in zip(x, y))

#------------Escrevendo Anotacoes de Tipo----------------

from typing import List

def total(xs: List[float]) -> float:
    return sum(total)

#tipos em variaveis
x: int = 5

#indicar dicas de tipo em linha
from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None # allowed to be either a float or None

#tipos compostos
from typing import Dict, Iterable, Tuple

#chaves sao strings e valores sao inteiros
counts: Dict[str, int] = {'data': 1, 'science': 2}

#lista de inteiros
lazy = True
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    evens = [0, 2, 4, 6, 8]

#tupla tem um tipo para cada elemento
triple: Tuple[int, float, int] = (10, 2.3, 5)

#representar funcoes de primeira classe
from typing import Callable

#repetidor é uma funcao que recebe dois argumentos - uma string e um inteiro - e retorna outra string
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"

#anotacoes de tipo sao objetos
Number = int
Numbers = List[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)

#------------Acabou----------------