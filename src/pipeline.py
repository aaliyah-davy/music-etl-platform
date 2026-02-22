from logger import get_logger
import subprocess

logger = get_logger(__name__)

logger.info("Starting pipeline")

subprocess.run(["python", "producer/producer.py"])
logger.info("Producer finished")

subprocess.run(["python", "consumer/consumer.py"])
logger.info("Consumer finished")

subprocess.run(["python", "transform/run_transform.py"])
logger.info("Transform finished")

logger.info("Pipeline completed")