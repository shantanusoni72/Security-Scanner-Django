import requests
import re
import sys
import threading
import socket

def portscanner(url):
	startingPort = 0
	endingPort = 1000
	scanning(url,startingPort,endingPort)

def scanning(url,startingPort,endingPort):
	for port in range(startingPort,endingPort+1):
		Thread = threading.Thread(target = scanPorts,args=(url,port,))
		Thread.start()

def scanPorts(url,port):
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	final = con.connect_ex((url,port))
	if final:
		pass
	else:
		portSet = "Port {} is open".format(port)
		print(portSet)
	con.close()