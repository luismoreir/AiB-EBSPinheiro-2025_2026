""" Exemplo do desenho de formas gráficas complexas, 
utilizando funções do módulo turtle. """
import turtle
# Função para desenhar uma circuferência
def desenha_circulo(t, raio):
    t.circle(raio)
    
def circunferencia(cor,x,y,veloc,raio):
    for angle in range(0, 360, 15):
        turtle.goto(x, y)
        turtle.color(cor)
        turtle.speed(veloc)
        turtle.seth(angle)
        turtle.circle(raio)
        
# Configuração inicial da tartaruga
turtle.reset()
circunferencia("red",0,0,100,100)
circunferencia("black",-100,0,100,40)
circunferencia("green",0,-100,100,40)
circunferencia("gray",100,0,100,40)
circunferencia("blue",0,100,100,40)
turtle.goto(-100,0)
# Finalizar o desenho
turtle.done()