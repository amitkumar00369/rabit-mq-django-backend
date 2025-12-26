import pika
from dotenv import load_dotenv
load_dotenv()
import os
import json


def public_message(payload):
    params = pika.URLParameters(os.getenv("RABIT_URL"))
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=os.getenv("QUEUE_NAME"), durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=os.getenv("QUEUE_NAME"),
        body=json.dumps(payload),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()