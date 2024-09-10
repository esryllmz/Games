import pygame
import sys
import random

# Oyun alanı boyutları
WIDTH = 800
HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Karakter özellikleri
PLAYER_SIZE = 50
PLAYER_SPEED = 5
PLAYER_RANGE = 75

# Düşman özellikleri
ENEMY_SIZE = 30
ENEMY_SPEED = 3
ENEMY_COUNT = 5

# Pygame başlatma
pygame.init()

# Oyun ekranı oluşturma
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Tarzı Oyun")

# Font
font = pygame.font.Font(None, 36)

# Karakter ve düşmanların başlangıç konumlarını belirleme
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT // 2 - PLAYER_SIZE // 2
enemies = []
for _ in range(ENEMY_COUNT):
    enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
    enemy_y = random.randint(0, HEIGHT - ENEMY_SIZE)
    enemies.append((enemy_x, enemy_y))

# Ana karakterin çizimi
def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, PLAYER_SIZE, PLAYER_SIZE))

# Düşmanların çizimi
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, (enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE))

# Düşmanları öldürme metni çizimi
def draw_kill_text():
    text = font.render("Press 'R' to increase player range or 'S' to increase speed", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(text, text_rect)

# Ana oyun döngüsü
clock = pygame.time.Clock()
running = True
while running:
    # Ekranı temizleme
    screen.fill(WHITE)

    # Olayları dinleme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Klavye girişlerini kontrol etme
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_y += PLAYER_SPEED

    # Karakterin sınırları kontrol etme
    player_x = max(0, min(WIDTH - PLAYER_SIZE, player_x))
    player_y = max(0, min(HEIGHT - PLAYER_SIZE, player_y))

    # Düşman hareketi
    for i in range(len(enemies)):
        enemy_x, enemy_y = enemies[i]
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left':
            enemy_x -= ENEMY_SPEED
        elif direction == 'right':
            enemy_x += ENEMY_SPEED
        elif direction == 'up':
            enemy_y -= ENEMY_SPEED
        elif direction == 'down':
            enemy_y += ENEMY_SPEED
        # Düşmanın sınırları kontrol etme
        enemy_x = max(0, min(WIDTH - ENEMY_SIZE, enemy_x))
        enemy_y = max(0, min(HEIGHT - ENEMY_SIZE, enemy_y))
        enemies[i] = (enemy_x, enemy_y)

    # Çizimler
    draw_player(player_x, player_y)
    draw_enemies()
    draw_kill_text()

    # Düşmanlara çarpışma kontrolü ve düşman öldürme
    for i, enemy in enumerate(enemies):
        enemy_rect = pygame.Rect(enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE)
        player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
        if keys[pygame.K_SPACE] and abs(player_x - enemy[0]) < PLAYER_RANGE and abs(player_y - enemy[1]) < PLAYER_RANGE:
            del enemies[i]
            print("Enemy killed!")
        if player_rect.colliderect(enemy_rect):
            print("You died!")
            running = False
            break

    # Ekranı güncelleme
    pygame.display.update()

    # Oyun hızını ayarlama
    clock.tick(60)

# Pygame kapatma
pygame.quit()
sys.exit()
