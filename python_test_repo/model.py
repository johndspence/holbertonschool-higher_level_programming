#!/usr/bin/python
class Model:

    # Constructor
    def __init__(self, n = 0):
        self.__value = n
        self.__callbacks = []

    # Callback
    def add_callback(self, func):
        self.__callbacks.append(func)

    def del_callback(self, func):
        i = 0
        for f in self.__callbacks:
            if f == func:
                del self.__callbacks[i]
                ++ i

    def do_callbacks(self):
        for f in self.__callbacks:
            f(self.__value)

    # Setter/Getter
    def set(self, n):
        self.__value = n
        self.__do_callbacks()

    def get(self):
        return self.__value
