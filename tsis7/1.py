import pygame
import datetime
import os

pygame.init()
path = os.getcwd()
#Setting up the screen, loading images
clock_image = pygame.image.load(path+r"\tsis7\images\main-clock.png")
min_arrow_image = pygame.image.load(path+r"\tsis7\images\left-hand.png")
sec_arrow_image = pygame.image.load(path+r"\tsis7\images\right-hand.png")
screen = pygame.display.set_mode((700, 700))

#Variables for minutes and seconds of the current moment
current_date = datetime.datetime.now()
minutes = current_date.minute
seconds = current_date.second

#Functions for roating arrows
def rotate_min(angle):
        image = pygame.transform.rotate(min_arrow_image, angle)
        x = clock_image.get_width()/2-image.get_width()/2
        y = clock_image.get_height()/2-image.get_height()/2
        screen.blit(image,(x,y))

def rotate_sec(angle):    
        image = pygame.transform.rotate(sec_arrow_image, angle)
        x = clock_image.get_width()/2-image.get_width()/2
        y = clock_image.get_height()/2-image.get_height()/2
        screen.blit(image,(x,y))
        

#Getting angles for arrows for current time
min_angle = 90
sec_angle = 90
min_angle = min_angle - minutes/60*360
sec_angle = sec_angle - seconds/60*360

#Programm loop
done = False
while not done:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
    screen.fill(0)
    screen.blit(clock_image,(0,0))
    rotate_sec(sec_angle)
    rotate_min(min_angle)
    min_angle += 0.1
    sec_angle += 6

    #Updating screen after each second
    pygame.time.wait(1000)
    pygame.display.flip()
