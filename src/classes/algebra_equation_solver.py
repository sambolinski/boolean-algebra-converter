from .error_window import ErrorWindow
import math
class BooleanAlgebraEquationAnalysis:
    def __init__(self, algebra, full_algebra,variable_list="",placement=0):
        #This class is sued when solving the algebra
        self.__algebra = algebra
        self.__full_algebra = full_algebra
        self._placement = placement
        self._boolean = ["XOR", "AND", "OR", "NOR", "NAND", "NXOR", "NOT"]
        self._alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self._comparison_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self._brackets = ["(",")"]
        self._variable_binary_list = variable_list
    def error_check(self):
        #this method is used in a try statement to see if there are any errors, if there are, this method is called.
        widget_list = self._master.winfo_children()
        widget_list[0].delete(0, len(widget_list[0].get()))
        widget_list[1].invoke()
    def split_boolean_input(self):
        #this function takes the inputted algebra (e.g XOR(A,B)) and splits it into ["XOR","A","B"], this removes brackets and makes the algebra easier to understand
        self._updated_algebra = []
        _temp_bin_string = ""
        _alphabet_boolean = False
        _loop_alphabet_boolean = False
        for i in range(len(self.__algebra)-1):
            #looks through the algebra to see if there are any logic gates.
            if self.__algebra[i] != "1" and self.__algebra[i] != "0":
                _loop_alphabet_boolean = False
                _alphabet_boolean = False
                #this if statement checks to see if there is any binary.

            #these if statements are used to split the raw input into an array that can be used. they are split into gates and variables.
            if self.__algebra[i] == "X" and self.__algebra[i+1] == "O" and self.__algebra[i+2] == "R" and self.__algebra[i-1] != "N":
                self._updated_algebra.append("XOR")
            elif self.__algebra[i] == "O" and self.__algebra[i+1] == "R" and (self.__algebra[i-1] != "X" and self.__algebra[i-1] != "N"):
                self._updated_algebra.append("OR")
            elif self.__algebra[i] == "A" and self.__algebra[i+1] == "N" and self.__algebra[i+2]=="D" and self.__algebra[i-1] !="N":
                self._updated_algebra.append("AND")
            elif self.__algebra[i] == "N" and self.__algebra[i+1] == "A" and self.__algebra[i+2] == "N" and self.__algebra[i+3]=="D":
                self._updated_algebra.append("NAND") 
            elif self.__algebra[i]=="N" and self.__algebra[i+1] == "O" and self.__algebra[i+2] == "R":
                self._updated_algebra.append("NOR")
            elif self.__algebra[i]=="N" and self.__algebra[i+1] == "X" and self.__algebra[i+2] == "O" and self.__algebra[i+3] == "R":
                self._updated_algebra.append("NXOR")
            elif self.__algebra[i]=="N" and self.__algebra[i+1] == "O" and self.__algebra[i+2] == "T":
                self._updated_algebra.append("NOT")
            elif self.__algebra[i] in self._alphabet and ((self.__algebra[i+1] not in self._alphabet) and (self.__algebra[i-1] not in self._alphabet)):
                self._updated_algebra.append(str(self.__algebra[i]))
            if (self.__algebra[i] == "1" or self.__algebra[i] == "0") and (_loop_alphabet_boolean == False):
                for k in range(i,len(self.__algebra)):
                    #if binary is used this table will detect it and add it to the array.
                    if (self.__algebra[k] == "1" or self.__algebra[k] == "0") and (_alphabet_boolean == False):
                        _temp_bin_string += self.__algebra[k]
                    if self.__algebra[k] != "1" and self.__algebra[k] != "0":
                        _alphabet_boolean = True
                self._updated_algebra.append(_temp_bin_string)
                _temp_bin_string = ""
                _loop_alphabet_boolean = True      
        return self._updated_algebra
    def get_variable_list(self):
        #this function gets the list of variables. eg XOR(A,B) will have A and B as variables.
        self._variable_list = []
        self._variable_list_without_binary = []
        for i in range(len(self._updated_algebra)):
            if self._updated_algebra[i] in self._alphabet:
                self._variable_list.append(self._updated_algebra[i])
            if (self._updated_algebra[i] not in self._alphabet) and (self._updated_algebra[i] not in self._boolean):
                self._variable_list.append(self._updated_algebra[i])
            self._variable_list = list(set(self._variable_list))
            self._variable_list.sort()
        for i in range(len(self._variable_list)):
            if self._variable_list[i] in self._alphabet:
                self._variable_list_without_binary.append(self._variable_list[i])
        return self._variable_list
    def generate_variable_binary_list(self):
        #this subroutine is used to get the varaibles default bit setting and the default bit amount.

        #########################################################################################################
        #the length of the bit pattern is 2^n, where n is the number of variables.                              #
        #the rows will be a binary number, and the columns will increment the next row by one                   #
        #EXAMPLE:                                                                                               #
        # ABC                                                                                                   #
        # 000 = 0                                                                                               #
        # 001 = 1                                                                                               #
        # 010 = 2                                                                                               #
        # 011 = 3                                                                                               #
        # 100 = 4                                                                                               #
        # 101 = 5                                                                                               #
        # 110 = 6                                                                                               #
        # 111 = 7                                                                                               #
        #                                                                                                       #
        #I found a pattern which happens in each column.                                                        #
        #in each column, the bits alternate between 1 and 0 every, 2^c, where c is the column number            #
        #so every ((2^n)/(2^c)) the bits should alternate between 0 and 1. where n is the number of variables   #
        #and c is the column number.                                                                            #
        #########################################################################################################
        string_base = ""
        bit_alteration = 0
        count = 0
        variable_counter = 0
        self._variable_binary_list = []
        bit_num = 0
        #REFER TO DOCUMENTED DESIGN FOR MORE INFO (The Truth Table Solving Algorithm Overview)
        for i in range(len(self.__full_algebra)):
            if self.__full_algebra[i] in self._comparison_alphabet:
                self._comparison_alphabet.remove(self.__full_algebra[i])
                bit_num += 1
        for i in range(len(self._variable_list)):
            if self._variable_list[i] not in self._alphabet:
                self._variable_binary_list.append([self._variable_list[i],self._variable_list[i]])
        for bit_placement in range(bit_num):
            if self._placement == 0:
                bit_alteration = int(((2**bit_num) / (2**(bit_placement+1))))
            else:
                bit_alteration = int(((2**bit_num) / (2**(self._placement))))
                #self._placement += 1
            for bit_amount in range(int((2**bit_num)/(bit_alteration))):
                if count == 0:
                    for bit_switch_0 in range(bit_alteration):
                        string_base += "0"
                    count +=1
                elif count == 1:
                    for bit_switch_1 in range(bit_alteration):
                        string_base += "1"
                    count -=1
            
            if variable_counter > len(self._variable_list_without_binary):
                variable_counter = len(self._variable_list_without_binary)
            if variable_counter < len(self._variable_list_without_binary):
                
                self._variable_binary_list.append([self._variable_list_without_binary[variable_counter],string_base])

            string_base = ""
            variable_counter += 1
            
        #print("var_bin_list:",self._variable_binary_list) 
        return self._variable_binary_list
    def combine_variable_and_binary(self):
        #This function takes each variable and assigns the binary configuration from "generate_variable_binary_list"
        for i in range(len(self._updated_algebra)):
            if (self._updated_algebra[i] in self._alphabet):
                for j in range(len(self._variable_binary_list)):
                    if self._variable_binary_list[j][0] == self._updated_algebra[i]:
                        self._updated_algebra[i] = self._variable_binary_list[j]
            if (self._updated_algebra[i] not in self._alphabet and self._updated_algebra[i] not in self._boolean):
                for j in range(len(self._variable_binary_list)):
                    if self._variable_binary_list[j][0] == self._updated_algebra[i]:
                        self._updated_algebra[i] = self._variable_binary_list[j]
        self._algebra_binary = self._updated_algebra
        return self._algebra_binary
        
