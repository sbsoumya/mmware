from kafka import KafkaProducer
from time import sleep
from json import dumps
import socket
import random
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['mmwserver:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
Plumber=socket.gethostname()
print ("Producer: "+Plumber+"-Kafka")              
for number in range(1000):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    data = {'number' : random.randint(1,101), 'plumber' : Plumber+"-Kafka", 'timestamp' : timestampStr}
    producer.send('kafkasample', value=data)
    print(data)
    sleep(5)
"""
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('sample', 'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
"""
