from turtle import *
from random import randint
t = Turtle()

for _  in range(4):
    t.fd(300)
    t.goto(0, 0)
    t.lt(90)

def desenha_circulo(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(color)
    t.circle(tamanho)
    t.end_fill()
x = randint(200, 300)
y = randint(200, 300)

desenha_circulo(x, y, 50, "red")

def desenha_retângulo(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(color)
    t.fd(tamanho)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(tamanho)
    t.lt(90)
    t.fd(150)
    t.end_fill()
x = randint(-400, 200)
y = randint(-400, 200)

desenha_retângulo(x, y, 100, "green")

def desenha_triângulo(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(color)
    for _ in range(3):
       t.fd(tamanho)
       t.lt(120)
    t.end_fill()
x = randint(-400, -100)
y = randint(-400, -100)

desenha_triângulo(x, y, 100, "blue")

def desenha_estrela(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.fd(tamanho)
        t.rt(144)
    t.fd(35)
    for _ in range(5):
        t.fd(25)
        t.rt(75)
    t.end_fill()

x = randint(-200, 200)
y = randint(-200, 200)

desenha_estrela(x, y, 100, "yellow")

mainloop()
