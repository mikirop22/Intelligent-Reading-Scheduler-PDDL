import pygame, sys

with open('output.txt', 'r') as file:
    # Lee todas las líneas del archivo
    lines = file.readlines()

    # Encuentra la línea que contiene 'ff: found legal plan as follows'
    index = lines.index('ff: found legal plan as follows\n')

    # Obtén las líneas que contienen los pasos del plan
    plan_lines = lines[index + 1:]

    # Almacena los pasos del plan en una lista
    plan_steps = [line.strip() for line in plan_lines if line.strip()]

# Ahora, plan_steps contiene los pasos del plan como elementos de la lista


libros_y_meses = []  # Lista para almacenar el nombre del libro y el mes de cada elemento
for paso in range(len(plan_steps)-1):
    if paso==0:
        # Dividir la cadena en palabras
        palabras = plan_steps[0].split()

        # Obtener el nombre del libro y el primer mes (si hay)
        nombre_libro = palabras[3] if len(palabras) > 2 else None
        primer_mes = palabras[-2] if len(palabras) > 1 else None

        # Agregar el nombre del libro y el primer mes a la lista
        libros_y_meses.append((nombre_libro, primer_mes))
    else:
        # Dividir la cadena en palabras
        palabras = plan_steps[paso].split()

        # Obtener el nombre del libro y el primer mes (si hay)
        nombre_libro = palabras[2] if len(palabras) > 2 else None
        primer_mes = palabras[-2] if len(palabras) > 1 else None

        # Agregar el nombre del libro y el primer mes a la lista
        libros_y_meses.append((nombre_libro, primer_mes))

# Imprimir la lista resultante



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
calendario_original = pygame.image.load("calendari.png").convert_alpha()
foreground.set_colorkey(BLACK)

calendario_ancho = 200  
calendario_alto = 150  
calendario = pygame.transform.scale(calendario_original, (calendario_ancho, calendario_alto))

index_llibre = 0
mesos = ["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
index_mes = 0


# Bucle principal del juego
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            index_mes += 1

           
    if index_mes >= len(mesos): #per sortir del pygame
        done = True
        break

    # Dibujar el fondo en la pantalla
    screen.blit(background, (0, 0))
    screen.blit(foreground, (150,200))
    screen.blit(calendario, (10, 10))
    screen.blit(font.render(mesos[index_mes], True, BLACK), (82,78))

    ct = 0
    for llibre_mes in libros_y_meses: #mirem quins llibres ha llegit en el mes actual
        if mesos[index_mes] == llibre_mes[1]:
            screen.blit(font.render(llibre_mes[0], True, BLACK), (272, 360 + ct*18))
            ct+=1

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer el límite de velocidad del bucle
    clock.tick(60)
    


# Salir de Pygame
pygame.quit()
sys.exit()
