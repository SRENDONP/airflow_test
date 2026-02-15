#!/bin/bash
# Setup script for Airflow development environment

set -e

echo "🚀 Setting up Airflow development environment..."

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Set AIRFLOW_HOME
export AIRFLOW_HOME=$(pwd)

# Initialize Airflow database
echo "Initializing Airflow database..."
airflow db init

# Create admin user
echo "Creating admin user..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start Airflow:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Start the webserver: airflow webserver --port 8080"
echo "  3. In another terminal, start the scheduler: airflow scheduler"
echo ""
echo "Or use Docker Compose:"
echo "  docker-compose up -d"
echo ""
echo "Access the UI at: http://localhost:8080"
echo "Username: admin"
echo "Password: admin"
