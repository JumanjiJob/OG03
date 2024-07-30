import pygame
import random
import time

pygame.init()

running = True

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   # Задаем размеры экрана
pygame.display.set_caption("Игра Тир")                            # Название окна
icon = pygame.image.load("img/icon.jpg")                          # Вставляем картинку в иконку
pygame.display.set_icon(icon)                                     # Вызываем иконку

target_img = pygame.image.load("img/target.png")
target_img_1 = pygame.image.load("img/target_1.png")
target_width = 80                                                 # Размеры цели
target_height = 80

target_speed_x = 5
target_speed_y = 5
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

last_move_time = time.time()
move_delay = 3

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # Рандомная заливка фона

pygame.mouse.set_visible(False)

try:
    cursor_img = pygame.image.load("img/cursor.png")
    cursor_width, cursor_height = cursor_img.get_size()
except pygame.error as e:
    print(f"Не удалось загрузить изображение курсора: {e}")



while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_img = target_img_1
                screen.blit(target_img, (target_x, target_y))
                mouse_x, mouse_y = pygame.mouse.get_pos()
                screen.blit(cursor_img, (mouse_x - cursor_width // 2, mouse_y - cursor_height // 2))
                pygame.display.update()
                pygame.time.delay(200)
                target_img = pygame.image.load("img/target.png")  # смена изображения цели обратно на target_img
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

                #target_x += target_speed_x
    #target_y += target_speed_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(target_img,(target_x,target_y))
    screen.blit(cursor_img,(mouse_x - cursor_width // 2, mouse_y - cursor_height // 2))
    pygame.display.update()

pygame.quit()