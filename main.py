### APP ENFOCADA PARA REALIZAR EJERCICIO POR MEDIO DE RUTINAS DE GRUPOS MUSCULARES

# Importamos las librerias necesarias
import pygame
import time
import sys

# Inicializamos pygame
pygame.init()

# Colors app in rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREEN_BLACK = (0, 200, 0)
RED = (255, 0, 0)

#Size window 
WIDTH = 800
HEIGHT = 600

# Crear ventana
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Entrenador Personal BodyBuilder')

# Crear fuentes
fuente_titulo = pygame.font.SysFont('Arial', 36)
fuente_texto = pygame.font.SysFont('Arial', 24)

# Funcion para crear boton
def draw_button(x, y, width, height, color, text, text_color):
    pygame.draw.rect(window, color, (x, y, width, height))
    text_button = fuente_texto.render(text, True, text_color)
    window.blit(text_button, (x + (width - text_button.get_width()) // 2, y + (height - text_button.get_height()) // 2)) ## Centro el texto en el boton

# Bucle principal de la aplicación

running = True
while running:
    window.fill(WHITE)

    #Obtener posicion mouse
    mouse_pos = pygame.mouse.get_pos()

    #Efecto hover boton 
    if 100 <= mouse_pos[0] <= 250 and 100 <= mouse_pos[1] <= 250:
        color_buttom = GREEN_BLACK
    else:
        color_buttom = GREEN

    #Dibujar botones
    draw_button(100, 200, 150, 50, color_buttom, 'Pecho', BLACK) #Boton pecho
    draw_button(250, 300, 150, 50, BLACK, 'Salir', RED) #Boton salir

    #Obtener eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar click en boton rutina pecho
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 100 <= mouse_pos[0] <= 250 and 200 <= mouse_pos[1] <= 250:
                print('Click en boton pecho')

            if 250 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 350:
                running = False
        
    #Actualizar pantalla
    pygame.display.update()



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

# # Bucle principal de la aplicación
# ejecutando = True
# while ejecutando:
    # mostrar_menu_partes_cuerpo()

    # for evento in pygame.event.get():
    #     if evento.type == pygame.QUIT:
    #         ejecutando = False
    #     elif evento.type == pygame.KEYDOWN:
    #         if evento.key == pygame.K_1:
    #             iniciar_ejercicio('Pecho', 3, 10)
    #         elif evento.key == pygame.K_2:
    #             iniciar_ejercicio('Piernas', 4, 12)
    #         elif evento.key == pygame.K_3:
    #             iniciar_ejercicio('Espalda', 3, 8)

pygame.quit()
sys.exit()