import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platform Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Game variables
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 36)
coins = []
platforms = []

# Define classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = YELLOW
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(50, SCREEN_HEIGHT - self.height - 10, self.width, self.height)
        self.speed_x = 0
        self.speed_y = 0
        self.jump_power = -10

    def update(self):
        self.speed_y += 0.5  # Gravity
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Keep player inside the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # Check collisions with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.speed_y > 0:  # Falling down
                    self.rect.bottom = platform.rect.top
                    self.speed_y = 0
                elif self.speed_y < 0:  # Jumping up
                    self.rect.top = platform.rect.bottom
                    self.speed_y = 0

        # Check collisions with coins
        for coin in coins[:]:
            if self.rect.colliderect(coin.rect):
                coins.remove(coin)

        # Check if player falls off the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = 50
            self.rect.y = SCREEN_HEIGHT - self.height - 10
            self.speed_x = 0
            self.speed_y = 0

    def jump(self):
        self.speed_y = self.jump_power

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = BLACK
        self.width = 100
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = YELLOW
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)

# Create objects
player = Player()

# Create platforms
platform_positions = [
    (0, SCREEN_HEIGHT - 20),
    (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2),
    (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 20)
]

for x, y in platform_positions:
    platform = Platform(x, y)
    platforms.append(platform)

# Create coins
for _ in range(5):
    coin = Coin(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20))
    coins.append(coin)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_SPACE:
                player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    # Update objects
    player.update()

    # Draw objects
    for platform in platforms:
        pygame.draw.rect(screen, platform.color, platform.rect)

    for coin in coins:
        pygame.draw.rect(screen, coin.color, coin.rect)

    pygame.draw.rect(screen, player.color, player.rect)

    # Draw score
    score_text = game_font.render("Coins: " + str(len(coins)), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
