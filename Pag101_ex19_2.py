import matplotlib.pyplot
# Dados para o gráfico

# Dados para o gráfico
subjets = ["PortuguÊs","Matemática","Tecnologias","Inglês"]
averg = [15.4,17.3,18.1,13.3]
matplotlib.pyplot.plot(subjets, averg, '-o', color="blue",
                        linewidth=3)
#Apresenta o titulo do gráfico
matplotlib.pyplot.title( 'Média das Notas por Disciplina - 2025/2026')
#Apresente o rótulo do eixo do y
matplotlib.pyplot.ylabel( 'Média das Notas' )
#Apresenta o rótulo do eixo do x
matplotlib.pyplot.xlabel ('Disciplinas')
#Apresenta a grelha do gráfico
matplotlib.pyplot.grid ()
#Apresenta o gráfico numa janela
matplotlib.pyplot.show ()

