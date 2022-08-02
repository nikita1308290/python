from turtle import *

start = 200
goto(-150, -150)
while start > 0 :
    forward(start)
    left(360/5)
    start -= 5
    write(start, font=('Arial', 8, 'normal'))
mainloop()