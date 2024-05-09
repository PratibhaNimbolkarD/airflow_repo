from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id='question_2',
    description='This is the DAG for question no 2',
    schedule_interval='@daily',  # Added a schedule interval for daily execution
    start_date=datetime(2024, 5, 8)  # Added a start date
) as dag:
    task1 = BashOperator(
        task_id='print_current_date',
        bash_command='date',
    )

    task2 = BashOperator(
        task_id='echo_hello',
        bash_command='echo "Hello, Airflow!"',
    )

    task3 = BashOperator(
        task_id='execution',
        bash_command='echo "execution done"',
    )

    # Define task dependencies
    task1 >> task2 >> task3
