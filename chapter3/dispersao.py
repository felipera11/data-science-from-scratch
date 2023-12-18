from matplotlib import pyplot as plt

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

#nomeia cada posição
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                xy=(friend_count, minute_count), #coloca o rótulo com sua posição
                xytext=(5,-5), #mas compensa um pouco
                textcoords='offset points')
    
plt.title("Minutos Diários vs. Número de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("minutos diários passados no site")
plt.show()

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [ 100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Os eixos são compatíveis")
plt.xlabel("nota do teste 1")
plt.ylabel("nota do teste 2")
plt.axis("equal")
plt.show()
