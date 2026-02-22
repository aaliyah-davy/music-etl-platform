up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

producer:
	python3 producer/producer.py

consumer:
	python3 consumer/consumer.py

batch:
	python3 batch/load_history.py

transform:
	python3 transform/run_transform.py

help:
	@echo "Available commands:"
	@echo "make up        - start platform"
	@echo "make down      - stop platform"
	@echo "make producer  - run producer"
	@echo "make consumer  - run consumer"
	@echo "make batch     - load batch data"
	@echo "make transform - run transforms"