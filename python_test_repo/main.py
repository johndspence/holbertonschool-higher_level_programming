#!/usr/bin/python

# Main
from view import View
from model import Model
from controller import Controller

import Tkinter as tk
import wx

root = tk.Tk()
root.withdraw()
app = Controller(root)
root.mainloop()
