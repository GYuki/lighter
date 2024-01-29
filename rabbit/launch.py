import os

import pika
from rabbit.publisher.service import RabbitPublisherService
from rabbit.service import PikaService


def start_rabbit(application):
    ps = PikaService(
        pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST", "127.0.0.1"),
            port=os.getenv("RABBITMQ_PORT", 5672),
            virtual_host="/",
            credentials=pika.PlainCredentials(os.getenv("RABBITMQ_USER", "adm"), os.getenv("RABBITMQ_PASS", "1"))
        )
    )

    ps.setServiceParent(application)
    ps.startService()

    rps = RabbitPublisherService()
    rps.setServiceParent(application)
    rps.startService()
    return rps
