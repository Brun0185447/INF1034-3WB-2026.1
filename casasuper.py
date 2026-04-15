from pygame import*

init()

window = display.set_mode((1280, 720))
running = True
clock = time.Clock()

batman_img = image.load("batman.png")
batman_img = transform.scale(batman_img, (200, 200))

batman_font = font.Font("batmfa__.ttf", 50)

mixer.music.load("batman_1966.mp3")
mixer.music.play(-1)
indiana_jones_sfx = mixer.Sound("indiana-jones-theme-song.mp3")
star_wars_sfx = mixer.Sound("Star Wars.mp3")
pos_x = 950
background_color = "#97D1FA"



while running:
    clock.tick(60)
    for ev in event.get():
        if ev.type == QUIT:
            running == False
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                background_color = (245, 178, 64)
            elif key_pressed == K_m:
                indiana_jones_sfx.play()
            if key_pressed == K_e:
                background_color = (0, 0, 0)
            elif key_pressed == K_t:
                star_wars_sfx.play()
               
    

    dt = clock.get_time()/1000
    keys = key.get_pressed()
    mouse_x, mouse_y = mouse.get_pos()
    if keys[K_d]:
       pos_x = pos_x + 100 * dt
    elif keys[K_a]:
         pos_x = pos_x - 100 * dt
            
    window.fill(background_color)
    draw.rect(window, (150, 75, 0), (0, 650, 2000, 100))
    draw.rect(window, (128, 0, 128), (200, 450, 200, 200))
    draw.circle(window, (255, 255, 255), (pos_x, 110), 50)
    draw.polygon(window, (255, 165, 0), ((200, 450), (270, 300), (400, 450)))
    draw.circle(window, (255, 255, 255), (pos_x + 50, 110), 50)
    draw.circle(window, (255, 255, 255), (pos_x + 100, 110), 50)
    draw.circle(window, (255, 255, 255), (pos_x + 150, 110), 50)
    draw.rect(window, (0, 0, 128), (220, 540, 35, 50))
    draw.rect(window, (255, 255, 255), (290, 500, 85, 150))
    draw.circle(window, (0, 0, 0), (300, 600), 5)
    draw.circle(window, (255, 255, 0), (mouse_x, mouse_y), 50)
    draw.line(window, (255, 255, 0), (mouse_x, mouse_y), (180, 50), 3)
    draw.line(window, (255, 255, 0), (mouse_x, mouse_y), (150, 150), 3)
    draw.line(window, (255, 255, 0), (mouse_x, mouse_y), (110, 50), 3)
    draw.line(window, (255, 255, 0), (mouse_x, mouse_y), (80, 100), 3)
    draw.line(window, (255, 255, 0), (mouse_x, mouse_y), (80, 150), 3)
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
    
    display.update()