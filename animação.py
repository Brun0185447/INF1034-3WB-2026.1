import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Exemplo Pygame - Sprites e Eventos")
clock = pygame.time.Clock()

# Carregando as imagens exigidas
# Imagem 1: Fundo executado constantemente
fundo = pygame.image.load('Orc.png').convert() 
fundo = pygame.transform.scale(fundo, (800, 600))

# Imagem 2: Personagem (executa movimento enquanto a tecla é pressionada)
personagem = pygame.image.load('Edit Hammer Bro.png').convert_alpha()
person_rect = personagem.get_rect()
person_rect.topleft = (100, 450)

# Imagem 3: Spritesheet e Animações (EXTRA: Esquerda/Direita e Pulo)
soldado = pygame.image.load('Soldier.png').convert_alpha()

# Configurações de física e movimento
velocidade = 5
pulando = False
altura_pulo = 15
gravidade = 1

# Variáveis de controle de animação
frame_atual = 0
tempo_animacao = 0
tempo_por_frame = 100 # milissegundos

def obter_frame(sheet, quadro, largura_frame, altura_frame, escala=2):
    """Extrai um quadro da spritesheet"""
    imagem = pygame.Surface((largura_frame, altura_frame), pygame.SRCALPHA)
    imagem.blit(sheet, (0, 0), (quadro * largura_frame, 0, largura_frame, altura_frame))
    return pygame.transform.scale(imagem, (largura_frame * escala, altura_frame * escala))

# Loop principal do jogo
rodando = True
direcao_direita = True

while rodando:
    # 1. A imagem do fundo deve ser executada constantemente
    tela.blit(fundo, (0, 0))

    # Eventos do Pygame (Essencial para a Imagem 3)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        # A Imagem 3 deve ser executada com UM CLIQUE ou AO PRESSIONAR UMA TECLA
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando:
                pulando = True

    # 2. A Imagem 2 se move enquanto pressiono a tecla, e para ao soltar
    teclas = pygame.key.get_pressed()
    
    # Movimentação do personagem e controle de animação
    movendo = False
    if teclas[pygame.K_LEFT]:
        person_rect.x -= velocidade
        direcao_direita = False
        movendo = True
    if teclas[pygame.K_RIGHT]:
        person_rect.x += velocidade
        direcao_direita = True
        movendo = True

    # Lógica de pulo (EXTRA)
    if pulando:
        person_rect.y -= altura_pulo
        altura_pulo -= gravidade
        if altura_pulo < -15:
            pulando = False
            altura_pulo = 15
            
    # Desenho da Imagem 2 (Parada ou em movimento)
    tela.blit(personagem, person_rect)

    # 3. EXTRA: Animações do personagem
    if movendo or pulando:
        tempo_animacao += clock.get_time()
        if tempo_animacao >= tempo_por_frame:
            tempo_animacao = 0
            frame_atual = (frame_atual + 1) % 4 # Supondo 4 quadros na spritesheet
            
    # Exibe a sprite do personagem animada (tamanho 32x32 na spritesheet)
    frame_sprite = obter_frame(soldado, frame_atual, 32, 32, escala=3)
    if not direcao_direita:
        frame_sprite = pygame.transform.flip(frame_sprite, True, False)
        
    tela.blit(frame_sprite, (person_rect.x, person_rect.y - 50))

    # Atualização da tela e controle de FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()