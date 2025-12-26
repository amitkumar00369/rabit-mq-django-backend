# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from rabbit.producer import public_message

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.group_name = f"user_{self.user_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        public_message({
            "sender_id": data["sender_id"],
            "receiver_id": data["receiver_id"],
            "message": data["message"]
        })

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event["data"]))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