class TruthTableEvaluator:
    def __init__(self,algebra):
        self.__algebra = algebra
        self._boolean = ["XOR", "AND", "OR", "NOR", "NAND", "NXOR", "NOT"]
    def get_boolean_gate_count(self):
        #finds the amount of boolean gates in the equation.
        self._boolean_gate_count = 0
       
        for i in range(len(self.__algebra)):
            if self.__algebra[i] in self._boolean:
                self._boolean_gate_count += 1
        return self._boolean_gate_count
    def solve_truth_table(self):
        #this function solves the algebra, gate by gate. It goes through the entire algebra and detects which gate it is, and calls
        #the appropriate function.
        current_bool_gate = self._boolean_gate_count
        count_to_current_bool_gate = 0
        count = 0
        #the * will be appended on the keep len(algebra) constant.
        try:
            #this loop will scan through the list and pply the appropriate function
            while count < self._boolean_gate_count:
                for i in range(len(self.__algebra)-1):
                    if self.__algebra[i] in self._boolean and (count_to_current_bool_gate != current_bool_gate):
                        count_to_current_bool_gate += 1
                    if (self.__algebra[i] in self._boolean) and count_to_current_bool_gate == current_bool_gate:
                        if self.__algebra[i] == "AND":
                            self._boolean_result = self.AND(self.__algebra[i+1], self.__algebra[i+2])
                            self.__algebra[i] = [("AND",self.__algebra[i+1], self.__algebra[i+2]),self._boolean_result]
                            self.__algebra.pop(i+1)
                            self.__algebra.pop(i+1)
                            self.__algebra.append("*")
                            self.__algebra.append("*")
                            current_bool_gate -= 1
                        elif self.__algebra[i] == "XOR":
                            self._boolean_result = self.XOR(self.__algebra[i+1], self.__algebra[i+2])
                            self.__algebra[i] = [("XOR",self.__algebra[i+1], self.__algebra[i+2]),self._boolean_result]
                            self.__algebra.pop(i+1)
                            self.__algebra.pop(i+1)
                            self.__algebra.append("*")
                            self.__algebra.append("*")
                            current_bool_gate -= 1
                        elif self.__algebra[i] == "OR":
                            self._boolean_result = self.OR(self.__algebra[i+1], self.__algebra[i+2])
                            self.__algebra[i] = [("OR",self.__algebra[i+1], self.__algebra[i+2]),self._boolean_result]
                            self.__algebra.pop(i+1)
                            self.__algebra.pop(i+1)
                            self.__algebra.append("*")
                            self.__algebra.append("*")
                            current_bool_gate -= 1
                        elif self.__algebra[i] == "NAND":
                            self._boolean_result = self.NAND(self.__algebra[i+1], self.__algebra[i+2])
                            self.__algebra[i] = [("NAND",self.__algebra[i+1], self.__algebra[i+2]),self._boolean_result]
                            self.__algebra.pop(i+1)
                            self.__algebra.pop(i+1)
                            self.__algebra.append("*")
                            self.__algebra.append("*")
                            current_bool_gate -= 1
                        elif self.__algebra[i] == "NXOR":
                            self._boolean_result = self.NXOR(self.__algebra[i+1], self.__algebra[i+2])
                            self.__algebra[i] = [("NXOR",self.__algebra[i+1], self.__algebra[i+2]),self._boolean_result]
                            self.__algebra.pop(i+1)
                            self.__algebra.pop(i+1)
                            self.__algebra.append("*")
                            self.__algebra.append("*")
                            current_bool_gate -= 1
                        elif self.__algebra[i] == "NOR":
                            self._boolean_result = self.NOR(self.__algebra[i+1], self.__algebra[i+2])
                            self.__algebra[i] = [("NOR",self.__algebra[i+1], self.__algebra[i+2]),self._boolean_result]
                            self.__algebra.pop(i+1)
                            self.__algebra.pop(i+1)
                            self.__algebra.append("*")
                            self.__algebra.append("*")
                            current_bool_gate -= 1
                        elif self.__algebra[i] == "NOT":
                            self._boolean_result = self.NOT(self.__algebra[i+1])
                            self.__algebra[i] =[("NOT",self.__algebra[i+1]),self._boolean_result]
                            self.__algebra.pop(i+1)
                            self.__algebra.append("*")
                            self.__algebra.append("*")
                            current_bool_gate -= 1
                            
                count_to_current_bool_gate = 0
                count += 1
            self._algebra_size = len(self.__algebra)
            self._asterisk_counter = 0
        except:
            self.error_check()
            error_window = ErrorWindow(self,self._master,"invalid algebra input")
        #goes through the entire algebra and removes the
        for i in range(len(self.__algebra)):
            if self.__algebra[i] == "*":
                self._asterisk_counter += 1
        for i in range(self._asterisk_counter):
            self.__algebra.remove("*")
        return self.__algebra
    #BOOLEAN COMMAND METHODS
    def AND(self, variable_1,variable_2):
        #function to go through both variables bit arrangement, and ANDs each bit
        var1_and_var2 = ""
        for counter in range(len(variable_1[1])):
            if variable_1[1][counter] == "1" and variable_2[1][counter] == "1":
                var1_and_var2 += "1"
            elif variable_1[1][counter] == "0" or variable_2[1][counter] == "0":
                var1_and_var2 += "0"
        return var1_and_var2
    
    def XOR(self, variable_1,variable_2):
        #function to go through both variables bit arrangement, and XORs each bit
        var1_xor_var2 = ""
        for counter in range(len(variable_1[1])):
            if (variable_1[1][counter] == "1" and variable_2[1][counter] == "1") or (variable_1[1][counter] == "0" and variable_2[1][counter] == "0"):
                var1_xor_var2 += "0"
            elif (variable_1[1][counter] == "1" and variable_2[1][counter] == "0") or (variable_1[1][counter] == "0" and variable_2[1][counter] == "1"):
                var1_xor_var2 += "1"
        
        return var1_xor_var2
    
    def OR(self, variable_1,variable_2):
        #function to go through both variables bit arrangement, and ORs each bit
        var1_or_var2 = ""
        for counter in range(len(variable_1[1])):
            if (variable_1[1][counter] == "1" or variable_2[1][counter] == "1"):
                var1_or_var2 += "1"
            elif (variable_1[1][counter] == "0" and variable_2[1][counter] == "0"):
                var1_or_var2 += "0"
        return var1_or_var2
    def NOT(self,variable_1):
        #Puts each bit in teh varaible arrangement, and NOTs them
        not_var_1 = ""
        for counter in range(len(variable_1[1])):
            if variable_1[1][counter] == "1":
                not_var_1 += "0"
            elif variable_1[1][counter] == "0":
                not_var_1 += "1"
        return not_var_1
    def NAND(self,variable_1,variable_2):
        #Puts the 2 variables through the AND gate then the NOT gate
        var1_n_and_var2 = ["var1_n_and_var2", ""]
        var1_n_and_var2[1] = self.AND(variable_1,variable_2)
        var1_nand_var2 = self.NOT(var1_n_and_var2)
        return var1_nand_var2
    def NOR(self,variable_1,variable_2):
        #Puts the 2 variables through the OR gate then the NOT gate
        var1_n_or_var2 = ["var1_n_or_var2",""]
        var1_n_or_var2[1] = self.OR(variable_1,variable_2)
        var1_nor_var2 = self.NOT(var1_n_or_var2)
        return var1_nor_var2
    def NXOR(self,variable_1,variable_2):
        #Puts the 2 variables through the XOR gate then the NOT gate
        var1_n_xor_var2 = ["var1_n_xor_var2", ""]
        var1_n_xor_var2[1] = self.XOR(variable_1,variable_2)
        var1_nxor_var2 = self.NOT(var1_n_xor_var2)
        return var1_nxor_var2

