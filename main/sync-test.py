from kafka_adapters.sync_kafka_consumer import SyncKafkaConsumer
from kafka_adapters.sync_kafka_producer import SyncKafkaProducer
from utils.fake_api import FakeApi
from utils.profile import profile


default_topic = 'TestTopic'
default_group = 'TestGroup'
default_message = 'Hello'


def get_message_handler(fake_api):
    def message_handler(message):
        greeting = message.value
        print(greeting)
        response = fake_api.send_greeting(greeting)
        print(response)
    return message_handler


def produce_messages(limit):
    print('connecting to producer')
    producer = SyncKafkaProducer(default_topic)
    print('producing messages')
    for _ in range(limit):
        producer.send(default_message)
    print('finished')


def consume(handler, limit):
    print('connecting consumer')
    consumer = SyncKafkaConsumer(default_topic, group=default_group)
    print('starting consumer')
    consumer.start(handler, limit)
    print('finished')


@profile
def main():
    limit = 10
    request_duration = 1

    fake_api = FakeApi(request_duration)
    handler = get_message_handler(fake_api)

    produce_messages(limit)
    consume(handler, limit)


main()
