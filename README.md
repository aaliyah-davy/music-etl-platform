# music-etl-platform
End-to-end streaming + batch music data pipeline with PostgreSQL, Kafka, and Python


**Features**
1.	Streaming ingestion \
  	•	Kafka producer simulates real-time music events.\
  	•	Kafka consumer writes streaming data to music_events table in Postgres.
2.	Batch ingestion\
  	•	Load historical CSVs into Postgres.\
  	•	Handles appending without overwriting existing data.
3.	Data transformation\
	  •	Python scripts clean and transform raw data for analysis.
4.	Analytics\
  	•	Aggregates data into analytics.song_metrics table.\
  	•	Computes song play counts and average duration.
5.	Logging\
  	•	Centralized logging via logger.py.\
  	•	All scripts write to logs/pipeline.log.
6.	End-to-end execution\
	  •	Run the full pipeline with a single command via pipeline.py or Makefile.



**Tech Stack**
	•	Database: PostgreSQL 17\
	•	Message broker: Apache Kafka 3.7.0 (KRaft mode, no Zookeeper)\
	•	Language: Python 3.11\
	•	Data manipulation: pandas\
	•	Logging: Python logging module\
	•	Containerization: Docker + Docker Compose\
	•	Batch/analytics: SQL scripts for Postgres