class TableHeadings:
    def __init__(self,algebra):
        self.__algebra = algebra
        self._solved_title = []
        self._solved_table = []
        self._alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self._alphabet_comparison = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    def solve_headings(self):
        #This function is used to solve the column headings for the truth table.
        #the order of the column headings are the order you will solve a truth table
        
        boolean_variables = ["XOR","AND","OR","XOR","NXOR","NAND","NOR","NOT"]
        
        temp_var_string = ""
        variable_names = True
        boolean_count = 0
        boolean_amount = 0
        
        temp_deletion_list = []

        bit_length = 0
        #loops through the the algebra.
        for i in range(len(self.__algebra)):
            if self.__algebra[i] in boolean_variables:
                boolean_amount += 1
        for i in range(len(self.__algebra)):
            if self.__algebra[i] not in boolean_variables:
                self._alphabet.append(self.__algebra[i])
        set(self._alphabet)
        while boolean_count < boolean_amount:
            #####################################
            #this section seperates the boolean gates and the variables, so the variables are at the beginning
            
            if variable_names == True:
                for i in range(len(self.__algebra)):
                    if self.__algebra[i] not in boolean_variables and (self.__algebra[i] in self._alphabet):# or (len(self.__algebra[i]) == 2**bit_length):
                        self._solved_title.append(self.__algebra[i])
                        self._alphabet.remove(self.__algebra[i])
                    
                variable_names = False
            ######################################
            for i in range(len(self.__algebra)):
                not_boolean = False
                if self.__algebra[i] in boolean_variables:
                    #gets the amount of gates
                    boolean_count += 1
                if boolean_count == boolean_amount and boolean_amount > 0:
                    #this rebuilds the current step in sloving the truth table to make it look like what the user would enter.
                    if self.__algebra[i] != "NOT":
                        temp_var_string += self.__algebra[i]
                        temp_var_string += "("
                        temp_var_string += self.__algebra[i+1]
                        temp_var_string += ","
                        temp_var_string += self.__algebra[i+2]
                        temp_var_string += ")"
                    else:
                        temp_var_string += self.__algebra[i]
                        temp_var_string += "("
                        temp_var_string += self.__algebra[i+1]
                        temp_var_string += ")"
                        not_boolean = True
                    self.__algebra[i] = temp_var_string
                    self._solved_title.append(temp_var_string)
                    #Has to add * to the end, in order to not shorten the self.__algebra array. This will stop an out of index error.
                    if not_boolean == False:
                        self.__algebra.pop(i+1)
                        self.__algebra.pop(i+1)
                        self.__algebra.append("*")
                        self.__algebra.append("*")
                    else:
                        self.__algebra.pop(i+1)
                        self.__algebra.append("*")
                    temp_var_string = ""
                    boolean_count = 0
                    boolean_amount -= 1
                    
        self._table_variable_values = ""
    def solve_table(self):
        #this method solved the entire table. It starts by splitting the input into a list using .split_boolean_input()
        #it then loops through this array and splits it so there are no more brackets. just gates and variables.
        #after that it loops through the list again and solves each individual item in the list.
        #when one item has been solved. The binary result is appended to the column heading.
        #once the list is done, there will be an array with a solved column heading and binary combination.
        try:

            #full_algebra is what the smaller individual inputs are compared with.
            #the variable counter lets the program know if it has duplicated variables.
            full_algebra_class = BooleanAlgebraEquationAnalysis(self._solved_title[(len(self._solved_title)-1)],self._solved_title[(len(self._solved_title)-1)])
            full_algebra = full_algebra_class.split_boolean_input()

            #splits up the split up algebra removing brackets in order to make the algebra easier to work with.
            variable_list_class = BooleanAlgebraEquationAnalysis(self._solved_title[(len(self._solved_title)-1)],full_algebra)
            variable_list_class.split_boolean_input()
            variable_list_class.get_variable_list()
            variable_list = variable_list_class.generate_variable_binary_list()
            remove_array = []
            variable_counter_list = []
            variable_counter = 0
        
            for i in range(len(self._solved_title)):
                if (self._solved_title[i] not in self._alphabet_comparison) and (self._solved_title[i] in self._alphabet):
                    #this makes sure no duplicate variables are added. Any variable seen twice is added to the remove_array
                    remove_array.append(self._solved_title[i])
                elif self._solved_title[i] in self._alphabet:
                    self._alphabet_comparison.remove(self._solved_title[i])
            for i in range(len(remove_array)):
                self._solved_title.remove(remove_array[i])
            for i in range(len(self._solved_title)):
                temp_equation_class = BooleanAlgebraEquationAnalysis(str(self._solved_title[i]),full_algebra)
                temp_equation = temp_equation_class.split_boolean_input()
                for k in range(len(temp_equation)):
                    if temp_equation[k] in self._solved_title:
                        #.index finds the position of one item in another
                        variable_counter = self._solved_title.index(temp_equation[k])
                if self._solved_title[i] in self._alphabet:
                    #this counts the number of variables in the list, so they are not duplicated.
                    variable_counter += 1
                    variable_counter_list.append([self._solved_title[i],variable_counter])
                    self._alphabet.remove(self._solved_title[i])
                else:
                    variable_counter = 0

                #temp_var_algebra makes the input appear as if it was typed by the user.
                temp_var_algebra = "("+self._solved_title[i]+")"
                temp_var_algebra.replace(" ", "")
                self._equation = BooleanAlgebraEquationAnalysis(str(temp_var_algebra),full_algebra,variable_list,(variable_counter))
                self._equation.split_boolean_input()
                self._equation_for_transfer = self._equation.combine_variable_and_binary()
                self._solving_equation = TruthTableEvaluator(self._equation_for_transfer)
                self._solving_equation.get_boolean_gate_count()
                self._solved_equation = self._solving_equation.solve_truth_table()
                #This is the final solved table
                self._solved_table.append([self._solved_title[i],self._solved_equation[0][len(self._solved_equation)]])
        except:
            error_win = ErrorWindow(self._master,"Invalid Algebra Input")
        return self._solved_table


