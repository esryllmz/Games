import pygame
import sys
import random

# Oyun alanı boyutları
WIDTH = 800
HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Kart özellikleri
CARD_WIDTH = 100
CARD_HEIGHT = 100
GRID_ROWS = 4
GRID_COLS = 4
GAP = 10

# Pygame başlatma
pygame.init()

# Oyun ekranı oluşturma
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hafıza Eşleştirme Oyunu")

# Font yüklemesi
font = pygame.font.Font(None, 36)

# Renkli kartların listesi
colors = [WHITE, WHITE, BLACK, BLACK, (255, 0, 0), (255, 0, 0),
          (0, 255, 0), (0, 255, 0), (0, 0, 255), (0, 0, 255),
          (255, 255, 0), (255, 255, 0), (255, 128, 0), (255, 128, 0),
          (128, 0, 255), (128, 0, 255)]

# Kartların karıştırılması
random.shuffle(colors)

# Kartların yerleştirilmesi
cards = []
revealed = [False] * len(colors)  # Kartların açık olup olmadığını tutan liste
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        x = col * (CARD_WIDTH + GAP) + GAP
        y = row * (CARD_HEIGHT + GAP) + GAP
        cards.append(pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT))

# Kartların çizimi
def draw_cards():
    for i, card in enumerate(cards):
        if revealed[i]:
            pygame.draw.rect(screen, colors[i], card)
        else:
            pygame.draw.rect(screen, BLACK, card)

# Ana oyun döngüsü
clock = pygame.time.Clock()
running = True
selected_card_indexes = []
while running:
    # Ekranı temizleme
    screen.fill(WHITE)

    # Olayları dinleme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and len(selected_card_indexes) < 2:
            mouse_x, mouse_y = event.pos
            for i, card in enumerate(cards):
                if card.collidepoint(mouse_x, mouse_y) and not revealed[i]:
                    selected_card_indexes.append(i)
                    revealed[i] = True

    # Seçili kartları kontrol etme
    if len(selected_card_indexes) == 2:
        if colors[selected_card_indexes[0]] != colors[selected_card_indexes[1]]:
            revealed[selected_card_indexes[0]] = False
            revealed[selected_card_indexes[1]] = False
        selected_card_indexes = []

    # Kartları çizme
    draw_cards()

    # Ekranı güncelleme
    pygame.display.update()

    # Oyun hızını ayarlama
    clock.tick(60)

# Pygame kapatma
pygame.quit()
sys.exit()
