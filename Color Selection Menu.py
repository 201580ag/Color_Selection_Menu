import tkinter as tk
from tkinter import colorchooser

def choose_color():

    color = colorchooser.askcolor(title="Color Selection Menu")
    if color[1] is not None:
        hex_code = color[1][1:]
        rgb_values = color[0]
        print("\nSelected color:")
        print("HEX: ", hex_code)
        print("R, G, B: ", int(rgb_values[0]),int(rgb_values[1]), int(rgb_values[2]))
        choose_color()
choose_color()