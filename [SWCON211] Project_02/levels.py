from game_objects import Brick
from settings import *
import random

# def level_1():
#     colors = [RED, GREEN, BLUE, WHITE]  # 색상 리스트
#     bricks = []
#     for x in range(150, SCREEN_WIDTH - 150, BRICK_WIDTH):
#         color = random.choice(colors)
#         bricks.append(Brick(x, 50, color))
#     return bricks

# def level_2():
#     colors = [RED, GREEN, BLUE, WHITE]
#     bricks = []
#     for x in range(0, SCREEN_WIDTH, BRICK_WIDTH):
#         for y in range(0, SCREEN_HEIGHT // 3, BRICK_HEIGHT):
#             color = random.choice(colors)
#             if (x + y) % 2 == 0:
#                 bricks.append(Brick(x, y, color))
#     return bricks

# def level_3():
#     ascii_art = [
#         "            #                ",
#         "  ###      # #           # # ",
#         " #   #             ####  # # ",
#         "  ###    #######    ##   ### ",
#         "   #               #  #  # # ",
#         " #####     ###           # # ",
#         "          #   #              ",
#         "           ###               ",
#     ]
#     colors = [RED, GREEN, BLUE, WHITE]
#     bricks = []
#     y_offset = 100  # 시작 y 좌표
#     for y, row in enumerate(ascii_art):
#         for x, char in enumerate(row):
#             color = random.choice(colors)
#             if char == '#':
#                 bricks.append(Brick(x * BRICK_WIDTH, y * BRICK_HEIGHT + y_offset, color))
#     return bricks

def load_map_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    level = []
    for line in lines:
        # Strip the line of leading/trailing whitespace and newlines, then split
        clean_line = line.strip()
        bricks_row = [clean_line[i:i+7] for i in range(0, len(clean_line), 7)]
        level.append(bricks_row)
    return level

def create_bricks_from_data(level_data):
    bricks = []
    row_height = BRICK_HEIGHT  # Define this based on your game
    for y, row in enumerate(level_data):
        for x, col in enumerate(row):
            # Ensure that the color code is exactly 7 characters long ('#' + 6 hex digits)
            if len(col) != 7 or not col.startswith('#'):
                # Skip this color code if it's not in the expected format
                continue
            
            # Rest of the code remains the same...
            if col.strip() == '#000000':
                continue
            else:
                brick_x = x * BRICK_WIDTH
                brick_y = y * row_height
                color = tuple(int(col[i:i+2], 16) for i in (1, 3, 5))
                bricks.append(Brick(brick_x, brick_y, color))

    return bricks