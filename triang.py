#make a triangle

from turtle import *
def triangle(side_length, color):
    fillcolor(color)
    begin_fill()
    for _ in range(3):
        forward(side_length)
        left(120)
    end_fill()
triangle(200, "blue")
done() 
