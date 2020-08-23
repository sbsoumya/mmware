echo Zookeeper...
gnome-terminal --tab -- bash -c "sudo /usr/bin/zookeeper-server-start /etc/kafka/zookeeper.properties;bash"
read n
netstat -ntpul | grep 2181
read n
echo Kafka...
sudo rm /var/lib/kafka/meta.properties
sudo systemctl start confluent-kafka
gnome-terminal --tab -- bash -c "sudo systemctl status confluent-kafka;bash"
read n
netstat -ntpul | grep 9092
read n
echo Schema ... 
sudo systemctl start confluent-schema-registry
gnome-terminal --tab -- bash -c  "sudo systemctl status confluent-schema-registry;bash"
read n
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic kafkasample
read n
kafka-topics --list --zookeeper mmwserver:2181
echo MQTT Connector...
gnome-terminal --tab -- bash -c "connect-distributed /etc/schema-registry/connect-avro-distributed.properties;bash"
echo Enter server name:
read Server
curl -s -X DELETE localhost:8083/connectors/mqtt-source
curl -s -X POST -H 'Content-Type: application/json' http://localhost:8083/connectors -d '{
    "name" : "mqtt-source",
"config" : {
    "connector.class" : "io.confluent.connect.mqtt.MqttSourceConnector",
    "tasks.max" : "1",
    "mqtt.server.uri" : "tcp://piubuntu:1883",
    "mqtt.topics" : "mqttsample",
    "kafka.topic" : "kafkasample",
    "confluent.topic.bootstrap.servers": "localhost:9092",
    "confluent.topic.replication.factor": "1",
    "confluent.license":""
    }
}'
read n
echo ROS2 BRIDGE...
echo Run these commands...
cat ~/mmware_mmwareserver/ros2/ros2scripts/first_pubsub/start_ros2_bridge.sh
read n 
echo ALL DONE!!

