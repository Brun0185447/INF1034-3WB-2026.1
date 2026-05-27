import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Exemplo Pygame - Sprites e Eventos")
clock = pygame.time.Clock()

orc = pygame.image.load('Orc.png').convert() 
fundo = pygame.transform.scale(orc, (800, 600))

personagem = pygame.image.load('Edit Hammer Bro.png').convert_alpha()
personagem.get_rect().topleft = (100, 450)

soldado = pygame.image.load('Soldier.png').convert_alpha()

velocidade = 5
pulando = False
altura_pulo = 15
gravidade = 1

frame_atual = 0
tempo_animacao = 0
tempo_por_frame = 100 

def obter_frame(sheet, quadro, largura_frame, altura_frame, escala=2):
    imagem = pygame.Surface((largura_frame, altura_frame), pygame.SRCALPHA)
    imagem.blit(sheet, (0, 0), (quadro * largura_frame, 0, largura_frame, altura_frame))
    return pygame.transform.scale(imagem, (largura_frame * escala, altura_frame * escala))

running = True
direcao_direita = True

while running:
    screen.blit(fundo, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando:
                pulando = True
                
    teclas = pygame.key.get_pressed()    
    movendo = False
    if teclas[pygame.K_LEFT]:
        personagem.get_rect().x -= velocidade
        direcao_direita = False
        movendo = True
    if teclas[pygame.K_RIGHT]:
        personagem.get_rect().x += velocidade
        direcao_direita = True
        movendo = True

    if pulando:
        personagem.get_rect().y -= altura_pulo
        altura_pulo -= gravidade
        if altura_pulo < -15:
            pulando = False
            altura_pulo = 15
            
    screen.blit(personagem, personagem.get_rect())

    if movendo or pulando:
        tempo_animacao += clock.get_time()
        if tempo_animacao >= tempo_por_frame:
            tempo_animacao = 0
            frame_atual = (frame_atual + 1) % 4 
            
    frame_sprite = obter_frame(soldado, frame_atual, 32, 32, escala=3)
    if not direcao_direita:
        frame_sprite = pygame.transform.flip(frame_sprite, True, False)
        
    screen.blit(frame_sprite, (personagem.get_rect().x, personagem.get_rect().y - 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()