import c4d
from c4d import gui
import math
#Welcome to the world of Python

nullObject = []
nullCount = 0

def mainProcess():
	createNullObject()
	nullObject[nullCount][c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] = math.radians(90)

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