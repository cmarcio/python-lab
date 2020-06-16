from kafka import KafkaConsumer

bootstrap_servers = 'localhost:9092'


class SyncKafkaConsumer:
    def __init__(self, topic, group):
        self.consumer = KafkaConsumer(
            topic,
            group_id=group,
            bootstrap_servers=bootstrap_servers)

    def start(self, handler, limit=None):
        if limit:
            for (_, message) in zip(range(limit), self.consumer):
                handler(message)

        else:
            for message in self.consumer:
                handler(message)
