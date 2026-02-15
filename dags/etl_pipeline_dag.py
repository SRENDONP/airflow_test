"""
ETL Pipeline Example DAG
This DAG demonstrates a simple ETL (Extract, Transform, Load) pipeline pattern.
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import json


def extract_data():
    """Extract: Simulate data extraction from a source"""
    print("Extracting data from source...")
    data = {
        'users': [
            {'id': 1, 'name': 'Alice', 'age': 30},
            {'id': 2, 'name': 'Bob', 'age': 25},
            {'id': 3, 'name': 'Charlie', 'age': 35},
        ]
    }
    print(f"Extracted {len(data['users'])} records")
    return json.dumps(data)


def transform_data(**context):
    """Transform: Process and clean the extracted data"""
    print("Transforming data...")
    # Get data from previous task using XCom
    ti = context['ti']
    extracted_data = json.loads(ti.xcom_pull(task_ids='extract'))
    
    # Transform: Add a new field
    transformed_users = []
    for user in extracted_data['users']:
        user['age_group'] = 'senior' if user['age'] >= 30 else 'junior'
        transformed_users.append(user)
    
    print(f"Transformed {len(transformed_users)} records")
    return json.dumps(transformed_users)


def load_data(**context):
    """Load: Simulate loading data to a destination"""
    print("Loading data to destination...")
    # Get data from previous task using XCom
    ti = context['ti']
    transformed_data = json.loads(ti.xcom_pull(task_ids='transform'))
    
    # Simulate loading
    print("Loading the following records:")
    for user in transformed_data:
        print(f"  - {user}")
    
    print(f"Successfully loaded {len(transformed_data)} records")
    return "Load completed"


def validate_data(**context):
    """Validate: Check if the pipeline completed successfully"""
    print("Validating pipeline execution...")
    ti = context['ti']
    load_result = ti.xcom_pull(task_ids='load')
    
    if load_result == "Load completed":
        print("✓ Pipeline validation successful!")
        return True
    else:
        print("✗ Pipeline validation failed!")
        return False


# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'etl_pipeline_example',
    default_args=default_args,
    description='Simple ETL pipeline demonstration',
    schedule_interval='@hourly',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example', 'etl'],
) as dag:

    # ETL Tasks
    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_data,
    )

    validate = PythonOperator(
        task_id='validate',
        python_callable=validate_data,
    )

    # Define the pipeline flow
    extract >> transform >> load >> validate
