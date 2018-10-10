import tkinter as tk
from tkinter import filedialog
import subprocess
from classes.resolution import WindowResolution
from .error_window import ErrorWindow
from .help_window import HelpWindow
import os

class DropDownMenu:
    def __init__(self, master):
        self._master = master
        try:
            self._default_saves_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..' , 'saves'))
            self._default_options_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..' , 'data','options'))
            self._default_options_path += "\\options.txt"
        except:
            print("error")
    #SECTION OF CLASS TO DO WITH THE MENU TAB
    def menu(self):
        #this function makes the menu widget which appears at the top of the program
        self._main_menu = tk.Menu(self._master,tearoff=False)
        self._master.config(menu=self._main_menu)

    def get_font(self):
        #this method gets the font stored in the options.txt file.
        try:
            default_options_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'..' ,'..' , 'data','options'))
            default_options_path += "\\options.txt"
            options_file = open(default_options_path,"r")
            font_type = options_file.read()
        except:
            print("error")
        return font_type   
    #SECTION OF CLASS TO DO WITH THE FILE TAB
    def file_menu(self):
        #this function attaches the file menu to teh base menu,and provides functionallity
        self._file_menu = tk.Menu(self._main_menu,tearoff=False)
        self._main_menu.add_cascade(label="File", menu=self._file_menu)

        #new
        self._file_menu.add_command(label="New",command=self.file_menu_new)

        #save
        self._file_menu.add_command(label="Save",command=self.file_menu_save)
        
        #load
        self._file_menu.add_command(label="Load",command=self.file_menu_load)

        #Exit
        self._file_menu.add_separator()
        self._file_menu.add_command(label="Exit", command=self.file_menu_exit)
    def file_menu_new(self):
        #this method is used to remove an expression from teh textbox
        widget_list = self._master.winfo_children()
        try:
            widget_list[1].delete(0, len(widget_list[1].get()))
        except:
            print("entry empty")
        
    def file_menu_save(self):
        #this method is used to save a file.
        widget_list = self._master.winfo_children()
        algebra_value = widget_list[1].get()
        self._master.filename = filedialog.asksaveasfilename(initialdir=self._default_saves_path,initialfile=algebra_value,title = "Select file",defaultextension=".txt",filetypes=[("Text Files", "*.txt")])
        try:
            save_file = open(self._master.filename,"w")
            save_file.write(algebra_value)
            save_file.close()
        except:
            file_menu_save_error = ErrorWindow(self._master,"Not Valid File Directory")
    def file_menu_load(self):
        #this method is used to load a file
        self._master.filename = filedialog.askopenfilename(initialdir = self._default_saves_path,title = "Select file",defaultextension=".txt",filetypes=[("Text Files", "*.txt")])
        widget_list = self._master.winfo_children()
        
        try:
            open_file = open(self._master.filename,"r")
            algebra = open_file.read()
            open_file.close()
            success = True

        except:
            success = False
            file_menu_open_error = ErrorWindow(self._master,"Not Valid File Directory")
        if success == True:
            widget_list[1].delete(0, len(widget_list[1].get()))
            widget_list[1].insert(0,str(algebra))
            widget_list[2].invoke()
    def file_menu_exit(self):
        #this function will close the application.
        self._master.destroy()


    #SECTION OF CLASS TO DO WITH THE WINDOW TAB
    def window_menu(self):
        #this adds the window menu to the base menu. This will allow people to change options about the window.
        self._window_menu = tk.Menu(self._main_menu,tearoff=False)
        self._main_menu.add_cascade(label="Window", menu=self._window_menu)
        
        
        
        #changing resolution
        self._fullscreen_choice = tk.IntVar()
        self._window_resolution_submenu = tk.Menu(self._window_menu,tearoff=False)
        self._window_resolution_submenu.add_checkbutton(label="Fullscreen",variable=self._fullscreen_choice,command=self.resolution_fullscreen_callback)
        self._window_resolution_submenu.add_separator()
        self._window_resolution_submenu.add_command(label="1280x720", command=self.resolution_callback_1280x720)
        self._window_resolution_submenu.add_command(label="1360x768", command=self.resolution_callback_1360x768)
        self._window_resolution_submenu.add_command(label="1366x768", command=self.resolution_callback_1366x768)
        self._window_resolution_submenu.add_command(label="1600x900", command=self.resolution_callback_1600x900)
        self._window_resolution_submenu.add_command(label="1920x1080", command=self.resolution_callback_1920x1080)
        self._window_resolution_submenu.add_separator()
        self._window_resolution_submenu.add_command(label="Native", command=self.resolution_callback_native)
        self._window_menu.add_cascade(label="Resolution",menu=self._window_resolution_submenu, underline=0)


            
    def resolution_fullscreen_callback(self):
        #returns whether the user wants fullscreen or not.
        self._fullscreen_checkbox = self._fullscreen_choice.get()
        resolution_fullscreen_choice = WindowResolution(self._master)
        resolution_fullscreen_choice.fullscreen(self._fullscreen_checkbox)
        self.resolution_callback_native()
    def resolution_callback_1280x720(self):
        #calls the function to change the resolution to 1280x720
        self._window_width = 1280
        self._window_height = 720
        
        resolution = WindowResolution(self._master)
        resolution.set_window_resolution(self._window_width,self._window_height)
        widget_list = self._master.winfo_children()
        print(widget_list)
        widget_list[2].update()
        widget_list[2].update_idletasks()
        widget_list[3].update()
        widget_list[3].update_idletasks()
    def resolution_callback_1360x768(self):
        #calls the function to change the resolution to 1360x768
        self._window_width = 1360
        self._window_height = 768
        
        resolution = WindowResolution(self._master)
        resolution.set_window_resolution(self._window_width,self._window_height)
        widget_list = self._master.winfo_children()
        widget_list[2].update()
        widget_list[2].update_idletasks()
        widget_list[3].update()
        widget_list[3].update_idletasks()
    def resolution_callback_1366x768(self):
        #calls the function to change the resolution to 1366x768
        self._window_width = 1366
        self._window_height = 768
        
        resolution = WindowResolution(self._master)
        resolution.set_window_resolution(self._window_width,self._window_height)
        widget_list = self._master.winfo_children()
        widget_list[2].update()
        widget_list[2].update_idletasks()
        widget_list[3].update()
        widget_list[3].update_idletasks()
    def resolution_callback_1600x900(self):
        #calls the function to change the resolution to 1600x900
        self._window_width = 1600
        self._window_height = 900

        resolution = WindowResolution(self._master)
        resolution.set_window_resolution(self._window_width,self._window_height)
        widget_list = self._master.winfo_children()
        widget_list[2].update()
        widget_list[2].update_idletasks()
        widget_list[3].update()
        widget_list[3].update_idletasks()
    def resolution_callback_1920x1080(self):
        #calls the function to change the resolution to 1920x1080
        self._window_width = 1920
        self._window_height = 1080
        
        resolution = WindowResolution(self._master)
        widget_list = self._master.winfo_children()
        widget_list[2].update()
        widget_list[2].update_idletasks()
        widget_list[3].update()
        widget_list[3].update_idletasks()
        resolution.set_window_resolution(self._window_width, self._window_height)
    def resolution_callback_native(self):
        #gets the monitor resolution
        self._window_width = self._master.winfo_screenwidth()
        self._window_height = self._master.winfo_screenheight()
        
        resolution = WindowResolution(self._master)
        resolution.set_window_resolution(self._window_width, self._window_height)
        widget_list = self._master.winfo_children()
        widget_list[2].update()
        widget_list[2].update_idletasks()
        widget_list[3].update()
        widget_list[3].update_idletasks()
    
    #SECTION OF CLASS TO DO WITH THE OPTIONS TAB 
    def options_menu(self):
        #this function will attach the options menu to the base menu.
        self._options_menu = tk.Menu(self._main_menu,tearoff=False)
        self._main_menu.add_cascade(label="Options", menu=self._options_menu)
        self._font_menu = tk.Menu(self._options_menu,tearoff=False)
        self._font_menu.add_command(label="Courier New", command=self.font_courier_callback)
        self._font_menu.add_command(label="Arial", command=self.font_arial_callback)
        self._font_menu.add_command(label="Impact", command=self.font_impact_callback)
        self._options_menu.add_cascade(label="Fonts",menu=self._font_menu)
    def font_courier_callback(self):
        #this changes the font to "Courier_New"
        options_file = open(self._default_options_path,"w")
        font = "Courier " + "9"
        options_file.write(font)
        options_file.close()
    def font_arial_callback(self):
        #this changes the font to "Arial"
        options_file = open(self._default_options_path,"w")
        font = "Arial " + "9"
        options_file.write(font)
        options_file.close()
    def font_impact_callback(self):
        #this changes the font to "Impact"
        options_file = open(self._default_options_path,"w")
        font = "Impact " + "9"
        options_file.write(font)
        options_file.close()
    #SECTION OF CLASS TO DO WITH THE HELP TAB  
    def help_menu(self):
        #this function will attach the help menu to the base menu.
        self._help_menu = tk.Menu(self._main_menu,tearoff=False)
        self._main_menu.add_cascade(label="Help", menu=self._help_menu)
        self._help_menu.add_command(label="Help Window",command=self.open_help_menu)
    def open_help_menu(self):
        #this opens the help menu
        font_type = self.get_font()
        help_menu = HelpWindow(self._master,font_type)
    
