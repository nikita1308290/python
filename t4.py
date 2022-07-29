from turtle import *

speed(0)
side = 6
size = 150
pensize(5)
for i in range(side):
    pencolor('blue')
    forward(size)
    for i in range(6):
        pencolor('black')
        forward(75)
        pencolor('blue')
        circle(25)
        pencolor('black')
        left(360/6)
    left(360/side)
mainloop()