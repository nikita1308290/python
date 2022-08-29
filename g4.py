import pgzrun

WIDTH = 1200
HEIGHT = 700

#actor
p = Actor('char2', (50, 100))
q = Actor('char3', (500, 150))
speed = 5 #speed of movement
def draw():
    screen.fill('WHITE')
    p.draw()
    q.draw()

def update():
    player1_controls()
    player2_controls()

def player1_controls():
    if keyboard.UP and not p.top < 0:
        p.y +=-speed
    elif keyboard.DOWN and not p.bottom>HEIGHT:
        p.y +=speed
    elif keyboard.Left and not p.left<0:
        p.x +=-speed
    elif keyboard.RIGHT and not p.right>WIDTH:
        p.x +=speed
        p.angle = -10
    else:
        p.angle = 0

def player2_controls():
    if keyboard.W and not q.top < 0:
        q.x +=-speed
    elif keyboard.A and not q.left>HEIGHT:
        q.x +=speed
    elif keyboard.D and not q.right<0:
        q.y +=-speed
    elif keyboard.S and not q.bottom>WIDTH:
        q.y +=speed



pgzrun.go()