import turtle
tl = turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def moverParaPonto(ponto):
    tl.penup()
    tl.goto(ponto.x, ponto.y)
    tl.pendown()

tl.speed(1)

p1 = Ponto(100, 150)

moverParaPonto(p1)

turtle.done()
