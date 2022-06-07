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

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqtt.Client.connected_flag = False

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("PC")      #create new instance
client.on_connect = on_connect      #bind callback
print("Connecting to broker ", mqttBroker)
try:
    client.connect(mqttBroker)
except:
    print("can't connect")
    sys.exit(1)

while True:
    client.loop_start()
    while not client.connected_flag:
        print("connection wait loop")
        time.sleep(1)
    #print("main loop")
    '''
    feedback = uniform(0, 10)
    client.publish("feedback", feedback)
    print("Just published " + str(feedback) + " to topic feedback")
    '''
    time.sleep(0.1)

    client.subscribe("kontrol")
    client.on_message=on_message

    time.sleep(0.1)

    client.loop_stop()
#'''