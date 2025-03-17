import pygame 
import sys 
import config
import random

def draw_text(screen, text, x, y, font_size, color, font_name=None, bold=False, italic=False):
    if font_name:
        font = pygame.font.Font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)

    font.set_bold(bold)
    font.set_italic(italic)

    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x,y))

def init_game():
    pygame.init()

    pygame.font.init()

    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))

    pygame.display.set_caption(config.TITLE)

    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():

    screen = init_game()
    clock = pygame.time.Clock()

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)


        text1 = 'Nathan Barton'
        font_size1 = 43
        color1 = config.BLACK
        x1, y1 = (175, 225)

        text2 = 'AM Web'
        font_size2 = 43
        color2 = config.BLUE
        x2, y2 = (175, 250)

        text3 = 'Elk Rapids'
        font_size3 = 43
        color3 = config.RED
        x3, y3 = (400, 350)


        draw_text(screen, text1, x1, y1, font_size1, color1)
        draw_text(screen, text2, x2, y2, font_size2, color2, bold=True)
        draw_text(screen, text3, x3, y3, font_size3, color3, italic=True)

        pygame.display.flip()

        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()