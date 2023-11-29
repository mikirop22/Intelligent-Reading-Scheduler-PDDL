import pygame, sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode([600, 500])
pygame.display.set_caption("Juego")
BLACK = (0,0,0)
# Configurar el reloj
clock = pygame.time.Clock()

# Puntuación inicial
font = pygame.font.Font(None, 20)
text_color = BLACK

# Bandera para controlar si el juego está terminado
done = False

# Cargar la imagen de fondo
background = pygame.image.load("fons.jpg").convert()
foreground = pygame.image.load("llegint.png").convert_alpha()
foreground.set_colorkey(BLACK)

llibres = ["Libro 1", "Libro 2", "Libro 3", "Libro 4"]
index_llibre = 0
mesos = ["Gener","Febrer","Març","Abril","Maig","Juny","Juliol","Agost","Setembre","Octubre","Novembre","Desembre"]
index_mes = 0


# Bucle principal del juego
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            index_llibre += 1
    # Lógica del juego (puedes agregar más aquí)

    # Dibujar el fondo en la pantalla
    screen.blit(background, (0, 0))
    screen.blit(foreground, (150,200))
    screen.blit(font.render(llibres[index_llibre], True, BLACK), (265,365))

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer el límite de velocidad del bucle
    clock.tick(60)

# Salir de Pygame
pygame.quit()
