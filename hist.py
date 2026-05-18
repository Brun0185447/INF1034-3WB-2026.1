import pygame
import random
import sys

# 1. Inicialização do PyGame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Visualizador Interativo de Histogramas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_CLARO = (200, 200, 200)

# Fonte para os textos
FONTE = pygame.font.SysFont(None, 24)

# 2. Funções Auxiliares

def gerar_cor_aleatoria():
    """Gera uma cor RGB aleatoriamente, garantindo que não seja muito escura."""
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

def desenhar_eixos_e_rotulos(tela, num_faixas, max_valor, titulo, faixas_labels=None):
    """Desenha os eixos X e Y, as marcações e os rótulos de cada faixa."""
    # Desenha eixo Y
    pygame.draw.line(tela, PRETO, (100, 500), (100, 100), 2)
    # Desenha eixo X
    pygame.draw.line(tela, PRETO, (100, 500), (700, 500), 2)

    # Título do gráfico
    texto_titulo = FONTE.render(titulo, True, PRETO)
    tela.blit(texto_titulo, (LARGURA // 2 - texto_titulo.get_width() // 2, 50))

    # Marcações no eixo Y (proporcionais)
    for i in range(5):
        valor_y = int(max_valor * (i / 4))
        pos_y = 500 - int(400 * (i / 4))
        pygame.draw.line(tela, CINZA_CLARO, (90, pos_y), (100, pos_y), 2)
        texto_y = FONTE.render(str(valor_y), True, PRETO)
        tela.blit(texto_y, (60, pos_y - 10))

# 3. Modelos dos Dados

# --- Histograma 1: Aleatório ---
dados_h1 = [random.randint(1, 100) for _ in range(70)] # Pelo menos 50 números
faixas_h1 = 5 # 5 faixas
# Agrupa os 70 números em 5 faixas
categorias_h1 = [len([x for x in dados_h1 if (i * 20) <= x < ((i + 1) * 20)]) for i in range(faixas_h1)]
cores_h1 = [gerar_cor_aleatoria() for _ in range(faixas_h1)]

# --- Histograma 2: Estático com totais aleatórios ---
dados_estaticos = 100 # Total de números na lista estática
faixas_h2 = 7 # 7 faixas
# Soma dos elementos não ultrapassa o total
categorias_h2 = []
soma_atual = 0
for _ in range(faixas_h2 - 1):
    max_possivel = dados_estaticos - soma_atual
    valor = random.randint(0, max_possivel)
    categorias_h2.append(valor)
    soma_atual += valor
categorias_h2.append(dados_estaticos - soma_atual) # O restante vai para a última faixa
cores_h2 = [gerar_cor_aleatoria() for _ in range(faixas_h2)]

# --- Histograma 3: Input do Usuário ---
faixas_h3 = 10 # 10 faixas
categorias_h3 = [0] * faixas_h3 # Inicializa com zero
cores_h3 = [gerar_cor_aleatoria() for _ in range(faixas_h3)]
texto_usuario = "" # Buffer de input

# 4. Loop Principal e Menu Interativo
estado = 0 # 0: Histograma 1 | 1: Histograma 2 | 2: Histograma 3
clock = pygame.time.Clock()

def desenhar_histograma(tela, categorias, cores, titulo, faixas, max_valor_forcar=None):
    """Lógica principal para desenhar as barras do histograma na tela."""
    tela.fill(BRANCO)
    
    # Define o máximo para ajustar a escala Y
    max_valor = max_valor_forcar if max_valor_forcar else (max(categorias) if max(categorias) > 0 else 1)
    
    desenhar_eixos_e_rotulos(tela, faixas, max_valor, titulo)

    largura_barra = 400 // faixas
    espacamento = 20

    for i in range(faixas):
        valor = categorias[i]
        altura_barra = int((valor / max_valor) * 400) if max_valor > 0 else 0
        
        x = 120 + i * (largura_barra + espacamento)
        y = 500 - altura_barra
        
        # Desenha a barra
        pygame.draw.rect(tela, cores[i], (x, y, largura_barra, altura_barra))
        
        # Borda da barra
        pygame.draw.rect(tela, PRETO, (x, y, largura_barra, altura_barra), 2)
        
        # Rótulo da faixa/categoria no eixo X
        rotulo = FONTE.render(f"F {i+1}", True, PRETO)
        tela.blit(rotulo, (x + (largura_barra - rotulo.get_width()) // 2, 510))
        
        # Valor exato em cima da barra
        valor_texto = FONTE.render(str(valor), True, PRETO)
        tela.blit(valor_texto, (x + (largura_barra - valor_texto.get_width()) // 2, y - 20))

# Loop de execução
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        # Mudança de telas: Clica na seta para a direita para mudar o Histograma
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                estado = (estado + 1) % 3  # Vai de 0 a 2 ciclicamente
            
            # Input exclusivo do PyGame para o Histograma 3
            if estado == 2:
                if evento.key == pygame.K_BACKSPACE:
                    texto_usuario = texto_usuario[:-1]
                elif evento.key == pygame.K_RETURN:
                    try:
                        # Pega o que o usuário digitou, separa por vírgula e transforma em lista de inteiros
                        numeros_input = [int(n.strip()) for n in texto_usuario.split(',') if n.strip().isdigit()]
                        # Limita a lista ao tamanho do número de faixas (10)
                        numeros_input = numeros_input[:faixas_h3]
                        
                        # Limpa as categorias e preenche com as novas frequências limitadas
                        categorias_h3 = [0] * faixas_h3
                        for num in numeros_input:
                            if 0 <= num < faixas_h3:
                                categorias_h3[num] += 1
                        texto_usuario = "" # Limpa o input
                    except ValueError:
                        pass
                elif evento.unicode.isdigit() or evento.unicode == ',':
                    texto_usuario += evento.unicode

    # Renderização da Tela
    if estado == 0:
        desenhar_histograma(TELA, categorias_h1, cores_h1, "1. Histograma Aleatório (70 números, 5 faixas)", faixas_h1)
    elif estado == 1:
        desenhar_histograma(TELA, categorias_h2, cores_h2, "2. Histograma Estático com Valores Aleatórios (7 faixas)", faixas_h2)
    elif estado == 2:
        desenhar_histograma(TELA, categorias_h3, cores_h3, "3. Histograma via Input no PyGame (10 faixas)", faixas_h3, max_valor_forcar=50)
        
        # Instruções de como usar o input na tela
        instrucao = FONTE.render("Digite números de 0 a 9 separados por vírgula e aperte ENTER", True, PRETO)
        TELA.blit(instrucao, (120, 540))
        input_texto = FONTE.render(f"Seus numeros: {texto_usuario}", True, PRETO)
        TELA.blit(input_texto, (120, 570))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
