import matplotlib.pyplot as plt

# Pedir ao utilizador o número de vendas para cada marca
marcas = ['Lexus', 'Mercedes', 'Toyota', 'Opel', 'BMW']
vendas = []
for marca in marcas:
    vendas.append(int(input(f"Insira o número de vendas anuais para {marca}: ")))

# Criar o gráfico de hastes (stem plot)
plt.figure(figsize=(10, 6))
plt.stem(marcas, vendas)
plt.grid(True)
plt.xlabel('Marcas de Automóveis')
plt.ylabel('Número de Vendas Anuais')
plt.title('Vendas Anuais de Automóveis por Marca')
plt.show()