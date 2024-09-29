### APP ENFOCADA PARA REALIZAR EJERCICIO POR MEDIO DE RUTINAS DE GRUPOS MUSCULARES

# Importamos las librerias necesarias
import pygame
import time
import sys
from PIL import Image
import cv2


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

# Variables globales para el sistema de puntos
ejercicios_realizados = 0
total_ejercicios_pecho = 4  # Definir cuántos ejercicios debe completar para felicitar

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
def mostrar_texto(texto, fuente, color, x, y):
    superficie_texto = fuente.render(texto, True, color)
    window.blit(superficie_texto, (x, y))


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
            #frame_surface = pygame.transform.rotate(frame_surface, 270) # 
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
    mostrar_texto(f'Iniciando {ejercicio}', fuente_titulo, BLACK, 100, 50)
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
            mostrar_texto(f'Serie {serie_actual} - Repetición {repeticion_actual + 1}', fuente_texto, BLACK, 100, 150) # Numero de serie
            mostrar_texto(f'Rep. restantes: {repeticiones - repeticion_actual - 1}', fuente_texto, BLACK, 100, 200) # Numero de repeticiones restantes
            mostrar_texto(f'Tiempo: {time.strftime("%H:%M:%S", time.gmtime(time.time()))}', fuente_texto, BLACK, 100, 250) #Segundo 
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
                mostrar_texto(f'Descanso entre series: {descanso - tiempo_transcurrido} segundos', fuente_texto, BLACK, 100, 150)
                pygame.display.update()
            else:
                descanso_iniciado = False
                repeticion_actual = 0
                serie_actual += 1

        # Si se completaron todas las series, terminar el ejercicio
        if serie_actual > series:
            mostrar_texto('Ejercicio Completado', fuente_texto, BLACK, 100, 300)
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
    global ejercicios_realizados, total_ejercicios_pecho

    if ejercicios_realizados >= total_ejercicios_pecho:
        window.fill(WHITE)
        mostrar_texto('¡Felicitaciones!', fuente_titulo, BLACK, 100, 200)
        mostrar_texto('Has completado tu rutina de pecho.', fuente_titulo, BLACK, 100, 250)
        pygame.display.update()
        time.sleep(3)  # Pausa para que pueda ver el mensaje

        # Reiniciar el contador de ejercicios
        ejercicios_realizados = 0

        # Retornar al menú principal
        return_to_menu()

def return_to_menu():
    global view
    view = 'menu'

def draw_grid():
    # lINEAS HORIZONTALES
    for y in range (0, HEIGHT, SIZE_CELL):
        pygame.draw.line(window, GRAY, (0, y), (WIDTH, y))

    # LINEAS VERTICALES
    for x in range (0, WIDTH, SIZE_CELL):
        pygame.draw.line(window, GRAY, (x, 0), (x, HEIGHT))
# Funcion para mostrar menu

def show_menu():  # Vista menu
    window.fill(WHITE)
    draw_grid() # Llamar a la funcion para dibujar la cuadricula
    draw_button(100, 50, 150, 50, BLUE, PURPLE, "Bipces", BLACK)
    draw_button(100, 200, 150, 50, GREEN, GREEN_BLACK, 'Pecho', BLACK)
    draw_button(400, 150, 200, 75, GRAY, BLACK, 'Espalda', WHITE)
    draw_button(250, 300, 150, 50, BLACK, GRAY, 'Salir', WHITE)
    pygame.display.update()


# Vista pecho
def show_chest():
    window.fill(WHITE) # Color de la ventana o vista 
    draw_grid()
    draw_button(100, 200, 150, 50, GREEN, GREEN_BLACK, 'Press de banca', BLACK)
    draw_button(250, 300, 150, 50, BLACK, GRAY,  'Regresar', WHITE)
    mostrar_texto('Ejercios de Pecho', fuente_titulo, BLACK, 400, 0)
    pygame.display.update()

def show_biceps():
    window.fill(BLUE)
    draw_grid()
    draw_button (200, 100, 150, 50, BLACK, GRAY, 'Curl de biceps', WHITE)
    draw_button (200, 500, 150, 50, BLACK, GRAY, 'regresar', WHITE)
    mostrar_texto('Ejercios de biceps', fuente_titulo, BLACK, 400, 0)
    pygame.display.update()






view = 'menu'
running = True #flag para mantener la aplicacion en ejecucion
exercise = None


# Bucle principal de la aplicación
while running:

    #Definir vista 
    if view == 'menu':
        show_menu()
    elif view == 'chest':
        show_chest()
    elif view == 'biceps':
        show_biceps()
    elif view == 'exercise_press_bench':
        iniciar_ejercicio('Press de banca', 3, 10)
        view = 'chest'



    #Obtener posicion mouse
    mouse_pos = pygame.mouse.get_pos()

    #Obtener eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar click en boton 
        if event.type == pygame.MOUSEBUTTONDOWN:
          
          if view == 'menu':
              if 100 <= mouse_pos[0] <= 250 and 200 <= mouse_pos[1] <= 250:
                  view = 'chest'
              elif 100 <= mouse_pos[0] <= 250 and 50 <= mouse_pos[1] <= 100:
                  view = 'biceps'
              elif 250 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 350:
                  running = False

          elif view == 'chest':
              if 250 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 350: #Condicion para regresar al menu boton regresar
                  view = 'menu'
              elif 100 <= mouse_pos[0] <= 250 and 200 <= mouse_pos[1] <= 250: #Ejercicio press de banca
                  iniciar_ejercicio('Press de banca', 3, 10, video_path='media/pecho.mp4')

         
          
pygame.quit()
sys.exit()