import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Visualizador Interativo de Histogramas")
fonte = pygame.font.SysFont(None, 24)

def gerar_cor_aleatoria():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

def desenhar_eixos_e_rotulos(tela, num_faixas, max_valor, titulo, faixas_labels=None):
    pygame.draw.line(tela, (0, 0, 0), (100, 500), (100, 100), 2)
    pygame.draw.line(tela, (0, 0, 0), (100, 500), (700, 500), 2)
    
    texto_titulo = fonte.render(titulo, True, (0, 0, 0))
    tela.blit(texto_titulo, (800 // 2 - texto_titulo.get_width() // 2, 50))

    for i in range(5):
        valor_y = int(max_valor * (i / 4))
        pos_y = 500 - int(400 * (i / 4))
        pygame.draw.line(tela, (200, 200, 200), (90, pos_y), (100, pos_y), 2)
        texto_y = fonte.render(str(valor_y), True, (0, 0, 0))
        tela.blit(texto_y, (60, pos_y - 10))

dados_h1 = [random.randint(1, 100) for _ in range(70)] 
faixas_h1 = 5 

categorias_h1 = [len([x for x in dados_h1 if (i * 20) <= x < ((i + 1) * 20)]) for i in range(faixas_h1)]
cores_h1 = [gerar_cor_aleatoria() for _ in range(faixas_h1)]

dados_estaticos = 100 
faixas_h2 = 7 

categorias_h2 = []
soma_atual = 0
for _ in range(faixas_h2 - 1):
    max_possivel = dados_estaticos - soma_atual
    valor = random.randint(0, max_possivel)
    categorias_h2.append(valor)
    soma_atual += valor
categorias_h2.append(dados_estaticos - soma_atual) 
cores_h2 = [gerar_cor_aleatoria() for _ in range(faixas_h2)]

faixas_h3 = 10 
categorias_h3 = [0] * faixas_h3 
cores_h3 = [gerar_cor_aleatoria() for _ in range(faixas_h3)]
texto_usuario = "" 

estado = 0 
clock = pygame.time.Clock()

def desenhar_histograma(tela, categorias, cores, titulo, faixas, max_valor_forcar=None):
    tela.fill(255, 255, 255)
    
    max_valor = max_valor_forcar if max_valor_forcar else (max(categorias) if max(categorias) > 0 else 1)
    
    desenhar_eixos_e_rotulos(tela, faixas, max_valor, titulo)

    largura_barra = 400 // faixas
    espacamento = 20

    for i in range(faixas):
        valor = categorias[i]
        altura_barra = int((valor / max_valor) * 400) if max_valor > 0 else 0
        
        x = 120 + i * (largura_barra + espacamento)
        y = 500 - altura_barra
        
        pygame.draw.rect(tela, cores[i], (x, y, largura_barra, altura_barra))
        
        pygame.draw.rect(tela, (0, 0, 0), (x, y, largura_barra, altura_barra), 2)
        
        rotulo = fonte.render(f"F {i+1}", True, (0, 0, 0))
        tela.blit(rotulo, (x + (largura_barra - rotulo.get_width()) // 2, 510))
        
        valor_texto = fonte.render(str(valor), True, (0, 0, 0))
        tela.blit(valor_texto, (x + (largura_barra - valor_texto.get_width()) // 2, y - 20))

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                estado = (estado + 1) % 3  
            
            if estado == 2:
                if evento.key == pygame.K_BACKSPACE:
                    texto_usuario = texto_usuario[:-1]
                elif evento.key == pygame.K_RETURN:
                    try:
                        numeros_input = [int(n.strip()) for n in texto_usuario.split(',') if n.strip().isdigit()]
                        
                        numeros_input = numeros_input[:faixas_h3]
                        
                        categorias_h3 = [0] * faixas_h3
                        for num in numeros_input:
                            if 0 <= num < faixas_h3:
                                categorias_h3[num] += 1
                        texto_usuario = "" 
                    except ValueError:
                        pass
                elif evento.unicode.isdigit() or evento.unicode == ',':
                    texto_usuario += evento.unicode

    if estado == 0:
        desenhar_histograma(screen, categorias_h1, cores_h1, "1. Histograma Aleatório (70 números, 5 faixas)", faixas_h1)
    elif estado == 1:
        desenhar_histograma(screen, categorias_h2, cores_h2, "2. Histograma Estático com Valores Aleatórios (7 faixas)", faixas_h2)
    elif estado == 2:
        desenhar_histograma(screen, categorias_h3, cores_h3, "3. Histograma via Input no PyGame (10 faixas)", faixas_h3, max_valor_forcar=50)
        
        
        instrucao = fonte.render("Digite números de 0 a 9 separados por vírgula e aperte ENTER", True, (0, 0, 0))
        screen.blit(instrucao, (120, 540))
        input_texto = fonte.render(f"Seus numeros: {texto_usuario}", True, (0, 0, 0))
        screen.blit(input_texto, (120, 570))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
