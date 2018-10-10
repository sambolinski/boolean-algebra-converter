import tkinter as tk
import os
class DrawCircuit:
    def __init__(self,root,algebra,font):
        #This method draws a circuit to the screen

        #REFER TO DOCUMENTED DESIGN (Circuit Solving Algorithm Overview) for more information
        self._master = root
        self._font = font
        self.__solved_circuit = algebra
        self._alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self._boolean = ["XOR", "AND", "OR", "NOR", "NAND", "NXOR", "NOT"]
        self.__base_x_position = 100
        self.__base_y_position = 500
    def draw_gates(self):
        #this method is used to draw the gates to the screen.
        circuit_size = 0
        algebra_count = 0
        var_counter = 0
        var_position_counter = 0
        previous_variable_placement = 0
        label_array = []
        self.gate_list = []
        self.image_list = []
        checked_variables = []
        gate_image_location = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..' , 'data','gfx','gates'))
        for i in range(len(self.__solved_circuit)):
            #this counts how many variables there are.
            if self.__solved_circuit[i][0] in self._alphabet:
                algebra_count += 1
        circuit_size = len(self.__solved_circuit) - algebra_count
        
        variable_distance_counter = 0
        variable_position_list = []
        variable_temp_list = []
        
        
        for i in range(len(self.__solved_circuit)):
            for j in range(len(self.__solved_circuit[i][0])):
                #these for loops checked to see if variables have already been drawn to the screen, as they shouldn't be drawn again.
                if (self.__solved_circuit[i][0][j] in self._alphabet) and (self.__solved_circuit[i][0][j] not in checked_variables):                    
                    checked_variables.append(str(self.__solved_circuit[i][0][j]))
                    variable_temp_list.append([self.__solved_circuit[i][0][j]])
                    variable_temp_list.append(0)
                    variable_temp_list.append(self.__solved_circuit[i][-1])
                    if (self.__solved_circuit[i][0][j-1] in self._boolean) and (self.__solved_circuit[i][0][j-1] != "NOT"):
                        variable_temp_list.append(0)
                        #this means the line should be drawn to either the first or second gate.
                    else:
                        if self.__solved_circuit[i][0][j-1] == "NOT":
                            #this meands that the line should be drawn to the middle
                            variable_temp_list.append(2)
                        else:
                            variable_temp_list.append(1)
                    variable_position_list.append(variable_temp_list)
                    variable_temp_list = []


        for i in range(len(self.__solved_circuit)):
            variable_position_list.append(self.__solved_circuit[i])

        self.__solved_circuit = variable_position_list
        for i in range(len(self.__solved_circuit)):
            if (self.__solved_circuit[i][0][0] in self._boolean):
                #this section gets the file location of the gates that are being used.
                gate_image_location = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..' , 'data','gfx','gates'))
                try:
                    #tries to use a .png and if it fails, it will use a .gif
                    gate_image_location += "/" +str(self.__solved_circuit[i][0][0]) + ".png"
                except:
                    gate_image_location += "/" +str(self.__solved_circuit[i][0][0]) + ".gif"
                self.__gate_image = tk.PhotoImage(file=gate_image_location)
                self.image_list.append(self.__gate_image)
                #assigns the X,Y coordinate to the position in the self.__solved_circuit
                #XOR(AND(A,B),C) solved circuit would look like
                #[[['A'], 0, -3, 0], [['B'], 0, -3, 1], [['C'], 0, -2, 1], [['AND', 'A', 'B'], 1, -3], [['XOR', 'AND', 'A', 'B', 'C'], 2, -2]]
                #this clearly indicates the X,Y positions
                pos_x = ((self.__solved_circuit[i][-2])*100)+2 + self.__base_x_position
                pos_y = ((self.__solved_circuit[i][-1])*100)+2 + self.__base_y_position
                self.gate = self._master.create_image((pos_x, pos_y),image=self.image_list[len(self.image_list)-1],anchor="nw")
                self.gate_list.append(self.gate)
            else:
                if i == 0:
                    #this if statement is used to check is a variable has previously been used, this will avoind
                    #duplicates appearing.
                    previous_variable_placement = self.__solved_circuit[i][len(self.__solved_circuit[i])-1]
                if self.__solved_circuit[i][len(self.__solved_circuit[i])-1] == previous_variable_placement:
                    var_counter += 1
                else:
                    var_counter = 1
                previous_variable_placement = self.__solved_circuit[i][len(self.__solved_circuit[i])-1]

                gate_input_location = 0
                #these selection statements ate used to tell whether the output should go on the first or second input.
                if self.__solved_circuit[i][-1] == 0:
                    gate_input_location = 35
                elif self.__solved_circuit[i][-1] == 1:
                    gate_input_location = 69
                elif self.__solved_circuit[i][-1] == 2:
                    #this is used if a NOT gate is involced
                    gate_input_location = 52
                pos_x = 90 + self.__base_x_position
                pos_y = gate_input_location + self.__base_y_position + (self.__solved_circuit[i][-2])*100
                #this places the text in the correct place.
                self._master.create_text(pos_x,pos_y,font=self._font,text=self.__solved_circuit[i][0][0])
    def draw_lines(self):
        #This method is used to draw lines between variables and gates. As well as gates and other gates.
        in_list = False
        algebra_smaller_string = ""
        algebra_larger_string = ""
        gate_input = False
        gate_input_num = 0
        same_gate_count = 0
        compare_count = 0
        compare_bool = False
        drawn_line = False
        #this loop scans through the entire solved circuit.
        for i in range(len(self.__solved_circuit)):
            compare_algebra = self.__solved_circuit
            if same_gate_count == compare_count:
                compare_count = 0
            for k in range(i+1,len(compare_algebra)):
                if compare_algebra[i][0] == compare_algebra[k][0]:
                    same_gate_count += 1
            #This if statement is here because lines will only be drawn if there is more than one gate.
            if len(self.__solved_circuit) > 3:
                drawn_line = False
                for j in range(i+1,len(self.__solved_circuit)):
                    #this checks the current gate, with all future gates that it could possibly interact with.
                    for smaller_algebra_char in range(len(self.__solved_circuit[i][0])):
                        algebra_smaller_string += self.__solved_circuit[i][0][smaller_algebra_char]
                        
                    for larger_algebra_char in range(len(self.__solved_circuit[j][0])):
                        algebra_larger_string += self.__solved_circuit[j][0][larger_algebra_char]
                    #algebra_smaller_string and algebra_larger_string are compared with each other to see if a gate needs to be drawn.
                    if algebra_smaller_string == algebra_larger_string:
                        in_list = False
                        compare_count += 1
                    if (algebra_smaller_string in algebra_larger_string) and len(algebra_smaller_string) != len(algebra_larger_string) and in_list == False and compare_bool == False and drawn_line==False:
                        #this if statement decides if a gate needs to be drawn

                        
                        duplicates = self.check_duplicates(algebra_smaller_string,algebra_larger_string)

                        #if algebra_smaller_string = XORAB and algebra_larger_string = ANDXORABC
                        #then the if statement will detect that XORAB is not at the end of the string so it must be in the first input.
                        
                        if len(duplicates) > 0:
                            if duplicates[compare_count]+ len(algebra_smaller_string) == len(algebra_larger_string):
                                gate_input = True
                            else:
                                gate_input = False
                        else:
                            if algebra_larger_string.index(algebra_smaller_string)+ len(algebra_smaller_string) == len(algebra_larger_string):
                                gate_input = True
                            else:
                                gate_input = False
                            
                        in_list = True
                        if algebra_smaller_string not in self._alphabet:
                            in_list = False

                        #if gate_input == False, then the gate should be drawn on the first input.
                        if self.__solved_circuit[j][0][0] != "NOT":
                            if gate_input == False:
                                gate_input_num = 35
                                gate_input = True
                            else:
                                gate_input_num = 69
                                gate_input = False
                        else:
                            gate_input_num = 52
                        if str(self.__solved_circuit[i][0][0]) in self._alphabet:
                            #this checks if the line is being drawn between a variable or a gate.

                            #These calcualte the position of the start and end of the line depending on the coordinates in self.__solved_circuit
                            pos_x0 = ((self.__solved_circuit[i][1])*100) + self.__base_x_position + 104
                            pos_y0 = ((self.__solved_circuit[i][2])*100) + self.__base_y_position + gate_input_num
                            pos_x1 = ((self.__solved_circuit[j][-2])*100) + self.__base_x_position + 2
                            pos_y1 = ((self.__solved_circuit[j][-1])*100) + self.__base_y_position + gate_input_num
                        else:
                            #These calcualte the position of the start and end of the line depending on the coordinates in self.__solved_circuit
                            pos_x0 = ((self.__solved_circuit[i][-2])*100) + self.__base_x_position + 104
                            pos_y0 = ((self.__solved_circuit[i][-1])*100) + self.__base_y_position + 52
                            pos_x1 = ((self.__solved_circuit[j][-2])*100) + self.__base_x_position + 2
                            pos_y1 = ((self.__solved_circuit[j][-1])*100) + self.__base_y_position + gate_input_num
                        self._master.create_line(pos_x0,pos_y0,pos_x1,pos_y1,width=2)
                        drawn_line = True

                    algebra_smaller_string = ""
                    algebra_larger_string = ""
                compare_bool = False
                in_list = False
            
    def check_duplicates(self,small,large):
        #this method checks to see if there are any duplicate gates in a larger string.
        checked = False
        dup_index = []
        old_location = 0
        while checked != True:
            try:
                location = large.index(small)
                large = large[:location] + large[location+(len(small)):]
                dup_index.append(location+old_location)
                old_location += len(small)
            except:
                checked = True
        return dup_index
