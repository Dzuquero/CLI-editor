run:
	docker compose up --build

test:
	docker compose run vector-cli pytest
