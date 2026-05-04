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
pygame.display.set_caption("Validador de Senha/Email")
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

input_text = ""
mensagem = "Digite a senha (min 8 car, A, a, 0-9)"
cor_mensagem = (255, 255, 255)
senha_final = ""

running = True
while running:
    screen.fill((30, 30, 30))
    
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
                    cor_mensagem = (255, 0, 0) # Vermelho
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



