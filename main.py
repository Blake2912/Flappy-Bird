import random
import pygame

# Initializing pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Title and Icon
pygame.display.set_caption("Flappy Bird")
main_icon = pygame.image.load("bird-icon.png")
pygame.display.set_icon(main_icon)

# Clouds
no_of_clouds = random.randint(10,20)
cloudImg = []
cloud_X = []
cloud_Y = []
cloud_X_change = 0.3
for i in range(no_of_clouds):
    cloudImg.append(pygame.image.load("cloud.png"))
    cloud_X.append(random.randint(10,SCREEN_WIDTH-64))
    cloud_Y.append(random.randint(5,SCREEN_HEIGHT))

def show_cloud(x,y,i):
    screen.blit(cloudImg[i],(x,y))


# Player Bird
birdImg = pygame.image.load("bird.png")
bird_X = 50
bird_Y = (SCREEN_HEIGHT//2)-64
bird_Y_change = -0.5
bird_X_change = 0
bird_rotate_angle = 0

def load_bird(x,y,angle):
    rotated_image = pygame.transform.rotate(birdImg, angle)
    screen.blit(rotated_image,(x,y))

# Game loop
running = True
while running:
    screen.fill((0,169,244))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_DOWN:
                bird_Y_change = 2
                bird_X_change = 0.2
                bird_rotate_angle = -15.0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                bird_Y_change = -0.5
                bird_rotate_angle = 15
                bird_X_change = 0


    # Cloud movement
    for i in range(no_of_clouds):
        show_cloud(cloud_X[i],cloud_Y[i],i)
        cloud_X[i] += cloud_X_change
        if cloud_X[i] >= SCREEN_WIDTH:
            cloud_X[i] = -64
            cloud_Y[i] = random.randint(0,SCREEN_HEIGHT)
    
    load_bird(bird_X,bird_Y,bird_rotate_angle)
    bird_Y += bird_Y_change
    bird_X += bird_X_change

    # Bird Boundaries
    if bird_Y <= 0 or bird_Y >= SCREEN_HEIGHT-64:
        print("Game Over")
    
    pygame.display.update()