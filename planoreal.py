from turtle import*
from math import *
from time import sleep
def raiz_u(x):
    return sqrt(x)

t = Turtle()
t.speed(0)

t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

t.color('red')
t.pu()
t.goto(0, raiz_u(0))
t.pd()
for x in range(1, 100):
    t.goto(2*x, 10*raiz_u(2*x))
sleep(3)
t.clear()

t.color('black')
t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

def funcao_a(x):
    return 1/x
t.color('blue')
t.pu()
t.goto(1, 100*funcao_a(1))
t.pd()
for x in range(2, 100):
    t.goto(2*x, 100*funcao_a(x))

t.pu()
t.goto(-100, 100*funcao_a(-100))
t.pd()
for x in range(-99, -1):
    t.goto(2*x, 100*funcao_a(x))
sleep(3)
t.clear()

t.color('black')
t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

t.color('green')
def funcao_b(x):
    return 2**x
t.pu()
t.goto(-5, funcao_b(-5))
t.pd()
for x in range(-97, -1):
    t.goto(x, 450*funcao_b(x))
sleep(3)
t.clear()

t.color('black')
t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

t.color('yellow')
def funcao_d(x):
    return 5 - x**2
t.pu()
t.goto(7, funcao_d(7))
t.pd()
for x in range(1, 12):
    t.goto(x, funcao_d(x))
sleep(3)
t.clear()

t.color('black')
t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

t.color('purple')
def funcao_e(x):
    return x**2 - 5*x + 6
t.pu()
t.goto(1, funcao_e(1))
t.pd()
for x in range(1, 20):
    t.goto(x, funcao_e(x))
sleep(3)
t.clear()

t.color('black')
t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

t.color('orange')
def funcao_f(x):
    return x**3 - x**2 -x + 1
t.pu()
t.goto(-1, funcao_f(-1))
t.pd()
for x in range(-1, 20):
    t.goto(x, funcao_e(x))
sleep(3)
t.clear()

mainloop()
