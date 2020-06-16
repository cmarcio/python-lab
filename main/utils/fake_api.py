import time
import asyncio


class FakeApi:
    def __init__(self, request_duration):
        self.request_duration = request_duration

    def send_greeting(self, greeting):
        time.sleep(self.request_duration)
        return 'Hi!'

    async def send_greeting_async(self, greeting):
        await asyncio.sleep(self.request_duration)
        return 'Hi there!'
