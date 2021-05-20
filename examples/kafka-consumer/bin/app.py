import os
from kafka import KafkaConsumer
from json import loads

topic = os.getenv("KAFKA_TOPIC", "rds-signal")
group_id = os.getenv("GROUP_ID", "rds-testing-group")
consumer = KafkaConsumer(
     topic,
     bootstrap_servers=['kafkaserver:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id=group_id,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
     message = message.value
     print('New message' + ('-') * 50)
     print(f"{message['province']} ({message['coords']}): {message['FM']} (RSSI: {message['RSSI']}) \n")