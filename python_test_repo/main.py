#!/usr/bin/python

# Main

import Tkinter as tk
root = tk.Tk()
root.withdraw()
app = Controller(root)
root.mainloop()

from view import View
from model import Model
from controller import Controller
