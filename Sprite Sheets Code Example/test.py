import sys, pygame

pygame.init()

imageName = 'fatManWalk2.png'
frameWidth = 246;
frameHeight = 414;
totalFrames = 8;
columns = 4;

window = pygame.display.set_mode((frameWidth, frameHeight))
image = pygame.image.load(imageName)
frame = -1
row = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

    window.fill((255, 255, 255))
    frame += 1;
    if frame == columns:
        row += 1
    elif frame > totalFrames - 1:
        frame = 0
        row = 0

    window.blit(image, (0, 0), ((frame%columns)*frameWidth, row*frameHeight, frameWidth, frameHeight))
    pygame.display.update()
    clock.tick(10)
