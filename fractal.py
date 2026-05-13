import turtle
import tkinter as tk

# Configuração inicial do ambiente
screen = turtle.Screen()
screen.setup(800, 800)
screen.colormode(255)
t = turtle.Turtle()
t.speed(0)

# --- 1. FÁCIL (200XP): ESPIRAL QUADRADA ---
# Desenho recursivo visual (auto-similar), menos de 6 linhas, sem função.
# A lógica de crescimento simula a recursão de forma iterativa.
def desenhar_facil():
    t.reset()
    for i in range(100):
        t.pencolor(i*2, 0, 255-i*2) # Mudança de cores progressiva
        t.forward(i * 3)
        t.left(91)

# --- 2. MÉDIO (300XP): ÁRVORE DE 3 RAMOS ---
# 6 a 15 linhas, usa função genérica (tamanho, ângulo, nível).
# Alteração: 3 ramos em vez dos 2 tradicionais de sala de aula.
def arvore_tripla(t, tam, ang, nivel):
    if nivel > 0:
        t.pencolor(0, 255 - (nivel * 30), 50) # Cores mudam conforme a profundidade
        t.forward(tam)
        t.left(ang)
        arvore_tripla(t, tam * 0.7, ang, nivel - 1) # Ramo Esquerda
        t.right(ang)
        arvore_tripla(t, tam * 0.7, ang, nivel - 1) # Ramo Centro
        t.right(ang)
        arvore_tripla(t, tam * 0.7, ang, nivel - 1) # Ramo Direita
        t.left(ang)
        t.backward(tam)

# --- 3. DIFÍCIL (400XP): TRIÂNGULO DE SIERPINSKI ---
# 15+ linhas, função separada para a forma geométrica base (triângulo).
# Função recursiva genérica com controle de profundidade e tamanho.

def desenhar_triangulo_base(t, tam):
    """Função obrigatória separada para a forma geométrica (Nível Difícil)"""
    for _ in range(3):
        t.forward(tam)
        t.left(120)

def fractal_sierpinski(t, tam, nivel):
    """Função recursiva principal"""
    if nivel == 0:
        t.fillcolor(255, nivel * 40, 100)
        t.begin_fill()
        desenhar_triangulo_base(t, tam)
        t.end_fill()
    else:
        # Lógica de subdivisão em 3 partes
        fractal_sierpinski(t, tam / 2, nivel - 1)
        t.forward(tam / 2)
        fractal_sierpinski(t, tam / 2, nivel - 1)
        t.backward(tam / 2)
        t.left(60)
        t.forward(tam / 2)
        t.right(60)
        fractal_sierpinski(t, tam / 2, nivel - 1)
        t.left(60)
        t.backward(tam / 2)
        t.right(60)

# --- EXTRA (200XP): SLIDER PARA ATUALIZAÇÃO ---
def atualizar_desenho(valor):
    """Atualiza a abertura da árvore em tempo real usando o slider"""
    angulo = int(valor)
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()
    turtle.tracer(0) # Desliga animação para atualizar instantaneamente
    arvore_tripla(t, 120, angulo, 4)
    turtle.update() # Renderiza o desenho final

# Integração do Slider com Tkinter
root = screen.getcanvas().master
frame = tk.Frame(root)
frame.pack(side="bottom")

tk.Label(frame, text="Ângulo da Árvore (Extra):").pack(side="left")
slider = tk.Scale(frame, from_=10, to=90, orient="horizontal", command=atualizar_desenho)
slider.set(30) # Valor inicial
slider.pack(side="left")

# Botões para ver os outros desenhos
tk.Button(frame, text="Desenho Fácil", command=desenhar_facil).pack(side="left")
tk.Button(frame, text="Sierpinski (Difícil)", 
          command=lambda: (t.reset(), fractal_sierpinski(t, 300, 4))).pack(side="left")

print("Use o slider e os botões na janela do Turtle para interagir.")
screen.mainloop()


