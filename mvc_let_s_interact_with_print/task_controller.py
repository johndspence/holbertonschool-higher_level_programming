import Tkinter as tk

from task_model import TaskModel
from task_view import TaskView

class TaskController:

    # Constructor
    def __init__(self, master, model):

        # Private attributes
        self.__model = model
        self.__view = TaskView(master)
        self.__view.update_title(self.__model.get_title())

        # If master is not tk Class, raise exception
        if isinstance(master, tk.Tk) == False:
            raise Exception("master is not a tk.Tk()")

        # If model is not TaskModel class, raise exception
        if isinstance(model, TaskModel) == False:
            raise Exception("model is not a TaskModel")

        # Link all callbacks from model to update view
        self.__model.set_callback_title(self.__view.update_title)

        # link the button of view to update model
        self.__view.toggle_button.configure(command=self.__model.toggle)
