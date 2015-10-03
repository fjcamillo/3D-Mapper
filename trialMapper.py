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

#Variables for Arduino 
distance = 240	
rotationOnXAxis = 0
rotationOnZAxis = 0
#arduino = serial.Serial('COM37', 9600, timeout = .1)




def mainProcess():
	createNullObject()

def readArduinoSerial():
	stringFromArduino = arduino.readline()

def angleConditions(rotationOnZAxis,rotationOnXAxis):
	if rotationOnXAxis == 0:
		coordinateForXAngleEquals_0()
	elif rotationOnXAxis <= 89 and rotationOnXAxis > 0:
		coordinateForXAngleLessThanOrEquals_89()
	elif rotationOnXAxis == 90:
		coordinateForXAngleEquals_90
	elif rotationOnXAxis <= 179 and rotationOnXAxis >90:
		coordinateForXAngleLessThanOrEqual_179()
	elif rotationOnXAxis == 180:
		coordinateForAngleEquals_180

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

def createNullObject():
	nullObject.append(c4d.BaseObject(5140))
	doc.InsertObject( nullObject[nullCount] )

def addEvent():
	c4d.EventAdd()

def createPointOfOrigin():
	nullObject.append(c4d.BaseObject(5140))
	doc.InsertObject( nullObject[nullCount] )
	nullCount += 1

if __name__=='__main__':
    mainProcess()
    addEvent()