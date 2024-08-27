from kafka import KafkaProducer

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send messages
for i in range(10):
    producer.send('disaster-response', value=b'This is message ' + bytes(str(i), 'utf-8'))
    print(f'Sent message {i}')

# Flush and close
producer.flush()
producer.close()
