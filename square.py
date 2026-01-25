import turtle
desenho = turtle.Turtle()
lado = int(input("Digite o tamanho do lado do quadrado: "))
for n in range(4):
    desenho.forward(lado)
    desenho.right(90)
turtle.done()