from kafka import KafkaProducer

bootstrap_servers = 'localhost:9092'


class SyncKafkaProducer:
    def __init__(self, topic):
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def send(self, message):
        self.producer.send(self.topic, str.encode(f'{message}'))
