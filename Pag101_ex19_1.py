'''Exemplo da elaboração de um gráfico, utilizando funções do módulo pyplot da
biblioteca matplotlib'''

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Dados para o gráfico
countrys = ["Portugal","Brasil","Alemanha","França","Bélgica"]
scores = [10,5,7,4,9]

bar_labels = countrys
bar_colors = ['blue', 'green', 'red', 'purple', 'orange']

ax.bar(countrys, scores, label=bar_labels,color=bar_colors)
ax.set_ylabel('Pontuações')
ax.set_title('Campeonato do Mundo de Futebol')
ax.set_xlabel('País')
ax.legend(title='Cores do País')
plt.show()

