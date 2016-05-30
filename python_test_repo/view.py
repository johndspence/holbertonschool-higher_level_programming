#!/usr/bin/python

import Tkinter as tk


class View(tk.Toplevel):

    # Constructor
    def __init__(self, master):
        tk.TopLevel__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        # Label number
        self.__number_var = tk.StringVar()
        self.__number_label = tk.Label(self, textvariable=self.__number_var)
        self.__number_label.pack(side='left')

        # Increase button
        self.inc_button = tk.Button(self, text='+', width=2)
        self.inc_button.pack(side='left')

        # Decrease Button
        self.dec_button = tk.Button(self, text='-', width=2)
        self.dec_button.pack(side='left')

    # Update UI
    def update_number(self, n):
        self.__number_var.set(str(n))
