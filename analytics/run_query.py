import psycopg2
from MusicPlatform.src import logger

logger = get_logger(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="music_dw",
    user="admin",
    password="admin"
)
cursor = conn.cursor()

logger.info("Running analytics script")

with open("sql/song_metrics.sql", "r") as f:
    cursor.execute(f.read())

conn.commit()
logger.info("Analytics finished successfully")
cursor.close()
conn.close()
