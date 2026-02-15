"""
Task Dependencies Example DAG
This DAG demonstrates different ways to set task dependencies in Airflow.
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator


def task_a():
    print("Executing Task A")
    return "Task A completed"


def task_b():
    print("Executing Task B")
    return "Task B completed"


def task_c():
    print("Executing Task C")
    return "Task C completed"


def task_d():
    print("Executing Task D")
    return "Task D completed"


# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define the DAG
with DAG(
    'task_dependencies_example',
    default_args=default_args,
    description='DAG showing task dependency patterns',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example', 'dependencies'],
) as dag:

    # Create tasks
    start = BashOperator(
        task_id='start',
        bash_command='echo "Starting workflow"',
    )

    task_a_op = PythonOperator(
        task_id='task_a',
        python_callable=task_a,
    )

    task_b_op = PythonOperator(
        task_id='task_b',
        python_callable=task_b,
    )

    task_c_op = PythonOperator(
        task_id='task_c',
        python_callable=task_c,
    )

    task_d_op = PythonOperator(
        task_id='task_d',
        python_callable=task_d,
    )

    end = BashOperator(
        task_id='end',
        bash_command='echo "Workflow completed"',
    )

    # Set task dependencies - demonstrates branching and joining
    # Start -> Task A -> Task B -> End
    #       -> Task C -> Task D -> End
    start >> [task_a_op, task_c_op]
    task_a_op >> task_b_op >> end
    task_c_op >> task_d_op >> end
