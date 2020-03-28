from kafka import KafkaProducer
import json
import time

KAFKA_TOPIC = 'KafkaEvents'
BOOTSTRAP_SERVERS = 'kafka:9092'


class KafkaProducerSync:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def test(self, n):
        started = []
        finished = []
        message = {'hello': 'world'}
        for i in range(n):
            started.append(time.time())
            self.producer.send(KAFKA_TOPIC, message)
            finished.append(time.time())
        print(f'producer ellapsed time for {n} messages:\
            {max(finished) - min(started)}s')
