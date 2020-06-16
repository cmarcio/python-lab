from kafka_adapters.async_kafka_consumer import AsyncKafkaConsumer
from kafka_adapters.async_kafka_producer import AsyncKafkaProducer
from utils.fake_api import FakeApi
from utils.profile import profile_async
import asyncio

default_topic = 'TestTopic'
default_group = 'TestGroup'
default_message = 'Hello'


def get_message_handler(fake_api):
    async def message_handler(message):
        greeting = message.value
        print(greeting)
        response = await fake_api.send_greeting_async(greeting)
        print(response)
    return message_handler


async def produce_messages(limit):
    producer = AsyncKafkaProducer(default_topic)
    print('producing messages')
    await producer.send_many([default_message for _ in range(limit)])
    print('finished')


async def consume_messages(handler, limit):
    consumer = AsyncKafkaConsumer(default_topic, group=default_group)
    print('starting consumer')
    await consumer.start(handler, limit)
    print('finished')


@profile_async
async def main():
    limit = 100000
    request_duration = 1

    fake_api = FakeApi(request_duration)
    handler = get_message_handler(fake_api)

    await produce_messages(limit)
    await consume_messages(handler, limit)

asyncio.run(main())
