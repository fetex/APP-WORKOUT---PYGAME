### APP ENFOCADA PARA REALIZAR EJERCICIO POR MEDIO DE RUTINAS DE GRUPOS MUSCULARES

# Importamos las librerias necesarias
import pygame
import time
import sys

# Inicializamos pygame
pygame.init()

# Definir constantes de la ventana
ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)



# Crear ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Entrenador Personal BodyBuilder')

# Crear fuentes
fuente_titulo = pygame.font.SysFont('Arial', 36)
fuente_texto = pygame.font.SysFont('Arial', 24)

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