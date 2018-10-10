import tkinter as tk
from classes.resolution import WindowResolution
from classes.base_window_class import MainWindow
from classes.menu import DropDownMenu
from classes.error_window import ErrorWindow
from classes.algebra_equation_solver import CircuitSolver
import os

#main function that loads the window, and all of the window assets
def base_window_load():
    #Makes the root and starts the window
    root_window = tk.Tk()
    #sets the screen resolution
    window_resolution = WindowResolution(root_window)
    window_resolution.set_window_resolution()
    window_width_res = window_resolution.get_x()
    window_height_res = window_resolution.get_y()
    #window base and design
    window_base = MainWindow(root_window,window_width_res,window_height_res)
    window_base.algebra_canvas()
    window_base.table_canvas()

    #loads the drop down menu
    window_drop_down_menu = DropDownMenu(root_window)
    window_drop_down_menu.menu()
    window_drop_down_menu.file_menu()
    window_drop_down_menu.window_menu()
    window_drop_down_menu.options_menu()
    window_drop_down_menu.help_menu()

    root_window.update()
    root_window.mainloop()

def main():
    pass
if __name__ == "__main__":
    base_window_load()
