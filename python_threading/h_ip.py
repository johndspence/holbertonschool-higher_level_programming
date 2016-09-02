import threading
import requests
import urllib2
import json

class IPThread(threading.Thread):
	def __init__(self, ip, callback):
		threading.Thread.__init__(self)
		self.__ip = ip
		self.__callback = callback

	'''converts an IP address to a country name by using an API and passes
		that country name to a callback function'''
	def run(self):
		response = requests.get('https://api.ip2country.info/ip?' + str(self.__ip))
		obj = json.loads(response.text)
		self.__callback(obj.get('countryName').encode('utf-8'))
		print "Search: " + str(self.__ip)
		print "countryName: " + obj.get('countryName').encode('utf-8')
