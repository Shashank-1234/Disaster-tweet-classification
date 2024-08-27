from kafka import KafkaConsumer

# Create a Kafka consumer
consumer = KafkaConsumer(
    'disaster-response',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

# Consume messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
