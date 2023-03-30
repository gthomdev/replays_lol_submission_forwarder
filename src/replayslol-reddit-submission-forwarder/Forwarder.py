import json
import pika
from Submission import Submission
from Helpers import load_config


def on_message(channel, method, properties, body):
    try:
        json_body = json.loads(body)
        submission = Submission.from_json(json_body)
        print(f"Received message: {submission}")
    except json.JSONDecodeError as e:
        print(f"Error decoding message: {e}")
    finally:
        channel.basic_ack(delivery_tag=method.delivery_tag)


class Forwarder:
    def __init__(self, config):
        self.queue_name = config["queue"]["name"]
        self.queue_host = config["queue"]["host"]

    def watch_queue(self):
        connection_parameters = pika.ConnectionParameters(host=self.queue_host)
        try:
            connection = pika.BlockingConnection(connection_parameters)
            channel = connection.channel()
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue=self.queue_name, on_message_callback=on_message)
            print(f"Watching queue: {self.queue_name} on host: {self.queue_host}")
            channel.start_consuming()
        except Exception as e:
            print(f"Error connecting to queue: {e}")


if __name__ == "__main__":
    config = load_config("config.yaml")
    forwarder = Forwarder(config)
    forwarder.watch_queue()
