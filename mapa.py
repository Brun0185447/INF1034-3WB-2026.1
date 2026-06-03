import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo Side-Scroller')
clock = pygame.time.Clock()
tile_size = 40

mapa=[
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                        W",
"W                                        W",
"W                                        W",
"W         P            P                 W",
"W       PPPPP        PPPPP               W",
"W                                        W",
"W                                        W",
"W                    P                   W",
"W                  PPPPP                 W",
"W       P                        P       W",
"W     PPPPP                    PPPPP     W",
"W                                        W",
"W                                        W",
"W                                        W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

def carregar_mapa(mapa):
    with open(mapa, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

class Camera:
    def __init__(self, largura_mapa, altura_mapa):
        self.camera = pygame.Rect(0, 0, largura_mapa, altura_mapa)
        self.largura = largura_mapa
        self.altura = altura_mapa

    def aplicar(self, entidade):
        return entidade.rect.move(self.camera.topleft)

    def aplicar_posicao(self, pos_x, pos_y):
        return pos_x + self.camera.x, pos_y + self.camera.y

    def atualizar(self, alvo):
        x = -alvo.rect.x + int(400)
        y = -alvo.rect.y + int(300)
        x = min(0, x)  
        x = max(-(self.largura - 800), x) 
        y = min(0, y)  
        y = max(-(self.altura - 600), y)  
        self.camera = pygame.Rect(x, y, self.largura, self.altura)

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            self.sheet = pygame.image.load('Soldier.png').convert_alpha()
        except:
            self.sheet = pygame.Surface((30, 50))
            self.sheet.fill((255, 0, 0))

        self.frames_andando_direita = [
            self.sheet.subsurface((0, 0, 32, 32)),
            self.sheet.subsurface((32, 0, 32, 32)),
            self.sheet.subsurface((64, 0, 32, 32))
        ]
        
        self.animacoes = {
            'idle': self.sheet.subsurface((0, 0, 32, 32)),
            'direita': self.frames_andando_direita,
            'esquerda': [pygame.transform.flip(f, True, False) for f in self.frames_andando_direita],
            'pulando': self.sheet.subsurface((32, 0, 32, 32))
        }

        self.imagem_atual = 'idle'
        self.frame_index = 0
        self.image = self.animacoes[self.imagem_atual]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.vx = 0
        self.vy = 0
        self.gravidade = 0.8
        self.no_chao = False

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.vx = 0
        
        if keys[pygame.K_LEFT]:
            self.vx = -5
            self.imagem_atual = 'esquerda'
        elif keys[pygame.K_RIGHT]:
            self.vx = 5
            self.imagem_atual = 'direita'
        else:
            self.imagem_atual = 'idle'

        if keys[pygame.K_SPACE] and self.no_chao:
            self.vy = -12
            self.no_chao = False

    def aplicar_gravidade(self):
        self.vy += self.gravidade
        self.rect.y += self.vy

    def colisao_tiles(self, direcao, blocos):
        if direcao == 'horizontal':
            for bloco in blocos:
                if self.rect.colliderect(bloco):
                    if self.vx > 0: self.rect.right = bloco.left
                    if self.vx < 0: self.rect.left = bloco.right
        
        if direcao == 'vertical':
            for bloco in blocos:
                if self.rect.colliderect(bloco):
                    if self.vy > 0:
                        self.rect.bottom = bloco.top
                        self.vy = 0
                        self.no_chao = True
                    if self.vy < 0:
                        self.rect.top = bloco.bottom
                        self.vy = 0

    def update(self):
        self.get_input()
        self.aplicar_gravidade()

        if self.imagem_atual in ['direita', 'esquerda']:
            self.frame_index += 0.2
            if self.frame_index >= len(self.animacoes[self.imagem_atual]):
                self.frame_index = 0
            self.image = self.animacoes[self.imagem_atual][int(self.frame_index)]
        else:
            self.image = self.animacoes[self.imagem_atual]


player = Jogador(100, 100)
todos_sprites = pygame.sprite.Group()
todos_sprites.add(player)

largura_mundo = len(mapa[0]) * tile_size
altura_mundo = len(mapa) *tile_size
camera = Camera(largura_mundo, altura_mundo)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((135, 206, 235))

    tiles_colisao = []
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            tile_rect = pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size)
            if mapa[i][j] == 'W':  
                pygame.draw.rect(screen, (100, 50, 0), camera.aplicar(tile_rect))
                tiles_colisao.append(tile_rect)
            elif mapa[i][j] == 'P':  
                pygame.draw.rect(screen, (34, 139, 34), camera.aplicar(tile_rect))
                tiles_colisao.append(tile_rect)

    player.rect.x += player.vx
    player.colisao_tiles('horizontal', tiles_colisao)
    player.colisao_tiles('vertical', tiles_colisao)

    camera.atualizar(player)

    screen.blit(player.image, camera.aplicar(player))

    pygame.display.update()
    clock.tick(60)
