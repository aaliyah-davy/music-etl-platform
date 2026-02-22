import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="music_dw",
    user="admin",
    password="admin"
)

cursor = conn.cursor()

with open("transform/run_transform.sql") as f:
    cursor.execute(f.read())

conn.commit()
conn.close()

print("Transformation complete")