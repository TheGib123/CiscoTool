import os
import serial.tools.list_ports

# desired port you want to connect to
desiredPort = "Cisco".upper()

# gets all com ports
ports = serial.tools.list_ports.comports()

# dictionary of ports with there number and description
portDic = {}

#puts all ports in use into portDic
def PutPortsInDictionary():
    for port in ports:
        portDic[port.description.upper()] = port.device

# gets the port number that matches desiredPort string
def GetPortNumber():
    portNum = -1
    for desc, device in portDic.items():
        if (desiredPort in desc): 
            portNum = device
            break
    return portNum

# opens putty to session with desired port
def OpenPutty(comPort):
    print (comPort + " - Connected")
    os.system('putty -serial ' + comPort + '-m OUTPUT.txt')


#def Start(ports):
def ConnectToCissco():
    PutPortsInDictionary()
    comPort = GetPortNumber()
    
    if comPort != -1:
        OpenPutty(comPort)
    else:
        print ("Com Port was not found with description " + desiredPort)
        print
        print ("Com Ports found")
        for port in ports:
            print ("           " + str(port))
        print ()
        print ("make sure cisco device is seen in device manager")
	
	
	
class CONFIG_INFO:
	def __init__(self, hostname, vlan, ip_address, tag):
		self.hostname = hostname
		self.vlan = "Vlan" + vlan
		self.ip_address = ip_address
		self.tag = tag
	

	
def GetInfo():
	hostname = ""
	vlan = ""
	ip_address = ""
	tag = ""
	satisfiedInput = False
	
	while True:
		print ("hostname")
		hostname = input()
		print ("ip address")
		ip_address = input()
		print ("vlan")
		vlan = input()
		print ("property tag number")
		tag = input()
		print ()
		print ()
		print ()
		print ("is all information correct TYPE y or n")
		print ("   hostname ------" + hostname)
		print ("   ip address ----" + ip_address)
		print ("   vlan ----------" + vlan)
		print ("   property tag --" + tag)
		satisfiedInput = input().lower()
		if satisfiedInput == "y":
			break
			
	config = CONFIG_INFO(hostname, vlan, ip_address, tag)
	return config
		
	
	
def GenerateFile(info):
    my_file = str(os.getcwd()) + "\\files\\base_config.txt"
    my_file2 = str(os.getcwd()) + "\\files\\OUTPUT.txt"

    f = open(my_file, "r")
    f2 = open(my_file2, "w")
    for l in f:
        if ("SWITCH_HOSTNAME" in l):
            l = l.replace("SWITCH_HOSTNAME", info.hostname)
            f2.write(l)
        elif ("SWITCH_VLAN" in l):
            l = l.replace("SWITCH_VLAN", info.vlan)
            f2.write(l)
        elif ("SWITCH_TAG" in l):
            l = l.replace("SWITCH_TAG", info.tag)
            f2.write(l)
        elif ("SWITCH_IP_ADDRESS" in l):
            l = l.replace("SWITCH_IP_ADDRESS", info.ip_address)
            f2.write(l)
        else:
            f2.write(l)
    f.close()
    f2.close()
    print ()
    print ("config file genertated to files\OUTPUT.txt")
    print ()
	
	
def Main():
    print("GENERATE AND INSTALL BASIC CONFIGURATION ON CISCO DEVICE")
    info = GetInfo()
    #info = CONFIG_INFO('lu-kod-1234', '299', '192.168.20.1', '123456')
    GenerateFile(info)

    print ("to procceed with install on cisco device enter y or n")
    ans = input()
    if (ans == "y"):
        ConnectToCissco()
    input()
	
	
	
    
Main() 

