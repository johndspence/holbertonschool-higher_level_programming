import threading
import sys

'''Create a class that hold each word'''
class StrLenThread(threading.Thread):
    def __init__(self, word):
        if type(word) is not str:
            raise Exception("word is not a string")
        threading.Thread.__init__(self)
        self.word = word

    '''Add the length of each word to the total_str_length'''
    def run(self):
        global total_str_length
        StrLenThread.total_str_length += len(word)

'''If user has not entered a string, raise an exception'''
if  len(sys.argv) != 2:
    raise Exception("Enter a string in quotes")
text = sys.argv[1]

words = text.split(" ")

StrLenThread.total_str_length = len(words) - 1

'''An array to hold the threads'''
str_length_threads = []

'''
For each element in words array, use the StrLenThread method to add its length
 to total_str_length'''
for word in words:
    str_length_thread = StrLenThread(word)

    ''' add each thread into the str_length_threads array'''
    str_length_threads += [str_length_thread]

    str_length_thread.start()

''' when the threads complete, close them together'''
for t in str_length_threads:
    t.join()

print "%d" % StrLenThread.total_str_length
