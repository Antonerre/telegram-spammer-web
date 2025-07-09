import asyncio
import random
from telethon import TelegramClient

class TelegramSpammer:
    def __init__(self, api_id, api_hash, phone_number, chat, delay, messages):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.chat = chat
        self.delay = delay
        self.messages = messages
        self.running = False
        self.client = TelegramClient("web_session", api_id, api_hash)

    async def start(self):
        await self.client.start(self.phone_number)
        self.running = True
        while self.running:
            message = random.choice(self.messages)
            try:
                await self.client.send_message(self.chat, message)
                print(f"✅ Отправлено: {message}")
            except Exception as e:
                print(f"❌ Ошибка: {e}")
            await asyncio.sleep(self.delay)

    def stop(self):
        self.running = False
