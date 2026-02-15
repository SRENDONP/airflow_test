# Airflow Test Project

A learning and testing project for Apache Airflow, featuring example DAGs and best practices.

## 📋 Overview

This project provides a practical environment to learn and test Apache Airflow concepts. It includes:

- Multiple example DAGs demonstrating common patterns
- Docker-based setup for easy deployment
- Test suite for validating DAG integrity
- Production-ready project structure

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Python 3.8+ (for local development)
- Make (optional, for using Makefile commands)

### Using Docker (Recommended)

**Option 1: Using Makefile (simplest)**
```bash
# Start Airflow
make start

# View logs
make logs

# Stop Airflow
make stop

# See all available commands
make help
```

**Option 2: Using Docker Compose directly**

1. **Start Airflow services:**
   ```bash
   docker-compose up -d
   ```

2. **Access the Airflow UI:**
   - Open your browser to http://localhost:8080
   - Login with:
     - Username: `airflow`
     - Password: `airflow`

3. **Stop Airflow services:**
   ```bash
   docker-compose down
   ```

### Local Development Setup

**Using the setup script:**
```bash
bash setup.sh
```

**Or manually:**

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize Airflow database:**
   ```bash
   export AIRFLOW_HOME=$(pwd)
   airflow db init
   ```

4. **Create an admin user:**
   ```bash
   airflow users create \
       --username admin \
       --firstname Admin \
       --lastname User \
       --role Admin \
       --email admin@example.com \
       --password admin
   ```

5. **Start Airflow:**
   ```bash
   # Terminal 1: Start the webserver
   airflow webserver --port 8080

   # Terminal 2: Start the scheduler
   airflow scheduler
   ```

## 📚 Example DAGs

### 1. Hello World DAG (`hello_world_dag.py`)
A simple introduction to Airflow with BashOperator and PythonOperator.

**Key concepts:**
- Basic DAG definition
- BashOperator and PythonOperator
- Linear task dependencies

### 2. Task Dependencies DAG (`task_dependencies_dag.py`)
Demonstrates different patterns for setting task dependencies.

**Key concepts:**
- Parallel task execution
- Branching and joining workflows
- Multiple dependency patterns

### 3. ETL Pipeline DAG (`etl_pipeline_dag.py`)
A complete ETL (Extract, Transform, Load) pipeline example.

**Key concepts:**
- XCom for passing data between tasks
- ETL pattern implementation
- Data validation

## 🧪 Testing

Run the test suite to validate all DAGs:

```bash
# Make sure Airflow is installed
pip install apache-airflow

# Run tests
python tests/test_dags.py
```

Or use pytest:
```bash
pip install pytest
pytest tests/
```

## 📁 Project Structure

```
airflow_test/
├── dags/                          # DAG files
│   ├── hello_world_dag.py         # Simple hello world example
│   ├── task_dependencies_dag.py   # Task dependency patterns
│   └── etl_pipeline_dag.py        # ETL pipeline example
├── plugins/                       # Custom Airflow plugins
├── logs/                          # Airflow logs (gitignored)
├── tests/                         # Test files
│   └── test_dags.py              # DAG integrity tests
├── docker-compose.yml             # Docker Compose configuration
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## 🎓 Learning Resources

- [Official Airflow Documentation](https://airflow.apache.org/docs/)
- [Airflow Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
- [DAG Writing Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#writing-a-dag)

## 🔧 Configuration

### Environment Variables

You can customize the Docker setup by creating a `.env` file:

```env
AIRFLOW_UID=50000
_AIRFLOW_WWW_USER_USERNAME=admin
_AIRFLOW_WWW_USER_PASSWORD=admin123
```

### Airflow Configuration

For production use, customize the Airflow configuration:
- Edit `docker-compose.yml` to adjust environment variables
- Mount a custom `airflow.cfg` for advanced configuration

## 🛠️ Common Commands

```bash
# List all DAGs
docker-compose exec airflow-webserver airflow dags list

# Test a specific DAG
docker-compose exec airflow-webserver airflow dags test <dag_id> <execution_date>

# Trigger a DAG manually
docker-compose exec airflow-webserver airflow dags trigger <dag_id>

# View logs
docker-compose logs -f airflow-scheduler
docker-compose logs -f airflow-webserver
```

## 🐛 Troubleshooting

### Permission Issues
If you encounter permission issues with Docker:
```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up -d
```

### Database Issues
If the database gets corrupted:
```bash
docker-compose down -v  # Remove volumes
docker-compose up -d     # Restart with fresh database
```

## 📝 Contributing

Feel free to add more example DAGs or improve existing ones! Make sure to:
1. Follow Airflow best practices
2. Add appropriate documentation
3. Test your DAGs before committing

## 📄 License

This is a learning project and is free to use for educational purposes.