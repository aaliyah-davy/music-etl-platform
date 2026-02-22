from kafka import KafkaConsumer
import json
import psycopg2
from datetime import datetime
from logger import get_logger

# Connecting to Postgres
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="music_dw",
    user="admin",
    password="admin"
)

cursor = conn.cursor()

# Creating Kafka consumer
consumer = KafkaConsumer(
    "music_stream",
    bootstrap_servers="localhost:9092",
    group_id="music-consumer",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print("Consumer started...")

for message in consumer:
    event = message.value

    cursor.execute(
        """
        INSERT INTO music_events
        (user_id, artist, song, genre, duration_sec, event_time)
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            event["user_id"],
            event["artist"],
            event["song"],
            event["genre"],
            event["duration_sec"],
            datetime.fromtimestamp(event["timestamp"])
        )
    )

    conn.commit()

    logger = get_logger("consumer")
    logger.info("Inserted into Postgres")

    print("Inserted:", event)