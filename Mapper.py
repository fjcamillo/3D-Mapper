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
i= 0

arduino = serial.Serial('COM37', 115200, timeout = .1)
def mainProcess():
	createNullObjectFirstNull()
	main()


def secondProcess():
    while rotationOnZAxis != 10:
        debuggerThingy()
    	readArduinoSerial()
        angleConditions(rotationOnXAxis, rotationOnZAxis)
    	createNullObjectNextNull(nullCount)


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

def angleConditions(rotationOnXAxisAngle, rotationOnZAxisAngle):
	if rotationOnXAxisAngle == 0:
		if rotationOnZAxisAngle > 90:
			rotationOnZAxisAngle = 180 - rotationOnZAxisAngle
			coordinateForXAngleEquals_0()
		else:
			coordinateForXAngleEquals_0()
	elif rotationOnXAxisAngle <= 89 and rotationOnXAxisAngle > 0:
		if rotationOnZAxisAngle > 90:
			rotationOnZAxisAngle = 180 - rotationOnZAxisAngle
			coordinateForXAngleLessThanOrEquals_89()
		else:
			coordinateForXAngleLessThanOrEquals_89()
	elif rotationOnXAxisAngle == 90:
		if rotationOnZAxisAngle > 90:
			rotationOnZAxisAngle = 180 - rotationOnZAxisAngle
			coordinateForXAngleEquals_90()
		else:
			coordinateForXAngleEquals_90()
	elif rotationOnXAxisAngle <= 179 and rotationOnXAxisAngle >90:
		if rotationOnZAxisAngle > 90:
			rotationOnZAxisAngle = 180 - rotationOnZAxisAngle
			coordinateForXAngleLessThanOrEqual_179()
		else:
			coordinateForXAngleLessThanOrEqual_179()
	elif rotationOnXAxisAngle == 180:
		if rotationOnZAxisAngle > 90:
			rotationOnZAxisAngle = 180 - rotationOnZAxisAngle
			coordinateForAngleEquals_180()
		else:
			coordinateForAngleEquals_180()

def coordinateForXAngleEquals_0():
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = (distance)*math.cos(math.radians(rotationOnZAxis))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*math.sin(math.radians(rotationOnZAxis))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = 0

def coordinateForXAngleLessThanOrEquals_89():
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = ((distance)*(math.cos(math.radians(rotationOnZAxis)))) - (((2)*(distance)*(math.cos(math.radians(rotationOnZAxis))))*(math.sin(math.radians(180-((180))))))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*(math.sin(math.radians(rotationOnZAxis)))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = (distance)*(math.cos(math.radians(rotationOnZAxis)))*(math.sin(math.radians(rotationOnXAxis)))

def coordinateForXAngleEquals_90():
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = 0
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*(math.sin(math.radians(rotationOnZAxis)))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = (distance)*(math.cos(math.radians(rotationOnZAxis)))

def coordinateForXAngleLessThanOrEqual_179():
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = (((distance)*(math.cos(math.radians(rotationOnZAxis)))) - (((2)*(distance)*(math.cos(math.radians(rotationOnZAxis))))*(math.sin(math.radians(180-((180)))))))*(-1)
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*(math.sin(math.radians(rotationOnZAxis)))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = ((distance)*(math.cos(math.radians(rotationOnZAxis)))*(math.sin(math.radians(rotationOnXAxis))))*(-1)

def coordinateForAngleEquals_180():
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = ((distance)*(math.cos(math.radians(rotationOnZAxis))))*(-1)
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = (distance)*(math.sin(math.radians(rotationOnZAxis)))
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = 0

def createNullObjectFirstNull():
	nullObject.append(c4d.BaseObject(5140))
	doc.InsertObject( nullObject[nullCount] )

def createNullObjectNextNull(nullCounting):
	nullObject.append(c4d.BaseObject(5140))
	nullCounting += 1

def createDocInsertObject():
	while i != nullCount:
		doc.InsertObject( nullObject[nullCount] )
		i += 1

def addEvent():
	c4d.EventAdd()

def createPointOfOrigin():
	nullObject.append(c4d.BaseObject(5140))
	doc.InsertObject( nullObject[nullCount] )
	nullCount += 1

def main():
    secondProcess()
    createDocInsertObject()
    addEvent()

if __name__=='__main__':
	mainProcess()