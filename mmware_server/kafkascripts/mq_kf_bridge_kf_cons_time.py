from kafka import KafkaConsumer
from json import loads
from datetime import datetime
topic= "kafkasample"
#consumer = KafkaConsumer(topic,bootstrap_servers=['mmwserver:9092'],value_deserializer=lambda x: loads(x.decode('utf-8')[))
consumer = KafkaConsumer(topic,bootstrap_servers=['mmwserver:9092']) 
oldnumber=0;
oldplumber="GOD";
Timedict={}
for message in consumer:
	#print (message.value)
	try:
		try:
			message_dict= loads(message.value)
		except:
			try:
                                message_dict= loads(message.value[7:])
			except:
                                print (message.value[7:])
				print ("message parsing hack failed")
		
		recvtime = datetime.now()
                timestampStr = recvtime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
                print(timestampStr+":"+message_dict["plumber"]+" sent "+str(message_dict["number"])+" at "+message_dict["timestamp"])
                senttime=datetime.strptime(message_dict["timestamp"],"%d-%b-%Y (%H:%M:%S.%f)")
                #print(senttime)
                timediff=recvtime-senttime
                try:
                    Timedict[message_dict["plumber"]][0] = Timedict[message_dict["plumber"]][0]+1
                    Timedict[message_dict["plumber"]][1] = Timedict[message_dict["plumber"]][1]+timediff
                    Timedict[message_dict["plumber"]][2]=Timedict[message_dict["plumber"]][1]/Timedict[message_dict["plumber"]][0]
                except:
                    Timedict[message_dict["plumber"]]=[1,timediff,timediff]
                for key in Timedict:
                    print(key+" "+str(Timedict[key][0]))
                    print(Timedict[key][2])
                    #print(key+":"+ Timedict[key][2].strftime('%M:%S.%f')+'\n')
               #print(Timedict)

		
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
