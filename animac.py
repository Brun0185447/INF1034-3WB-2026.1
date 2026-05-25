import pygame
import os

# 1. Configurações Iniciais
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desafio de Animações Pygame")

clock = pygame.time.Clock()
FPS = 60

# 2. Carregamento de Imagens (Simulação)
# Substitua os caminhos abaixo pelos nomes reais dos seus arquivos
HERO_IDLE = [pygame.Surface((64, 64))] # Animação 1 constante
HERO_WALK = [pygame.Surface((64, 64))] # Animação 2 pressionando
HERO_JUMP = [pygame.Surface((64, 64))] # Animação 3 ao clicar/pressionar

# Se tiver imagens reais, descomente e ajuste:
# HERO_IDLE = [pygame.image.load("hero_walk 1.png"), pygame.image.load("hero_walk 2.png"), pygame.image.load("hero_walk 3.png")]

# Carregando Spritesheet (Exemplo conceitual para ler pedaços de uma imagem única)
def get_sprite(spritesheet, x, y, largura, altura):
    frame = pygame.Surface((largura, altura))
    frame.blit(spritesheet, (0, 0), (x, y, largura, altura))
    return frame

# try:
#     megaman = pygame.image.load("megaman_spritesheet.png").convert_alpha()
#     HERO_WALK = [get_sprite(megaman, 0, 0, 32, 32), get_sprite(megaman, 32, 0, 32, 32)]
# except FileNotFoundError:
#     pass

# 3. Variáveis de estado e movimento
pos_x, pos_y = 100, 400
velocidade = 5
direcao_x = 1 # 1 para direita, -1 para esquerda

# Pulo
pulando = False
gravidade = 1
velocidade_pulo = 15
altura_pulo = velocidade_pulo

# Controle de Animações
frame_atual = 0
tempo_animacao = 0
velocidade_animacao = 10 # Controla a velocidade do frame

# 4. Loop Principal
rodando = True
animacao_ativa = 3 # Controla qual animação é acionada por evento

while rodando:
    clock.tick(FPS)
    tempo_animacao += 1

    # --- EVENTOS (Input do Usuário) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
        # Animação 3: Acionada por UM CLIQUE ou PRESSIONAR uma vez (EVENTO)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not pulando:
                pulando = True
                animacao_ativa = 3 # Atribui a animação de pulo
    
    # Animação 2: Executada ENQUANTO a tecla estiver pressionada
    keys = pygame.key.get_pressed()
    andando = False
    
    if keys[pygame.K_LEFT]:
        pos_x -= velocidade
        direcao_x = -1
        andando = True
    elif keys[pygame.K_RIGHT]:
        pos_x += velocidade
        direcao_x = 1
        andando = True

    # --- LÓGICA DE MOVIMENTO E FÍSICA ---
    if pulando:
        pos_y -= altura_pulo
        altura_pulo -= gravidade
        if altura_pulo < -velocidade_pulo:
            pulando = False
            altura_pulo = velocidade_pulo

    # --- LÓGICA DE ANIMAÇÃO ---
    if anda: 
        # Lógica para animação 2 (andando)
        pass
    # elif pulando:
        # Lógica para animação 3 (pulando)
        pass
    else:
        # Animação 1: Constante (Idle)
        pass

    # --- RENDERIZAÇÃO ---
    tela.fill((30, 30, 30)) # Fundo cinza
    
    # Desenho simples (substitua pela imagem atual do seu herói/spritesheet)
    pygame.draw.rect(tela, (255, 0, 0), (pos_x, pos_y, 50, 50)) 
    
    pygame.display.flip()

pygame.quit()
