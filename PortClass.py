# programmer:  Chace Gibson
# date :       9/18/2019
# description: set of classes for controling ports

import serial.tools.list_ports
import os

class PortClass():
	# finds all com ports and puts them in a dictionary
	def ReturnPortsInDictionary(self):
		portDic = {}
		ports = serial.tools.list_ports.comports()
		for port in ports:
			portDic[port.description.upper()] = port.device
		return portDic
	
	# returns port number if the description matches else it returns false
	def GetPortNumber(self, desiredPort, portDic):
		portNum = False
		for desc, device in portDic.items():
			if (desiredPort in desc): 
				portNum = device
				break
		return portNum
	
	# opens putty with port number
	def OpenPutty(self, comPort):
		print (comPort + " - Connected")
		os.system('putty -serial ' + comPort )
	
	# prints ports
	def PrintPorts(self, ports):
		print ("Com Ports found")
		for port in ports:
			print ("           " + str(port))
			

	
class CONFIG_INFO:
	def __init__(self, hostname, vlan, ip_address, tag):
		self.hostname = hostname
		self.vlan = "Vlan" + vlan
		self.ip_address = ip_address
		self.tag = tag
		