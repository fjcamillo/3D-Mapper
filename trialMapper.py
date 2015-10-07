import c4d
from c4d import gui
import math
import serial
#Welcome to the world of Python

#Note:
#[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] holds the XAngle Rotation
#[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] holds the YAngle Rotation must be negative for correct angle

nullObject = []
nullCount = 0
stringSentence = []
#Variables for Arduino 
distance = 0
rotationOnXAxis = 0
rotationOnZAxis = 0

arduino = serial.Serial('COM37', 115200, timeout = .1)
def mainProcess():
	createNullObjectFirstNull()
	main()


def secondProcess():
    while rotationOnXAxis < 90 and rotationOnXAxis < 2 :
    	readArduinoSerial()
        angleConditions()
    	createNullObjectNextNull()

def debuggerThingy():
	print arduino.readline()
	

def readArduinoSerial():
	stringFromArduino = str(arduino.readline())
	stringSentence = stringFromArduino.split()
	if "YAngle:" in  stringSentence:
		stringSentence.remove('YAngle:')
		rotationOnZAxis = int(str(stringSentence[0]))

	if "XAngle: " in stringSentence:
		stringSentence.remove('XAngle:')
		rotationOnXAxis = int(str(stringSentence[0]))

	if "Distance:" in stringSentence:
		stringSentence.remove("Distance:")
		distance = int(str(stringSentence[0]))

	else:
		pass

def angleConditions():
	if rotationOnXAxis == 0:
		if rotationOnZAxis > 90:
			rotationOnZAxis = 180 - rotationOnZAxis
			coordinateForXAngleEquals_0(distance, rotationOnZAxis)
		else:
			coordinateForXAngleEquals_0(distance, rotationOnZAxis)
	elif rotationOnXAxis <= 89 and rotationOnXAxis > 0:
		if rotationOnZAxis > 90:
			rotationOnZAxis = 180 - rotationOnZAxis
			coordinateForXAngleLessThanOrEquals_89(distance, rotationOnZAxis, rotationOnXAxis)
		else:
			coordinateForXAngleLessThanOrEquals_89(distance, rotationOnZAxis, rotationOnXAxis)
	elif rotationOnXAxis == 90:
		if rotationOnZAxis > 90:
			rotationOnZAxis = 180 - rotationOnZAxis 
			coordinateForXAngleEquals_90(distance, rotationOnZAxis)
		else:
			coordinateForXAngleEquals_90(distance, rotationOnZAxis)
	elif rotationOnXAxis <= 179 and rotationOnXAxis >90:
		if rotationOnZAxisAngle > 90:
			rotationOnZAxis = 180 - rotationOnZ
			coordinateForXAngleLessThanOrEqual_179(distance, rotationOnZAxis, rotationOnXAxis)
		else:
			coordinateForXAngleLessThanOrEqual_179(distance, rotationOnZAxis, rotationOnXAxis)
	elif rotationOnXAxis == 180:
		if rotationOnZAxis > 90:
			rotationOnZAxis = 180 - rotationOnZAxis
			coordinateForAngleEquals_180(distance, rotationOnZAxis)
		else:
			coordinateForAngleEquals_180(distance, rotationOnZAxis)

def coordinateForXAngleEquals_0(distance, rotationOnZAxis):
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = (distance)*math.cos(math.radians(rotationOnZAxis))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*math.sin(math.radians(rotationOnZAxis))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = 0

def coordinateForXAngleLessThanOrEquals_89(distance, rotationOnZAxis, rotationOnXAxis):
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = ((distance)*(math.cos(math.radians(rotationOnZAxis)))) - (((2)*(distance)*(math.cos(math.radians(rotationOnZAxis))))*(math.sin(math.radians(180-((180))))))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*(math.sin(math.radians(rotationOnZAxis)))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = (distance)*(math.cos(math.radians(rotationOnZAxis)))*(math.sin(math.radians(rotationOnXAxis)))

def coordinateForXAngleEquals_90(distance, rotationOnZAxis):
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = 0
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*(math.sin(math.radians(rotationOnZAxis)))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = (distance)*(math.cos(math.radians(rotationOnZAxis)))

def coordinateForXAngleLessThanOrEqual_179(distance, rotationOnZAxis, rotationOnXAxis):
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = (((distance)*(math.cos(math.radians(rotationOnZAxis)))) - (((2)*(distance)*(math.cos(math.radians(rotationOnZAxis))))*(math.sin(math.radians(180-((180)))))))*(-1)
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*(math.sin(math.radians(rotationOnZAxis)))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = ((distance)*(math.cos(math.radians(rotationOnZAxis)))*(math.sin(math.radians(rotationOnXAxis))))*(-1)

def coordinateForAngleEquals_180(distance, rotationOnZAxis):
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = ((distance)*(math.cos(math.radians(rotationOnZAxis))))*(-1)
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*(math.sin(math.radians(rotationOnZAxis)))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = 0

def createNullObjectFirstNull():
	nullObject.append(c4d.BaseObject(5140))
	doc.InsertObject( nullObject[nullCount] )

def createNullObjectNextNull():
	nullObject.append(c4d.BaseObject(5140))
	nullCount = -1
	doc.InsertObject( nullObject[nullCount] )

def createDocInsertObject():
	doc.InsertObject( nullObject[nullCount] )

def addEvent():
	c4d.EventAdd()

def createPointOfOrigin():
	nullObject.append(c4d.BaseObject(5140))
	doc.InsertObject( nullObject[nullCount] )
	nullCount += 1

def main():
    secondProcess()
    addEvent()

if __name__=='__main__':
	mainProcess()