import tkinter as tk
from .window_configuration import BaseWindow

class HelpWindow(BaseWindow):
    def __init__(self,master,font):
        super(HelpWindow,self).__init__()
        #this class inherits from BaseWindow.
        #this class is the window that appears to the user when they press the help window button.
        self._master = master
        self.__font = font
        self._help_window = tk.Toplevel(self._master,bg=self._bg_colour)
        self._help_window.title("Help")
        self._help_window.geometry("%dx%d%+d%+d" % (750, 600, 250, 125))
        self._help_msg = tk.Message(self._help_window,font = self.__font,bg=self._bg_colour,text=("Boolean Algebra Help \n \n \n \n"+
                                                                                 "EXPRESSION INPUT \n"+
                                                                                 "Boolean expressions are inputted as functions\n "+
                                                                                 "a function is one of the gates OR,AND,XOR,NOR,NAND,NXOR,NOT\n"+
                                                                                 "a variable can be binary i.e 0100, or a capital letter from the alphabet i.e A,B,C,D... \n"+
                                                                                 "Choose a Gate, then open (, then two (one variable if gate is NOT) variables seprateed by commas, then a closed )\n"+
                                                                                 "EXAMPLE \n"+
                                                                                 "A XOR B \n"+
                                                                                 "Take gate XOR, then (, then two variables seperated by commas, then closed ) \n"+
                                                                                 "XOR(A,B)\n\n"+
                                                                                 "For more complicated expressions we have to put functions insiede fo functions \n \n"+
                                                                                 "A OR B AND C \n"+
                                                                                 "First we and B and C which gives us AND(B,C) \n"+
                                                                                 "This leaves us with A OR AND(B,C) \n"+
                                                                                 "We take the OR gate, place (, then place A, the second variable is AND(B,C) \n"+
                                                                                 "This gives us OR(A,AND(B,C)) \n"+
                                                                                 "After that, press 'Generate Truth Table', or 'Generate Circuit' \n\n\n"+
                                                                                 "SAVE \n"+
                                                                                 "Once an expression has been inputted, press File>Save\n"+
                                                                                 "This will take you to a new window where you can choose a name\n"+
                                                                                 "Choose a name and press enter, this will save your expression\n\n"+
                                                                                 "OPEN\n"+
                                                                                 "Press File>Load \n"+
                                                                                 "Select a file and press enter \n"+
                                                                                 "The file should automatically draw a truth table"))
        self._help_msg.pack()

