import tkinter as Tk
from .resolution import WindowResolution
from .window_configuration import BaseWindow
class CircuitWindow(BaseWindow):
    def __init__(self,root):
        #this inherits data from the BaseWindow class
        super(CircuitWindow,self).__init__()
        self._master = root
        self._circuit_window = Tk.Toplevel(self._master)
        self._circuit_window.title("Circuit Generator")
    def load_window(self):
        #this method initialises the window that will appear when the generate circuit button is pressed
        window_change = WindowResolution(self._circuit_window)
        window_change.set_window_resolution(-100,-100)
        
        window_x = window_change.get_x()
        window_y  = window_change.get_y()
        print("window_x",window_x)
        print("window_y",window_y)
        self._circuit_frame = Tk.Frame(self._circuit_window,width = window_x,height=window_y,bg="#DEFCAE")
        self._circuit_frame.pack(fill="both",expand=True)
        self._circuit_frame.grid_rowconfigure(0, weight=1)
        self._circuit_frame.grid_columnconfigure(0, weight=1)
        self._circuit_canvas = Tk.Canvas(self._circuit_frame,bg=self._bg_colour,width=window_x,height=window_y)
        self._circuit_canvas.pack(side="left",expand=True,fill="both")
    def circuit_window_callback(self):
        #this is a return callback of the circuit canvas that the gates will be drawn on
        return self._circuit_canvas
        
        
