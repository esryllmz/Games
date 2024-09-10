import pygame
import random

# Oyun alanı boyutları
WIDTH = 800
HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Uzay gemisi başlangıç konumu ve boyutu
ship_width = 50
ship_height = 50
ship_x = WIDTH / 2 - ship_width / 2
ship_y = HEIGHT - 2 * ship_height

# Düşman gemisi başlangıç konumu, boyutu ve hızı
enemy_width = 50
enemy_height = 50
enemy_speed = 5
enemy_list = []

# Mermi başlangıç konumu, boyutu ve hızı
bullet_width = 5
bullet_height = 15
bullet_speed = 10
bullet_list = []

# Skor
score = 0

# Pygame başlatma
pygame.init()

# Oyun ekranı oluşturma
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uzay Savaşı Oyunu")

# Uzay gemisi çizimi
def draw_ship(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, ship_width, ship_height))

# Düşman gemisi oluşturma
def create_enemy():
    enemy_x = random.randint(0, WIDTH - enemy_width)
    enemy_y = random.randint(-HEIGHT, 0)
    enemy_list.append([enemy_x, enemy_y])

# Düşman gemileri çizimi
def draw_enemies():
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

# Mermi çizimi
def draw_bullets():
    for bullet in bullet_list:
        pygame.draw.rect(screen, GREEN, (bullet[0], bullet[1], bullet_width, bullet_height))

# Ana oyun döngüsü
running = True
clock = pygame.time.Clock()
while running:
    # Ekranı temizleme
    screen.fill(BLACK)

    # Olayları dinleme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_x -= 10
            elif event.key == pygame.K_RIGHT:
                ship_x += 10
            elif event.key == pygame.K_SPACE:
                bullet_list.append([ship_x + ship_width / 2 - bullet_width / 2, ship_y])

    # Uzay gemisini çizme
    draw_ship(ship_x, ship_y)

    # Düşman gemilerini oluşturma ve hareket ettirme
    if len(enemy_list) < 5: # Aynı anda en fazla 5 düşman gemisi
        create_enemy()
    for enemy in enemy_list:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemy_list.remove(enemy)

    # Mermileri hareket ettirme
    for bullet in bullet_list:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullet_list.remove(bullet)

    # Mermileri ve düşman gemilerini çizme
    draw_bullets()
    draw_enemies()

    # Mermi - düşman çarpışmalarını kontrol etme
    for bullet in bullet_list:
        for enemy in enemy_list:
            if bullet[0] < enemy[0] + enemy_width and bullet[0] + bullet_width > enemy[0] and bullet[1] < enemy[1] + enemy_height and bullet[1] + bullet_height > enemy[1]:
                bullet_list.remove(bullet)
                enemy_list.remove(enemy)
                score += 10

    # Skoru ekrana yazdırma
    font = pygame.font.SysFont(None, 30)
    text = font.render("Skor: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    # Ekranı güncelleme
    pygame.display.update()

    # Oyun hızını ayarlama
    clock.tick(60)

# Pygame kapatma
pygame.quit()