class CircuitSolver:
    def __init__(self,algebra):
        self._algebra_column=algebra
        
        self._solved_algebra_coord = ""
        self._boolean = ["XOR", "AND", "OR", "NOR", "NAND", "NXOR", "NOT"]
        self._alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        
    def solve_circuit(self):
        #this method solves the coordinates for the gates and variables.
        #REFER TO DOCUMENTED DESIGN (Circuit Solving Algorithm Overview) for more information
        # on how this works
        gate_count = 0
        alphabet_counter = 0
        single_gate_data = []
        all_gate_data = []
        used_variables = []
        #self._algebra = []
        for alphabet_count in range(len(self._algebra_column)):
            if self._algebra_column[alphabet_count][0] in self._alphabet:
                #counts the number of variables used.
                alphabet_counter += 1
        for count in range(len(self._algebra_column)):
            #this splits the algebra for easier use.
            solve_algebra = BooleanAlgebraEquationAnalysis(str([self._algebra_column[count][0]]),str([self._algebra_column[count][0]]))
            split_algebra = solve_algebra.split_boolean_input()
            self._algebra_column[count] = split_algebra


        #astrisks are used to avoind indexing a part of a list that has been removed.           
        for i in range(len(self._algebra_column)):
            if self._algebra_column[i][0] in self._alphabet:
                self._algebra_column[i] = "*"
        astrisk_count = 0
        for i in range(len(self._algebra_column)):
            if self._algebra_column[i][0] == "*":
                astrisk_count += 1
        for i in range(astrisk_count):
            self._algebra_column.remove("*")
        for column in range(len(self._algebra_column)):
            #This section detemines the X coordinate
            for column_algebra in range(len(self._algebra_column[column])):
                if self._algebra_column[column][column_algebra] in self._boolean:
                    gate_count += 1

            #single_gate_data is a list of the Gate with the coordinates
            single_gate_data.append(self._algebra_column[column])
            single_gate_data.append(gate_count)

            #This section detemines the Y coordinate
            if self._algebra_column[column][0] in self._alphabet:
                single_gate_data.append(math.floor(column/2))
            else:
                single_gate_data.append(column-alphabet_counter)

            #all_gate_data is a list of all single_gate_data
            all_gate_data.append(single_gate_data)
            gate_count = 0
            single_gate_data = []
        self._solved_algebra_coord = all_gate_data
        return self._solved_algebra_coord
