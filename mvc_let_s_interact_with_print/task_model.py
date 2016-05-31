
class TaskModel:


    # Constructor
    def __init__(self, title):
        # Receives a phrase (called a "title") and places it in
        # the private variable __title
        if title == "" or type(title) != str:
            raise Exception("title is not a string")
        self.__title = title
        # Set private empty variable for callback_function
        # entitled, confusingly, "callback_title"
        self.__callback_title = []

    # Overriding function for title in TaskModel
    def __str__(self):
        return self.__title

    # Getter of title
    def get_title(self):
        return self.__title

    # Setter of title
    def set_callback_title(self, value):
        self.__callback_title = value

    # Toggle function using extended slice method
    def toggle(self):
        self.__title = self.__title[::-1]

        # If a callback function is present, run that
        # callback function passing the title variable
        if self.__callback_title != None:
            self.__callback_title(self.__title)
