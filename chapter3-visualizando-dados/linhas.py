from matplotlib import pyplot as plt

#mostrar tendencias

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x,y in zip(variance, bias_squared)]
xs = [i for i,_ in enumerate(variance)]

#podemos fazer multiplas chamadas para plt.plot
#para mostrar multiplas séries no mesmo gráfico
plt.plot(xs, variance, 'g-', label='variance') #linha verde sólida
plt.plot(xs, bias_squared, 'r-.', label='bias^2') #linha com tracejado vermelho
plt.plot(xs, total_error, 'b:', label='total error') #linha com pontilhado azul

#porque atribuimos rótulos para cada série
#podemos obter uma legenda gratuita
#loc=9 significa "top center"
plt.legend(loc=9)
plt.xlabel("complexidade do modelo")
plt.xticks([])
plt.title("Compromisso entre Polarização e Variância")
plt.show()
