# consumer.py

import os
import django
import pika
import json
from dotenv import load_dotenv
load_dotenv()

# ✅ Django bootstrap
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbitMq_django.settings')
django.setup()

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

def callback(ch, method, properties, body):
    data = json.loads(body.decode())

    receiver_group = f"user_{data['receiver_id']}"

    async_to_sync(channel_layer.group_send)(
        receiver_group,
        {
            "type": "chat_message",
            "data": data
        }
    )

params = pika.URLParameters(os.getenv("RABIT_URL"))
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=os.getenv("QUEUE_NAME"),durable=True)
channel.basic_consume(
    queue=os.getenv("QUEUE_NAME"),
    on_message_callback=callback,
    auto_ack=True
)

print("RabbitMQ consumer started")
channel.start_consuming()
