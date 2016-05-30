#!/usr/bin/python

# Main
import Tkinter as tk
from model import Model
from controller import Controller
from view import View

root = tk.Tk()
root.withdraw()
root.mainloop()
app = Controller(root)
