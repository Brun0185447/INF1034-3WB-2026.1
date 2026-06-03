import pygame
import sys

# Inicialização
pygame.init()
LARGURA, ALTURA = 800, 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo Side-Scroller com Pygame')
clock = pygame.time.Clock()

mapa=[
    "................T",
    "................T",
    ".......TTT......T",
    "................T",
    "..TTT...........T",
    "................T",
    ".......TTT......T",
    ".T..............T",
    "TTTTTTTTTTTTTTTTT",
] carregar_mapa('mapa.txt')

# Carregar o mapa a partir de um arquivo .txt
def carregar_mapa(arquivo):
    with open(arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines()]


TIPO_TILE = 40  # Tamanho do tile em pixels

# --- CLASSES DO JOGO ---

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # EXTRA: Dicionário para acessar o corte / estados diretamente
        # (Ideal para quando carregar a imagem principal)
        self.animacoes = {
            'idle': pygame.Surface((32, 48)), 
            'run': pygame.Surface((32, 48)),
            'jump': pygame.Surface((32, 48))
        }
        # Apenas para fins visuais neste exemplo (usar imagens reais depois)
        self.animacoes['idle'].fill((255, 0, 0)) # Vermelho: parado
        self.animacoes['run'].fill((0, 255, 0))   # Verde: correndo
        self.animacoes['jump'].fill((0, 0, 255))  # Azul: pulando

        self.image = self.animacoes['idle']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Movimento e Física
        self.vel_x = 0
        self.vel_y = 0
        self.gravidade = 0.8
        self.velocidade_jogador = 5
        self.forca_pulo = -15
        self.no_chao = False
        self.direcao = 1 # 1 = direita, -1 = esquerda

    def movimentar(self):
        self.vel_x = 0
        keys = pygame.key.get_pressed()

        # Esquerda e Direita
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.velocidade_jogador
            self.direcao = -1
        if keys[pygame.K_RIGHT]:
            self.vel_x = self.velocidade_jogador
            self.direcao = 1

        # Pulo (disponível quando estiver no chão)
        if keys[pygame.K_SPACE] and self.no_chao:
            self.vel_y = self.forca_pulo
            self.no_chao = False

        # Gravidade
        self.vel_y += self.gravidade
        self.rect.y += self.vel_y

    # Colisão usando a função ensinada em sala: rect.colliderect()
    def aplicar_colisoes(self, eixo, blocos):
        if eixo == 'x':
            for bloco in blocos:
                if self.rect.colliderect(bloco.rect):
                    if self.vel_x > 0: # Indo para a direita
                        self.rect.right = bloco.rect.left
                    if self.vel_x < 0: # Indo para a esquerda
                        self.rect.left = bloco.rect.right
        
        if eixo == 'y':
            for bloco in blocos:
                if self.rect.colliderect(bloco.rect):
                    if self.vel_y > 0: # Caindo
                        self.rect.bottom = bloco.rect.top
                        self.vel_y = 0
                        self.no_chao = True
                    elif self.vel_y < 0: # Pulando e batendo a cabeça
                        self.rect.top = bloco.rect.bottom
                        self.vel_y = 0

    def atualizar_animacao(self):
        # Seleciona o estado utilizando o dicionário de animações
        if not self.no_chao:
            self.image = self.animacoes['jump']
        elif self.vel_x != 0:
            self.image = self.animacoes['run']
        else:
            self.image = self.animacoes['idle']
            
        # Caso o jogador vire para a esquerda, espelha a imagem
        if self.direcao == -1:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self, blocos):
        self.movimentar()
        self.aplicar_colisoes('x', blocos)
        self.aplicar_colisoes('y', blocos)
        self.atualizar_animacao()

class Bloco(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TIPO_TILE, TIPO_TILE))
        self.image.fill((100, 100, 100)) # Cinza para obstáculo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Camera:
    def __init__(self, largura_mapa, altura_mapa):
        self.camera = pygame.Rect(0, 0, largura_mapa, altura_mapa)
        self.largura = largura_mapa
        self.altura = altura_mapa

    def aplicar(self, entidade):
        return entidade.rect.move(self.camera.topleft)

    def atualizar(self, alvo):
        # Centraliza a câmera no personagem
        x = -alvo.rect.x + int(LARGURA / 2)
        y = -alvo.rect.y + int(ALTURA / 2)

        # Limita a câmera para não mostrar fora do mapa
        x = min(0, x)  # Limite esquerdo
        x = max(-(self.largura - LARGURA), x) # Limite direito
        y = min(0, y)  # Limite superior
        y = max(-(self.altura - ALTURA), y) # Limite inferior

        self.camera = pygame.Rect(x, y, self.largura, self.altura)

# --- CARREGAR O CENÁRIO ---

todas_as_sprites = pygame.sprite.Group()
blocos = pygame.sprite.Group()

largura_mapa = len(mapa[0]) * TIPO_TILE
altura_mapa = len(mapa) * TIPO_TILE

# Montando o mapa
for i, linha in enumerate(mapa):
    for j, caractere in enumerate(linha):
        if caractere == 'T':
            bloco = Bloco(j * TIPO_TILE, i * TIPO_TILE)
            blocos.add(bloco)
            todas_as_sprites.add(bloco)

# Personagem spawnando no topo
player = Jogador(50, 50)
todas_as_sprites.add(player)

camera = Camera(largura_mapa, altura_mapa)

# --- GAME LOOP ---
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30)) # Cor de fundo da fase

    # Atualizações
    player.update(blocos)
    camera.atualizar(player)

    # Desenho com a câmera aplicada
    for sprite in todas_as_sprites:
        screen.blit(sprite.image, camera.aplicar(sprite))

    pygame.display.update()
    clock.tick(60
