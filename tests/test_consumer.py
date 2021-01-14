from unittest import TestCase, IsolatedAsyncioTestCase
# from unittest.mock import MagicMock, AsyncMock


class TestConsumerSync(TestCase):
    def test(self):
        self.assertTrue(True)


class TestConsumerAsync(IsolatedAsyncioTestCase):
    async def test(self):
        self.assertTrue(True)
