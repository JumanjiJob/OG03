import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Двигающаяся цель")

# Цвета
white = (255, 255, 255)

# Параметры цели
target_width = 50
target_height = 50
target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)

# Загрузка изображений
target_img = pygame.image.load("img/target.png")
target_img_1 = pygame.image.load("img/target_1.png")
cursor_img = pygame.image.load("img/cursor.png")
cursor_width, cursor_height = cursor_img.get_size()

# Главный цикл игры
running = True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_img = target_img_1  # смена изображения цели на target_img_1

                # Отрисовка цели и курсора
                screen.blit(target_img, (target_x, target_y))
                mouse_x, mouse_y = pygame.mouse.get_pos()
                screen.blit(cursor_img, (mouse_x - cursor_width // 2, mouse_y - cursor_height // 2))

                pygame.display.update()  # обновление экрана
                pygame.time.delay(500)  # задержка на 3 секунды

                target_img = pygame.image.load("img/target.png")  # смена изображения цели обратно на target_img
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)

    # Отрисовка цели и курсора
    screen.blit(target_img, (target_x, target_y))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_img, (mouse_x - cursor_width // 2, mouse_y - cursor_height // 2))

    # Обновление экрана
    pygame.display.update()

pygame.quit()
