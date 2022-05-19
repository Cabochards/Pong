import pygame
import random

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Volley Pong")
terrain_image = pygame.image.load("terrain.jpg")


class Paddle:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.height = 100
        self.width = 15
        self.image = pygame.image.load(image)
        self.score = 0

    def display(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, dist):
        self.y += dist

    def run(self):
        self.display()
        if self.y < -self.height:
            self.y += 600
        elif self.y > 600:
            self.y -= 600


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.side = 21
        self.direc_x = random.choice([-0.5, 0.5])
        self.direc_y = random.choice([-0.5, 0.5])
        self.image = pygame.image.load("balle.png")
        self.speed = 1

    def display(self):
        screen.blit(self.image, (self.x, self.y))

    def run(self):
        if self.y <= 0 or self.y > 600 - self.side:
            self.direc_y *= -1

        if self.speed > 5:
            self.speed = 5

        self.y += self.direc_y * self.speed
        self.x += self.direc_x * self.speed
        self.speed += 0.001
        self.display()

    def check_collision(self, p_left, p_right):
        if self.x < p_left.x + p_left.width:
            if p_left.y < self.y < p_left.y + p_left.height:
                self.direc_x *= -1
                if self.y + self.side <= p_left.y:
                    self.direc_y *= -1

        if self.x + self.side > p_right.x:
            if p_right.y < self.y < p_right.y + p_right.height:
                self.direc_x *= -1

        if self.x < 0:
            self.x = 400
            self.y = 300
            self.speed = 1
            p_right.score += 1

        if self.x > 800 + self.side:
            self.x = 400
            self.y = 300
            self.speed = 1
            p_left.score += 1

        self.run()


p1 = Paddle(10, 100, 'barre1.png')
p2 = Paddle(780, 100, 'barre2.png')
ball = Ball(300, 300)
paddles = [p1, p2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        p1.move(-5)

    if keys[pygame.K_s]:
        p1.move(5)

    if keys[pygame.K_UP]:
        p2.move(-5)

    if keys[pygame.K_DOWN]:
        p2.move(5)

    ball.check_collision(p1, p2)

    ball.run()
    p1.run()
    p2.run()
    pygame.display.flip()
    screen.blit(terrain_image, (0, 0))
    clock.tick(120)
    pygame.display.set_caption(str(p1.score)+":"+str(p2.score))
