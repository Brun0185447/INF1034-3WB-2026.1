import turtle
import tkinter as tk

screen = turtle.Screen()
screen.title("Fractais Recursivos")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.colormode(255)

# Desenho Fácil (Até 6 linhas, sem função)
# Fractal: Espiral Quadrada

def desenho_facil(tamanho=10):
    t.pu()
    t.goto(0, 0)
    t.pd()
    for i in range(50):
        t.fd(i * 5)
        t.rt(90)
sleep(3)
t.clear()

# Desenho Médio (6-15 linhas, com função)
# Fractal: Árvore Binária (Modificada: 3 ramos)

def arvore_recursiva(tamanho, angulo, t):
    if tamanho > 10:
        t.fd(tamanho)
        t.lt(angulo)
        arvore_recursiva(tamanho - 15, angulo, t)
        t.rt(angulo * 2)
        arvore_recursiva(tamanho - 15, angulo, t)
        t.lt(angulo)
        t.backward(tamanho)

def chamar_arvore(tamanho_base=100, angulo=30):
    t.clear()
    t.pu() 
    t.goto(0, -200)
    t.pd()
    t.lt(90)
    arvore_recursiva(tamanho_base, angulo, t)
    t.rt(90)
sleep(3)
t.clear()

# Desenho Difícil (15+ linhas, com função)
# Fractal: Tapete de Sierpinski Simplificado

def desenhar_quadrado(t, tamanho):
    """Desenha um quadrado preenchido"""
    t.begin_fill()
    for _ in range(4):
        t.fd(tamanho)
        t.rt(90)
    t.end_fill()

def sierpinski(t, tamanho, ordem):
    t.clear()
    if ordem == 0:
        desenhar_quadrado(t, tamanho)
    else:
        for _ in range(4):
            sierpinski(t, tamanho / 3, ordem - 1)
            t.fd(tamanho / 3)
            sierpinski(t, tamanho / 3, ordem - 1)
            t.fd(tamanho / 3)
            t.rt(90)
            t.fd(tamanho / 3)
            t.rt(90)
            t.fd(2 * tamanho / 3)
            t.rt(180)

def chamar_sierpinski(tamanho=300, ordem=2):
    t.clear()
    t.pu()
    t.goto(-150, 150)
    t.pd()
    sierpinski(t, tamanho, ordem)
sleep(3)
t.clear()

# Interatividade com Slider
def atualizar(val):
    # Escolha qual fractal atualizar (ex: o médio - árvore)
    param = float(val)
    chamar_arvore(tamanho_base=100, angulo=param)

# Janela de controle (Slider)
root = tk.Tk()
root.title("Controle")
slider = tk.Scale(root, from_=10, to=90, orient=tk.HORIZONTAL, command=atualizar)
slider.set(30)
slider.pack()

# Execução Inicial 
# chamar_facil()
# chamar_arvore()
chamar_sierpinski()

screen.mainloop()


