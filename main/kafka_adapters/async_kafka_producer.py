from contextlib import asynccontextmanager
from aiokafka import AIOKafkaProducer
import asyncio

bootstrap_servers = 'localhost:9092'


@asynccontextmanager
async def get_producer():
    producer = AIOKafkaProducer(bootstrap_servers=bootstrap_servers)
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()


class AsyncKafkaProducer:
    def __init__(self, topic):
        self.topic = topic

    async def send(self, message):
        async with get_producer() as producer:
            await producer.send_and_wait(self.topic, f'{message}')

    async def send_many(self, messages):
        futures = []
        async with get_producer() as producer:
            for message in messages:
                f = await producer.send(self.topic, str.encode(f'{message}'))
                futures.append(f)
            await asyncio.gather(*futures)
