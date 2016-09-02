import Tkinter as tk

# Inherit model from tk.Toplevel
class TaskView(tk.Toplevel):
    # Constructor
    def __init__(self, master):
        # if master is not tk.Tk
        if isinstance(master, tk.Tk) == False:
            raise Exception("master is not a tk.Tk()")

        # Beginning of tk method??
        tk.Toplevel.__init__(self, master)
        # Delete master when window is closed?
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        # idk what this does.

        # Private attributes
        # tk String Widget
        self.__title_var = tk.StringVar()

        # tk Label Widget
        self.__title_label = tk.Label(self, textvariable=self.__title_var)

        # Public Attributes
        # tk Button Widget
        self.toggle_button = tk.Button(self, text="reverse")

        # tk pack widgets to align label to right and button to left
        self.toggle_button.pack(side=tk.LEFT)
        self.__title_label.pack(side=tk.RIGHT)

    # Method outside class: update title (phrase)
    def update_title(self, title):
        # exception raising
        if type(title) != str:
            raise Exception("title is not a string")
        self.__title_var.set(title)
