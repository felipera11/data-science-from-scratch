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

