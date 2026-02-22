from kafka import KafkaProducer
from faker import Faker
import json
import time
import random
from logger import get_logger

fake = Faker()

# Creating Kafka producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def generate_music_event():
    return {
        "user_id": fake.uuid4(),
        "artist": fake.name(),
        "song": fake.word(),
        "genre": random.choice(["Pop", "Rock", "Hip-Hop", "Jazz", "Electronic", \
                                "Metal", "Punk", "Folk", "Country", "Blues", "Soul", "R&B", \
                                 "Funk", "Classical", "Reggae", "Ambient", "Latin", "Disco", \
                                "Techno", "House", "Indie", "Alternative", "Grunge", "Ska"]),
        "duration_sec": random.randint(30, 300),
        "timestamp": time.time()
    }

while True:
    event = generate_music_event()

    producer.send(
        "music_stream",
        value=event
    )

    print("Sent:", event)

    logger = get_logger("producer")
    logger.info("Message sent")

    time.sleep(2)