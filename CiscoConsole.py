# programmer:  Chace Gibson
# date :       9/18/2019
# description: Program to open up com port


from PortClass import PortClass
import serial.tools.list_ports
import os

desiredPort = "Cisco".upper()
#desiredPort = "commun".upper()



def Main():
	portList = PC.ReturnPortsInDictionary()                     #list of all com ports
	PC.PrintPorts(portList)                                            #prints out com ports
	portNum = PC.GetPortNumber(desiredPort, portList)                  
	if (portNum != False):
		PC.OpenPutty(portNum)                                            
	else:
		print ("")
		print ("Type in the COM port manually if it is not named cisco EXAMPLE(com1, com2)")
		print ("Or prss enter once connected to cisco device")
		comPort = input().upper()
		if (comPort != ""):
			port = PC.GetPortNumber(comPort, portList)
			if (port != False):
				PC.OpenPutty(port)
			else:
				print ("port " + comPort + " is not seen by the operating system")
	x = input("Press enter")
	
	


	
PC = PortClass()
os.system('cls')
while True:
	print ("CONNECT TO CISCO DEVICE")
	Main()
	os.system('cls')

