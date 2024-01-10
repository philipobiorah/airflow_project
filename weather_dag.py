from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from weather_etl import run_weather_etl 
    
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'weather_dag',
    default_args=default_args,
    description='Weather ETL code',
    schedule_interval='@daily'
)

run_etl = PythonOperator(
    task_id='complete_weather_etl',
    python_callable=run_weather_etl,
    dag=dag,
)