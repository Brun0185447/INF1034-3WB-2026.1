from pygame import*
import sys

init()

batman_img = image.load("batman.png")
batman_img = transform.scale(batman_img, (200, 200))

batman_font = font.Font("batmfa_.ttf", 50)

mixer.music.load("batman_1966.mp3")
mixer.music.play(-1)

window = display.set_mode((1280, 720))
window.fill((152, 209, 250))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    #Desenhar a partir daqui
    draw.rect(window, (255, 0 , 0), (200, 300, 100, 50))
    draw.circle(window, (255, 255, 0), (500, 600), 200)
    draw.polygon(window, (0, 255 , 0), ((200, 300), (250, 150), (300, 300)))
    draw.line(window, (255, 0, 255), (100, 100), (200, 200), 3)

    #Desenhar imagens
    window.blit(batman_img, (0, 0))

    #Desenhar texto
    batman_text = batman_font.render("I am Batman", True, (0, 0, 0))
    window.blit(batman_text, (100, 400))

    display.update()