import pygame
import os


pygame.init()

screen_width = 800
screen_height = 600

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Music Player")

music_files = ["music1.mp3", "music2.mp3", "music3.mp3"]
current_music = 0

pygame.mixer.init()
pygame.mixer.music.load(music_files[current_music])

# Function to display message on screen
def display_message(message):
    text = font.render(message, True, black)
    screen.blit(text, (screen_width//2 - text.get_width()//2, 20))

# Function to play music
def play_music():
    pygame.mixer.music.play()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to play next music
def next_music():
    global current_music
    current_music = (current_music + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music])
    pygame.mixer.music.play()

# Function to play previous music
def previous_music():
    global current_music
    current_music = (current_music - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music])
    pygame.mixer.music.play()

running = True
while running:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
                display_message("Playing")
            elif event.key == pygame.K_s:
                stop_music()
                display_message("Stopped")
            elif event.key == pygame.K_n:
                next_music()
                display_message("Next")
            elif event.key == pygame.K_b:
                previous_music()
                display_message("Previous")

    pygame.display.update()

pygame.quit()
