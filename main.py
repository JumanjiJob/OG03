import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600                                               # Задаем размеры экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   # Создаем экран с заданными размерами (размеры передаются в виде кортежа)
pygame.display.set_caption("Игра Тир")                            # Название окна
icon = pygame.image.load("img/icon.jpg")                          # Создаем иконку нашей игры
pygame.display.set_icon(icon)                                     # Вызываем иконку

target_img = pygame.image.load("img/target.png")                  # Картинка цели (утка)
target_img_1 = pygame.image.load("img/target_1.png")              # Картинка подбитой цели (подбитая утка)
target_width, target_height = target_img.get_size()               # Размеры цели (утки)

target_speed_x = 5
target_speed_y = 5
target_x = random.randint(0, SCREEN_WIDTH - target_width)         # Координата х нашей цели (утки)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)       # Координата У нашей цели (утки)

last_move_time = time.time()
move_delay = 0.25

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Рандомный цвет для заливки фона игрового экрана

pygame.mouse.set_visible(False)                                    # Отключаем видимость курсора мыши

cursor_img = pygame.image.load("img/cursor.png")                   # Картинка-прицел
cursor_width, cursor_height = cursor_img.get_size()                # Передаем ширину и высоту загруженного изображения курсора

# Счетчик попаданий
hit_count = 0

# Шрифт для отображения счета
font = pygame.font.Font(None, 36)

running = True
while running:                                                     # Основной цикл игры
    screen.fill(color)                                             # Заливка фона рандомным цветом
    for event in pygame.event.get():                               # Цикл для перебора всех событий в игре
        if event.type == pygame.QUIT:                              # Условие выхода из игры (закрытие игрового экрана)
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:                   # Если произошел клик, определяется координата, где этот клик произошел
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:  # Если произошло попадание в цель:
                hit_count += 1                                      # Увеличиваем счетчик попаданий
                target_img = target_img_1                           # Изменение картинки с утки на подбитую утку
                screen.blit(target_img, (target_x, target_y))       # Отрисовка цели на определенных координатах
                screen.blit(cursor_img, (mouse_x - cursor_width // 2, mouse_y - cursor_height // 2))  # Отрисовка курсора (прицела) на опр-ых координатах
                pygame.display.update()                             # Обновление экрана
                pygame.time.delay(200)                              # Задержка на 200 мс
                target_img = pygame.image.load("img/target.png")    # смена изображения цели обратно на target_img
                target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Новое перемещение цели на новые рандомные координаты
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Обновление позиции цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на столкновение со стенками экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    mouse_x, mouse_y = pygame.mouse.get_pos()  # Обновляем координаты на которых произошол клик
    screen.blit(target_img, (target_x, target_y))  # Отрисовка цели на определенных координатах
    screen.blit(cursor_img, (mouse_x - cursor_width // 2, mouse_y - cursor_height // 2))  # Отрисовка курсора (прицела) на опр-ых координатах

    # Отображение счетчика попаданий
    score_text = font.render(f"Попадания: {hit_count}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()  # Обновление экрана
    pygame.time.delay(15)

pygame.quit()
