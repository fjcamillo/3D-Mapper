import c4d
from c4d import gui
import serial

#Welcome to the world of Python
#Code for receiving Serial Data from the arduino
#Variables
arduino = serial.Serial('COM37',115200, timeout = .1)
handshakeReply = "Handshake Received"
checkDistance = "Distance:"
checkColor = "Color:"
checkYAngle = "YAngle:"
checkXAngle = "XAngle"
global Output1		#X Angle
global Output2		#YAngle

#c4d.CallCommand(200000067)  Command for duplicate
# c4d.CallCommand(5140) Command to create Null


def setDistanceNull():
	c4d.CallCommand(5140) #setups Null

def main():
	 stringFromSerial = arduino.readline()
	 listOfStringFromSerial = stringFromSerial.strip()



def checkStringReceived():
	if checkDistance in listOfStringFromSerial:
		pass

	elif checkColor in listOfStringFromSerial:
		pass

	elif checkYAngle in listOfStringFromSerial:
		pass

	elif checkXAngle in listOfStringFromSerial:
		pass
		
	else:
		pass

#Cinema 4d Functions to display output
def displayNullForDistance():
	pass

def setNullColor():
	pass

def setYAngle():
	pass

def setXAngle():
	pass




#def callPointOfOrigin():
#	c4d.CallCommand(5140)

if __name__=='__main__':
    main()
