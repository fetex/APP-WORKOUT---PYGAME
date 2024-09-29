### APP ENFOCADA PARA REALIZAR EJERCICIO POR MEDIO DE RUTINAS DE GRUPOS MUSCULARES

# Importamos las librerias necesarias
import pygame
import time
import sys



# Primero: librerias 
# Segundo: Constantes, variables, 
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
BLUE = (52, 152, 219)
ORANGE = (243, 156, 18)


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
fuente_texto2= pygame.font.SysFont("Arial", 15)


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

# Función para mostrar texto en pantalla
def show_text(texto, fuente, color, x, y):
    superficie_texto = fuente.render(texto, True, color)
    window.blit(superficie_texto, (x, y))

def draw_grid():
    # lINEAS HORIZONTALES
    for y in range (0, HEIGHT, SIZE_CELL):
        pygame.draw.line(window, GRAY, (0, y), (WIDTH, y))

    # LINEAS VERTICALES
    for x in range (0, WIDTH, SIZE_CELL):
        pygame.draw.line(window, GRAY, (x, 0), (x, HEIGHT))
# Funcion para mostrar menu

def show_menu():  # Vista menu
    window.fill(BLUE)
    show_text("Hola, soy tu entrenador personalizado", fuente_titulo, BLACK, 50, 50)
    show_text("selecciona la parte del cuerpo que deseas entrenar el dia de hoy:", fuente_texto, BLACK, 50, 100)
    draw_grid() # Llamar a la funcion para dibujar la cuadricula
    draw_button(100, 200, 150, 50, ORANGE, GRAY, 'Tren Superior', BLACK)
    draw_button(100, 450, 150, 50, ORANGE, GRAY, 'Tren Inferior', BLACK)
    draw_button(600, 500, 150, 50, BLACK, GRAY, 'Salir', WHITE)
    pygame.display.update()


# Vista push up
def show_pushUp():
    window.fill(BLUE) # Color de la ventana o vista 
    show_text('push up', fuente_titulo, BLACK, 300, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_grid()
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    pygame.display.update()

def show_pressBanca():
    window.fill(BLUE)
    show_text('Press banco plano', fuente_titulo, BLACK, 250, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_grid()
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    pygame.display.update()
    pygame.display.update()

def show_CurlBicep():
    window.fill(BLUE)
    show_text('Curl bicep', fuente_titulo, BLACK, 250, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_grid()
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    pygame.display.update()
    pygame.display.update()

def show_plancha():
    window.fill(BLUE)
    show_text('Plancha', fuente_titulo, BLACK, 250, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_grid()
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'Finalizar', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    pygame.display.update()

def show_sentadillas():
    window.fill(BLUE)
    show_text('Sentadillas', fuente_titulo, BLACK, 250, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_grid()
    # draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    pygame.display.update()


def show_congratulations():
    window.fill(BLUE)
    show_text('Felicitacioes ', fuente_titulo, BLACK, 250, 50)
    show_text("Llegaste al final de tu rutina de tren superior, eres un ¡crack!", fuente_titulo, BLACK, 50, 100)
    draw_button(350, 500, 200, 100, PURPLE, GRAY,  'Finalizar', WHITE)
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
running = True #flag para mantener la aplicacion en ejecucion
exercise = None


# Bucle principal de la aplicación
while running:

    #Definir vista 
    if view == 'menu':
        show_menu()
    elif view == 'pushUp':
        show_pushUp()
    elif view == 'presbanca':
        show_pressBanca()
    elif view == 'CurlBicep':
        show_CurlBicep()
    elif view == 'Plancha':
        show_plancha()
    elif view == 'Sentadillas':
        show_sentadillas()
    elif view == 'Felicitaciones':
        show_congratulations()

    # elif view == 'exercise':
    #     show_exercise('Press de banca', frames_gif)

    #Obtener posicion mouse
    mouse_pos = pygame.mouse.get_pos()

    #Obtener eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar click en boton 
        if event.type == pygame.MOUSEBUTTONDOWN:
          
          if view == 'menu':
              if 100 <= mouse_pos[0] <= 250 and 200 <= mouse_pos[1] <= 250: # Ventana de ejercicios de tren superior 
                  view = 'pushUp'
              elif 100 <= mouse_pos[0] <= 250 and 450 <= mouse_pos[1] <= 500: # Ventana de ejercicios de tren inferior 
                  view = 'Sentadillas'
              elif 600 <= mouse_pos[0] <= 750 and 500 <= mouse_pos[1] <= 550: # Boton de salir
                  running = False
           
          elif view == 'pushUp':
               if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #Condicion para regresar al menu principal
                  view = 'menu'
               elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #Condicion para ir al siguiente ejercicio
                  view = "presbanca"
               
          elif view == 'presbanca':
             if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #condicion para el ejercio anterior
                  view = 'pushUp'
             elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #condicion para el siguiente ejercicio
                  view = 'CurlBicep'
             
          elif view == 'CurlBicep':
            if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550:
                view = 'presbanca'
            elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550:
                view = 'Plancha'
             
          elif view == 'Plancha':
              if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #condicion para ir al ejercicio anterior 
                  view = 'CurlBicep'
              elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #condición para finalizar la rutina 
                  view = "Felicitaciones"
          
          elif view == 'Felicitaciones':
                if 350 <= mouse_pos[0] <= 550 and 500 <= mouse_pos[1] <= 600:
                    view = "menu"
             
        

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