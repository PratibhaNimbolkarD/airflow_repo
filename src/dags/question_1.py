from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='question_1',
    description='This is question one DAG',
    start_date=datetime(2024, 5, 8, 0, 0, 0)  # Changed the start date
) as dag:

    task1 = BashOperator(
        task_id='print_date',
        bash_command="echo 'Today is $(date)'",  # Modified the bash command to print today's date
    )

    task2 = BashOperator(
        task_id='echo_message',
        bash_command='echo "This is the second command"',  # Modified the bash command
    )

    task3 = BashOperator(
        task_id='echo_complete',
        bash_command='echo "All tasks are completed"',  # Modified the bash command
    )

    # Define task dependencies
    task1 >> task2 >> task3
