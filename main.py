import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   # Задаем размеры экрана

pygame.display.set_caption("Игра Тир")                            # Название окна
icon = pygame.image.load("img/images.jpg")                        # Вставляем картинку в иконку
pygame.display.set_icon(icon)                                     # Вызываем иконку

target_img = pygame.image.load("img/target.png")                  # Объект по которому мы будем стрелять
target_width = 80                                                 # Размеры цели
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)      # Рандомное перемещение цели
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # Рандомная заливка фона





running = True
while running:
    pass

pygame.quit()
