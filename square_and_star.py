""" Exemplo do desenho de formas gráficas complexas, 
utilizando funções do módulo turtle. """
import turtle
# Função para desenhar um quadrado
def desenha_quadrado(t, tamanho):
    for _ in range(4):
        t.forward(tamanho)
        t.right(90)
# Função para desenhar uma estrela de cinco pontas
def desenha_estrela(t, tamanho):
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)
# Configuração inicial da tartaruga
t = turtle.Turtle()
t.speed(1)  # Definir a velocidade de desenho
# Desenhar um quadrado
desenha_quadrado(t, 100)
# Mover a tartaruga para uma nova posição
t.penup()
t.goto(-150, 0)
t.pendown()
# Desenhar uma estrela
desenha_estrela(t, 100)
# Finalizar o desenho
turtle.done()