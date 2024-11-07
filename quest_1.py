import turtle
t = turtle.Turtle()

class forma:
    def desenhar(self):
        t.penup()
        t.forward(200)
        t.color('#ad1010')
        t.pensize(5)
        t.pendown()
        t.right(180)
        t.forward(400)
        t.penup()
        for _ in range(2):
            t.right(90)
            t.forward(200)
        t.pendown()
        t.right(90)
        t.forward(400)
        
class circulo(forma):
    def desenhar(self):
        t.left(90)
        t.color('#107fe0')
        t.circle(200)
        
class quadrado(forma):
    def desenhar(self):
        t.color('#7114e3')
        t.penup
        t.forward(200)
        t.pendown
        for _ in range(4):
            t.left(90)
            t.forward(400)
        
forma = forma()
circulo = circulo()
quadrado = quadrado()
forma.desenhar()
circulo.desenhar()
quadrado.desenhar()

turtle.done()