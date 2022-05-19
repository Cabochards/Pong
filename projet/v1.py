import pygame

screen = pygame.display.set_mode((600, 600))

class Paddle:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.height = 100
        self.width = 15
        self.image = pygame.image.load(image)
    
    def display(self):
        # pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.width, self.height))
        screen.blit(self.image, (self.x, self.y))

    def move(self, dist):
        self.y += dist

    def run(self):
        self.display()
        if self.y < -self.height:
            self.y += 600
        elif self.y > 600:
            self.y -= 600

p1 = Paddle(10,100, 'barre1.png')
p2 = Paddle(580,100, 'barre2.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        p1.move(-1)

    if keys[pygame.K_s]:
        p1.move(1)

    if keys[pygame.K_UP]:
        p2.move(-1)

    if keys[pygame.K_DOWN]:
        p2.move(1)
    
    p1.run()
    p2.run()
    pygame.display.flip()
    screen.fill((0,0,0))