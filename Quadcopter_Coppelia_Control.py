import sim as vrep # access all the VREP elements
import sys
import numpy as np
import time
import random

vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # start a connection

if clientID != -1:
    print ("Connected to remote API server")
else:
    print("Not connected to remote API server")
    sys.exit("Could not connect")

"""
for i in range(100):
    r += 0.1
    errorCode, Quadcopter_target_handle = vrep.simxGetObjectHandle(clientID, 'Quadcopter_target', vrep.simx_opmode_oneshot_wait)
    errorCode, rotation = vrep.simxGetObjectOrientation(clientID, Quadcopter_target_handle, -1, vrep.simx_opmode_oneshot)
    errorCode, euler = vrep.simxGetIntegerSignal(clientID, "euler", vrep.simx_opmode_streaming)
    errorCode, rotCorr = vrep.simxGetIntegerSignal(clientID, "rotCorr", vrep.simx_opmode_streaming)
    vrep.simxSetObjectOrientation(clientID, Quadcopter_target_handle, -1, (0,0,np.pi*r), vrep.simx_opmode_oneshot)
    print(str(i) + " : " + str(rotation))
    time.sleep(0.2)
"""
#errorCode, Quadcopter_target_handle = vrep.simxGetObjectHandle(clientID, 'Quadcopter_target', vrep.simx_opmode_oneshot_wait)
#vrep.simxSetObjectPosition(clientID, Quadcopter_target_handle, -1, (1,0,1), vrep.simx_opmode_oneshot)

#""" # Manual Control
for posisi in range(5):
    x = float(input("input x: "))
    y = float(input("input y: "))
    errorCode, Quadcopter_target_handle = vrep.simxGetObjectHandle(clientID, 'Quadcopter_target', vrep.simx_opmode_oneshot_wait)
    if(errorCode==vrep.simx_return_ok):
        vrep.simxSetObjectPosition(clientID, Quadcopter_target_handle, -1, (x,y,1), vrep.simx_opmode_oneshot)
r = float(input("input r: "))
vrep.simxSetObjectOrientation(clientID, Quadcopter_target_handle, -1, (0,0,np.pi*r), vrep.simx_opmode_oneshot)
#"""

""" # Staged Control
#x = 0
r = 0
for i in range(5):
    x = round(random.uniform(-1.0, 1.0), 2)
    y = round(random.uniform(-1.0, 1.0), 2)
    print("x : ", x)
    print("y : ", y)
    #x = float(input("Input x: "))
    #x += 0.1
    errorCode, Quadcopter_target_handle = vrep.simxGetObjectHandle(clientID, 'Quadcopter_target', vrep.simx_opmode_oneshot_wait)
    if(errorCode==vrep.simx_return_ok):
        vrep.simxSetObjectPosition(clientID, Quadcopter_target_handle, -1, (x,y,1), vrep.simx_opmode_oneshot)
        errorCode, prop1_velocity = vrep.simxGetIntegerSignal(clientID, "prop1_velocity", vrep.simx_opmode_streaming)
        errorCode, prop2_velocity = vrep.simxGetIntegerSignal(clientID, "prop2_velocity", vrep.simx_opmode_streaming)
        errorCode, prop3_velocity = vrep.simxGetIntegerSignal(clientID, "prop3_velocity", vrep.simx_opmode_streaming)
        errorCode, prop4_velocity = vrep.simxGetIntegerSignal(clientID, "prop4_velocity", vrep.simx_opmode_streaming)
        print("prop1 v : ", prop1_velocity)
        print("prop2 v : ", prop2_velocity)
        print("prop3 v : ", prop3_velocity)
        print("prop4 v : ", prop4_velocity)
    #errorCode, Quadcopter_base_handle = vrep.simxGetObjectHandle(clientID, 'Quadcopter_base', vrep.simx_opmode_oneshot_wait)
    #errorCode, Quadcopter_propeller_joint_handle = vrep.simxGetObjectHandle(clientID, 'Quadcopter_propeller_joint', vrep.simx_opmode_oneshot_wait)
    
    if i == 4:
        time.sleep(7)
        for v in range(20):
            r += 0.3
            print("r = ", r)
            vrep.simxSetObjectOrientation(clientID, Quadcopter_target_handle, -1, (0,0,np.pi*r), vrep.simx_opmode_oneshot)
            errorCode, prop1_velocity = vrep.simxGetIntegerSignal(clientID, "prop1_velocity", vrep.simx_opmode_streaming)
            errorCode, prop2_velocity = vrep.simxGetIntegerSignal(clientID, "prop2_velocity", vrep.simx_opmode_streaming)
            errorCode, prop3_velocity = vrep.simxGetIntegerSignal(clientID, "prop3_velocity", vrep.simx_opmode_streaming)
            errorCode, prop4_velocity = vrep.simxGetIntegerSignal(clientID, "prop4_velocity", vrep.simx_opmode_streaming)
            print("prop1 v : ", prop1_velocity)
            print("prop2 v : ", prop2_velocity)
            print("prop3 v : ", prop3_velocity)
            print("prop4 v : ", prop4_velocity)
            time.sleep(0.2)
    #vrep.simxyaw
    
    time.sleep(1)
"""