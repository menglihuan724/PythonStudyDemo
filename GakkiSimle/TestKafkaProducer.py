from kafka import KafkaProducer
import json
import logging
logging.basicConfig(level = logging.DEBUG)
#timeout=60
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(10):
    feature=producer.send('foobar', b'some_message_bytes')