### APP ENFOCADA PARA REALIZAR EJERCICIO POR MEDIO DE RUTINAS DE GRUPOS MUSCULARES

# Importamos las librerias necesarias
import pygame
import time
import sys
import cv2







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

# Variables globales para el sistema de puntos
ejercicios_realizados = 0
total_ejercicios_rutina = 4  # Definir cuántos ejercicios debe completar para felicitar



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

# def draw_grid():
#     # lINEAS HORIZONTALES
#     for y in range (0, HEIGHT, SIZE_CELL):
#         pygame.draw.line(window, GRAY, (0, y), (WIDTH, y))

#     # LINEAS VERTICALES
#     for x in range (0, WIDTH, SIZE_CELL):
#         pygame.draw.line(window, GRAY, (x, 0), (x, HEIGHT))


def play_exercise_video(ruta):
    # Dimensiones de la ventana de video
    video_width, video_height = 640, 480
    video_window = pygame.display.set_mode((video_width, video_height))
    pygame.display.set_caption("Video - Rutina de Ejercicio")

    # Cargar el video usando OpenCV
    video = cv2.VideoCapture(ruta)
    clock = pygame.time.Clock()

    running_video = True
    while running_video:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_video = False

        # Leer el frame actual del video
        ret, frame = video.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame_rgb)
            frame_surface = pygame.transform.rotate(frame_surface, 270) # rotar video segun angulo
            frame_surface = pygame.transform.scale(frame_surface, (video_width, video_height))
            video_window.blit(frame_surface, (0, 0))
            pygame.display.update()
            clock.tick(30)  # Controlar la tasa de frames por segundo del video
        else:
            running_video = False  # Cuando el video termina, cerramos la ventana

    video.release()

    # Al finalizar el video, restauramos la ventana principal
    pygame.display.set_mode((WIDTH, HEIGHT))  # Restaurar el tamaño de la ventana principal
    pygame.display.set_caption('Entrenador Personal BodyBuilder')

# Función para simular un ejercicio
def iniciar_ejercicio(ejercicio, series, repeticiones, descanso=5, video_path=None):
    global ejercicios_realizados

    # Si se proporciona una ruta de video, se reproduce el video del ejercicio
    if video_path:
        play_exercise_video(video_path)

    # Después de reproducir el video, procedemos con el flujo del ejercicio
    window.fill(WHITE)
    show_text(f'Iniciando {ejercicio}', fuente_titulo, BLACK, 100, 50)
    pygame.display.update()

    serie_actual = 1
    descanso_iniciado = False
    tiempo_inicio_descanso = 0

    clock = pygame.time.Clock()
    repeticion_actual = 0

    running_ejercicio = True
    while running_ejercicio:
        window.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_ejercicio = False

        # Mostrar información del ejercicio actual
        if repeticion_actual < repeticiones:
            show_text(f'Serie {serie_actual} - Repetición {repeticion_actual + 1}', fuente_texto, BLACK, 100, 150) # Numero de serie
            show_text(f'Rep. restantes: {repeticiones - repeticion_actual - 1}', fuente_texto, BLACK, 100, 200) # Numero de repeticiones restantes
            repeticion_actual += 1
            pygame.display.update()
            clock.tick(1)  # Simular una repetición por segundo

        # Si se completaron las repeticiones, iniciar descanso
        elif serie_actual <= series and not descanso_iniciado:
            descanso_iniciado = True
            tiempo_inicio_descanso = pygame.time.get_ticks()

        # Manejar el temporizador de descanso
        elif descanso_iniciado:
            tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio_descanso) // 1000
            if tiempo_transcurrido < descanso:
                show_text(f'Descanso entre series: {descanso - tiempo_transcurrido} segundos', fuente_texto, BLACK, 100, 150)
                pygame.display.update()
            else:
                descanso_iniciado = False
                repeticion_actual = 0
                serie_actual += 1

        # Si se completaron todas las series, terminar el ejercicio
        if serie_actual > series:
            show_text('Ejercicio Completado', fuente_texto, BLACK, 100, 300)
            draw_button(250, 350, 150, 50, BLACK, GRAY, 'Regresar', WHITE)
            pygame.display.update()
            running_ejercicio = False

            # Incrementar el contador de ejercicios realizados
            ejercicios_realizados += 1

            # Verificar si ha completado todos los ejercicios de la rutina
            verificar_completacion_rutina()

        clock.tick(30)  # Controlar la tasa de fotogramas por segundo (FPS)

    time.sleep(2)
    pygame.display.update()


