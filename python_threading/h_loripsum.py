import threading
from threading import Lock
import urllib2


'''use urllib2 method to retrieve and append a text string in a file,
	locking the file while doing so'''
class LoripsumThread(threading.Thread):
	def __init__(self, filename):
		self.filename = filename
		threading.Thread.__init__(self)

	def run(self):
		lock = Lock()
		with lock:
			towrite = urllib2.urlopen('http://loripsum.net/api/1/short')
			with open(self.filename, 'a') as text_file:
				text_file.write(towrite.read())
