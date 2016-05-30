#!/usr/bin/python

# Main
import Tkinter as tk
root = tk.Tk()
root.withdraw()

root.mainloop()

from model import Model
from controller import Controller
app = Controller(root)
from view import View
