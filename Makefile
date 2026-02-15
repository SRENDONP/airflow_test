.PHONY: help setup start stop restart logs test clean

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: ## Set up the local development environment
	@bash setup.sh

start: ## Start Airflow using Docker Compose
	@echo "Starting Airflow..."
	@docker-compose up -d
	@echo "Airflow is starting. Access it at http://localhost:8080"
	@echo "Username: airflow, Password: airflow"

stop: ## Stop Airflow services
	@echo "Stopping Airflow..."
	@docker-compose down

restart: stop start ## Restart Airflow services

logs: ## View Airflow logs
	@docker-compose logs -f

logs-scheduler: ## View scheduler logs
	@docker-compose logs -f airflow-scheduler

logs-webserver: ## View webserver logs
	@docker-compose logs -f airflow-webserver

test: ## Run DAG tests
	@echo "Running DAG tests..."
	@python3 tests/test_dags.py

clean: ## Clean up temporary files and stop services
	@echo "Cleaning up..."
	@docker-compose down -v
	@rm -rf logs/* __pycache__ dags/__pycache__ tests/__pycache__
	@rm -f airflow.db airflow.cfg airflow-webserver.pid
	@echo "Clean complete!"

list-dags: ## List all DAGs (requires Airflow to be running)
	@docker-compose exec airflow-webserver airflow dags list

trigger-dag: ## Trigger a DAG (usage: make trigger-dag DAG_ID=hello_world)
	@docker-compose exec airflow-webserver airflow dags trigger $(DAG_ID)
