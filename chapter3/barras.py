from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

#plote as arras com coordenadas x à esquerda [xs], coordenadas y [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("Meus filmes favoritos") #adiciona um título
plt.ylabel("# de Premiações") #adiciona um rótulo no eixo y

#rotulos no eixo x, com nomes dos filmes em barra centralizada
plt.xticks(range(len(movies)), movies)

plt.show()

#plotar histograma de valores agrupados
from collections import Counter
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

#agrupa as notas em intervalos de 10: 70-79, 80-89, 90-99, mas coloque 100 na categoria 90-99

histograma = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histograma.keys()], #desloca cada barra para a direita em 5
        histograma.values(), #dá para cada barra sua altura correta
        10, #dá para cada barra a largura de 10
        edgecolor=(0,0,0)) #preto

plt.axis([-5, 105, 0, 5]) #eixo x de -5 a 105, eixo y de 0 a 5

plt.xticks([10 * i for i in range(11)]) #rótulos do eixo x em 0, 10, ..., 100
plt.xlabel("Decil")
plt.ylabel("# de Alunos")
plt.title("Distribuição das Notas do Teste 1")
plt.show()