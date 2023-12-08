import pygame
import random
import sys

# Setup
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG M1 MAC PORT PYGAME [C] Flames LABS")

font = pygame.font.Font(None, 24)
start_text = font.render("PRESS SPACE TO START", True, WHITE)

# Menu logic
menu_active = True

while menu_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_active = False

    screen.fill(BLACK)
    screen.blit(start_text, (225, 270))

    # Copyright text
    copy_text = font.render("PONG M1 MAC PORT PYGAME [C] Flames LABS 2023", True, WHITE)
    screen.blit(copy_text, (150, 560))
    pygame.display.flip()

# Rest of setup
clock = pygame.time.Clock()
score_font = pygame.font.Font(None, 36)

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 10
        self.score = 0

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    def move(self, up):
        if up:
            self.y -= self.speed
        else:
            self.y += self.speed

        # Prevent paddle from moving off-screen
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = -5
        self.speed_y = 5

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with top and bottom walls
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y *= -1

        # Ball collision with paddles
        if self.x - self.radius <= paddle1.x + paddle1.width and self.x + self.radius >= paddle1.x:
            if self.y >= paddle1.y and self.y <= paddle1.y + paddle1.height:
                self.speed_x *= -1

        if self.x + self.radius >= paddle2.x and self.x - self.radius <= paddle2.x + paddle2.width:
            if self.y >= paddle2.y and self.y <= paddle2.y + paddle2.height:
                self.speed_x *= -1

        # Ball out of bounds
        if self.x <= 0:
            self.reset()
            paddle2.score += 1

        if self.x >= WIDTH:
            self.reset()
            paddle1.score += 1

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x *= -1
        self.speed_y = random.choice([5, -5])

paddle1 = Paddle(10, HEIGHT // 2 - 40, 10, 80)
paddle2 = Paddle(780, HEIGHT // 2 - 40, 10, 80)
ball = Ball(WIDTH // 2, HEIGHT // 2, 8)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move(up=True)
    if keys[pygame.K_s]:
        paddle1.move(up=False)

    # AI for second paddle
    if ball.y < paddle2.y + paddle2.height / 2:
        paddle2.move(up=True)
    elif ball.y > paddle2.y + paddle2.height / 2:
        paddle2.move(up=False)

    ball.update()

    # Drawing code
    screen.fill(BLACK)
    paddle1.draw()
    paddle2.draw()
    ball.draw()

    # Score
    p1_score = score_font.render(str(paddle1.score), True, WHITE)
    p2_score = score_font.render(str(paddle2.score), True, WHITE)
    screen.blit(p1_score, (310, 10))
    screen.blit(p2_score, (450, 10))

    # Copyright text
    copy_text = font.render("PONG M1 MAC PORT PYGAME [C] Flames LABS 2023", True, WHITE)
    screen.blit(copy_text, (150, 560))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
