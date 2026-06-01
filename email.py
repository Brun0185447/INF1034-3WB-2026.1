import pygame
import sys

def valida_email(email):
    return email[-8:] == '@puc.com'

def possuiMaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': 
            return True
    return False

def possuiMinuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': 
            return True
    return False

def possuiNumero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9': 
            return True
    return False

def valida_senha(senha):
    check_tamanho = len(senha) >= 8
    check_maiuscula = possuiMaiuscula(senha)
    check_minuscula = possuiMinuscula(senha)
    check_numero = possuiNumero(senha)
    return check_tamanho and check_maiuscula and check_minuscula and check_numero

def criptografa_senha(senha):
    senha_cripto = ""
    for char in senha:
        if char.isdigit():
            ref = ord('0')
            pos_alpha = ord(char) - ref
            pos_cesar = (pos_alpha + 3) % 10
            senha_cripto += chr(ref + pos_cesar)
        elif 'A' <= char <= 'Z':
            ref = ord('A')
            pos_alpha = ord(char) - ref
            pos_cesar = (pos_alpha + 3) % 26
            senha_cripto += chr(ref + pos_cesar)
        elif 'a' <= char <= 'z':
            ref = ord('a')
            pos_alpha = ord(char) - ref
            pos_cesar = (pos_alpha + 3) % 26
            senha_cripto += chr(ref + pos_cesar)
        else:
            senha_cripto += char
    return senha_cripto

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Validador de Email")
font = pygame.font.Font('batmfa__.ttf', 20)
clock = pygame.time.Clock()

email_usuario = ''
resultado_validacao = ''
cor_texto = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                
                if valida_email(email_usuario):
                    resultado_validacao = "Email Valido!"
                    cor_texto = (0, 255, 0) 
                else:
                    resultado_validacao = "Email Invalido! Tente novamente."
                    cor_texto = (255, 0, 0) 
            elif event.key == pygame.K_BACKSPACE:
                email_usuario = email_usuario[:-1]
            else:
                email_usuario += event.unicode

    
    screen.fill((30, 30, 30))
    
   
    texto_surf = font.render(f"Email: {email_usuario}", True, (255, 255, 255))
    resultado_surf = font.render(resultado_validacao, True, cor_texto)
    
    screen.blit(texto_surf, (10, 50))
    screen.blit(resultado_surf, (10, 100))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Validador de Senha")
font = pygame.font.Font('batmfa__.ttf', 20)
clock = pygame.time.Clock()


input_text = ""
mensagem = "Digite a senha (min 8 car, A, a, 0-9)"
cor_mensagem = (255, 255, 255)
senha_final = ""

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                
                if valida_senha(input_text):
                    senha_final = criptografa_senha(input_text)
                    mensagem = f"Senha Criptografada: {senha_final}"
                    cor_mensagem = (0, 255, 0) 
                else:
                    mensagem = "Senha Inválida! Tente novamente."
                    cor_mensagem = (255, 0, 0) 
                input_text = "" 
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    txt_surface = font.render(input_text, True, (255, 255, 255))
    msg_surface = font.render(mensagem, True, cor_mensagem)
    
    screen.blit(txt_surface, (50, 50))
    screen.blit(msg_surface, (50, 100))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()

pygame.init()

batman_img = image.load("batman.png")
batman_img = transform.scale(batman_img, (200, 200))

batman_font = font.Font("batmfa__.ttf", 20)

mixer.music.load("batman_1966.mp3")
mixer.music.play(-1)

window = display.set_mode((1280, 720))
window.fill((152, 209, 250))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    draw.rect(window, (150, 75, 0), (0, 650, 2000, 100))
    draw.rect(window, (128, 0, 128), (200, 450, 200, 200))
    draw.circle(window, (255, 255, 255), (950, 110), 50)
    draw.polygon(window, (255, 165, 0), ((200, 450), (270, 300), (400, 450)))
    draw.circle(window, (255, 255, 255), (1000, 110), 50)
    draw.circle(window, (255, 255, 255), (1050, 110), 50)
    draw.circle(window, (255, 255, 255), (1100, 110), 50)
    draw.rect(window, (0, 0, 128), (220, 540, 35, 50))
    draw.rect(window, (255, 255, 255), (290, 500, 85, 150))
    draw.circle(window, (0, 0, 0), (300, 600), 5)
    draw.circle(window, (255, 255, 0), (80, 70), 50)
    draw.rect(window, (150, 75, 0), (550, 500, 50, 150))
    draw.circle(window, (0, 255, 0), (570, 500), 65)
    draw.circle(window, (255, 0, 0), (570, 500), 10)
    draw.circle(window, (255, 255, 0), (570, 530), 10)
    draw.circle(window, (255, 165, 0), (530, 500), 10)
    draw.circle(window, (128, 0, 128), (550, 500), 5)
    

    window.blit(batman_img, (40, 460))

    batman_text = batman_font.render("I am Batman", True, (0, 0, 0))
    window.blit(batman_text, (850, 200))
    batman_text = batman_font.render("I'm vengeance", True, (0, 0, 0))
    window.blit(batman_text, (810, 400))
    
    pygame.display.update()
    sys.exit()





