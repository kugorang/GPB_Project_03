import pygame
import settings

def render_map(screen, level_data):
    row_height = settings.BRICK_HEIGHT
    column_width = settings.BRICK_WIDTH

    color_map = {
        'R': settings.RED,
        'G': settings.GREEN,
        'B': settings.BLUE,
        'W': settings.WHITE,
        '0': settings.BLACK  # Representing an empty space
    }

    for y, row in enumerate(level_data):
        for x, char in enumerate(row):
            color = color_map.get(char, settings.BLACK)
            if color != settings.BLACK:
                pygame.draw.rect(screen, color, (x * column_width, y * row_height, column_width, row_height))
