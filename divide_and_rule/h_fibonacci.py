import threading
'''
Creates a class FibonacciThread, inheriting threading.thread from Python
library.  This class calls fibonacci method and prints the sequence number and
the fibonacci number
'''
class FibonacciThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)

        if type(number) is not int:
            raise Exception("number is not an integer")
        self.__number = number

    def run(self):
        print str(self.__number) + "-->" + str(fibonacci(self.__number))

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
