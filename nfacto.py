import pygame
import math


pygame.init()


WIDTH = 800
HEIGHT = 600


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perfect Circle")


radius = 50
x = WIDTH // 2
y = HEIGHT // 2

drawing = False
start_pos = None
end_pos = None

trail = []


running = True

def draw_circle():
    pygame.draw.circle(screen, GREEN, (x, y), radius, 2)


def draw_trail():
    if len(trail) > 1:
        pygame.draw.lines(screen, RED, False, trail, 2)


def calculate_roundness():
    distance = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
    roundness = (distance / (2 * math.pi * radius)) * 100
    return round(roundness, 2)


def calculate_distance_error():
    distance = math.sqrt((end_pos[0] - x)**2 + (end_pos[1] - y)**2)
    if distance < radius:
        return True
    return False


def calculate_speed_error():
    speed = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
    if speed < 5:
        return True
    return False


while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                end_pos = event.pos
                drawing = False
                trail = []

   
    screen.fill(BLACK)

   
    draw_trail()

    
    if start_pos and end_pos:
        roundness = calculate_roundness()
        text = f"ОКРУЖНОСТЬ : {roundness}%"
        font = pygame.font.Font(None, 30)

       
        if roundness >= 90:
            text_render = font.render(text, True, GREEN)
        else:
            text_render = font.render(text, True, RED)
        screen.blit(text_render, (10, 10))

    
    if start_pos and end_pos:
        if calculate_distance_error():
            error_text = "СЛИШКОМ БЛИЗКО К ЦЕНТРУ!"
            error_render = font.render(error_text, True, RED)
            screen.blit(error_render, (10, 50))
        if calculate_speed_error():
            error_text = "БЫСТРЕЕ!"
            error_render = font.render(error_text, True, RED)
            screen.blit(error_render, (10, 80))

   
    if drawing:
        current_pos = pygame.mouse.get_pos()
        trail.append(current_pos)
        

    pygame.display.flip()

pygame.quit()
