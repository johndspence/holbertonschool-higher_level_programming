import threading

'''
This class reverses each word it receives and appends it to
sentence
'''
class ReverseStrThread(threading.Thread):
    def __init__(self, word):
        if type(word) is not str:
            raise Exception("word is not a string")
        self.word = word
        threading.Thread.__init__(self)

    sentence = " "


    def run(self):
        ReverseStrThread.sentence += self.word[::-1] + " "
