import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Fruit")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game variables
score = 0
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 36)
fruits = []

# Define classes
class Fruit:
    def __init__(self):
        self.color = random.choice([RED, GREEN, BLUE])
        self.size = 30
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - self.size),
                                 -self.size, self.size, self.size)
        self.speed_y = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speed_y

class Basket:
    def __init__(self):
        self.color = BLACK
        self.width = 100
        self.height = 20
        self.rect = pygame.Rect((SCREEN_WIDTH - self.width) // 2, SCREEN_HEIGHT - self.height,
                                 self.width, self.height)

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - self.width // 2
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - self.width:
            self.rect.x = SCREEN_WIDTH - self.width

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Create objects
basket = Basket()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update objects
    basket.update()

    # Create new fruits
    if random.random() < 0.05:
        fruits.append(Fruit())

    # Update and draw fruits
    for fruit in fruits[:]:
        fruit.update()
        if fruit.rect.y > SCREEN_HEIGHT:
            fruits.remove(fruit)
        elif fruit.rect.colliderect(basket.rect):
            fruits.remove(fruit)
            score += 1

    # Draw objects
    for fruit in fruits:
        pygame.draw.rect(screen, fruit.color, fruit.rect)
    basket.draw()

    # Draw score
    score_text = game_font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
