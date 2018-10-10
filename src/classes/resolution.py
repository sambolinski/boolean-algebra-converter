import tkinter as tk

#using this import to give me the width and height of the users screen,
#this will only work on computers running windows

class WindowResolution:
    def __init__(self,master):
        self._master = master
        self._window_width = 0
        self._window_height = 0
    def set_window_resolution(self,resolution_choice_width=1200,resolution_choice_height=750):
        #this function sets the window resolution to the resolution selected from the menu. the default is 1200x750
        #the position of the window is the midpoint of the monitor
        if resolution_choice_width == 0 and resolution_choice_height == 0:
            self._window_width = self._master.winfo_screenwidth()
            self._window_height = self._master.winfo_screenheight()
        else:
            self._window_width = resolution_choice_width
            self._window_height = resolution_choice_height
        if resolution_choice_width < 0 and resolution_choice_height < 0: 
            self._window_width = self._master.winfo_screenwidth() - abs(resolution_choice_width)
            self._window_height = self._master.winfo_screenheight() - abs(resolution_choice_width)
        else:
            self._window_width = resolution_choice_width
            self._window_height = resolution_choice_height
            
        self._window_position_x = (self._master.winfo_screenwidth() // 2) - (self._window_width // 2)
        self._window_position_y = (self._master.winfo_screenheight() // 2) - (self._window_height // 2)
        self._master.update()
        self._master.resizable(width=False, height=False)
        self._master.update_idletasks()
        self._master.geometry('%dx%d+%d+%d' % (self._window_width, self._window_height, self._window_position_x, self._window_position_y))
    def get_x(self):
        #this function gets the x axis resolution of the window
        self.window_resolution_x = self._window_width
        return self.window_resolution_x
    def get_y(self):
        #this function gets the y axis resolution of the window
        self.window_resolution_x = self._window_height
        return self.window_resolution_x
    def fullscreen(self,choice):
        #this function puts the window in fullscreen(removes the window border)
        self._fullscreen_choice = choice
        if self._fullscreen_choice == 1:
            self._master.update()
            self._master.update_idletasks()
            self._master.overrideredirect(True)
            self._master.update()
            self._master.update_idletasks()
        elif self._fullscreen_choice == 0:
            self._master.update()
            self._master.update_idletasks()
            self._master.overrideredirect(False)
            self._master.update()
            self._master.update_idletasks()

        #the .update() and .update_idletasks() are used to refresh tkinter widgets
        


        
        
    
