from kafka import KafkaConsumer
import json
import time

KAFKA_TOPIC = 'KafkaEvents'
BOOTSTRAP_SERVERS = 'kafka:9092'
CONSUMER_GROUP = 'kafka-group'


class KafkaConsumerSync:
    def __init__(self):
        self.consumer = KafkaConsumer(
            KAFKA_TOPIC,
            group_id=CONSUMER_GROUP,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_deserializer=json.loads)

    def test(self, n, avg_time):
        started = []
        finished = []
        for (message, i) in zip(self.consumer, range(n)):
            started.append(time.time())
            self._fake_handler(message, avg_time)
            finished.append(time.time())
            if i == n - 1:
                break
        print(f'consumer ellapsed time for {n} messages:\
            {max(finished) - min(started)}s')

    def _fake_handler(self, message, avg_time):
        time.sleep(avg_time)
