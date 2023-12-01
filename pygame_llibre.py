import pygame, sys, os

with open('output.txt', 'r', encoding='utf-16') as file:
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
font = pygame.font.Font(None, 20)
text_color = BLACK

# Bandera para controlar si el juego está terminado
done = False

# Cargar la imagen de fondo
background = pygame.image.load("fons.jpg").convert()
foreground = pygame.image.load("llegint3.png").convert_alpha()
calendario_original = pygame.image.load("calendari.png").convert_alpha()
foreground.set_colorkey(WHITE)

calendario_ancho = 200  
calendario_alto = 150  
calendario = pygame.transform.scale(calendario_original, (calendario_ancho, calendario_alto))


mesos = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
index_mes = 0

meses_orden = {mes: i + 1 for i, mes in enumerate(mesos)}

meses_faltantes = set(mesos) - set(mes for libro, mes in libros_y_meses)
lista_final = libros_y_meses.copy()

for mes_faltante in sorted(meses_faltantes, key=lambda x: meses_orden[x]):
    lista_final.append(('', mes_faltante))

print(lista_final)
# Ordenar la lista de listas por el número correspondiente al mes
lista_ordenada = sorted(lista_final, key=lambda x: meses_orden.get(x[1], float('inf')))
print("llsta final:",lista_ordenada)


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
            index_llibre += 1
                
            if index_llibre >= len(lista_ordenada):
                done = True
                break

    # Dibujar el fondo en la pantalla
    screen.blit(background, (0, 0))
    screen.blit(foreground, (150,200))
    screen.blit(calendario, (10, 10))
    screen.blit(font.render(lista_ordenada[index_llibre][1], True, BLACK), (82,78))
    screen.blit(font.render(lista_ordenada[index_llibre][0], True, BLACK), (272, 360))       

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer el límite de velocidad del bucle
    clock.tick(60)


# Salir de Pygame
pygame.quit()
sys.exit()