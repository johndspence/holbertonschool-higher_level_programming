import threading
from threading import Lock
import sys

lock = Lock()

'''
This class defines the list of numbers and initiates the threads
It also defines the add method, the sorting check, and returns
to main the ordered array
'''
class OrderedArray(threading.Thread):
    def __init__(self):
        pass

    list = []

    def add(self, number):
        if type(number) is not int:
            raise Exception("number is not an integer")
        thread = OrderedArrayThread(number)
        thread.start()

    def isSorting(self):
        if threading.activeCount == 1:
            return True
        return False

    def __str__(self):
        with lock:
            return str(OrderedArray.list)
'''
This class is a thread that appends each number it receives to the list
OrderedArray.list and then sorts it
'''
class OrderedArrayThread(threading.Thread):
    def __init__(self, number):
        if type(number) is not int:
            raise Exception("number is not an integer")
        self.number = number
        threading.Thread.__init__(self)

    def run(self):
            with lock:
                OrderedArray.list.append(self.number)
                OrderedArray.list.sort()
