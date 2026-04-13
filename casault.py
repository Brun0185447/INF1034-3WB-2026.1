from pygame import*

init()
screen = display.set_mode((1200, 720))
running = True
clock = time.Clock()

fonte = font.Font("batmfa_.ttf", 50)
image = image.load("batman.png")
image = transform.scale(batman_img, (200, 200))


image = image.load("batman.png")
image = transform.scale(image, (200, 200))
mixer.music.load("batman_1966.mp3")
mixer.music.play(-1)



pos_x = 300
background_color = "#97D1FA"

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                background_color = (245, 178, 64)


    dt = clock.get_time()/1000
    keys = key.get_pressed()
    print(keys)

    if keys[K_d]:
       pos_x = pos_x + 100 * dt
    elif keys[K_a]:
        pos_x = pos_x - 100 * dt


    screen.fill(background_color)
    draw.rect(screen, "#0D1664", (100, 200, 200, 50))
    draw.circle(screen, "#FFF251", (100, 100), 50)
    draw.polygon(screen, "#F28838", ((400, 300), (450, 300), (425, 250)))
    draw.line(screen, "#FFF251", (10, 150), (100, 20), 4)

    screen.blit(image, (40, 460))
    draw.circle(screen, "#FFFFFF", (100, 100), 50)