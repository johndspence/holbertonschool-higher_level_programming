
import threading
from random import randint
from time import sleep

'''class Store receives 10 items and 3 person capacity and establishes
	a semaphore of 3 people'''
class Store():
	def __init__(self, item_number, person_capacity):
		self.item_number = item_number
		self.person_capacity = person_capacity
		self.semaphore = threading.BoundedSemaphore(self.person_capacity)

	'''enter method of store models one person entering the store and
		decrements the semaphore'''
	def enter(self):
		self.semaphore.acquire()

	'''buy method of store models person buying an item and decrements
		the number of available items'''
	def buy(self):
		sleep(randint(5,10))
		if self.item_number >= 0 :
			self.item_number = self.item_number - 1
		if self.item_number < 0:
			return False
		self.semaphore.release()
		return True
