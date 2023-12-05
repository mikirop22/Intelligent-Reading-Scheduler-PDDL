import pygame, sys, os

with open('output.txt', 'r') as file:
    # Lee todas las líneas del archivo
    lines = file.readlines()

    # Encuentra la línea que contiene 'ff: found legal plan as follows'
    start_index = next((i for i, line in enumerate(lines) if 'ff: found legal plan as follows' in line), None)

    # Encuentra la línea que contiene 'time spent:'
    end_index = next((i for i, line in enumerate(lines) if 'time spent:' in line), None)

    if start_index is not None and end_index is not None:
        # Obtén las líneas entre 'ff: found legal plan as follows' y 'time spent:'
        content_between = lines[start_index + 1: end_index]

        # Almacena el contenido entre las dos frases en una lista
        plan_steps = [line.strip() for line in content_between if line.strip()]

    else:
        print("No se encontraron ambas frases en el archivo.")


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



# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode([600, 500])
pygame.display.set_caption("Juego")
BLACK = (0,0,0)
WHITE = (255,255,255)
# Configurar el reloj
clock = pygame.time.Clock()

# Puntuación inicial
fontl = pygame.font.Font(None, 15)
fontc = pygame.font.Font(None, 25)
text_color = BLACK

# Bandera para controlar si el juego está terminado
done = False

# Cargar la imagen de fondo
background = pygame.image.load("fons.jpg").convert()
llegint_images = [pygame.image.load(f"llegint{i}.png").convert_alpha() for i in range(5)]
for img in llegint_images:
    img.set_colorkey(WHITE)
calendario_original = pygame.image.load("calendari.png").convert_alpha()
hivern = pygame.image.load("hivern.png").convert_alpha()
primavera = pygame.image.load("primavera.png").convert_alpha()
estiu = pygame.image.load("estiu.png").convert_alpha()
tardor = pygame.image.load("tardor.png").convert_alpha()




calendario_ancho = 200  
calendario_alto = 150  
calendario = pygame.transform.scale(calendario_original, (calendario_ancho, calendario_alto))

x = 230
y = 180
hivern = pygame.transform.scale(hivern, (x, y))
primavera = pygame.transform.scale(primavera, (x, y))
estiu = pygame.transform.scale(estiu, (x, y))
tardor = pygame.transform.scale(tardor, (x, y))


mesos = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
index_mes = 0

meses_orden = {mes: i + 1 for i, mes in enumerate(mesos)}

meses_faltantes = set(mesos) - set(mes for libro, mes in libros_y_meses)
lista_final = libros_y_meses.copy()

for mes_faltante in sorted(meses_faltantes, key=lambda x: meses_orden[x]):
    lista_final.append(('', mes_faltante))


# Ordenar la lista de listas por el número correspondiente al mes
lista_ordenada = sorted(lista_final, key=lambda x: meses_orden.get(x[1], float('inf')))



index_llibre = 0

llegits = []
def tots_llegits(mes, llegits):
    ll = []
    for llibre_mes in libros_y_meses: #mirem quins llibres ha llegit en el mes actual
        if mes == llibre_mes[1]:
            ll.append(llibre_mes[0])

    
    for llibre in llegits:
        if llibre not in ll:
            return False
    return True
        
        
# Bucle principal del juego
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
                
            if index_llibre+1 >= len(lista_ordenada):
                done = True
                break
            else:
                index_llibre += 1
    # Dibujar el fondo en la pantalla
    screen.blit(background, (0, 0))
    screen.blit(calendario, (10, 10))
    screen.blit(fontc.render(lista_ordenada[index_llibre][1], True, BLACK), (55,78))
    if lista_ordenada[index_llibre][1] == "ENERO" or lista_ordenada[index_llibre][1] == "FEBRERO" or lista_ordenada[index_llibre][1] == "DICIEMBRE":
        screen.blit(hivern, (200,20))
    if lista_ordenada[index_llibre][1] == "MARZO" or lista_ordenada[index_llibre][1] == "ABRIL" or lista_ordenada[index_llibre][1] == "MAYO":
        screen.blit(primavera, (200,20))
    if lista_ordenada[index_llibre][1] == "JUNIO" or lista_ordenada[index_llibre][1] == "JULIO" or lista_ordenada[index_llibre][1] == "AGOSTO":
        screen.blit(estiu, (200,20))
    if lista_ordenada[index_llibre][1] == "SEPTIEMBRE" or lista_ordenada[index_llibre][1] == "OCTUBRE" or lista_ordenada[index_llibre][1] == "NOVIEMBRE":
        screen.blit(tardor, (200,20))

    # Cambiar la imagen `foreground` según el índice actual
    
    if lista_ordenada[index_llibre][0] != '':
        
        current_llegint_index = index_llibre % len(llegint_images)
        screen.blit(llegint_images[current_llegint_index], (150, 200))
        screen.blit(fontl.render(lista_ordenada[index_llibre][0], True, BLACK), (265, 355))       

    else:
        screen.blit(fontc.render(lista_ordenada[index_llibre][1], True, BLACK), (55,78))
    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer el límite de velocidad del bucle
    clock.tick(60)


# Salir de Pygame
pygame.quit()
sys.exit()