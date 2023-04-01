import pygame

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)

screen_width = 600
screen_height = 400

ball_radius = 25
ball_width = 2 * ball_radius
ball_height = 2 * ball_radius
ball_x = screen_width // 2
ball_y = screen_height // 2

speed = 20

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Moving Ball")

def draw_ball(x, y):
    pygame.draw.circle(screen, red, (x, y), ball_radius)

running = True
while running:
    screen.fill(white)

    draw_ball(ball_x, ball_y)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= speed
            elif event.key == pygame.K_DOWN:
                ball_y += speed
            elif event.key == pygame.K_LEFT:
                ball_x -= speed
            elif event.key == pygame.K_RIGHT:
                ball_x += speed

    if ball_x < ball_radius:
        ball_x = ball_radius
    elif ball_x > screen_width - ball_radius:
        ball_x = screen_width - ball_radius
    if ball_y < ball_radius:
        ball_y = ball_radius
    elif ball_y > screen_height - ball_radius:
        ball_y = screen_height - ball_radius

    pygame.display.update()
    clock.tick(60)

pygame.quit()
