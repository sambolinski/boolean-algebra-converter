import tkinter as tk
#from .algebra_sortingv6 import TruthTableValues

class TruthTable():
    def __init__(self, parent,solved_table,font):
        self._font = font
        self._master = parent
        self._table_list = []
        self._table_variable_text = ""
        self._border_width = 0
        self._pad_y = 0
        self._pad_x = 0
        #makes a label with the background colour of white.
        self._solved_table = solved_table
        self._main_label= tk.Label(self._master,bg="#000000")


    def draw_table(self):
        #this function makes a table using the tkinter widget Label. It takes the solved data, and the column headings to display it.
        #[['A', '01'], ['01', '01'], ['XOR(A,01)', '00']]
        for row in range(len(self._solved_table[0][1])+1):
            current_row = []
            for column in range(len(self._solved_table)):
                if row == 0:
                    #column heading row
                    self._table_variable_text = self._solved_table[column][0]
                    self._border_width = 3
                    self._pad_y = 2
                else:
                    #binary row
                    self._table_variable_text = self._solved_table[column][1][row-1]
                    self._border_width = 3
                    self._pad_y = 1
                
                label = tk.Label(self._master,font=self._font, text=self._table_variable_text,bd=self._border_width, width=len(self._solved_table[column][0]))
                label.config(highlightbackground="#000000")
                label.grid(row=row,column=column, padx=self._pad_x,pady=self._pad_y)
                current_row.append(label)
            self._table_list.append(current_row)
        return self._main_label
