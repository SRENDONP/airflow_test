"""
Simple Hello World DAG
This is a basic example DAG that prints 'Hello World' using a BashOperator.
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def print_hello():
    """Simple Python function to print Hello"""
    print("Hello from Python!")
    return "Hello World"


# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'hello_world',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example', 'tutorial'],
) as dag:

    # Task 1: Print Hello using BashOperator
    hello_bash = BashOperator(
        task_id='hello_bash',
        bash_command='echo "Hello World from Bash!"',
    )

    # Task 2: Print Hello using PythonOperator
    hello_python = PythonOperator(
        task_id='hello_python',
        python_callable=print_hello,
    )

    # Task 3: Print date
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    # Set task dependencies
    hello_bash >> hello_python >> print_date
