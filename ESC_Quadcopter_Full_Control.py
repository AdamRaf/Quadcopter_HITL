# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import serial #serial with arduino for PPM Encoder

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

speed = 700

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)

        sen = line.split(": ")
        ch = sen[0]
        val = int(sen[1])

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

        pi.set_servo_pulsewidth(ESC1, throttle)
        pi.set_servo_pulsewidth(ESC2, throttle)
        pi.set_servo_pulsewidth(ESC3, throttle)
        pi.set_servo_pulsewidth(ESC4, throttle)
        print("throttle = %d" % throttle)

        if yaw != 0:
            if yaw > 0 :
                pi.set_servo_pulsewidth(ESC1, speed - yaw) #CW
                pi.set_servo_pulsewidth(ESC2, speed + yaw) #CCW
                pi.set_servo_pulsewidth(ESC3, speed - yaw) #CW
                pi.set_servo_pulsewidth(ESC4, speed + yaw) #CCW
            if yaw < 0 :
                pi.set_servo_pulsewidth(ESC1, speed + yaw) #CW
                pi.set_servo_pulsewidth(ESC2, speed - yaw) #CCW
                pi.set_servo_pulsewidth(ESC3, speed + yaw) #CW
                pi.set_servo_pulsewidth(ESC4, speed - yaw) #CCW
            print("yaw = %d" % yaw)

        if roll != 0:    
            if roll > 0 :
                pi.set_servo_pulsewidth(ESC1, speed + roll) #CW
                pi.set_servo_pulsewidth(ESC2, speed + roll) #CCW
                pi.set_servo_pulsewidth(ESC3, speed - roll) #CW
                pi.set_servo_pulsewidth(ESC4, speed - roll) #CCW
            if roll < 0 :
                pi.set_servo_pulsewidth(ESC1, speed - roll) #CW
                pi.set_servo_pulsewidth(ESC2, speed - roll) #CCW
                pi.set_servo_pulsewidth(ESC3, speed + roll) #CW
                pi.set_servo_pulsewidth(ESC4, speed + roll) #CCW
            print("roll = %d" % roll)

        if pitch != 0:    
            if pitch > 0 :
                pi.set_servo_pulsewidth(ESC1, speed + pitch) #CW
                pi.set_servo_pulsewidth(ESC2, speed - pitch) #CCW
                pi.set_servo_pulsewidth(ESC3, speed - pitch) #CW
                pi.set_servo_pulsewidth(ESC4, speed + pitch) #CCW
            if pitch < 0 :
                pi.set_servo_pulsewidth(ESC1, speed - pitch) #CW
                pi.set_servo_pulsewidth(ESC2, speed + pitch) #CCW
                pi.set_servo_pulsewidth(ESC3, speed + pitch) #CW
                pi.set_servo_pulsewidth(ESC4, speed - pitch) #CCW
            print("pitch = %d" % pitch)