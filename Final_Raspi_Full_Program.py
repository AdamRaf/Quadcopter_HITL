# This single ESC Driver program is made by AGT @instructable.com.

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import serial #serial with arduino for PPM Encoder

import paho.mqtt.client as mqtt
import sys

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("Successfully connected")
    else:
        print("Bad connection, returned code: ", rc)

def on_message(clent, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))

ESC1 = 4  #GPIO4  Connect the ESC in this GPIO pin
ESC2 = 16 #GPIO16
ESC3 = 18 #GPIO18
ESC4 = 12 #GPIO12

pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)
pi.set_servo_pulsewidth(ESC4, 0)

ch1 = 1110 #Yaw
ch2 = 1090 #Pitch
ch3 = 600  #Throttle
ch4 = 1090 #Roll

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

mqtt.Client.connected_flag = False

mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client("raspi")
client.on_connect = on_connect  #bind callback
print("connecting to broker ", mqttBroker)
try:
    client.connect(mqttBroker)
except:
    print("can't connect")
    sys.exit(1)

while True:
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        
            sen = line.split(": ")
            ch = sen[0]
            val = int(sen[1])
        except (IndexError, UnicodeDecodeError, ValueError):
            continue

        if ch == "CH1":
            ch1 = val
        elif ch == "CH2":
            ch2 = val
        elif ch == "CH3":
            ch3 = val
        elif ch == "CH4":
            ch4 = val
        
        throttle = ch3
        yaw = ch1 - 1110
        roll = ch4 - 1090
        pitch = ch2 - 1090
        
        motor1 = throttle - yaw + roll + pitch #CW
        motor2 = throttle + yaw + roll - pitch #CCW
        motor3 = throttle - yaw - roll - pitch #CW
        motor4 = throttle + yaw - roll + pitch #CCW
        
        if motor1 > 2400:
            motor1 = 2400
        if motor1 < 500:
            motor1 = 500
            
        if motor2 > 2400:
            motor2 = 2400
        if motor2 < 500:
            motor2 = 500
            
        if motor3 > 2400:
            motor3 = 2400
        if motor3 < 500:
            motor3 = 500
            
        if motor4 > 2400:
            motor4 = 2400
        if motor4 < 500:
            motor4 = 500
        
        pi.set_servo_pulsewidth(ESC1, motor1)
        pi.set_servo_pulsewidth(ESC2, motor2)
        pi.set_servo_pulsewidth(ESC3, motor3)
        pi.set_servo_pulsewidth(ESC4, motor4)
        print("speed1 = %d" % motor1)
        print("speed2 = %d" % motor2)
        print("speed3 = %d" % motor3)
        print("speed4 = %d" % motor4)
        
        #client.loop_start()
        data = str(motor1) + " " + str(motor2) + " " + str(motor3) + " " + str(motor4)
        client.publish("kontrol", data)
        print("Just published " + str(data) + " to topic kontrol")
        
        #time.sleep(0.2) #time.sleep() becomes a big delay problem for MQTT protocol
        '''
        client.subscribe("feedback")
        client.on_message = on_message
        '''
        #time.sleep(0.2)
        #client.loop_stop()

'''
import paho.mqtt.client as mqtt
import time
import sys
from random import randrange, uniform

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("Successfully connected")
    else:
        print("Bad connection, returned code: ", rc)

def on_message(clent, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))
 
mqtt.Client.connected_flag = False

mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client("raspi")
client.on_connect = on_connect  #bind callback
print("connecting to broker ", mqttBroker)
try:
    client.connect(mqttBroker)
except:
    print("can't connect")
    sys.exit(1)

while True:
    client.loop_start()
    rand = uniform(20, 21)
    client.publish("kontrol", rand)
    print("Just published " + str(rand) + " to topic kontrol")
    
    time.sleep(0.1)
    
    client.subscribe("feedback")
    client.on_message = on_message
    
    time.sleep(0.1)
    client.loop_stop()
'''