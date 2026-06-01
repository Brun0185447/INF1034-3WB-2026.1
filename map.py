from pygame import* 
import sys

init()
screen = display.set_mode((800, 600))
display.set_caption('Hello World!')
clock= time.Clock()
tile_size=60

mapa=[
    "GGGGGGAGGGGGG",
    "GGGGGGAGGGGGG",
    "GGGGGGAGGGGGG",
    "GGGGGGAGGGGGG",
    "GGGGGGAAAGGGG",
    "GGGGGGGGAGGGG",
    "GGGGGGGGAGGGG",
    "PPPPPPPPAPPPP",
    "AAAAAAAAAAAAA",
    "AAAAAAAAAAAAA",
]


while True:
     for ev in event.get():
        if ev.type == QUIT:
           quit()
           sys.exit()

     clock.tick(60)
     dt=clock.get_time()

     #Primeiro mapa
     for i in range(len(mapa)): #Para cada linha
        for j in range(len(mapa[i])): #Para cada coluna
           if mapa[i][j] == "G":
               draw.rect(screen, (39,153,0), (tile_size*j, tile_size*i, tile_size, tile_size))
           elif mapa[i][j] == "P":
               draw.rect(screen, (230,235,134), (tile_size*j, tile_size*i, tile_size, tile_size))
           elif mapa[i][j] == "A":
               draw.rect(screen, (63,125,232), (tile_size*j, tile_size*i, tile_size, tile_size))



     display.update()
     clock.tick(60)