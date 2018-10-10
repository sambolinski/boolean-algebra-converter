import tkinter as tk
class ErrorWindow:
    def __init__(self,parent,message):
        #this class is used to spawn an error window if there is a problem with the program
        self._master = parent
        self._message = message
        if self._master != "":
            #this checks to see if the error window has a parent window.
            error = tk.Toplevel(self._master,bd=5,relief="ridge",width=20,height=20,padx=40,pady=40)
        else:
            root = tk.Tk()
            error = tk.Toplevel(root,bd=5,relief="ridge",width=20,height=20,padx=40,pady=40)
        
        error.overrideredirect(1)
        error.title("Error")
        msg = tk.Message(error,text=self._message)
        msg.pack()
        close_button = tk.Button(error,text="close",command=error.destroy)
        close_button.pack()
        
