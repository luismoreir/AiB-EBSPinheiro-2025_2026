import turtle
t = turtle.Pen()
t.penup()
x=40
y=40
t.setpos(x,y)
t.pendown()
for m in range(100):
    t.forward(m*2)
    t.left(91)  