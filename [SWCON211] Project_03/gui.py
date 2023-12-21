import tkinter as tk
from tkinter import colorchooser
import threading
from map_editor import *
from map_saver import save_map

def on_color_select():
    color_code = colorchooser.askcolor(title="Choose a brick color")[1]
    if color_code:
        set_current_color(color_code)

def create_gui():
    root = tk.Tk()
    
    root.geometry('300x150')
    root.minsize(300, 150)

    root.title("Map Editor")
    
    load_settings_button  = tk.Button(root, text="Load Game Setting", command=select_and_load_settings)
    load_settings_button.pack()
    
    # Add this in your GUI setup code
    # import_button = tk.Button(root, text="Import Map", command=load_map)
    # import_button.pack()

    color_button = tk.Button(root, text="Select Color", command=on_color_select)
    color_button.pack()

    start_button = tk.Button(root, text="Open Map Editor", command=lambda: threading.Thread(target=start_map_editor).start())
    start_button.pack()

    save_button = tk.Button(root, text="Save Map", command=save_map)
    save_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()