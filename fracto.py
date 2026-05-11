from turtle import*
import random
t=Turtle()

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
print(random_color())

def drawSquare(t, size):
    t.pd()
    t.begin.fill()
    t.fillcolor("blue")
    for i in range(4):
        t.fd(size)
        t.rt(90)
    t.end.fill()
    t.pu()

def drawSquareFractal(t, size, step = 50):
    if size == 0 or step == 0:
        return
    t.fd(size/1.5)
    t.lt(10)
    drawSquare(t, size)
    drawSquareFractal(t, size-1, step-1)#-3, step

colormode(255)
t.speed(0)

drawSquareFractal(t, 50)#200

def drawStarFractal(t, size):
    if size<10:
        return
    for i in range(5):
        t.fd(size)
        drawStarFractal
mainloop()   