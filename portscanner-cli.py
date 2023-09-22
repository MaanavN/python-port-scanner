#!/bin/python3

import sys
import socket
import datetime as dt



def get_hostname():
	try:
		global ip_addr
		ip_addr = input("Enter an ip address: ")
	except KeyboardInterrupt:
		sys.exit()


def validate_hostname():
	while True:
		try:
			octets = str(ip_addr).split(".")
			if len(octets) > 4  or len(octets) < 0:
				print("Hostname does not seem valid.")
				get_hostname()
			else:
				validation = (float(ip_addr))/2
				print("Hostname does not seem valid.")
				get_hostname()
		
		except ValueError:
			break
			
		except KeyboardInterrupt:
			sys.exit()



get_hostname()
validate_hostname()
target = socket.gethostbyname(ip_addr)

while True:
	try:
		p1 = int(input("Enter the starting port: "))
		break
	except ValueError:
		p1 = int(input("Enter the starting port: "))
	except KeyboardInterrupt:
		sys.exit()

while True:
	try:
		p2 = int(input("Enter the ending port: "))
		break
	except ValueError:
		p2 = int(input("Enter the ending port: "))
	except KeyboardInterrupt:
		sys.exit()



print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(dt.datetime.now())}")
print("-" * 50)



try:
	for port in range(p1, p2):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("\nHostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("\nCould not connect to the server")
	sys.exit()
