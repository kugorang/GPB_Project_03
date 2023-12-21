from tkinter import messagebox
from map_editor import level_data
from settings import MAP_SAVE_PATH

def save_map():
    with open(MAP_SAVE_PATH, 'w') as file:
        for row in level_data:
            file.write(''.join([str(col) if col != " " else '#000000' for col in row]) + '\n')
            
    messagebox.showinfo("Save Map", f"Save map successfully from {MAP_SAVE_PATH}")