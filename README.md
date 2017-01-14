# 3D-Mapper
Digital Signal Processing Activity #3

3DMapper is a Python-Cinema4D-IOT Tool in generating maps.

The 3DMapper is accompanied by an arduino uno with an attached ultrasonic sensor. The ultrasonic sensor measures the distance of the objects within the vicinity. Using a servo the ultrasonic could sweep through a 180 degree angle of space.

The arduino uno then sends th data to a Python Algorithm running in Cinema 4D using a serial connection with a baudrate of 9600. On the python side, I used pyserial to allow the algorithm to connect on the serial port. The python then interprets the data, then using Cinema 4D specific python functions and callbacks, I was able to create a 3D representation on Cinema 4D using the points gathered physically by the arduino uno and ultrasonic sensor.

This 3DMapper app could also be used with different hardware distance monitoring device that could enhance the data and make the 3DMapping in Cinema4D accurate.
