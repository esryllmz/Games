import pygame
import sys
import random

# Oyun alanı boyutları
WIDTH = 800
HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Balon özellikleri
BALLOON_RADIUS = 30
BALLOON_SPEED = 5
BALLOON_FREQUENCY = 30

# Pygame başlatma
pygame.init()

# Oyun ekranı oluşturma
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Popping Game")

# Balonları saklamak için liste oluşturma
balloons = []

# Oyuncu imleci çizimi
def draw_cursor(x, y):
    pygame.draw.circle(screen, RED, (x, y), 5)

# Balon çizimi
def draw_balloons():
    for balloon in balloons:
        pygame.draw.circle(screen, RED, (balloon[0], balloon[1]), BALLOON_RADIUS)

# Balonları hareket ettirme
def move_balloons():
    for balloon in balloons:
        balloon[0] += balloon[2]  # X koordinatını güncelle
        balloon[1] += balloon[3]  # Y koordinatını güncelle

        # Ekran kenarlarına çarpma kontrolü
        if balloon[0] < BALLOON_RADIUS or balloon[0] > WIDTH - BALLOON_RADIUS:
            balloon[2] *= -1  # X yönünü tersine çevir
        if balloon[1] < BALLOON_RADIUS or balloon[1] > HEIGHT - BALLOON_RADIUS:
            balloon[3] *= -1  # Y yönünü tersine çevir

# Balonları oluşturma
def create_balloon():
    x = random.randint(BALLOON_RADIUS, WIDTH - BALLOON_RADIUS)
    y = random.randint(BALLOON_RADIUS, HEIGHT - BALLOON_RADIUS)
    dx = random.choice([-1, 1])  # Rasgele X yönü seç
    dy = random.choice([-1, 1])  # Rasgele Y yönü seç
    balloons.append([x, y, dx, dy])

# Balonları kontrol etme ve ekrandan çıkarma
def check_balloons():
    for balloon in balloons:
        if balloon[1] < -BALLOON_RADIUS or balloon[1] > HEIGHT + BALLOON_RADIUS:
            balloons.remove(balloon)

# Balon patlatma kontrolü
def pop_balloon(mouse_x, mouse_y):
    for balloon in balloons:
        if ((balloon[0] - mouse_x)**2 + (balloon[1] - mouse_y)**2)**0.5 <= BALLOON_RADIUS:
            balloons.remove(balloon)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Sol fare tuşuna basıldığında
                mouse_x, mouse_y = event.pos
                pop_balloon(mouse_x, mouse_y)

    # Balonları oluşturma ve kontrol etme
    if random.randint(1, BALLOON_FREQUENCY) == 1:
        create_balloon()
    move_balloons()
    check_balloons()

    # Fare imleci çizme
    mouse_x, mouse_y = pygame.mouse.get_pos()
    draw_cursor(mouse_x, mouse_y)

    # Balonları çizme
    draw_balloons()

    # Ekranı güncelleme
    pygame.display.update()

    # Oyun hızını ayarlama
    clock.tick(60)

# Pygame kapatma
pygame.quit()
sys.exit()
