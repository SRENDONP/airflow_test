"""
DAG de Ejemplo - Apache Airflow
================================

Este DAG demuestra el uso básico de Airflow con:
- PythonOperator: para ejecutar funciones Python
- BashOperator: para ejecutar comandos bash
- Dependencias entre tareas

Autor: Tu nombre
Fecha: 2024-01-01
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


# Configuración por defecto del DAG
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definición del DAG
dag = DAG(
    dag_id='ejemplo_dag',
    default_args=default_args,
    description='Un DAG de ejemplo para demostrar funcionalidades básicas de Airflow',
    schedule_interval=timedelta(days=1),  # Ejecutar diariamente
    catchup=False,  # No ejecutar fechas pasadas
    tags=['ejemplo', 'tutorial'],
)


# ============================================================================
# DEFINICIÓN DE FUNCIONES
# ============================================================================

def saludar(**context):
    """
    Función de ejemplo que imprime un saludo y retorna información.

    Args:
        **context: Contexto de Airflow con información de la ejecución

    Returns:
        str: Mensaje de confirmación
    """
    execution_date = context['execution_date']
    print(f"¡Hola desde Apache Airflow!")
    print(f"Fecha de ejecución: {execution_date}")
    print(f"DAG: {context['dag'].dag_id}")
    print(f"Task: {context['task'].task_id}")
    return "¡Saludo completado exitosamente!"


def procesar_datos(**context):
    """
    Función de ejemplo que simula procesamiento de datos.

    Args:
        **context: Contexto de Airflow

    Returns:
        dict: Resultado del procesamiento
    """
    import time
    import random

    print("Iniciando procesamiento de datos...")

    # Simular procesamiento
    time.sleep(2)
    records_processed = random.randint(100, 1000)

    print(f"Procesados {records_processed} registros")
    print("Datos procesados exitosamente!")

    return {
        'status': 'success',
        'records_processed': records_processed,
        'timestamp': str(datetime.now())
    }


def finalizar(**context):
    """
    Función final que resume la ejecución del DAG.

    Args:
        **context: Contexto de Airflow
    """
    print("=" * 50)
    print("RESUMEN DE EJECUCIÓN")
    print("=" * 50)
    print(f"DAG: {context['dag'].dag_id}")
    print(f"Execution Date: {context['execution_date']}")
    print(f"Run ID: {context['run_id']}")
    print("Todas las tareas completadas exitosamente!")
    print("=" * 50)


# ============================================================================
# DEFINICIÓN DE TAREAS
# ============================================================================

# Tarea 1: Saludo inicial
tarea_saludo = PythonOperator(
    task_id='saludar',
    python_callable=saludar,
    provide_context=True,
    dag=dag,
)

# Tarea 2: Comando Bash
tarea_bash = BashOperator(
    task_id='comando_bash',
    bash_command='echo "Ejecutando comando desde Bash" && echo "Fecha: $(date)" && echo "Usuario: $USER"',
    dag=dag,
)

# Tarea 3: Procesamiento de datos
tarea_procesar = PythonOperator(
    task_id='procesar_datos',
    python_callable=procesar_datos,
    provide_context=True,
    dag=dag,
)

# Tarea 4: Finalización
tarea_finalizar = PythonOperator(
    task_id='finalizar',
    python_callable=finalizar,
    provide_context=True,
    dag=dag,
)


# ============================================================================
# DEFINICIÓN DE DEPENDENCIAS
# ============================================================================

# Flujo de ejecución:
# saludar -> comando_bash -> procesar_datos -> finalizar

tarea_saludo >> tarea_bash >> tarea_procesar >> tarea_finalizar
