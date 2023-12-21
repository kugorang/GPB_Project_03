import pygame
import tkinter as tk
import importlib.util
from tkinter import filedialog, messagebox
import settings

current_color = (255, 255, 255)  # Default color (white)
level_data = [[" " for _ in range(settings.SCREEN_WIDTH // settings.BRICK_WIDTH)] for _ in range(settings.SCREEN_HEIGHT // settings.BRICK_HEIGHT)]

def load_map():
    root = tk.Tk()
    root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

    # Show an Open dialog box and return the path to the selected file
    filename = filedialog.askopenfilename(title="Select Map File",
                                          filetypes=(("Map files", "*.txt"), ("All files", "*.*")))

    if filename:
        with open(filename, 'r') as file:
            map_data = file.readlines()

        # Process and display the map data...
        display_map(map_data)

def display_map(map_data):
    # Constants for the size of each tile/brick
    BRICK_WIDTH = 50
    BRICK_HEIGHT = 20

    # Loop through each row of the map data
    for y, row in enumerate(map_data):
        # Assuming the map is stored in a specific format, parse it accordingly
        bricks_row = [row[i:i+7] for i in range(0, len(row), 7)]  # Adjust if your format is different

        # Loop through each brick's color code in the row
        for x, color_code in enumerate(bricks_row):
            # Calculate the position for the brick based on its index and the constants
            brick_x = x * BRICK_WIDTH
            brick_y = y * BRICK_HEIGHT

            # Check if the space is empty (represented as '#000000')
            if color_code.strip() != '#000000':
                # Convert the color code to an RGB tuple
                color = tuple(int(color_code[i:i+2], 16) for i in (1, 3, 5))

                # Draw the brick on the screen at the calculated position with the specified color
                draw_brick(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT, color)
                
def draw_brick(x, y, width, height, color):
    # This will depend on your graphics library, but generally, you would:
    # 1. Set the drawing color to 'color'
    # 2. Draw a rectangle (or other shape) at the position (x, y) with the specified width and height
    pass  # Replace with actual drawing code

def select_and_load_settings():
    # Create a root window but hide it, as we only want the file dialog
    root = tk.Tk()
    root.withdraw()

    # Show an "Open" dialog box and return the path to the selected file
    settings_path = filedialog.askopenfilename(
        title="Select settings.py",
        filetypes=(("Python files", "*.py"), ("All files", "*.*"))  # Filter to only show .py files
    )

    if settings_path:
        # If a file was selected, attempt to load it as a module
        load_settings_from_path(settings_path)
    else:
        print("No file selected.")

def load_settings_from_path(path):
    try:
        # Load the module specified by the path
        spec = importlib.util.spec_from_file_location("settings", path)
        settings = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(settings)

        # Access the settings from the Brick Breaker game
        settings_vars = vars(settings)
        print("Loaded settings:", settings_vars)  # Optional: for logging or debugging

        # Show the loaded settings as an alert
        messagebox.showinfo("Settings Loaded", f"Settings loaded successfully from {path}")

    except Exception as e:
        # If something goes wrong, show an error message
        messagebox.showerror("Error", f"Failed to load settings: {e}")

    # Ensure the root tkinter window is closed after displaying the message
    tk.Tk().withdraw()

def load_settings_at_runtime(path_to_settings):
    # Load the module specified by the path
    spec = importlib.util.spec_from_file_location("settings", path_to_settings)
    settings = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(settings)

    return settings

# 색상을 설정하는 함수
def set_current_color(color):
    global current_color
    current_color = color

def start_map_editor():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event)

        screen.fill(settings.BG_COLOR)
        draw_grid(screen)
        pygame.display.flip()
    pygame.quit()

def handle_mouse_click(event):
    x, y = event.pos
    grid_x, grid_y = x // settings.BRICK_WIDTH, y // settings.BRICK_HEIGHT
    if 0 <= grid_x < len(level_data[0]) and 0 <= grid_y < len(level_data):
        level_data[grid_y][grid_x] = current_color

def draw_grid(screen):
    for y, row in enumerate(level_data):
        for x, color in enumerate(row):
            if color != " ":
                pygame.draw.rect(screen, color, (x * settings.BRICK_WIDTH, y * settings.BRICK_HEIGHT, settings.BRICK_WIDTH, settings.BRICK_HEIGHT))