def verificar_completacion_rutina():
    global ejercicios_realizados, total_ejercicios_rutina

    if ejercicios_realizados >= total_ejercicios_rutina:
        window.fill(WHITE)
        show_text('¡Felicitaciones!', fuente_titulo, BLACK, 100, 200)
        show_text('Has completado tu rutina.', fuente_titulo, BLACK, 100, 250)
        pygame.display.update()
        time.sleep(3)  # Pausa para que pueda ver el mensaje

        # Reiniciar el contador de ejercicios
        ejercicios_realizados = 0

        # Retornar al menú principal
        return_to_menu()

def return_to_menu():
    global view
    view = 'menu'


# Funcion para mostrar menu
def show_menu():  # Vista menu
    window.fill(BLUE)
    show_text("Hola, soy tu entrenador personalizado", fuente_titulo, BLACK, 50, 50)
    show_text("selecciona la parte del cuerpo que deseas entrenar el dia de hoy:", fuente_texto, BLACK, 50, 100)
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
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    draw_button(300,250, 150, 100,GRAY, WHITE, 'Iniciar', BLACK)
    pygame.display.update()

def show_pressBanca():
    window.fill(BLUE)
    show_text('Press banco plano', fuente_titulo, BLACK, 250, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    draw_button(300,250, 150, 100,GRAY, WHITE, 'Iniciar', BLACK)

    pygame.display.update()
    pygame.display.update()

def show_CurlBicep():
    window.fill(BLUE)
    show_text('Curl bicep', fuente_titulo, BLACK, 300, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    draw_button(300,250, 150, 100,GRAY, WHITE, 'Iniciar', BLACK)
    pygame.display.update()
    pygame.display.update()

def show_plancha():
    window.fill(BLUE)
    show_text('Plancha', fuente_titulo, BLACK, 300, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'Finalizar', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    draw_button(300,250, 150, 100,GRAY, WHITE, 'Iniciar', BLACK)
    pygame.display.update()

def show_congratulations():
    window.fill(BLUE)
    show_text('Felicitaciones ', fuente_titulo, BLACK, 280, 50)
    show_text("Has ganado 100 puntos", fuente_texto, RED, 300, 100)
    show_text("Llegaste al final de tu rutina, eres un ¡crack!", fuente_texto, BLACK,175, 150)
    draw_button(300, 450, 200, 100, PURPLE, GRAY,  'Finalizar', WHITE)
    pygame.display.update()

def show_extensionRodillas():
    window.fill(BLUE)
    show_text('Extension Rodilla', fuente_titulo, BLACK, 250, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    draw_button(300,250, 150, 100,GRAY, WHITE, 'Iniciar', BLACK)
    pygame.display.update()

def show_desplazamientos():
    window.fill(BLUE)
    show_text('Desplazamientos', fuente_titulo, BLACK, 250, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    draw_button(300,250, 150, 100,GRAY, WHITE, 'Iniciar', BLACK)
    pygame.display.update()

def show_sentadillas():
    window.fill(BLUE)
    show_text('Sentadillas', fuente_titulo, BLACK, 300, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'siguiente', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    draw_button(300,250, 150, 100,GRAY, WHITE, 'Iniciar', BLACK)
    pygame.display.update()

def show_flexionDeRodilla():
    window.fill(BLUE)
    show_text('Flexion de Rodilla', fuente_titulo, BLACK, 250, 50)
    show_text("Acuéstate boca abajo, manos a la altura de los hombros y cuerpo recto,", fuente_texto2, BLACK, 50, 100)
    show_text("Baja Flexionando los codos y baja el pecho hacia el suelo.", fuente_texto2, BLACK, 50, 125)
    show_text("Sube, Empujando con las manos para volver a la posición inicial.", fuente_texto2, BLACK, 50, 150)
    draw_button(450, 500, 150, 50, ORANGE, GRAY, 'Finalizar', BLACK)
    draw_button(200, 500, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    draw_button(300,250, 150, 100,GRAY, WHITE, 'Iniciar', BLACK)
    pygame.display.update()


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
    elif view == 'Felicitaciones':
        show_congratulations()
    elif view == 'ExtensionRodillas':
        show_extensionRodillas()
    elif view == 'Desplazamientos':
        show_desplazamientos()
    elif view == 'Sentadillas':
        show_sentadillas()
    elif view == 'FlexionRodillas':
        show_flexionDeRodilla()

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
                  view = 'ExtensionRodillas'
              elif 600 <= mouse_pos[0] <= 750 and 500 <= mouse_pos[1] <= 550: # Boton de salir
                  running = False
           
          elif view == 'pushUp':
               if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #Condicion para regresar al menu principal
                  view = 'menu'
               elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #Condicion para ir al siguiente ejercicio
                  view = "presbanca"
               elif 300 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
                   iniciar_ejercicio('Push Up', 3, 10, 5, 'push_up.mp4')
               
          elif view == 'presbanca':
             if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #condicion para el ejercio anterior
                  view = 'pushUp'
             elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #condicion para el siguiente ejercicio
                  view = 'CurlBicep'
             elif 300 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
                   iniciar_ejercicio('Press Banca', 3, 10, 5, 'media/push_up.mp4')
             
          elif view == 'CurlBicep':
            if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550:
                view = 'presbanca'
            elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550:
                view = 'Plancha'
            elif 300 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
                   iniciar_ejercicio('CurlBicep', 3, 10, 5, 'media/push_up.mp4')
             
          elif view == 'Plancha':
              if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #condicion para ir al ejercicio anterior 
                  view = 'CurlBicep'
              elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #condición para finalizar la rutina 
                  view = "Felicitaciones"
              elif 300 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
                   iniciar_ejercicio('Plancha', 3, 10, 5, 'media/push_up.mp4')
          
          elif view == 'Felicitaciones':
                if 300 <= mouse_pos[0] <= 500 and 450 <= mouse_pos[1] <= 550:
                    view = "menu"

          elif view == 'ExtensionRodillas':
               if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #Condicion para regresar al menu principal
                  view = 'menu'
               elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #Condicion para ir al siguiente ejercicio
                  view = "Desplazamientos"
               elif 300 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
                   iniciar_ejercicio('Extension de Rodillas', 3, 10, 5, 'media/push_up.mp4')  

          elif view == 'Desplazamientos':
               if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #Condicion para regresar al menu principal
                  view = 'ExtensionRodillas'
               elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #Condicion para ir al siguiente ejercicio
                  view = 'Sentadillas'
               elif 300 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
                   iniciar_ejercicio('Desplazamientos', 3, 10, 5, 'media/push_up.mp4')     

          elif view == 'Sentadillas':
               if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #Condicion para regresar al menu principal
                  view = 'Desplazamientos'
               elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #Condicion para ir al siguiente ejercicio
                  view = 'FlexionRodillas'
               elif 300 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
                   iniciar_ejercicio('Sentadillas', 3, 10, 5, 'media/push_up.mp4')   
        
          elif view == 'FlexionRodillas':
               if 200 <= mouse_pos[0] <= 350 and 500 <= mouse_pos[1] <= 550: #Condicion para regresar al menu principal
                  view = 'Sentadillas'
               elif 450 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550: #Condicion para ir al siguiente ejercicio
                  view = "Felicitaciones"
               elif 300 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
                   iniciar_ejercicio('Flexión Rodillas', 3, 10, 5, 'media/push_up.mp4')   


pygame.quit()
sys.exit()
