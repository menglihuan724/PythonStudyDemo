from kafka import KafkaProducer,KafkaConsumer
import json
import logging
logging.basicConfig(level = logging.DEBUG)
consumer = KafkaConsumer('test', group_id="test",bootstrap_servers='192.168.0.106:9092')
while(True):
    print(consumer.poll().items())