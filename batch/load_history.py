import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/spotify_churn_dataset.csv")

engine = create_engine(
    "postgresql+psycopg2://admin:admin@localhost:5432/music_dw"
)

df.to_sql(
    "historical_plays",
    engine,
    if_exists="append",
    index=False
)

print("Batch load complete")