from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('sample',bootstrap_servers=['mmwserver:9092'],value_deserializer=lambda x: loads(x.decode('utf-8')))
oldnumber=0;
oldplumber="GOD";

for message in consumer:
	try:
		message_dict= message.value
		print (message_dict["plumber"]+" counts "+ str(message_dict["number"]))
		if oldnumber>message_dict["number"]:
			
			winner = oldplumber
		else:
			winner= message_dict["plumber"]
		
		oldnumber=message_dict["number"]
		oldplumber=message_dict["plumber"]
		
		print (oldplumber+" wins!!")
		
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
