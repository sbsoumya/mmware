from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient

topic= "kafkasample"

#consumer = KafkaConsumer(topic,bootstrap_servers=['mmwserver:9092'],value_deserializer=lambda x: loads(x.decode('utf-8')[))
consumer = KafkaConsumer(topic,bootstrap_servers=['mmwserver:9092']) 
oldnumber=0;
oldplumber="GOD";

client = MongoClient('mmwserver:27017')
collection = client.sample.kafkasample
for message in consumer:
	try:
		
		try:
			message_dict= loads(message.value)
		except:
			try:
				#print (message.value[6:])
				message_dict= loads(message.value[6:])
			except:
				#print (message.value[6:])
				print ("message parsing hack failed")
		
		print (message_dict["plumber"]+" counts "+ str(message_dict["number"]))
		
		collection.insert_one(message_dict)
		print('{} added to {}'.format(message, collection))
		if oldnumber>message_dict["number"]:
			
			winner = oldplumber
		else:
			winner= message_dict["plumber"]
		
		oldnumber=message_dict["number"]
		oldplumber=message_dict["plumber"]
		
		print (winner+" wins!!")
		
	except:
		print ("message not in format")

"""consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
     """
