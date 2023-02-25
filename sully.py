import pygame

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('sullyspritesheet.png').convert_alpha()

BG = (50, 50, 50)

def get_image(sheet, width, height):
    image = pygame.Surface((width,height)).convert_alpha()
    return image

frame_0 = get_image(sprite_sheet_image,20,20)

screen.fill(BG)
    

run = True
while run:

    screen.blit(sprite_sheet_image, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            pygame.display.update()

            pygame.quit()