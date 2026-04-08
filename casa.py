from pygame import*
import sys

init()

batman_img = image.load("batman.png")
batman_img = transform.scale(batman_img, (200, 200))

batman_font = font.Font("batmfa__.ttf", 50)

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
    draw.line(window, (255, 255, 0), (100, 50), (180, 50), 3)
    draw.line(window, (255, 255, 0), (100, 100), (150, 150), 3)
    draw.line(window, (255, 255, 0), (100, 150), (110, 50), 3)
    draw.line(window, (255, 255, 0), (80, 70), (80, 100), 3)
    draw.rect(window, (150, 75, 0), (520, 450, 50, 100))
    draw.circle(window, (0, 255, 0), (520, 450), 65)
    draw.circle(window, (255, 0, 0), (520, 400), 10)
    draw.circle(window, (255, 255, 0), (530, 400), 10)
    draw.circle(window, (255, 165, 0), (510, 400), 10)
    draw.circle(window, (128, 0, 128), (520, 350), 5)
    


    window.blit(batman_img, (80, 120))

    batman_text = batman_font.render("I am Batman", True, (0, 0, 0))
    window.blit(batman_text, (100, 400))
    batman_text = batman_font.render("I'm vengeance", True, (0, 0, 0))
    window.blit(batman_text, (100, 500))
    
    display.update()
