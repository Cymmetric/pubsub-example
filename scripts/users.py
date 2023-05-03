import asyncio
import json
import os

from gcloud.aio.pubsub import PubsubMessage
from gcloud.aio.pubsub import PublisherClient


async def publish():
    client = PublisherClient()
    project_id = os.getenv('PUBSUB_PROJECT_ID')

    topic = client.topic_path(project_id, 'users')

    data = json.dumps({
        "user_id": 12345
    }).encode("utf-8")

    # PubsubMessage(data, attributes)
    message = [
        PubsubMessage(bytes(data), type="suspend")
    ]

    await client.publish(topic, message)

    await client.close()

asyncio.run(publish())