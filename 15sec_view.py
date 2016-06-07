import pygame
import numpy as np
import random
import cv2
import facebook



def posterization(n, img):
    indices = np.arange(0,256)   # List of all colors 
    divider = np.linspace(0,255,n+1)[1] # we get a divider
    quantiz = np.int0(np.linspace(0,255,n)) # we get quantization colors
    color_levels = np.clip(np.int0(indices/divider),0,n-1) # color levels 0,1,2..
    palette = quantiz[color_levels] # Creating the palette

    img = palette[img]  # Applying palette on image
    return cv2.convertScaleAbs(img) # Converting image back to uint8


# screen resolution
width = 800
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


image = pygame.image.load("/home/pi/out.jpg")
bg = pygame.image.load("/home/pi/background.jpg")
clock = pygame.time.Clock()
 
p_level = [2,3,4]
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 80)
pygame.mouse.set_visible(False)
for i in range(0,2):     
    counter, text = 15, '15'.rjust(3)
    image = image = cv2.imread("/home/pi/out.jpg", 1)
    image = posterization(random.choice(p_level), image)
    cv2.imwrite("/home/pi/final.jpg", image)
    image1 = pygame.image.load("/home/pi/final.jpg")
    while counter > 0:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter -=1
                text = str(counter).rjust(3)

        screen.fill((176,182,147))
        # screen.blit(bg, (0,0))
        screen.blit(image1,(0,0))
        screen.blit(font.render(text, True, (255, 255, 255)), (20, 735))
        clock.tick()
        pygame.display.flip()  


pygame.quit()
