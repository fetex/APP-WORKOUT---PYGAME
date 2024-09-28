### APP ENFOCADA PARA REALIZAR EJERCICIO POR MEDIO DE RUTINAS DE GRUPOS MUSCULARES

# Importamos las librerias necesarias
import pygame
import time
import sys
from PIL import Image


# Primero: librerias 
# Segundo: Contantes, variables, 
# Tercero: Funciones

# Inicializamos pygame
pygame.init()

# Colors app in rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREEN_BLACK = (0, 200, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
PURPLE = (128, 0, 128)
BLUE = (3, 96, 146)


#Size window 
WIDTH = 800
HEIGHT = 600

SIZE_CELL = 50 #TAMANO DE CELDA EN PIXELES


# Crear ventana
window = pygame.display.set_mode((WIDTH, HEIGHT)) # Crear ventana con 
pygame.display.set_caption('Entrenador Personal BodyBuilder')

# Crear fuentes
fuente_titulo = pygame.font.SysFont('Arial', 36)
fuente_texto = pygame.font.SysFont('Arial', 24)


# def upload_gif(ruta_gif):
#     gif = Image.open(ruta_gif)
#     frames_gif = []
#     while True:
#         try:
#             frame = gif.copy().convert("RGBA")  # Convertir el frame a modo RGBA para Pygame
#             frame_pygame = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
#             frames_gif.append(frame_pygame)
#             gif.seek(gif.tell() + 1)
#         except EOFError:
#             pass
#     return frames_gif 


# frames_gif = upload_gif("media/pecho.gif")
# frame_actual = 0



def draw_button(x, y, width, height, color, color_hover, text, text_color):
    mouse_pos = pygame.mouse.get_pos() # Captura la posición del mouse para poder dar clik en el boton

    # Efecto hover boton
    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
        color = color_hover
    else: 
        color = color
    pygame.draw.rect(window, color, (x, y, width, height)) # Dibujar un rectangulo 
    text_button = fuente_texto.render(text, True, text_color) # Insertar texto en el boton
    window.blit(text_button, (x + (width - text_button.get_width()) // 2, y + (height - text_button.get_height()) // 2)) ## Centro el texto en el boton



def draw_grid():
    # lINEAS HORIZONTALES
    for y in range (0, HEIGHT, SIZE_CELL):
        pygame.draw.line(window, GRAY, (0, y), (WIDTH, y))

    # LINEAS VERTICALES
    for x in range (0, WIDTH, SIZE_CELL):
        pygame.draw.line(window, GRAY, (x, 0), (x, HEIGHT))
# Funcion para mostrar menu

def show_menu():
    window.fill(WHITE)
    draw_grid() # Llamar a la funcion para dibujar la cuadricula
    draw_button(100, 50, 150, 50, BLUE, PURPLE, "Bipces", BLACK)
    draw_button(100, 200, 150, 50, GREEN, GREEN_BLACK, 'Pecho', BLACK)
    draw_button(400, 150, 200, 75, GRAY, BLACK, 'Espalda', WHITE)
    draw_button(250, 300, 150, 50, BLACK, GRAY, 'Salir', WHITE)
    pygame.display.update()


# Vista pecho
def show_chest():
    window.fill(WHITE)
    draw_grid()
    draw_button(100, 200, 150, 50, GREEN, GREEN_BLACK, 'Press de banca', BLACK)
    draw_button(250, 300, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    pygame.display.update()

# Mostrar ejercicio
# def show_exercise(name, frames_gif): 
#     global frame_actual

#     window.fill(WHITE)

#     text_exercise = fuente_titulo.render(name, True, BLACK)
#     window.blit(text_exercise, (400,100))

#     #Mostrar gif
#     window.blit(frames_gif[frame_actual], (350,100))

#     # Actualizar gif 
#     frame_actual = (frame_actual + 1) % len(frames_gif)
#     draw_button(400, 500, 150, 50, BLACK, GRAY, 'Finalizar', WHITE)
#     pygame.display.update()




view = 'menu'
running = True
exercise = None


# Bucle principal de la aplicación
while running:

    #Definir vista 
    if view == 'menu':
        show_menu()
    elif view == 'chest':
        show_chest()
    elif view == 'exercise':
        show_exercise('Press de banca', frames_gif)

    #Obtener posicion mouse
    mouse_pos = pygame.mouse.get_pos()

    # print(mouse_pos)
    # print(view)

    #Efecto hover boton 
    if 100 <= mouse_pos[0] <= 250 and 200 <= mouse_pos[1] <= 250:
        color_buttom = GREEN_BLACK
    else:
        color_buttom = GREEN

    #Obtener eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar click en boton 
        if event.type == pygame.MOUSEBUTTONDOWN:
          
          if view == 'menu':
              if 100 <= mouse_pos[0] <= 250 and 200 <= mouse_pos[1] <= 250:
                  view = 'chest'
              elif 250 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 350:
                  running = False

          elif view == 'chest':
              if 250 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 350: #Condicion para regresar al menu boton regresar
                  view = 'menu'
              elif 100 <= mouse_pos[0] <= 250 and 200 <= mouse_pos[1] <= 250:
                  view = 'exercise'
                  exercise = 'Press de banca'
         
          elif view == 'exercise':
             if 400 <= mouse_pos[0] <= 550 and 500 <= mouse_pos[1] <= 550:
                 view = 'chest'
            
        


# # Función para mostrar texto en pantalla
# def mostrar_texto(texto, fuente, color, x, y):
#     superficie_texto = fuente.render(texto, True, color)
#     ventana.blit(superficie_texto, (x, y))

# # Menú de partes del cuerpo
# def mostrar_menu_partes_cuerpo():
#     ventana.fill(BLANCO)
#     mostrar_texto('Seleccione la parte del cuerpo a entrenar:', fuente_titulo, NEGRO, 100, 50)
#     mostrar_texto('1. Pecho', fuente_texto, NEGRO, 100, 150)
#     mostrar_texto('2. Piernas', fuente_texto, NEGRO, 100, 200)
#     mostrar_texto('3. Espalda', fuente_texto, NEGRO, 100, 250)
#     mostrar_texto('4. Hombros', fuente_texto, NEGRO, 100, 300)
#     mostrar_texto('5. Brazos', fuente_texto, NEGRO, 100, 350)
#     pygame.display.update()

# # Función para simular un ejercicio
# def iniciar_ejercicio(ejercicio, series, repeticiones):
#     ventana.fill(BLANCO)
#     mostrar_texto(f'Iniciando {ejercicio}', fuente_titulo, NEGRO, 100, 50)
#     serie_actual = 1
#     for serie in range(series):
#         for repeticion in range(repeticiones):
#             ventana.fill(BLANCO)
#             mostrar_texto(f'Serie {serie_actual} - Repetición {repeticion + 1}', fuente_texto, NEGRO, 100, 150)
#             mostrar_texto(f'Rep. restantes: {repeticiones - repeticion - 1}', fuente_texto, NEGRO, 100, 200)
#             mostrar_texto(f'Tiempo: {time.strftime("%H:%M:%S", time.gmtime(time.time()))}', fuente_texto, NEGRO, 100, 250)
#             pygame.display.update()
#             time.sleep(1)  # Simular la pausa entre repeticiones
#         serie_actual += 1
#     mostrar_texto('Ejercicio Completado', fuente_texto, NEGRO, 100, 300)
#     pygame.display.update()
#     time.sleep(2)



pygame.quit()
sys.exit()