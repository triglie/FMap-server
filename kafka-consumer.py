import os
from kafka import KafkaConsumer
from json import loads

topic = "rds-signal"
group_id = "my-group"
consumer = KafkaConsumer(
     topic,
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id=group_id,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('{} read'.format(message))