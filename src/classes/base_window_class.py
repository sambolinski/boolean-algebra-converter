import tkinter as tk
import random
from .resolution import WindowResolution
from .truth_table import TruthTable
from .algebra_equation_solver import BooleanAlgebraEquationAnalysis
from .algebra_equation_solver import TruthTableEvaluator
from .algebra_equation_solver import TableHeadings
from .error_window import ErrorWindow
from .algebra_equation_solver import CircuitSolver
from .circuit_window import CircuitWindow
from .draw_circuit import DrawCircuit
from .window_configuration import BaseWindow
import os
#This class is the base of the window



class MainWindow(BaseWindow):
    def __init__(self, master,window_x,window_y):
        #Inherits from BaseWindow
        super(MainWindow,self).__init__()
        #This class sets up the entire window for the user
        self._master = master
        self._master.title("Boolean Algebra Converter")
        self._border_colour = "#210351"
        self._resolution_x = window_x
        self._resolution_y = window_y
        self._algebra = ""
        self._solved_equation = ""
        self._solved_table = ""
        self._table = []
        self._main_frame = tk.Frame(self._master)
        self._master.configure(background=self._bg_colour)
    def get_font(self):
        #This gets the font from options.txt
        default_options_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'..' ,'..' , 'data','options'))
        default_options_path += "\\options.txt"
        options_file = open(default_options_path,"r")
        font_type = options_file.read()
        return font_type     
    def algebra_canvas(self):
        #This function draws the algebra input.
        self._algebra_canvas_width = int(round(self._resolution_x * 0.58))
        self._algebra_canvas_height = int(round(self._resolution_y * 0.066))
        self._algebra_pad_x = int(round(self._resolution_x * 0.01))
        self._algebra_pad_y = int(round(self._resolution_y * 0.0215))
        #these variables use the base window size and set the canvas size relative to that.


        
        self._algebra_entry = tk.Entry(self._master,width=50)
        self._algebra_entry.grid(row=0,column=0)
        self._table_button = tk.Button(self._master, text="Generate Truth Table", fg="black",command=self.algebra_callback)
        self._table_button.grid(row=1,column=0)
        #self._table_button.place(x=self._algebra_pad_x+350,y=self._algebra_pad_y)
        self._circuit_button = tk.Button(self._master, text="Generate Circuit", fg="black",command=self.circuit_callback)
        self._circuit_button.grid(row=2,column=0)
        
        self._master.bind("<Return>",self.algebra_callback)
    def table_canvas(self):
        #This function draws the truth table.
        self._table_canvas_width = int(round(self._resolution_x * 0.800))
        self._table_canvas_height = int(round(self._resolution_y * 0.835))
        ##self._table_pad_x = int(round(self._resolution_x * 0.61))
        self._table_pad_x = int(round(self._resolution_x * 0.01))
        self._table_pad_y = int(round(self._resolution_y * 0.104))
        #these variables use the base window size and set the canvas size relative to that.

        
        self._main_table_frame = tk.Frame(self._master,borderwidth=5,relief="ridge",highlightbackground=self._border_colour,width=self._table_canvas_width, height=self._table_canvas_height)
        self._main_table_frame.grid(row=3,column=0)
        self._main_table_canvas = tk.Canvas(self._main_table_frame,bg=self._bg_colour,highlightbackground=self._bg_colour,width=self._table_canvas_width-15,height=self._table_canvas_height-15)

        
        #self._main_table_canvas.configure(background=self._bg_colour)
        font_type = self.get_font()
        self.table_values_class = TruthTable(self._main_table_canvas,self._solved_table,font_type)
        widget_list = self._main_table_frame.winfo_children()
        self._main_table_frame.update()
        self._main_table_canvas.update()
        self._master.update_idletasks()
        self._master.update()

        self._main_table_frame.pack_propagate(0)
        self._main_table_frame.update_idletasks()
        self._main_table_frame.update()
    def algebra_callback(self,event=None):
        #this method is used for sending data to the different solving methods.
        font_type = self.get_font()
        error = False
        for widget in self._main_table_frame.winfo_children():
            widget.destroy()
        try:
            self._string_var = self._algebra_entry.get()
            self._updated_algebra = BooleanAlgebraEquationAnalysis((str(self._string_var)),(str(self._string_var)))
            self._updated_algebra = self._updated_algebra.split_boolean_input()
            self._table_heading = TableHeadings(self._updated_algebra)
            self._table_heading.solve_headings()
            self._solved_table = self._table_heading.solve_table()
        except:
            error_win = ErrorWindow(self._master,"Invalid Algebra Input")
            error = True
        if error == False:
            self.table_values_class = TruthTable(self._main_table_frame,self._solved_table,font_type)
            self._table = self.table_values_class.draw_table()
            self._master.update_idletasks()
            self._master.update()
        self._main_table_frame.update()
        self._main_table_canvas.update()
    def circuit_callback(self):
        #this method sends data taken from the textbox ands ends it to the solving classes.
        font_type = self.get_font()
        error = False
        try:
            #This is the section where the table headings are solved. 
            self._string_var = self._algebra_entry.get()
            self._updated_algebra = BooleanAlgebraEquationAnalysis((str(self._string_var)),(str(self._string_var)))
            self._updated_algebra = self._updated_algebra.split_boolean_input()
            self._table_heading = TableHeadings(self._updated_algebra)
            self._table_heading.solve_headings()
            self._solved_table = self._table_heading.solve_table()
        except:
            error_win = ErrorWindow(self._master,"Invalid Algebra Input")
            error = True
        if error == False:
            #The table_headings are used when solving the circuit, the data is send to the solving classes.
            self._circuit_result = CircuitSolver(self._solved_table)
            self.solved_circuit = self._circuit_result.solve_circuit()
            self._circuit_window = CircuitWindow(self._master)
            self._circuit_window.load_window()
            circuit_tk_window = self._circuit_window.circuit_window_callback()
            self._circuit_gui = DrawCircuit(circuit_tk_window,self.solved_circuit,font_type)
            self._circuit_gui.draw_gates()
            self._circuit_gui.draw_lines()
