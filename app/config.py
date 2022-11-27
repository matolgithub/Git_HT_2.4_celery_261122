from os import getenv
from kombu import Queue, Exchange
from dotenv import load_dotenv


load_dotenv()

task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
)

backend_redis = getenv('BACKEND_REDIS')
broker_redis = getenv('BROKER_REDIS')
