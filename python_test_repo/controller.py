#!/usr/bin/python
class Controller:

    # Constructor
    def __init__(self, root):

        # Retrieve my model (or create)
        self.my_number = Model()
        self.my_number.add_callback(self.number_change)

        # Create the view
        self.view_number = View(root)

        # Link View elements to Controller
        self.view_number.inc_button.config(command=self.inc_number)
        self.view_number.dec_button.config(command=self.dec_number)

        self.number_change(self.my_number.get())

    # Action to Model from View elements
    def inc_number(self):
        self.my_number.set(self.my_number.get() + 1)

    def dec_number(self):
        self.my_number.set(self.my_number.get() - 1)

    # Update View from Model
    def number_change(self, n):
        self.view_number.update_number(n)
