import pygame
import sys

# 1. Configurações Básicas
pygame.init()
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Exemplo de Animações Pygame")
RELOGIO = pygame.time.Clock()

# Função auxiliar para carregar e fatiar spritesheets
def carregar_spritesheet(arquivo, qtd_colunas, qtd_linhas, largura_frame, altura_frame):
    spritesheet = pygame.image.load(arquivo).convert_alpha()
    frames = []
    for linha in range(qtd_linhas):
        for coluna in range(qtd_colunas):
            x = coluna * largura_frame
            y = linha * altura_frame
            frame = spritesheet.subsurface(pygame.Rect(x, y, largura_frame, altura_frame))
            frames.append(frame)
    return frames

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Exemplo fictício de spritesheet: 160x50px, com 4 frames de 40x50px
        # Substitua 'megaman_spritesheet.png' pelo seu arquivo e ajuste as medidas
        self.frames_andando = carregar_spritesheet('megaman_spritesheet.png', 4, 1, 40, 50)
        
        self.imagem_atual = 0
        self.image = self.frames_andando[self.imagem_atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 200)
        
        self.velocidade = 5
        self.tempo_animacao = 0
        self.velocidade_animacao = 100 # milissegundos
        
        # Estados
        self.andando = False
        self.pulando = False

    def atualizar_animacao(self):
        if self.andando:
            self.tempo_animacao += RELOGIO.get_time()
            if self.tempo_animacao >= self.velocidade_animacao:
                self.tempo_animacao = 0
                self.imagem_atual = (self.imagem_atual + 1) % len(self.frames_andando)
                self.image = self.frames_andando[self.imagem_atual]
        else:
            self.imagem_atual = 0 # Frame estático
            self.image = self.frames_andando[self.imagem_atual]

    def update(self):
        # Movimentação contínua (pressionando a tecla)
        keys = pygame.key.get_pressed()
        self.andando = False # Reseta o estado
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
            self.andando = True
        
        # EXTRA: Movimentação para a esquerda
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
            self.andando = True

        self.atualizar_animacao()

    def pular(self):
        # Executado apenas uma vez ao apertar a tecla/clicar
        if not self.pulando:
            self.pulando = True
            # Adicione lógica de pulo aqui (ex: alterar self.rect.y)

# 2. Inicialização dos Objetos
grupo_personagem = pygame.sprite.Group()
jogador = Personagem()
grupo_personagem.add(jogador)

# 3. Game Loop
rodando = True
while rodando:
    TELA.fill((50, 50, 50)) # Cor de fundo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
        # Terceira animação: Executada com UM CLIQUE ou AO PRESSIONAR UMA TECLA
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Exemplo: Pressionar Espaço para pular
                jogador.pular()

    # Atualiza as posições e o estado da animação 
    grupo_personagem.update()

    # Desenha os sprites
    grupo_personagem.draw(TELA)

    pygame.display.flip()
    RELOGIO.tick(60)

pygame.quit()
sys.exit()