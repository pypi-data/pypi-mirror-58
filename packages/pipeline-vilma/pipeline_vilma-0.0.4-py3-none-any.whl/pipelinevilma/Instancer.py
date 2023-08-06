import datetime
import json
import pymongo
import time
from loguru import logger
from pipelinevilma.Messager import Messager


class Instancer:
    def __init__(self, number_of_providers, queue_server, input_queue, output_queue):
        self.number_of_providers = number_of_providers
        self.input_queue = input_queue
        self.input_queues = []
        for i in range(number_of_providers):
            self.input_queues.append(Messager(queue_server, input_queue + str(i+1)))
        self.delivery = Messager(queue_server, output_queue)

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""

    def run(self):
        raise NotImplementedError("Should have implemented this")

    def create_custom_instance(self):
        raise NotImplementedError("Should have implemented this")

    def create_instance_by_time_window(self, sensor_id, time_window_s):
        MAX_RETRIES = 10
        messages = []

        body = False
        retries = 0
        while not body and retries < MAX_RETRIES:
            retries += 1
            body = self.input_queues[sensor_id-1].get_message(self.input_queue + str(sensor_id))
            logger.debug(f"[{retries}] Getting the first message...")

        if retries == 0:
            print(f"Did not get the first message after retries")
            return False

        message = json.loads(body)
        time_window_begin = message['createdAt']
        logger.info(f"Got the first message! Time window begins at {time_window_begin}")
        logger.info(f"Aggregating the messages in the next {time_window_s}s")

        actual_time = time_window_begin
        limit_time = time_window_begin + time_window_s
        while actual_time < limit_time:
            body = self.input_queues[sensor_id-1].get_message(self.input_queue + str(sensor_id))
            if body:
                message = json.loads(body)
                messages.append(message)
                actual_time = message['createdAt']

        return messages

    def create_instance_by_repetition(self, sensor_id, number_of_messages):
        messages = []
        for i in range(number_of_messages):
            messages.append(self.input_queues[sensor_id-1].get_message(self.input_queue + str(sensor_id)))

        return messages

    def sync_providers_last_messages(self):
        messages = []
        for i in range(self.number_of_providers):
            message = False
            while not message:
                message = self.input_queues[i].get_message(self.input_queue + str(i+1))
            messages.append(message)

    def forward(self, message):
        self.delivery.publish(message)
