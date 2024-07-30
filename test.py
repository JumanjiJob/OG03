import pygame
import random
import time

pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

# Загрузка изображений
target_img = pygame.image.load("img/target.png")
target_img_1 = pygame.image.load("img/target_1.png")
target_width = 80
target_height = 80

# Начальные параметры цели
target_speed_x = 5
target_speed_y = 5
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Время последнего нажатия на цель
last_click_time = 0
click_delay = 0.25

# Рандомная заливка фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

pygame.mouse.set_visible(False)

# Загрузка изображения курсора
try:
    cursor_img = pygame.image.load("img/cursor.png")
    cursor_width, cursor_height = cursor_img.get_size()
except pygame.error as e:
    print(f"Не удалось загрузить изображение курсора: {e}")

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_img = target_img_1
                last_click_time = time.time()
                # Перемещение цели в случайное положение
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Обновление позиции цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на столкновение со стенками экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Проверка времени для смены изображения обратно
    if time.time() - last_click_time >= click_delay:
        target_img = pygame.image.load("img/target.png")

    # Отрисовка цели и курсора
    screen.blit(target_img, (target_x, target_y))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_img, (mouse_x - cursor_width // 2, mouse_y - cursor_height // 2))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
