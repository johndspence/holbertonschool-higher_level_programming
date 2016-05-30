#!/usr/bin/python

# Main

import Tkinter as tk
from view import View
from model import Model
from controller import Controller

root = tk.Tk()
root.withdraw()
app = Controller(root)
root.mainloop()
