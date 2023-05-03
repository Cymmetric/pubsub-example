import asyncio
import os

from gcloud.aio.pubsub import PublisherClient, SubscriberClient


async def setup():
    publisher = PublisherClient()
    subscriber = SubscriberClient()

    project_id = os.getenv('PUBSUB_PROJECT_ID')

    print("Creating topic: users")
    topic = publisher.topic_path(project_id, 'users')
    await publisher.create_topic(topic)

    print("\nCreating Subscription: organizations-users")
    subscription = subscriber.subscription_path(project_id, 'organizations-users')
    await subscriber.create_subscription(subscription, topic)

    print("\nCreating Subscription: search-users")
    subscription = subscriber.subscription_path(project_id, 'search-users')
    await subscriber.create_subscription(subscription, topic)

    await publisher.close()
    await subscriber.close()

asyncio.run(setup())