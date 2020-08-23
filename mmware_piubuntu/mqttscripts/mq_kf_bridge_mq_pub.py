import paho.mqtt.client as mqtt #import the client1
from time import sleep
from json import dumps
import socket
import random
from datetime import datetime

broker_address="piubuntu" 
topic = "mqttsample"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Publishing message to topic",topic)	

Plumber=socket.gethostname()
Plumber=Plumber+"mqtt"
print ("MQTT Publisher: "+Plumber)              
for number in range(1000):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    data = {'number' : random.randint(1,101), 'plumber' : Plumber, 'timestamp' : timestampStr}
    message=dumps(data)
    print(message)
    client.publish(topic,message)
    sleep(5)
