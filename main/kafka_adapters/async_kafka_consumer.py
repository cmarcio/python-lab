from contextlib import asynccontextmanager
from aiokafka import AIOKafkaConsumer
import asyncio

bootstrap_servers = 'localhost:9092'


@asynccontextmanager
async def get_consumer(topic, group_id):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id=group_id)
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        yield consumer
    finally:
        await consumer.stop()


class AsyncKafkaConsumer:
    def __init__(self, topic, group):
        self.topic = topic
        self.group = group

    async def start(self, handler, limit=None):
        async with get_consumer(self.topic, self.group) as consumer:
            counter = 0
            async for msg in consumer:
                counter += 1
                if counter == limit:
                    break
                asyncio.create_task(handler(msg), name='handlertask')
            await self.batch_pending()

    async def batch_pending(self):
        loop = asyncio.get_running_loop()
        pending = asyncio.all_tasks(loop=loop)
        pending_handlers = [task for task in pending
                            if task.get_name() == 'handlertask']
        await asyncio.gather(*pending_handlers)
