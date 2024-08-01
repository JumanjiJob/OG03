import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
color = (173,216,230)

pygame.mouse.set_visible(False)
cursor_img = pygame.image.load('img/cursor.png')
cursor_width, cursor_height = cursor_img.get_size()

target_img = pygame.image.load('img/target.png')
target_img_1 = pygame.image.load('img/target_1.png')
target_width, target_height = target_img.get_size()

target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor_x, cursor_y = pygame.mouse.get_pos()
            if target_x < cursor_x < target_x + target_width and target_y < cursor_y < target_y + target_height:
                target_img = target_img_1
                screen.blit(target_img, (target_x, target_y))
                screen.blit(cursor_img, (cursor_x - cursor_width//2, cursor_y - cursor_height//2))
                pygame.display.update()
                pygame.time.delay(200)
                target_img = pygame.image.load('img/target.png')
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    cursor_x, cursor_y = pygame.mouse.get_pos()
    screen.blit(target_img, (target_x, target_y))
    screen.blit(cursor_img, (cursor_x - cursor_width // 2, cursor_y - cursor_height // 2))
    pygame.display.update()



pygame.quit()

