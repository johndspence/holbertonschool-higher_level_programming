import threading

'''
This class increases total_str_length by the length of
each word that it receives
'''
class StrLengthThread(threading.Thread):
    def __init__(self, word):
        if type(word) is not str:
            raise Exception("word is not a string")
        threading.Thread.__init__(self)
        self.word = word

    def run(self):
        StrLengthThread.total_str_length += len(self.word)
