import asyncio
import json
import os

from gcloud.aio.pubsub import SubscriberClient
from gcloud.aio.pubsub import subscribe


project_id = os.getenv('PUBSUB_PROJECT_ID')

subscriber_client = SubscriberClient()
subscription = subscriber_client.subscription_path(project_id, 'organizations-users')


async def callback(message):
    type = message.attributes['type']
    data = json.loads(message.data)

    if type == 'suspend':
        print(f'\nRemove user from organizations: {data["user_id"]}')


async def run():
    await subscribe(
        subscription,
        callback,
        subscriber_client
    )

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(run())
except KeyboardInterrupt:
    loop.close()