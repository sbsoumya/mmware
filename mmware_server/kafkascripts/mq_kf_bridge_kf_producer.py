from kafka import KafkaProducer
from time import sleep
from json import dumps
from datetime import datetime
import socket
import random

producer = KafkaProducer(bootstrap_servers=['mmwserver:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
Plumber=socket.gethostname()
print ("Producer: "+Plumber+"-Kafka")              
for number in range(10000):
    dateTimeObj = datetime.now()
    data = {'number' : random.randint(1,101), 'plumber' : Plumber+"-Kafka", 'timestamp' :dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")}
    producer.send('kafkasample', value=data)
    print(data)
    sleep(5)
"""
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('sample', 'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
"""
