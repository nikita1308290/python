import pgzrun

WIDTH = 500
HEIGHT = 500


box = Rect((50,150), (50,100))
box2 = Rect((105,150), (50,50))

def draw():
    screen.fill('White')
    screen.draw.text('hola amigos', (50, 50), color='Blue')
    screen.draw.text('this is game programming', (50,80), color='green', fontsize=30)
    screen.draw.rect(box, color='green')
    screen.draw.filled_rect(box2, color='red')

def update():
    box.x +=4
    box2.y +=4

pgzrun.go()