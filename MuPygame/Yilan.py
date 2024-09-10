# Write your code here :-)
import pygame
import random

# Oyun alanı boyutları
WIDTH = 600
HEIGHT = 400

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Yılan başlangıç konumu ve boyutu
snake_x = WIDTH / 2
snake_y = HEIGHT / 2
snake_size = 10

# Yılanın hızı ve yönü
snake_speed = 10
snake_dx = 0
snake_dy = 0

# Yem başlangıç konumu ve boyutu
food_x = random.randint(0, WIDTH - snake_size)
food_y = random.randint(0, HEIGHT - snake_size)
food_size = 10

# Yılanın vücudu (başlangıçta sadece baş)
snake_body = [(snake_x, snake_y)]

# Pygame başlatma
pygame.init()

# Oyun ekranı oluşturma
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yilan Oyunu")

# Ana oyun döngüsü
running = True
while running:
    # Ekranı temizleme
    screen.fill(WHITE)

    # Olayları dinleme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -snake_speed
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = snake_speed
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -snake_speed
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = snake_speed

    # Yılanın hareketi
    snake_x += snake_dx
    snake_y += snake_dy

    # Yılanın ekrandan çıkıp çıkmadığını kontrol etme
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        running = False

    # Yılanın yemeği yemesi
    if snake_x < food_x + food_size and snake_x + snake_size > food_x and snake_y < food_y + food_size and snake_y + snake_size > food_y:
        food_x = random.randint(0, WIDTH - snake_size)
        food_y = random.randint(0, HEIGHT - snake_size)
        snake_body.append((snake_x, snake_y))

    # Yılanın vücudunu güncelleme
    snake_body = snake_body[-1:] + snake_body[:-1]
    snake_body[0] = (snake_x, snake_y)

    # Yılanın vücudunu çizme
    for x, y in snake_body:
        pygame.draw.rect(screen, GREEN, (x, y, snake_size, snake_size))

    # Yemi çizme
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))

    # Ekranı güncelleme
    pygame.display.update()

    # Oyun hızını ayarlama
    pygame.time.Clock().tick(20)

# Pygame kapatma
pygame.quit()
