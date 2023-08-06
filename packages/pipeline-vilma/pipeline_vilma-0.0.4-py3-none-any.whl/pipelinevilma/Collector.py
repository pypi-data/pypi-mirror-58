import json
import pymongo
import datetime
from loguru import logger
from pipelinevilma.Messager import Messager


class Collector:
    def __init__(self,  bypass, queue_server, queue_input, queue_output, database_options):
        self.bypass = bypass
        self.receiver = Messager(queue_server, queue_input)
        self.delivery = Messager(queue_server, queue_output)

        client = pymongo.MongoClient(database_options['url'])
        db = client[database_options['name']]
        self.database_collection = db[database_options['collections']['collector']]

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def run(self):
        self.receive(self.on_new_message)

    def persist(self, message):
        message['createdAt'] = datetime.datetime.utcnow()
        self.database_collection.insert_one(message)

    def on_new_message(self, ch, method, properties, body):
        # Callback function
        logger.info("Message received!")
        message = json.loads(body)

        if ch.is_open:
            ch.basic_ack(method.delivery_tag)
            if(not self.bypass):
                logger.info("Persisting image on the database...")
                self.persist(message)
                logger.info("Done!")
            logger.info("Forwarding the message to the next component...")
            self.forward(body)
            logger.info("Done!")

    def receive(self, callback):
        self.receiver.consume(callback)

    def forward(self, message):
        self.delivery.publish(message)
